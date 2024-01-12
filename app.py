import os
from flask import Flask, request, render_template, redirect, url_for, flash
from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository
from lib.user_repository import UserRepository
from lib.space_repository import *
from lib.forms import RegisterForm, LoginForm, NewListingForm, BookingForm
from flask_login import login_user, LoginManager, login_required, logout_user, current_user
from lib.user import User
from flask_bcrypt import Bcrypt
from flask_paginate import Pagination, get_page_args
from lib.booking_repository import BookingRepository
from datetime import date
from lib.booking import Booking

# Create a new Flask app
app = Flask(__name__, static_url_path='/static')
bcrypt = Bcrypt(app)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_secret_key')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "sign_in"

@login_manager.user_loader
def load_user(user_id):
    connection = get_flask_database_connection(app)
    
    # Load user information
    user_repository = UserRepository(connection)
    user = user_repository.find_by_id(int(user_id))
    space_repository = SpaceRepository(connection)
    spaces = space_repository.find_user_spaces(user_id)
    if user:
        user.spaces = spaces
    return user 


# REMOVED THE INDEX ROOT SO IT GOES 
@app.route('/', methods=['GET'])
def get_index():
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    listings = repo.all()    
    page, per_page, offset= get_page_args()
    total = len(listings)
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')
    paginated_products = listings[offset: offset + per_page]
    current_page = int(request.args.get('page', 1))
    
    return render_template('index.html', listings=paginated_products, pagination=pagination, paginated_products=paginated_products, current_page=current_page, user=current_user)



#THIS FUNCTION HANDES THE SING IN, IF USER AND PASSWORD IS CORRECT THEN IT WILL REDIRECT TO THE PROFILE PAGE
@app.route('/login', methods=['GET', 'POST'])
def get_login_details():
    form = LoginForm()
    if form.validate_on_submit():
        connection = get_flask_database_connection(app)
        user_repository = UserRepository(connection)
        user = user_repository.find_by_name(form.username.data)
        if user and bcrypt.check_password_hash(user.password.encode('utf-8'), form.password.data.encode('utf-8')):
            login_user(user)
            return redirect(url_for('profile_page'))
        else:
            flash('Invalid username or password. Please try again.', 'error')

    return render_template('login.html', form=form)


@app.route('/profile', methods=['GET'])
@login_required
def profile_page():
    connection = get_flask_database_connection(app)
    space_repository = SpaceRepository(connection)
    spaces = space_repository.find_user_spaces(current_user.id)
    listing = space_repository.all()
    
    booking_repository = BookingRepository(connection)
    bookings = booking_repository.find_user_bookings(current_user.id)
    return render_template('profile.html', user=current_user, spaces=spaces, bookings=bookings, listing=listing)


# I ALSO CREATED A LOG OUT FUNCTION. 
@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('get_index'))


@app.route('/create_account', methods=['GET', 'POST'])
def get_create_account():
    form = RegisterForm()
    if form.validate_on_submit():
        connection = get_flask_database_connection(app)
        repo = UserRepository(connection)
        username = form.username.data
        email = form.email.data
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        
        user = User(None, username, email, hashed_password)
        success, user = repo.create(user)
        if success:
            flash("Registration successful")
            return redirect(url_for('profile_page'))
        elif not success and repo.find_by_name(form.username.data) is not None and not success and repo.find_by_email(form.email.data) is not None:
            flash("Username and email already exist. Please choose a different username and email.")
        elif not success and repo.find_by_name(form.username.data) is not None:
            flash("Username already exists. Please choose a different username.")
        elif not success and repo.find_by_email(form.email.data) is not None:
            flash("Email already exists. Please choose a different email.")


    return render_template('create_account.html', form=form)



@app.route('/new_listing', methods=['GET', 'POST'])
@login_required
def create_space():
    form = NewListingForm()
    if form.validate_on_submit():
        connection = get_flask_database_connection(app)
        repository = SpaceRepository(connection)
        today = date.today()
        space = Space(None, form.address.data, form.name.data, form.price.data, form.image_path.data, form.description.data, today, form.date_added.data, current_user.id )
        repository.create(space)
        flash('Space created successfully!', 'success')
    else:
        print(form.errors)
    
    return render_template("new_listing.html", form=form, user=current_user)


@app.route('/space/<int:id>', methods=['GET', 'POST'])
def get_space_done(id):
    connection = get_flask_database_connection(app)
    repo = BookingRepository(connection)
    space_repo = SpaceRepository(connection)
    space = space_repo.find(id)
    form = BookingForm()
    selected_date = form.booking_date.data

    if form.validate_on_submit() and current_user.is_authenticated:
            if not repo.find_booking(selected_date):
                booking = Booking(None, current_user.id, space.id, selected_date, space.name)
                repo.create(booking)
                flash("Booking successful!", "success")
                return redirect(url_for('profile_page'))
            else:
                flash("That date is unavailable, please choose another")
    else:
        flash("Please log in to make a booking")


    return render_template("space.html", space=space, form=form, user=current_user)



if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

