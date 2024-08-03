from Repository.base_repository import BaseRepository


class ReviewService(BaseRepository):
    def __init__(self):
        super().__init__()
    
    def validate_rating(self, rating):
        if rating < 1 or rating > 5:
            return (False, "Rating must be between 1 and 5.", 400)
        return (True, None, 200)
    
    def validate_user(self, user_id):
        user = self.get(user_id, "User")
        if not user:
            return (False, "User not found", 404)
        return (True, None, 200)
                
    def validate_place(self, place_id):
        place = self.get(place_id, "Place")
        if not place:
            return (False, "Place not found", 404)
        return (True, None, 200)
            
    def validate_review(self, user_id, place_id):
        data = self._load()
        place = data.get("Place").get(place_id)
        if place.get("host_id") == user_id:
            return (False, "You cannot review your own place.", 400)
        return (True, None, 200)