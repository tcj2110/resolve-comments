import requests
from utils import constants as git_constants


class Authenticate:
    def __init__(self, token, username):
        self.token = token
        self.username = username
        self.repos = []
        self.profile = {}

    def create_get_authorizations(self, password):
        #will be done soon
        f = "to be one"

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
                                auth=(self.username, self.token), params=params)
        self.repos = response.json()

    def get_pull_requests(self, owner, repo):
        params = {
            "state": "all",
            "sort": "updated",
            "direction": "desc"
        }
        url = git_constants.GITHUB_REPO + ("%s/%s/pulls" % (owner, repo))
        response = requests.get(url, auth=(self.username, self.token), params=params)
        return response.json()

    def get_pr_reviews(self, owner, repo, pr_id):
        #returns a list of reviews underneath a PR.
        url = 'https://api.github.com/repos/:owner/:repo/pulls/:number/reviews'

        implemented = False

    def get_pr_comments(self, owner, repo, pr_id):

        implemented = False
        url = 'https://api.github.com/repos/:owner/:repo/pulls/:number/reviews'
        #returns a list of comments

    def get_repo_issues(self, owner, repo):
        implemented = False
        url = ' https://api.github.com/repos/:owner/:repo/issues'


