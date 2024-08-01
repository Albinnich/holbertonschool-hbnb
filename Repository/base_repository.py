import json
import os

from Persistence.IPersistence import IPersistenceManager

class BaseRepository(IPersistenceManager):
    def __init__(self):
        self.FILE_PPATH = "data.json"
        
        if not os.path.isfile(self.FILE_PPATH):
            with open(self.FILE_PPATH, "w") as file:
                json.dump({}, file)
                
    def create(self, entity):
        entity_id = entity.id
        entity_type = type(entity).__name__
        data = self.load()
        if entity_type not in data:
            data[entity_type] = {}
        data[entity_type][entity_id] = entity.__dict__
        with open(self.FILE_PPATH, "w") as file:
            json.dump(data, file)
            
        def get (self, entity_id, entity_type):
            data = self.load()
            if entity_type not in data:
                return False
            if entity_id not in data[entity_type]:
                return False
            return data[entity_type][entity_id]
        
        def update(self, entity):
            entity_id = entity.id
            entity_type = type(entity).__name__
            data = self.load()
            if entity_type not in data:
                return False
            if entity_id not in data[entity_type]:
                return False
            data[entity_type][entity_id] = entity.__dict__
            with open(self.FILE_PPATH, "w") as file:
                json.dump(data, file)
                
        def delete(self, entity_id, entity_type):
            data = self.load()
            if entity_type not in data:
                return False
            if entity_id not in data[entity_type]:
                return False
            del data[entity_type][entity_id]
            with open(self.FILE_PPATH, "w") as file:
                json.dump(data, file)
                
        def load(self):
            with open(self.FILE_PPATH, "r") as file:
                return json.load(file)
            
        def write(self, data):
            with open(self.FILE_PPATH, "w") as file:
                json.dump(data, file)