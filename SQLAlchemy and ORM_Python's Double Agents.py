from sqlalchemy import Column, Integer, String, Date, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'Users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    phone_number = Column(String)
    registration_date = Column(Date)
    user_type = Column(String)
    
    # Relationship with Reservations table
    reservations = relationship('Reservation', back_populates='guest')

class Host(Base):
    __tablename__ = 'Hosts'
    
    id = Column(Integer, primary_key=True)
    bio = Column(String)
    profile_picture = Column(String)
    location = Column(String)
    
    # Relationship with User table
    user_id = Column(Integer, ForeignKey('Users.id'))
    user = relationship('User', back_populates='hosts')
    
    # Relationship with Rooms table
    rooms = relationship('Room', back_populates='host')

class Guest(Base):
    __tablename__ = 'Guests'
    
    id = Column(Integer, primary_key=True)
    profile_picture = Column(String)
    location = Column(String)
    
    # Relationship with User table
    user_id = Column(Integer, ForeignKey('Users.id'))
    user = relationship('User', back_populates='guests')

class Room(Base):
    __tablename__ = 'Rooms'
    
    id = Column(Integer, primary_key=True)
    host_id = Column(Integer, ForeignKey('Hosts.id'))
    room_type = Column(String)
    description = Column(String)
    capacity = Column(Integer)
    price_per_night = Column(Float)
    has_ac = Column(Boolean)
    has_refrigerator = Column(Boolean)
    
    # Relationship with Host table
    host = relationship('Host', back_populates='rooms')
    
    # Relationship with Reservations table
    reservations = relationship('Reservation', back_populates='room')

class Reservation(Base):
    __tablename__ = 'Reservations'
    
    id = Column(Integer, primary_key=True)
    guest_id = Column(Integer, ForeignKey('Guests.id'))
    room_id = Column(Integer, ForeignKey('Rooms.id'))
    check_in_date = Column(Date)
    check_out_date = Column(Date)
    payment_status = Column(String)
    
    # Relationship with Guest table
    guest = relationship('Guest', back_populates='reservations')
    
    # Relationship with Room table
    room = relationship('Room', back_populates='reservations')
    
    # Relationship with Payments table
    payment = relationship('Payment', uselist=False, back_populates='reservation')

class Payment(Base):
    __tablename__ = 'Payments'
    
    id = Column(Integer, primary_key=True)
    reservation_id = Column(Integer, ForeignKey('Reservations.id'))
    payment_date = Column(Date)
    amount = Column(Float)
    payment_method = Column(String)
    
    # Relationship with Reservation table
    reservation = relationship('Reservation', back_populates='payment')

class Review(Base):
    __tablename__ = 'Reviews'
    
    id = Column(Integer, primary_key=True)
    guest_id = Column(Integer, ForeignKey('Guests.id'))
    host_id = Column(Integer, ForeignKey('Hosts.id'))
    reservation_id = Column(Integer, ForeignKey('Reservations.id'))
    rating = Column(Integer)
    comment = Column(String)
    
    # Relationship with Guest table
    guest = relationship('Guest')
    
    # Relationship with Host table
    host = relationship('Host')
    
    # Relationship with Reservation table
    reservation = relationship('Reservation')

