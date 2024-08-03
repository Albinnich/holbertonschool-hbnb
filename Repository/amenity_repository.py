from Repository.base_repository import BaseRepository
from Service.amenity_service import AmenityService

class AmenityRepository(AmenityService):
    def __init__(self):
        super().__init__()
    
    def get_amenities(self):
        data = self._load()
        return list(data["Amenity"].values())
    
    def get_amenity_details(self, amenity_id):
        amenity = self.get(amenity_id, "Amenity")
        if not amenity:
            return (False, "Amenity not found")
        return (True, amenity)


    def create_amenity(self, amenity):
        valid, msg = self.validate_amenity(amenity.name)
        if not valid:
            return (False, msg)
        self.save(amenity)
        return (True, amenity.id)    

    def update_amenity(self, amenity_id, amenity):
        data = self._load()
        valid, msg = self.validate_amenity(amenity.name)
        if not valid:
            return (False, msg)
        if amenity_id not in data["Amenity"]:
            return (False, "Amenity not found")
        self.update(amenity)
        return (True, None)
    
    def delete_amenity(self, amenity_id):
        data = self._load()
        if amenity_id not in data["Amenity"]:
            return (False, "Amenity not found")
        self.delete(amenity_id, "Amenity")
        return (True, None)