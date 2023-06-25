-- Users table
CREATE TABLE Users (
    id INTEGER PRIMARY KEY,
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
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    bio TEXT,
    profile_picture TEXT,
    location TEXT,
    FOREIGN KEY (user_id) REFERENCES Users (id)
);

-- Guests table
CREATE TABLE Guests (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    profile_picture TEXT,
    location TEXT,
    FOREIGN KEY (user_id) REFERENCES Users (id)
);

-- Rooms table
CREATE TABLE Rooms (
    id INTEGER PRIMARY KEY,
    host_id INTEGER,
    room_type TEXT,
    description TEXT,
    capacity INTEGER,
    price_per_night REAL,
    is_ac_available BOOLEAN,
    has_refrigerator BOOLEAN,
    FOREIGN KEY (host_id) REFERENCES Hosts (id)
);

-- Reservations table
CREATE TABLE Reservations (
    id INTEGER PRIMARY KEY,
    guest_id INTEGER,
    room_id INTEGER,
    check_in_date TEXT,
    check_out_date TEXT,
    payment_status TEXT,
    FOREIGN KEY (guest_id) REFERENCES Guests (id),
    FOREIGN KEY (room_id) REFERENCES Rooms (id)
);

-- Reviews table
CREATE TABLE Reviews (
    id INTEGER PRIMARY KEY,
    guest_id INTEGER,
    reservation_id INTEGER,
    rating INTEGER,
    comment TEXT,
    FOREIGN KEY (guest_id) REFERENCES Guests (id),
    FOREIGN KEY (reservation_id) REFERENCES Reservations (id)
);

-- Payments table (optional for guest)
CREATE TABLE Payments (
    id INTEGER PRIMARY KEY,
    reservation_id INTEGER,
    payment_date TEXT,
    amount REAL,
    payment_method TEXT,
    FOREIGN KEY (reservation_id) REFERENCES Reservations (id)
);

