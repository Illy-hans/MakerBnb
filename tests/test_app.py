from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
# def test_get_index(page, test_web_address):
#     # We load a virtual browser and navigate to the /index page
#     page.goto(f"http://{test_web_address}/index")

#     # We look at the <p> tag
#     strong_tag = page.locator("p")

#     # We assert that it has the text "This is the homepage."
#     expect(strong_tag).to_have_text("This is the homepage.")

"""
When we GET the login page, it renders the template
"""
def test_get_login(page, test_web_address):
    page.goto(f"http://{test_web_address}/login")
    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text("Sign In")

"""
When we call index.html, it renders the template
"""

def test_get_index(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Welcome to MakersBnB")

"""
When we got to the index page, it shows all listings on the page
"""
def test_get_index_listings(page, test_web_address, db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f"http://{test_web_address}")
    list_items = page.locator(".image-container")
    expect(list_items).to_have_text(['\n\n\n'            
                                    'Opulent Oak Haven£300 per night\n\n\n'            
                                    'Stonegate Sanctuary£560 per night\n\n\n'
                                    'Glass Vista Retreat£720 per night\n\n\n'            
                                    'Remote Hillside Lodge£110 per night\n\n\n'            
                                    'Alpine Oasis£150 per night\n\n\n'            
                                    'Stone Serenity£340 per night\n\n\n'            
                                    'Garden View Haven£80 per night\n\n'] )
    
"""
When we click on sign in page, it redirects us to the correct page
"""
def test_get_sign_in_page_from_landing_page(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    page.click(".navbar-nav :nth-child(1) .nav-link")
    assert page.url == f"http://{test_web_address}/login"


"""
When click on create account, it shows us the create account page
"""
def test_get_creat_account_page_from_landing_page(page, test_web_address):
    page.goto(f"http://{test_web_address}")
    page.click(".navbar-nav :nth-child(2) .nav-link")
    assert page.url == f"http://{test_web_address}/create_account"


"""
When user is signed in, it displays you are logged in
"""
def test_nav_bar_displays_user_logged_in_on_index(page, test_web_address, db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f"http://{test_web_address}/login")
    page.fill("#username_input input", "test")
    page.fill("#password_input input", "123abcD!")
    page.click(".button")
    page.click(".navbar-nav :nth-child(2) .nav-link")
    user_tag = page.locator(".navbar-nav :nth-child(1) .nav-link")
    sign_out_tag = page.locator(".navbar-nav :nth-child(2) .nav-link")
    assert page.url == f"http://{test_web_address}/"
    expect(user_tag).to_have_text("Hi, test")
    expect(sign_out_tag).to_have_text("Sign Out")

"""
When the user has signed out, it shows the the sign in and create account buttons
"""
def test_nav_bar_displays_user_logged_out_on_index(page, test_web_address, db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f"http://{test_web_address}/login")
    page.fill("#username_input input", "test")
    page.fill("#password_input input", "123abcD!")
    page.click(".button")
    page.click(".navbar-nav :nth-child(2) .nav-link")
    assert page.url == f"http://{test_web_address}/"
    page.click(".navbar-nav :nth-child(2) .nav-link")
    assert page.url == f"http://{test_web_address}/"
    user_tag = page.locator(".navbar-nav :nth-child(1) .nav-link")
    sign_out_tag = page.locator(".navbar-nav :nth-child(2) .nav-link")
    expect(user_tag).to_have_text("Sign In")
    expect(sign_out_tag).to_have_text("Create Account")

"""
When you click on a listing of the index page, it should redirect you to said listing
"""
def test_listing_redirection_on_index(page, test_web_address, db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f"http://{test_web_address}/")
    # page.click(".image-container :nth-child(1) :nth-child(1)") <-- alternative syntax to below
    page.click(".image-container .listing-container a[href='/space/1']")
    assert page.url == f"http://{test_web_address}/space/1"



def test_page_has_loaded_images(page, test_web_address, db_connection):
        db_connection.seed('seeds/makersbnb.sql')
        page.goto(f"http://{test_web_address}/")
        page.screenshot(path="images.png")
        
        # image_selector = "a[href='/space/1']" <-- alternative syntax to below
        image_selector1 = "img[src='static//images/oakhaven.png']" 
        image_selector2 = "img[src='static//images/stonegate.png']"
        image_selector3 = "img[src='static//images/glassvista.png']"
        image_selector4 = "img[src='static//images/hillsidelodge.png']"
        image_selector5 = "img[src='static//images/alpineoasis.png']"
        image_selector6 = "img[src='static//images/stoneserenity.png']"
        image_selector7 = "img[src='static//images/gardenviewhaven.png']"

        page.wait_for_selector(image_selector1)
        page.wait_for_selector(image_selector2)
        page.wait_for_selector(image_selector3)
        page.wait_for_selector(image_selector4)
        page.wait_for_selector(image_selector5)
        page.wait_for_selector(image_selector6)
        page.wait_for_selector(image_selector7)

        
        assert page.is_visible(image_selector1) 
        assert page.is_visible(image_selector2) 
        assert page.is_visible(image_selector3)
        assert page.is_visible(image_selector4) 
        assert page.is_visible(image_selector5)
        assert page.is_visible(image_selector6)
        assert page.is_visible(image_selector7)
