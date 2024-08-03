from Repository.base_repository import BaseRepository

class AmenityService(BaseRepository):
    def __init__(self):
        super().__init__()
    
    def validate_amenity(self, name):
        data = self._load()
        if "Amenity" in data:
            for amenity in data["Amenity"].values():
                if amenity["name"] == name:
                    return (False, "This amenity name already exists.")
        return (True, None)

    