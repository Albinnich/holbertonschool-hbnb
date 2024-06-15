import json
import os

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, 'w') as f:
            json_objects = {k: v.__dict__ for k, v in self.__objects.items()}
            json.dump(json_objects, f)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                json_objects = json.load(f)
                for key, value in json_objects.items():
                    cls_name = key.split('.')[0]
                    cls = eval(cls_name)
                    self.__objects[key] = cls(**value)
