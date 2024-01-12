from lib.booking_repository import *
import datetime


def test_find_users_who_booked_same_space(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = BookingRepository(db_connection)
    user = repository.find(1)
    assert user == [
        Booking(1, 1, 3, datetime.date(2024,2,1), 'Glass Vista Retreat'),
        Booking(2, 1, 2, datetime.date(2024,4,10), 'Stonegate Sanctuary'),
    ]

    
def test_create_booking(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = BookingRepository(db_connection)
    booking = Booking(None, 1, 1, '2022-01-01', 'Devon')
    repository.create(booking)
    user = repository.find(1)
    assert user == [
        Booking(1, 1, 3, datetime.date(2024,2,1), 'Glass Vista Retreat'),
        Booking(2, 1, 2, datetime.date(2024,4,10), 'Stonegate Sanctuary'),
        Booking(8, 1, 1, datetime.date(2022,1,1), 'Devon')
    ]


def test_find_booking_by_date(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = BookingRepository(db_connection)
    booking = repository.find_booking('2024-02-01')

    assert booking == True 


def test_find_booking_false(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = BookingRepository(db_connection)
    booking = repository.find_booking('2027-03-01')

    assert booking == None


