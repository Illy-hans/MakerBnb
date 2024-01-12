import psycopg
from lib.booking import Booking

class BookingRepository():

    def __init__(self, connection):
        self._connection = connection

    def find(self, user_id):
        result = self._connection.execute("SELECT * FROM bookings WHERE user_id = %s", [user_id])
        if result:
            bookings = []
            for row in result:
                bookings.append(Booking(row['id'], row['user_id'], row['space_id'], row['date_booked'], row['space_name']))
            return bookings
        else:
            return None
        
    def create(self, booking):
        self._connection.execute("INSERT INTO bookings (user_id, space_id, date_booked, space_name) VALUES (%s, %s, %s, %s)", [booking.user_id, booking.space_id, booking.date_booked, booking.space_name])
        return None
    
    def find_user_bookings(self, user_id):
        rows = self._connection.execute("SELECT * FROM bookings WHERE user_id = %s", [user_id])
        bookings = []
        for row in rows:
            item = Booking(row['id'], row['user_id'], row['space_id'], row['date_booked'], row['space_name'])
            bookings.append(item)
        return bookings
    
    def find_booking(self, date_booked):
        rows = self._connection.execute("SELECT * FROM bookings WHERE date_booked = %s", [date_booked])
        if rows:
            return True 
        
