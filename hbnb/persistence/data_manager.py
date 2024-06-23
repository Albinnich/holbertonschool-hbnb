import json
import os
from models.user import User
from models.country import Country
from models.city import City
from persistence.i_persistence_manager import IPersistenceManager

class DataManager:
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

    def save_user(self, user):
        if not isinstance(user, User):
            raise ValueError("Expected instance of User")

    def save_country(self, country):
        if 'countries' not in self.data:
            self.data['countries'] = []

        self.data['countries'].append(country.to_dict())
        self._save_data()

    def save_city(self, city):
        if 'cities' not in self.data:
            self.data['cities'] = []

        self.data['cities'].append(city.to_dict())
        self._save_data()
        
        # Check if user with the same email already exists
        if self.get_user_by_email(user.email):
            raise ValueError("User with this email already exists")

        user_dict = user.to_dict()
        user_dict['id'] = len(self.data.get('users', [])) + 1  # Generate unique ID
        if 'users' not in self.data:
            self.data['users'] = []
        self.data['users'].append(user_dict)
        self._save_data()

    def get_user(self, user_id):
        users = self.data.get('users', [])
        for user in users:
            if user['id'] == user_id:
                return User(**user)
        return None

    def get_user_by_email(self, email):
        users = self.data.get('users', [])
        for user in users:
            if user['email'] == email:
                return User(**user)
        return None

    def get_countries(self):
        if 'countries' in self.data:
            return [Country(**country_data) for country_data in self.data['countries']]
        return []

    def get_country_by_code(self, country_code):
        if 'countries' in self.data:
            for country_data in self.data['countries']:
                if country_data['code'] == country_code:
                    return Country(**country_data)
        return None

     def get_cities(self):
        if 'cities' in self.data:
            return [City(**city_data) for city_data in self.data['cities']]
        return []

    def get_city_by_id(self, city_id):
        if 'cities' in self.data:
            for city_data in self.data['cities']:
                if city_data['id'] == city_id:
                    return City(**city_data)
        return None

    def update_city(self, city):
        if 'cities' in self.data:
            for idx, existing_city in enumerate(self.data['cities']):
                if existing_city['id'] == city.id:
                    self.data['cities'][idx] = city.to_dict()
                    self._save_data()
                    return
        raise ValueError("City not found")

    def update_user(self, user):
        if not isinstance(user, User):
            raise ValueError("Expected instance of User")
        
        users = self.data.get('users', [])
        for idx, existing_user in enumerate(users):
            if existing_user['id'] == user.id:
                users[idx] = user.to_dict()
                self._save_data()
                return
        raise ValueError("User not found")

    def delete_user(self, user_id):
        users = self.data.get('users', [])
        self.data['users'] = [user for user in users if user['id'] != user_id]
        self._save_data()

    def delete_city(self, city_id):
        if 'cities' in self.data:
            self.data['cities'] = [city for city in self.data['cities'] if city['id'] != city_id]
            self._save_data()
        else:
            raise ValueError("City not found")

    def get_all_users(self):
        users = self.data.get('users', [])
        return [User(**user) for user in users]

