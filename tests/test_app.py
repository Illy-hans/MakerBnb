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
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("MakersBnB")

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
    print(list_items)
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

"""
When click on create account, it shows us the create account page
"""

"""
When user is signed in, it displays you are logged in
"""

"""
When the user has signed out, it shows the the sign in and create account buttons
"""