from abc import ABC, abstractmethod

class IPersistenceManager(ABC):
    @abstractmethod
    def save(self, entity):
        pass

    @abstractmethod
    def get(self, entity_id, entity_type):
        pass

    @abstractmethod
    def update(self, entity):
        pass

    @abstractmethod
    def delete(self, entity_id, entity_type):
        pass

class DataManager(IPersistenceManager):
    def save(self, entity):
        # Logic to save entity to storage
        pass

    def get(self, entity_id, entity_type):
        # Logic to retrieve an entity based on ID and type
        pass

    def update(self, entity):
        # Logic to update an entity in storage
        pass

    def delete(self, entity_id, entity_type):
        # Logic to delete an entity from storage
        pass