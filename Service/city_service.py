from Repository.base_repository import BaseRepository


class CityService(BaseRepository):
    def __init__(self):
        super().__init__()

    def validate_city(self, city_name, country_code):
        data = self._load()
        if "City" in data:
            for city in data["City"].values():
                if city["name"] == city_name and city["country_code"] == country_code:
                    return (False, "This city already exists in this country.")
        return (True, None)
    
    def validate_country(self, country_code):
        with open("countries.json", "r") as file:
            data = file.read()
        if country_code not in data:
            return (False, "This country does not exist.")
        return (True, None)
    