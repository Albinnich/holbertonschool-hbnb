from Model.basemodel import BaseModel

class User(BaseModel):
    def __init__(self, email, first_name, last_name, password=""):
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        
        def __str__(self):
            return self.id
