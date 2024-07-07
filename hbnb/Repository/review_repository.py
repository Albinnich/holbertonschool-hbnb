from Service.review_service import ReviewService


class ReviewRepository(ReviewService):
    def __init__(self):
        super().__init__()
    
    def get_all_reviews(self):
        data = self._load()
        return list(data.get("Review").values())
    
    def get_review_details(self, review_id):
        data = self._load()
        if review_id not in data.get("Review"):
            return (False, "Review not found", 404)
        return (True, data.get("Review").get(review_id), 200)
    
    def get_user_reviews(self, user_id):
        data = self._load()
        if user_id not in data.get("User"):
            return (False, "User not found", 404)
        reviews = data.get("Review")
        user_reviews = []
        for review in reviews.values():
            if review.get("user_id") == user_id:
                user_reviews.append(review)
        return (True, user_reviews, 200)
    
    def get_place_reviews(self, place_id):
        data = self._load()
        if place_id not in data.get("Place"):
            return (False, "Place not found", 404)
        reviews = data.get("Review")
        place_reviews = []
        for review in reviews.values():
            if review.get("place_id") == place_id:
                place_reviews.append(review)
        return (True, place_reviews, 200)
    
    def create_new_review(self, review):
        valid, msg, status_code = self.validate_rating(review.rating)
        if not valid:
            return (False, msg, status_code)
        valid, msg, status_code = self.validate_user(review.user_id)
        if not valid:
            return (False, msg, status_code)
        valid, msg, status_code = self.validate_place(review.place_id)
        if not valid:
            return (False, msg, status_code)
        valid, msg, status_code = self.validate_review(review.user_id, review.place_id)
        if not valid:
            return (False, msg, status_code)
        self.save(review)
        return (True, None, 201)
    
    def update_review(self, review_id, review):
        valid, msg, status_code = self.validate_rating(review.rating)
        if not valid:
            return (False, msg, status_code)
        valid, msg, status_code = self.validate_user(review.user_id)
        if not valid:
            return (False, msg, status_code)
        valid, msg, status_code = self.validate_place(review.place_id)
        if not valid:
            return (False, msg, status_code)
        valid, msg, status_code = self.validate_review(review.user_id, review.place_id)
        if not valid:
            return (False, msg, status_code)
        data = self._load()
        if review_id not in data.get("Review"):
            return (False, "Review not found", 404)
        self.update(review)
        return (True, None, 200)
    
    def delete_review(self, review_id):
        data = self._load()
        if review_id not in data.get("Review"):
            return (False, "Review not found", 404)
        self.delete(review_id, "Review")
        return (True, None, 204)