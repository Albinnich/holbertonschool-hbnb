import uuid
from datetime import datetime

class Place:
    def __init__(self, name, description, address, city_id, latitude, longitude, host_id, number_of_rooms, number_of_bathrooms, price_per_night, max_guests, amenity_ids):
        self.id = None  # Assume this is set by the DataManager
        self.name = name
        self.description = description
        self.address = address
        self.city_id = city_id
        self.latitude = latitude
        self.longitude = longitude
        self.host_id = host_id
        self.number_of_rooms = number_of_rooms
        self.number_of_bathrooms = number_of_bathrooms
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.amenity_ids = amenity_ids
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update(self, name=None, description=None, address=None, city_id=None, latitude=None, longitude=None, number_of_rooms=None, number_of_bathrooms=None, price_per_night=None, max_guests=None, amenity_ids=None):
        if name:
            self.name = name
        if description:
            self.description = description
        if address:
            self.address = address
        if city_id:
            self.city_id = city_id
        if latitude:
            self.latitude = latitude
        if longitude:
            self.longitude = longitude
        if number_of_rooms:
            self.number_of_rooms = number_of_rooms
        if number_of_bathrooms:
            self.number_of_bathrooms = number_of_bathrooms
        if price_per_night:
            self.price_per_night = price_per_night
        if max_guests:
            self.max_guests = max_guests
        if amenity_ids:
            self.amenity_ids = amenity_ids
        self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()

    def delete(self):
        pass

    def __str__(self):
        return f"[Place] ({self.id}) {self.__dict__}"
