import os
from flask import Flask, request, render_template, redirect, url_for, flash
from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository
from lib.user_repository import UserRepository
from lib.forms import RegisterForm, LoginForm
from flask_login import login_user, LoginManager, login_required, logout_user, current_user
from lib.user import User
from flask_bcrypt import Bcrypt
from lib.booking_repository import BookingRepository
import hashlib

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

@app.route('/index', methods=['GET'])
def get_index():
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    listings = repo.all()
    return render_template('index.html', listings = listings)


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

#Test123!@111


#IF LOG IN AND PASSWORD IS CORRECT USER IS REDIRECT TO THIS PAGE. 
@app.route('/profile', methods=['GET'])
@login_required
def profile_page():
    connection = get_flask_database_connection(app)
    space_repository = SpaceRepository(connection)
    spaces = space_repository.find_user_spaces(current_user.id)
    booking_repository = BookingRepository(connection)
    bookings = booking_repository.find_user_bookings(current_user.id)
    return render_template('profile.html', user=current_user, spaces=spaces, bookings=bookings)

# I ALSO CREATED A LOG OUT FUNCTION. 
@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('get_login_details'))


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
        repo.create(user)
        login_user(user)
        flash('Account created successfully!', 'success')
        return redirect(url_for('profile_page'))
    else:
        flash(form.errors)

    return render_template('create_account.html', form=form)



@app.route('/space/<int:id>', methods=['GET'])
def get_space_page(id):
    connection = get_flask_database_connection(app)
    repo = SpaceRepository(connection)
    space = repo.find(id)
    return render_template("space.html", space=space)

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

