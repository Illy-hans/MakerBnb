from lib.space_repository import SpaceRepository
from lib.space import Space
import datetime


# # test get all spaces
def test_can_get_all_spaces(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = SpaceRepository(db_connection)
    assert repository.all() == [
Space(1, '123 Horse Lane', 'Wild horses', 56, '/images/lilkim.jpg', 'A light, warm, and modern space for a gathering.', datetime.date(2020,10,22), 1),
Space(2, '5 Zoo lane', 'Zootropolis', 124, '/images/zoos.jpg', 'A nice warm bed amongst the animals', datetime.date(2019,8,21), 2),
Space(3, '789 Starlight Street', 'Celestial Haven', 72, '/images/celestial_haven.jpg', 'Experience the tranquility under the stars in this celestial haven.', datetime.date(2022,2,8), 3), 
Space(4, '101 Mountain View', 'Mountain Hideaway', 110, '/images/mountain_hideaway.jpg', 'Escape to the serene mountains and enjoy the breathtaking views.', datetime.date(2023,1,17), 2),
Space(5, '222 Beachfront Road', 'Ocean Paradise Villa', 150, '/images/ocean_paradise.jpg', 'Relax by the beach in this luxurious oceanfront villa.', datetime.date(2022,11,30), 1),
Space(6, '333 Skyline Tower', 'Cityscape Loft', 95, '/images/cityscape_loft.jpg', 'A modern loft with stunning views of the city skyline.', datetime.date(2020,12,3), 3),
Space(7, '444 Lakeside Drive', 'Tranquil Lake Cottage', 80, '/images/lake_cottage.jpg', 'Escape to this cozy cottage by the lake for a peaceful retreat.', datetime.date(2021,9,25), 2)
    ]
    


# # test create space
def test_create_spaces(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = SpaceRepository(db_connection)
    repository.create(Space(None, 'test address', 'test name', 11, '/image/path', 'very nice test description', datetime.date(2023,2,10), 1))
    assert repository.all() == [
Space(1, '123 Horse Lane', 'Wild horses', 56, '/images/lilkim.jpg', 'A light, warm, and modern space for a gathering.', datetime.date(2020,10,22), 1),
Space(2, '5 Zoo lane', 'Zootropolis', 124, '/images/zoos.jpg', 'A nice warm bed amongst the animals', datetime.date(2019,8,21), 2),
Space(3, '789 Starlight Street', 'Celestial Haven', 72, '/images/celestial_haven.jpg', 'Experience the tranquility under the stars in this celestial haven.', datetime.date(2022,2,8), 3), 
Space(4, '101 Mountain View', 'Mountain Hideaway', 110, '/images/mountain_hideaway.jpg', 'Escape to the serene mountains and enjoy the breathtaking views.', datetime.date(2023,1,17), 2),
Space(5, '222 Beachfront Road', 'Ocean Paradise Villa', 150, '/images/ocean_paradise.jpg', 'Relax by the beach in this luxurious oceanfront villa.', datetime.date(2022,11,30), 1),
Space(6, '333 Skyline Tower', 'Cityscape Loft', 95, '/images/cityscape_loft.jpg', 'A modern loft with stunning views of the city skyline.', datetime.date(2020,12,3), 3),
Space(7, '444 Lakeside Drive', 'Tranquil Lake Cottage', 80, '/images/lake_cottage.jpg', 'Escape to this cozy cottage by the lake for a peaceful retreat.', datetime.date(2021,9,25), 2),
Space(8, 'test address', 'test name', 11, '/image/path', 'very nice test description', datetime.date(2023,2,10), 1)
    ]


# #  test find space
def test_find_space(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = SpaceRepository(db_connection)
    assert repository.find(3) == Space(3, '789 Starlight Street', 'Celestial Haven', 72, '/images/celestial_haven.jpg', 'Experience the tranquility under the stars in this celestial haven.', datetime.date(2022,2,8), 3)


# # test delete space
def test_delete_space(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = SpaceRepository(db_connection)
    repository.delete(1)
    assert repository.all() == [
Space(2, '5 Zoo lane', 'Zootropolis', 124, '/images/zoos.jpg', 'A nice warm bed amongst the animals', datetime.date(2019,8,21), 2),
Space(3, '789 Starlight Street', 'Celestial Haven', 72, '/images/celestial_haven.jpg', 'Experience the tranquility under the stars in this celestial haven.', datetime.date(2022,2,8), 3), 
Space(4, '101 Mountain View', 'Mountain Hideaway', 110, '/images/mountain_hideaway.jpg', 'Escape to the serene mountains and enjoy the breathtaking views.', datetime.date(2023,1,17), 2),
Space(5, '222 Beachfront Road', 'Ocean Paradise Villa', 150, '/images/ocean_paradise.jpg', 'Relax by the beach in this luxurious oceanfront villa.', datetime.date(2022,11,30), 1),
Space(6, '333 Skyline Tower', 'Cityscape Loft', 95, '/images/cityscape_loft.jpg', 'A modern loft with stunning views of the city skyline.', datetime.date(2020,12,3), 3),
Space(7, '444 Lakeside Drive', 'Tranquil Lake Cottage', 80, '/images/lake_cottage.jpg', 'Escape to this cozy cottage by the lake for a peaceful retreat.', datetime.date(2021,9,25), 2)
    ]

# # test update space
