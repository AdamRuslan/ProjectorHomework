-- Users table
CREATE TABLE Users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT,
    email TEXT,
    first_name TEXT,
    last_name TEXT,
    phone_number TEXT,
    registration_date TEXT,
    user_type TEXT
);

-- Hosts table
CREATE TABLE Hosts (
    host_id INTEGER PRIMARY KEY,
    bio TEXT,
    profile_picture TEXT,
    location TEXT,
    FOREIGN KEY (host_id) REFERENCES Users (user_id)
);

-- Guests table
CREATE TABLE Guests (
    guest_id INTEGER PRIMARY KEY,
    profile_picture TEXT,
    location TEXT,
    FOREIGN KEY (guest_id) REFERENCES Users (user_id)
);

-- Rooms table
CREATE TABLE Rooms (
    room_id INTEGER PRIMARY KEY,
    host_id INTEGER,
    room_type TEXT,
    description TEXT,
    capacity INTEGER,
    price_per_night REAL,
    has_ac INTEGER,
    has_refrigerator INTEGER,
    FOREIGN KEY (host_id) REFERENCES Hosts (host_id)
);

-- Reservations table
CREATE TABLE Reservations (
    reservation_id INTEGER PRIMARY KEY,
    guest_id INTEGER,
    room_id INTEGER,
    check_in_date TEXT,
    check_out_date TEXT,
    payment_status TEXT,
    FOREIGN KEY (guest_id) REFERENCES Guests (guest_id),
    FOREIGN KEY (room_id) REFERENCES Rooms (room_id)
);

-- Reviews table
CREATE TABLE Reviews (
    review_id INTEGER PRIMARY KEY,
    guest_id INTEGER,
    host_id INTEGER,
    reservation_id INTEGER,
    rating INTEGER,
    comment TEXT,
    FOREIGN KEY (guest_id) REFERENCES Guests (guest_id),
    FOREIGN KEY (host_id) REFERENCES Hosts (host_id),
    FOREIGN KEY (reservation_id) REFERENCES Reservations (reservation_id)
);

-- Payments table (optional for guest)
CREATE TABLE Payments (
    payment_id INTEGER PRIMARY KEY,
    reservation_id INTEGER,
    payment_date TEXT,
    amount REAL,
    payment_method TEXT,
    FOREIGN KEY (reservation_id) REFERENCES Reservations (reservation_id)
);
