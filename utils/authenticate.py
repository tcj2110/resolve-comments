import requests
from utils import constants as git_constants


class Authenticate:
    def __init__(self, token, username):
        self.token = token
        self.username = username
        self.profile = {}

    def get_profile(self):
        response = requests.get(git_constants.GITHUB_USER_URL,
                                auth=(self.username, self.token))
        self.profile = response
        print(self.profile)

