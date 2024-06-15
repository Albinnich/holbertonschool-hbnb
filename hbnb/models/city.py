import uuid
from datetime import datetime

class City:
    def __init__(self, name, country_id):
        self.id = str(uuid.uuid4())
        self.name = name
        self.country_id = country_id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()

    def delete(self):
        pass

    def __str__(self):
        return f"[City] ({self.id}) {self.__dict__}"
