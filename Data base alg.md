Python

Table: Users

Primary Key: user_id
Attributes: username, password, email, first_name, last_name, phone_number, registration_date, user_type
Table: Hosts

Primary Key: host_id (foreign key referencing Users.user_id)
Attributes: bio, profile_picture, location
Table: Guests

Primary Key: guest_id (foreign key referencing Users.user_id)
Attributes: profile_picture, location
Table: Rooms

Primary Key: room_id
Foreign Key: host_id (referencing Hosts.host_id)
Attributes: room_type, description, capacity, price_per_night, has_ac, has_refrigerator
Table: Reservations

Primary Key: reservation_id
Foreign Key: guest_id (referencing Guests.guest_id)
Foreign Key: room_id (referencing Rooms.room_id)
Attributes: check_in_date, check_out_date, payment_status
Table: Reviews

Primary Key: review_id
Foreign Key: guest_id (referencing Guests.guest_id)
Foreign Key: host_id (referencing Hosts.host_id)
Foreign Key: reservation_id (referencing Reservations.reservation_id)
Attributes: rating, comment
Table: Payments (optional for guest)

Primary Key: payment_id
Foreign Key: reservation_id (referencing Reservations.reservation_id)
Attributes: payment_date, amount, payment_method