import json

from Model import city
from Service.city_service import CityService


class CityRepository(CityService):
    def __init__(self):
        super().__init__()

    def _load_countries(self):
        try:
            with open("countries.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def get_all_countries(self):
        countries = self._load_countries()
        return countries

    def get_country_details(self, country_code):
        countries = self._load_countries()
        valid, msg = self.validate_country(country_code)
        if not valid:
            return (False, msg)
        return (True, countries[country_code])

    def get_country_cities(self, country_code):
        valid, msg = self.validate_country(country_code)
        if not valid:
            return (False, msg)
        data = self._load()
        cities = []
        for city in data["City"].values():
            if city["country_code"] == country_code:
                cities.append(city)
        return cities
    
    def create_new_city(self, city):
        valid, msg = self.validate_city(city.name, city.country_code)
        if not valid:
            return (False, msg)
        self.save(city)
        return (True, city.id)
    
    def get_all_cities(self):
        data = self._load()
        return list(data["City"].values())

    def get_city_details(self, city_id):
        city = self.get(city_id, "City")
        if not city:
            return (False, "City not found")
        return (True, city)
        
    def update_city(self, city_id, city):
        valid, msg = self.validate_country(city.country_code)
        if not valid:
            return (False, msg)
        data = self._load()
        if city_id not in data["City"]:
            return (False, "City not found")
        self.update(city)
        return (True, None)

    def delete_city(self, city_id):
        data = self._load()
        if city_id not in data["City"]:
            return (False, "City not found")
        self.delete(city_id, "City")
        return (True, None)