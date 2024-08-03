from Service.user_service import UserService


class UserRepository(UserService):
    def __init__(self):
        super().__init__()
    
    def get_users(self):
        data = self._load()
        return list(data.get("User").values())
    
    def get_user_details(self, user_id):
        user = self.get(user_id, "User")
        if not user:
            return (False, "User not found", 404)
        return (True, user, 200)
    
    def create_user(self, user):
        valid, msg, status_code = self.validate_email(user.email)
        if not valid:
            return (False, msg, status_code)
        valid, msg, status_code = self.validate_creds(user.first_name, user.last_name)
        if not valid:
            return (False, msg, status_code)
        self.save(user)
        return (True, user.id, 201)
    
    def update_user(self, user_id, user):
        valid, msg, status_code = self.validate_email(user.email)
        if not valid:
            return (False, msg, status_code)
        if not self.validate_creds(user.first_name, user.last_name):
            return (False, msg, status_code)
        data = self._load()
        if user_id not in data.get("User"):
            return (False, "User not found", 404)
        self.update(user)
        return (True, None, 200)
    
    def delete_user(self, user_id):
        data = self._load()
        if user_id not in data.get("User"):
            return (False, "User not found", 404)
        user_reviews = self.get_user_reviews(user_id)
        for review in user_reviews:
            self.delete(review.get("id"), "Review")
        self.delete(user_id, "User")
        return (True, None, 204)
    
    def get_user_reviews(self, user_id):
        data = self._load()
        reviews = data.get("Review")
        user_reviews = []
        for review in reviews.values():
            if review.get("user_id") == user_id:
                user_reviews.append(review)
        return user_reviews