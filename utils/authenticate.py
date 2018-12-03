import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import requests  # noqa: E402
from utils import constants as git_constants  # noqa: E402


class Authenticate:
    def __init__(self, token, username):
        self.token = token
        self.username = username
        self.repos = []
        self.profile = {}

    def create_get_authorizations(self, password):
        # will be done soon, not the MVP
        # f = "to be one"
        pass

    def get_profile(self):
        response = requests.get(git_constants.GITHUB_USER_URL,
                                auth=(self.username, self.token))
        self.profile = response.json()
        print(self.profile)

    def load_repos(self):
        params = {
            "visibility": "all",
            "affiliation": "owner, collaborator, organization_member",
            "sort": "pushed",
            "direction": "asc"
        }
        response = requests.get(git_constants.REPOS,
                                auth=(self.username, self.token),
                                params=params)
        self.repos = response.json()
        print(self.repos)

    def get_pull_requests(self, owner, repo):
        params = {
            "state": "all",
            "sort": "updated",
            "direction": "desc"
        }
        url = git_constants.GITHUB_REPO + ("%s/%s/pulls" % (owner, repo))
        response = requests.get(url,
                                auth=(self.username, self.token),
                                params=params)
        return response.json()

    def get_pr_reviews(self, owner, repo, pr_id):
        url = 'https://api.github.com/repos/:owner/:repo/pulls/:number/reviews'
        # list = []
        url = "https://api.github.com/repos/:" + str(owner) + "/:" + str(repo)
        url += "/pulls/:" + str(pr_id) + "/reviews"
        response = requests.get(url,
                                auth=(self.username, self.token),
                                params=params)
        return response.json()

    def get_pr_comments(self, owner, repo, pr_id):
        url = git_constants.GITHUB_REPO + \
            ("%s/%s/pulls/%s/comments" % (owner, repo, pr_id))
        params = {
            "sort": "created",
            "direction": "desc"
        }
        print(url)
        response = requests.get(url,
                                auth=(self.username, self.token),
                                params=params)
        return response.json()

    def get_repo_issues(self, owner, repo):
        # implemented = False
        # url = ' https://api.github.com/repos/:owner/:repo/issues'
        pass
