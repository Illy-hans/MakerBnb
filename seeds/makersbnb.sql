
DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS spaces CASCADE;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP TABLE IF EXISTS bookings CASCADE;
DROP SEQUENCE IF EXISTS bookings_id_seq;


CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
	user_name text,
	email text,
	password text
);

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
	address text,
	name text,
    price int,
    image_path text,
    description text,
    date_added date,
    date_available date,
    user_id int,
    constraint fk_user foreign key(user_id) references users(id) ON DELETE CASCADE
);

CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    date_booked date,
    user_id int,
    space_id int,
    space_name text,
    constraint fk_user foreign key(user_id) references users(id) ON DELETE CASCADE,
    constraint fk_space foreign key(space_id) references spaces(id) ON DELETE CASCADE
);


INSERT INTO users (user_name, email, password) VALUES
('gustavo', 'gustavo@gustavo.com', 'Gustavo123456!'),
('Lil kim', 'femalerappers@femalerappers.com', '14d7d63e53c91431cb5b4a2e62dbb80881736ae7f228d5b4894935a108b1bfab'),
('Curious George', 'fakemonkey@fakemonkey.com', 'Curiousgeorge2£'),
('Barbie', 'dreamteam@barbiemail.com', 'ImjustKen123%*'),
('test', 'test123@testemail.com', '$2b$12$AHtXhF5zgqsR2FwD3YHjd.Li5qWsjQGNhHZq5cRxLSuqINSmq7LBy');

INSERT INTO spaces (address, name, price, image_path, description, date_added, date_available, user_id) VALUES
('123 Horse Lane', 'Opulent Oak Haven', 300, '/images/oakhaven.png', 'A lavish wooden house in the serene countryside, adorned with expensive decor, offering a retreat of unparalleled luxury.', '2020-10-22', '2024-06-22', 1),
('5 Zoo lane', 'Stonegate Sanctuary', 560, '/images/stonegate.png', 'A rural British stone and woodwork cabin nestled in a picturesque valley, blending traditional charm with modern elegance.', '2019-08-21', '2024-04-10', 2),
('789 Starlight Street', 'Glass Vista Retreat', 720, '/images/glassvista.png', 'A modern marvel of glass and wood, featuring a private swimming pool and stone steps, providing a luxurious escape into nature.', '2022-02-08', '2024-02-01', 3),
('101 Mountain View', 'Remote Hillside Lodge', 110, '/images/hillsidelodge.png', 'A secluded wooden lodge perched on a remote hillside, offering exclusive tranquility and breathtaking views.', '2023-01-17', '2024-05-15', 2),
('222 Beachfront Road', 'Alpine Oasis', 150, '/images/alpineoasis.png', 'A peaceful wooden cabin surrounded by towering pine trees in a snowy locale, providing a cozy and luxurious winter retreat.', '2022-11-30', '2024-10-12', 1),
('333 Skyline Tower', 'Stone Serenity', 340, '/images/stoneserenity.png', 'A contemporary stonework guest house with a refreshing swimming pool, offering a perfect blend of sophistication and relaxation.', '2020-12-03', '2024-08-20', 3),
('444 Lakeside Drive', 'Garden View Haven', 80, '/images/gardenviewhaven.png', 'A simple yet luxuriously appointed stonework cabin with a sprawling garden, providing an idyllic escape from the hustle and bustle.', '2021-09-25', '2024-09-18', 2);

INSERT INTO bookings (date_booked, user_id, space_id, space_name) VALUES
('2024-02-01', 1, 3, 'Glass Vista Retreat'),
('2024-04-10', 1, 2, 'Stonegate Sanctuary'),
('2024-05-15', 2, 4, 'Remote Hillside Lodge' ),
('2024-06-22', 2, 1, 'Opulent Oak Haven'),
('2024-08-20', 2, 6, 'Stone Serenity'),
('2024-09-18', 3, 7, 'Garden View Haven'),
('2024-10-12', 3, 5, 'Alpine Oasis');

