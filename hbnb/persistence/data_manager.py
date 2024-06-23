class DataManager(IPersistenceManager):
    def __init__(self):
        self.storage = {
            "users": [],
            "places": [],
            "reviews": [],
            "amenities": [],
            "cities": []
        }
        self.id_counter = 1

    def _get_entity_list(self, entity_type):
        return self.storage[entity_type]

    def _assign_id(self, entity):
        entity.id = self.id_counter
        self.id_counter += 1

    def save(self, entity):
        entity_type = entity.__class__.__name__.lower() + 's'
        entity_list = self._get_entity_list(entity_type)
        self._assign_id(entity)
        entity_list.append(entity)

    def get(self, entity_id, entity_type):
        entity_list = self._get_entity_list(entity_type)
        for entity in entity_list:
            if entity.id == entity_id:
                return entity
        return None

    def update(self, entity):
        entity_type = entity.__class__.__name__.lower() + 's'
        entity_list = self._get_entity_list(entity_type)
        for i, existing_entity in enumerate(entity_list):
            if existing_entity.id == entity.id:
                entity_list[i] = entity
                entity.updated_at = datetime.now()
                break

    def delete(self, entity_id, entity_type):
        entity_list = self._get_entity_list(entity_type)
        for i, entity in enumerate(entity_list):
            if entity.id == entity_id:
                del entity_list[i]
                break
