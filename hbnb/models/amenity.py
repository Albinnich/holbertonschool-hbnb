from models.base_model import BaseModel

class Amenity(BaseModel):
    def __init__(self, name, description):
        super().__init__()
        self.name = name
        self.description = description

    def to_dict(self):
        amenity_dict = super().to_dict()
        amenity_dict.update({
            'name': self.name,
            'description': self.description
        })
        return amenity_dict
