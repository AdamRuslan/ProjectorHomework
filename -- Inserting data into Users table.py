-- Inserting data into Users table
INSERT INTO Users (user_id, username, password, email, first_name, last_name, phone_number, registration_date, user_type)
VALUES
    (1, 'john123', 'pass123', 'john@example.com', 'John', 'Doe', '123456789', '2022-01-01', 'Guest'),
    (2, 'jane456', 'pass456', 'jane@example.com', 'Jane', 'Smith', '987654321', '2022-02-01', 'Guest'),
    (3, 'host123', 'hostpass', 'host@example.com', 'Host', 'User', '555555555', '2022-03-01', 'Host');

-- Inserting data into Hosts table
INSERT INTO Hosts (host_id, bio, profile_picture, location)
VALUES
    (3, 'Experienced host with a passion for hospitality.', 'host_pic.jpg', 'New York, USA');

-- Inserting data into Guests table
INSERT INTO Guests (guest_id, profile_picture, location)
VALUES
    (1, 'john_pic.jpg', 'Los Angeles, USA'),
    (2, 'jane_pic.jpg', 'London, UK');

-- Inserting data into Rooms table
INSERT INTO Rooms (room_id, host_id, room_type, description, capacity, price_per_night, has_ac, has_refrigerator)
VALUES
    (1, 3, 'Entire Home', 'Beautiful apartment with a stunning view.', 4, 150.00, 1, 1),
    (2, 3, 'Private Room', 'Cozy room in a quiet neighborhood.', 2, 80.00, 0, 1),
    (3, 3, 'Entire Home', 'Spacious villa with a pool.', 8, 300.00, 1, 1);

-- Inserting data into Reservations table
INSERT INTO Reservations (reservation_id, guest_id, room_id, check_in_date, check_out_date, payment_status)
VALUES
    (1, 1, 1, '2022-06-15', '2022-06-20', 'Paid'),
    (2, 2, 2, '2022-07-10', '2022-07-15', 'Paid'),
    (3, 1, 3, '2022-08-05', '2022-08-10', 'Paid');

-- Inserting data into Reviews table
INSERT INTO Reviews (review_id, guest_id, host_id, reservation_id, rating, comment)
VALUES
    (1, 1, 3, 1, 5, 'Great experience, highly recommended!'),
    (2, 2, 3, 2, 4, 'Nice room, friendly host.'),
    (3, 1, 3, 3, 5, 'Amazing villa, exceeded our expectations.');

-- Inserting data into Payments table (optional for guest)
INSERT INTO Payments (payment_id, reservation_id, payment_date, amount, payment_method)
VALUES
    (1, 1, '2022-06-10', 750.00, 'Credit Card'),
    (2, 2, '2022-07-05', 400.00, 'PayPal'),
    (3, 3, '2022-08-01', 1500.00, 'Bank Transfer');
