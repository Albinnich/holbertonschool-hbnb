from Repository.base_repository import BaseRepository


class PlaceService(BaseRepository):
    def __init__(self):
        super().__init__()
    
    def validate_place(self, address):
        data = self._load()
        if "Place" in data:
            for place in data["Place"].values():
                if place.get("address") == address:
                    return (False, "Address already exists")
        return (True, None)
        
    def validate_cootdinates(self, latitude, longitude):
        if latitude > 90 or latitude < -90:
            return (False, "Latitude must be between -90 and 90")
        if longitude > 180 or longitude < -180:
            return (False, "Longitude must be between -180 and 180")
        return (True, None)
    
    def validate_quantity(self, number_of_rooms, number_of_bathrooms, max_guests):
        if number_of_rooms < 1:
            return (False, "Number of rooms must be greater than 0")
        if number_of_bathrooms < 1:
            return (False, "Number of bathrooms must be greater than 0")
        if max_guests < 1:
            return (False, "Max guests must be greater than 0")
        return (True, None)
    
    def validate_price(self, price):
        if price < 0:
            return (False, "Price must be greater than 0")
        return (True, None)
    
    def validate_city(self, city_id):
        city = self.get(city_id, "City")
        if not city:
            return (False, "City not found")
        return (True, None)
    
    def validate_host(self, host_id):
        host = self.get(host_id, "User")
        if not host:
            return (False, "Host not found")
        return (True, None)
    
    def validate_amentities(self, amenity_ids):
        data = self._load()
        if "Amenity" in data:
            for amenity_id in amenity_ids:
                if amenity_id not in data["Amenity"]:
                    return (False, "Amenity not found")
        return (True, None)