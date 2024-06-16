import uuid
from datetime import datetime

class User:
    emails = set()

    def __init__(self, email, first_name, last_name, password):
        if email in User.emails:
            raise ValueError("Email is not available")
        self.id = str(uuid.uuid4())
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        User.emails.add(email)

    def save(self):
        self.updated_at = datetime.now()

    def delete(self):
        User.emails.remove(self.email)

    def __str__(self):
        return f"[User] ({self.id}) {self.__dict__}"
