import requests

class UserRepository:
    API_URL = "https://jsonplaceholder.typicode.com/users"

    @staticmethod
    def fetch_all_users():
        response = requests.get(UserRepository.API_URL)
        response.raise_for_status()
        return response.json()