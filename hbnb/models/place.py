import uuid
from datetime import datetime

class Place:
    def __init__(self, name, description, number_rooms, max_guest, price_by_night):
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.number_rooms = number_rooms
        self.max_guest = max_guest
        self.price_by_night = price_by_night
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[Place] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def delete(self)
        pass
