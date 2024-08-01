from Model.basemodel import BaseModel

class Amenity(BaseModel):
    def __init__(self, name, description):
        super().__init__()
        self.name = name
        self.description = description
        
    def __str__(self):
        return self.id