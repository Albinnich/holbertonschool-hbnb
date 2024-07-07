from Service.place_service import PlaceService


class PlaceRepository(PlaceService):
    def __init__(self):
        super().__init__()
    
    def get_all_places(self):
        data = self._load()
        return list(data.get("Place").values())
    
    def get_place_details(self, place_id):
        place = self.get(place_id, "Place")
        if not place:
            return (False, "Place not found")
        return (True, place)
    
    def create_place(self, place):
        valid, msg = self.validete_place(place.address)
        if not valid:
            return (False, msg)
        valid, msg = self.validate_cootdinates(place.latitude, place.longitude)
        if not valid:
            return (False, msg)
        valid, msg = self.validate_quantity(place.number_of_rooms, place.number_of_bathrooms, place.max_guests)
        if not valid:
            return (False, msg)
        valid, msg = self.validate_price(place.price_per_night)
        if not valid:
            return (False, msg)
        valid, msg = self.validate_city(place.city_id)
        if not valid:
            return (False, msg)
        valid, msg = self.validate_host(place.host_id)
        if not valid:
            return (False, msg)
        valid, msg = self.validate_amentities(place.amenity_ids)
        if not valid:
            return (False, msg)
        self.save(place)
        return (True, place.id)
    
    def update_place(self, place_id, place):
        valid, msg = self.validate_place(place)
        if not valid:
            return (False, msg)
        valid, msg = self.validate_cootdinates(place.latitude, place.longitude)
        if not valid:
            return (False, msg)
        valid, msg = self.validate_quantity(place.number_of_rooms, place.number_of_bathrooms, place.max_guests)
        if not valid:
            return (False, msg)
        valid, msg = self.validate_price(place.price_per_night)
        if not valid:
            return (False, msg)
        valid, msg = self.validate_city(place.city_id)
        if not valid:
            return (False, msg)
        valid, msg = self.validate_amentities(place.amenity_ids)
        if not valid:
            return (False, msg)
        data = self._load()
        if place_id not in data.get("Place"):
            return (False, "Place not found")
        self.update(place)
        return (True, None)
        
    
    def delete_place(self, place_id):
        data = self._load()
        if place_id not in data.get("Place"):
            return (False, "Place not found")
        place_reviews = self.get_place_reviews(place_id)
        print(place_reviews)
        for review in place_reviews:
            self.delete(review.get("id"), "Review")
        self.delete(place_id, "Place")
        return (True, None)
    
    def get_place_reviews(self, place_id):
        data = self._load()
        reviews = data.get("Review")
        place_reviews = []
        for review in reviews.values():
            if review.get("place_id") == place_id:
                place_reviews.append(review)
        return place_reviews
    