from datetime import datetime
import uuid

class BaseModel:
    def __init__(self):
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        
    def __str__(self):
        return self.id