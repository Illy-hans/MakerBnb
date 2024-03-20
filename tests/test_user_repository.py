from lib.user_repository import UserRepository
from lib.user import User

"""
When we call UserRepository.all()
We get a list of all the user accounts
"""
def test_get_all_users(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)
    
    users = repository.all()

    assert users == [
                    User(1, 'gustavo', 'gustavo@gustavo.com', 'Gustavo123456!'),
                    User(2, 'Lil kim', 'femalerappers@femalerappers.com', '14d7d63e53c91431cb5b4a2e62dbb80881736ae7f228d5b4894935a108b1bfab'),
                    User(3, 'Curious George', 'fakemonkey@fakemonkey.com', 'Curiousgeorge2£'),
                    User(4, 'Barbie', 'dreamteam@barbiemail.com', 'ImjustKen123%*'),
                    User(5, 'test', 'test123@testemail.com', '$2b$12$AHtXhF5zgqsR2FwD3YHjd.Li5qWsjQGNhHZq5cRxLSuqINSmq7LBy')
    ]

"""
When we call UserRepository.create()
A new user record is added to the database
"""
def test_create_user(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)

    repository.create(User(None, 'Alan', 'test_email@test.com', '1Bcdefgh@'))

    assert repository.all() == [
                    User(1, 'gustavo', 'gustavo@gustavo.com', 'Gustavo123456!'),
                    User(2, 'Lil kim', 'femalerappers@femalerappers.com', '14d7d63e53c91431cb5b4a2e62dbb80881736ae7f228d5b4894935a108b1bfab'),
                    User(3, 'Curious George', 'fakemonkey@fakemonkey.com', 'Curiousgeorge2£'),
                    User(4, 'Barbie', 'dreamteam@barbiemail.com', 'ImjustKen123%*'),
                    User(5, 'test', 'test123@testemail.com', '$2b$12$AHtXhF5zgqsR2FwD3YHjd.Li5qWsjQGNhHZq5cRxLSuqINSmq7LBy'),
                    User(6, 'Alan', 'test_email@test.com', '1Bcdefgh@')
    ]

"""
When we call UserRepository.find() with email and password
it returns true if in database, false if not
"""
def test_find_user(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)

    user = repository.find('femalerappers@femalerappers.com', 'apassword!@A')

    assert user == True

"""
When creating a new account 
Passwords should use hashes instead of real password
"""

def test_hashed_passwords(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)

    repository.create(User(None, 'Alan', 'test_email@test.com', '1Bcdefgh@'))

    assert repository.all() == [
                    User(1, 'gustavo', 'gustavo@gustavo.com', 'Gustavo123456!'),
                    User(2, 'Lil kim', 'femalerappers@femalerappers.com', '14d7d63e53c91431cb5b4a2e62dbb80881736ae7f228d5b4894935a108b1bfab'),
                    User(3, 'Curious George', 'fakemonkey@fakemonkey.com', 'Curiousgeorge2£'),
                    User(4, 'Barbie', 'dreamteam@barbiemail.com', 'ImjustKen123%*'),
                    User(5, 'test', 'test123@testemail.com', '$2b$12$AHtXhF5zgqsR2FwD3YHjd.Li5qWsjQGNhHZq5cRxLSuqINSmq7LBy'),
                    User(6, 'Alan', 'test_email@test.com', '1Bcdefgh@')
    ]

"""
Test search by id 
"""

def test_search_users_by_id(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)

    assert repository.find_by_id(1) == User(1, 'gustavo', 'gustavo@gustavo.com', 'Gustavo123456!')