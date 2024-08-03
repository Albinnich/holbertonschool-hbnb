import re

from Repository.base_repository import BaseRepository


class UserService(BaseRepository):
    def __init__(self):
        super().__init__()
    
    def validate_email(self, email):
        if not re.match(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$', email):
            return (False, "This is not a valid email address. Please enter a valid email address.", 400)
        data = self._load()
        if "User" in data:
            for user in data["User"].values():
                if user["email"] == email:
                    return (False, "This email address is already in use. Please enter a different email address.", 400)
        return (True, None, 200)
        
    def validate_creds(self, fname, sname):
        if fname and sname:
            return (True, None, 200)
        return (False, "Please enter both first name and last name.", 400)