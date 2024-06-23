from persistence.data_manager import DataManager
from models.user import User

data_manager = DataManager()

# Create a new user
new_user = User(email="user@example.com", password="password", first_name="First", last_name="Last")
data_manager.save(new_user)

# Retrieve the user
retrieved_user = data_manager.get(new_user.id, 'User')
print(retrieved_user)

# Update the user
new_user.first_name = "UpdatedFirst"
data_manager.update(new_user)

# Delete the user
data_manager.delete(new_user.id, 'User')
