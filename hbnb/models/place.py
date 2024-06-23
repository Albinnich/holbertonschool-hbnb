from models.base_model import BaseModel

class Place(BaseModel):
    def __init__(self, name, description, address, city, latitude, longitude, host, num_rooms, bathrooms, price_per_night, max_guests):
        super().__init__()
        self.name = name
        self.description = description
        self.address = address
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
        self.host = host
        self.num_rooms = num_rooms
        self.bathrooms = bathrooms
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.amenities = []
        self.reviews = []

    def add_amenity(self, amenity):
        if amenity not in self.amenities:
            self.amenities.append(amenity)

    def add_review(self, review):
        self.reviews.append(review)

    def to_dict(self):
        place_dict = super().to_dict()
        place_dict.update({
            'name': self.name,
            'description': self.description,
            'address': self.address,
            'city': self.city,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'host': self.host.to_dict(),
            'num_rooms': self.num_rooms,
            'bathrooms': self.bathrooms,
            'price_per_night': self.price_per_night,
            'max_guests': self.max_guests,
            'amenities': [amenity.to_dict() for amenity in self.amenities],
            'reviews': [review.to_dict() for review in self.reviews]
        })
        return place_dict
