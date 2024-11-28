from repository.user_repository import UserRepository

class UserService:
    def __init__(self):
        self.repository = UserRepository()
        self.users = []

    def load_users(self):
        self.users = self.repository.fetch_all_users()
        
    def get_users(self):
        return self.users