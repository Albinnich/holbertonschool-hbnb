from Model.basemodel import BaseModel

class City(BaseModel):
    def __init__(self, name, country_id):
        super().__init__()
        self.name = name
        self.country_id = country_id
        
    def __str__(self):
        return self.id