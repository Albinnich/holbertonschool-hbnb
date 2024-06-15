import uuid
from datetime import datetime

class Country:
    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()

    def delete(self):
        pass

    def __str__(self):
        return f"[Country] ({self.id}) {self.__dict__}"
