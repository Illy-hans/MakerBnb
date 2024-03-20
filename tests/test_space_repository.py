from lib.space_repository import SpaceRepository
from lib.space import Space
import datetime
from unittest.mock import MagicMock

# # test get all spaces
def test_can_get_all_spaces(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = SpaceRepository(db_connection)
    assert repository.all() == [
Space(1, '123 Horse Lane', 'Opulent Oak Haven', 300, '/images/oakhaven.png', 'A lavish wooden house in the serene countryside, adorned with expensive decor, offering a retreat of unparalleled luxury.', datetime.date(2020,10,22), datetime.date(2024,6,22),  1),
Space(2, '5 Zoo lane', 'Stonegate Sanctuary', 560, '/images/stonegate.png', 'A rural British stone and woodwork cabin nestled in a picturesque valley, blending traditional charm with modern elegance.', datetime.date(2019,8,21), datetime.date(2024,4,10), 2),
Space(3, '789 Starlight Street', 'Glass Vista Retreat', 720, '/images/glassvista.png', 'A modern marvel of glass and wood, featuring a private swimming pool and stone steps, providing a luxurious escape into nature.', datetime.date(2022,2,8), datetime.date(2024,2,1), 3), 
Space(4, '101 Mountain View', 'Remote Hillside Lodge', 110, '/images/hillsidelodge.png', 'A secluded wooden lodge perched on a remote hillside, offering exclusive tranquility and breathtaking views.', datetime.date(2023,1,17), datetime.date(2024,5,15), 2),
Space(5, '222 Beachfront Road', 'Alpine Oasis', 150, '/images/alpineoasis.png', 'A peaceful wooden cabin surrounded by towering pine trees in a snowy locale, providing a cozy and luxurious winter retreat.', datetime.date(2022,11,30), datetime.date(2024,10,12), 1),
Space(6, '333 Skyline Tower', 'Stone Serenity', 340, '/images/stoneserenity.png', 'A contemporary stonework guest house with a refreshing swimming pool, offering a perfect blend of sophistication and relaxation.', datetime.date(2020,12,3), datetime.date(2024,8,20), 3),
Space(7, '444 Lakeside Drive', 'Garden View Haven', 80, '/images/gardenviewhaven.png', 'A simple yet luxuriously appointed stonework cabin with a sprawling garden, providing an idyllic escape from the hustle and bustle.', datetime.date(2021,9,25), datetime.date(2024,9,18), 2)
    ]

# # test create space
def test_create_spaces(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = SpaceRepository(db_connection)
    repository.create(Space(None, 'test address', 'test name', 11, 'images/zoos.jpg', 'very nice test description', datetime.date(2023,2,10), datetime.date(2024,10,10), 1))
    assert repository.all() == [
Space(1, '123 Horse Lane', 'Opulent Oak Haven', 300, '/images/oakhaven.png', 'A lavish wooden house in the serene countryside, adorned with expensive decor, offering a retreat of unparalleled luxury.', datetime.date(2020,10,22), datetime.date(2024,6,22),  1),
Space(2, '5 Zoo lane', 'Stonegate Sanctuary', 560, '/images/stonegate.png', 'A rural British stone and woodwork cabin nestled in a picturesque valley, blending traditional charm with modern elegance.', datetime.date(2019,8,21), datetime.date(2024,4,10), 2),
Space(3, '789 Starlight Street', 'Glass Vista Retreat', 720, '/images/glassvista.png', 'A modern marvel of glass and wood, featuring a private swimming pool and stone steps, providing a luxurious escape into nature.', datetime.date(2022,2,8), datetime.date(2024,2,1), 3), 
Space(4, '101 Mountain View', 'Remote Hillside Lodge', 110, '/images/hillsidelodge.png', 'A secluded wooden lodge perched on a remote hillside, offering exclusive tranquility and breathtaking views.', datetime.date(2023,1,17), datetime.date(2024,5,15), 2),
Space(5, '222 Beachfront Road', 'Alpine Oasis', 150, '/images/alpineoasis.png', 'A peaceful wooden cabin surrounded by towering pine trees in a snowy locale, providing a cozy and luxurious winter retreat.', datetime.date(2022,11,30), datetime.date(2024,10,12), 1),
Space(6, '333 Skyline Tower', 'Stone Serenity', 340, '/images/stoneserenity.png', 'A contemporary stonework guest house with a refreshing swimming pool, offering a perfect blend of sophistication and relaxation.', datetime.date(2020,12,3), datetime.date(2024,8,20), 3),
Space(7, '444 Lakeside Drive', 'Garden View Haven', 80, '/images/gardenviewhaven.png', 'A simple yet luxuriously appointed stonework cabin with a sprawling garden, providing an idyllic escape from the hustle and bustle.', datetime.date(2021,9,25), datetime.date(2024,9,18), 2),
Space(8, '1234 Foot Drive', 'Cosy Home', 120, 'images/zoos.jpg', 'A unique stay', datetime.date(2023,2,10), datetime.date(2024,10,10), 1)
    ]


# #  test find space
def test_find_space(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = SpaceRepository(db_connection)
    assert repository.find(3) == Space(3, '789 Starlight Street', 'Glass Vista Retreat', 720, '/images/glassvista.png', 'A modern marvel of glass and wood, featuring a private swimming pool and stone steps, providing a luxurious escape into nature.', datetime.date(2022,2,8), datetime.date(2024,2,1), 3)


# # test delete space
def test_delete_space(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = SpaceRepository(db_connection)
    repository.delete(1)
    assert repository.all() == [
Space(2, '5 Zoo lane', 'Stonegate Sanctuary', 560, '/images/stonegate.png', 'A rural British stone and woodwork cabin nestled in a picturesque valley, blending traditional charm with modern elegance.', datetime.date(2019,8,21), datetime.date(2024,4,10), 2),
Space(3, '789 Starlight Street', 'Glass Vista Retreat', 720, '/images/glassvista.png', 'A modern marvel of glass and wood, featuring a private swimming pool and stone steps, providing a luxurious escape into nature.', datetime.date(2022,2,8), datetime.date(2024,2,1), 3), 
Space(4, '101 Mountain View', 'Remote Hillside Lodge', 110, '/images/hillsidelodge.png', 'A secluded wooden lodge perched on a remote hillside, offering exclusive tranquility and breathtaking views.', datetime.date(2023,1,17), datetime.date(2024,5,15), 2),
Space(5, '222 Beachfront Road', 'Alpine Oasis', 150, '/images/alpineoasis.png', 'A peaceful wooden cabin surrounded by towering pine trees in a snowy locale, providing a cozy and luxurious winter retreat.', datetime.date(2022,11,30), datetime.date(2024,10,12), 1),
Space(6, '333 Skyline Tower', 'Stone Serenity', 340, '/images/stoneserenity.png', 'A contemporary stonework guest house with a refreshing swimming pool, offering a perfect blend of sophistication and relaxation.', datetime.date(2020,12,3), datetime.date(2024,8,20), 3),
Space(7, '444 Lakeside Drive', 'Garden View Haven', 80, '/images/gardenviewhaven.png', 'A simple yet luxuriously appointed stonework cabin with a sprawling garden, providing an idyllic escape from the hustle and bustle.', datetime.date(2021,9,25), datetime.date(2024,9,18), 2)
    ]

# # test update space
def test_update_space(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = SpaceRepository(db_connection)
    repository.update(2, {"address" : "one two three four"})
    assert repository.find(2) == Space(2, 'one two three four', 'Stonegate Sanctuary', 560, '/images/stonegate.png', 'A rural British stone and woodwork cabin nestled in a picturesque valley, blending traditional charm with modern elegance.', datetime.date(2019,8,21), datetime.date(2024,4,10), 2)

def test_update_price_space(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = SpaceRepository(db_connection)
    repository.update(2, {"price" : 200})
    assert repository.find(2) == Space(2, '5 Zoo lane', 'Stonegate Sanctuary', 200, '/images/stonegate.png', 'A rural British stone and woodwork cabin nestled in a picturesque valley, blending traditional charm with modern elegance.', datetime.date(2019,8,21), datetime.date(2024,4,10), 2)

def test_update_datetime_space(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = SpaceRepository(db_connection)
    repository.update(2, {"date_added" : datetime.date(2024,1,5)})
    assert repository.find(2) == Space(2, '5 Zoo lane', 'Stonegate Sanctuary', 560, '/images/stonegate.png', 'A rural British stone and woodwork cabin nestled in a picturesque valley, blending traditional charm with modern elegance.', datetime.date(2024,1,5), datetime.date(2024,4,10), 2)
