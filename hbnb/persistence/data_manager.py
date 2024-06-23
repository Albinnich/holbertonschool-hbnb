import json
import os
from persistence.i_persistence_manager import IPersistenceManager

class DataManager(IPersistenceManager):
    def __init__(self, filename='data.json'):
        self.filename = filename
        self.data = self._load_data()

    def _load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return {}

    def _save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)

    def save(self, entity):
        entity_type = type(entity).__name__.lower()
        if entity_type not in self.data:
            self.data[entity_type] = []
        self.data[entity_type].append(entity.to_dict())
        self._save_data()

    def get(self, entity_id, entity_type):
        entity_type = entity_type.lower()
        if entity_type in self.data:
            for entity in self.data[entity_type]:
                if entity['id'] == entity_id:
                    return entity
        return None

    def update(self, entity):
        entity_type = type(entity).__name__.lower()
        if entity_type in self.data:
            for idx, existing_entity in enumerate(self.data[entity_type]):
                if existing_entity['id'] == entity.id:
                    self.data[entity_type][idx] = entity.to_dict()
                    self._save_data()
                    return
        raise ValueError("Entity not found")

    def delete(self, entity_id, entity_type):
        entity_type = entity_type.lower()
        if entity_type in self.data:
            self.data[entity_type] = [entity for entity in self.data[entity_type] if entity['id'] != entity_id]
            self._save_data()
        else:
            raise ValueError("Entity type not found")
