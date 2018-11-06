import requests
from utils import constants as git_constants


class Authenticate:
    def __init__(self, token, username):
        self.token = token
        self.username = username
        self.repos = []
        self.profile = {}

    def create_get_authorizations(self, password):
        #will be done soon, not the MVP
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
        list = []
        url = "https://api.github.com/repos/:" + str(owner)+  "/:" +str(repo)
        url+=  "/pulls/:"+str(pr_id)+"/reviews"
        response = requests.get(url, auth=(self.username, self.token), params=params)
        return response.json()
  #      """
        ##for later in the semester, this function will return a list
 #       implemented = False
#        return list
 #       """

    def get_pr_comments(self, owner, repo, pr_id):
#<<<<<<< HEAD

        implemented = False
        url = 'https://api.github.com/repos/:owner/:repo/pulls/:number/reviews'
        #returns a list of comments
        url = "https://api.github.com/repos/:" + str(owner)+  "/:" +str(repo)
        url+=  "/pulls/:"+str(pr_id)+"/reviews"
#=======
        url = git_constants.GITHUB_REPO + ("%s/%s/pulls/%s/comments" % (owner, repo, pr_id))
        params = {
            "sort": "created",
            "direction": "desc"
        }
        print(url)
#>>>>>>> c9a694db5a9fb87b0c346f5fb00e7fa4ae3a8a10
        response = requests.get(url, auth=(self.username, self.token), params=params)
        return response.json()

    def get_repo_issues(self, owner, repo):
        implemented = False
        url = ' https://api.github.com/repos/:owner/:repo/issues'

##################################################################################
# This is my scratch work below
# Trying to figure out the workflow for OAuth
##################################################################################

# Given a user's username and password, generate an oauth token that
# grants permissions to:
#	repo
#	admin:org
#	admin:repo_hook
#	notifications
#	user
#	write:discussion
#	admin:gpg_key

from requests_oauthlib import OAuth2Session

# Credentials from registering the new application
client_id = GITHUB_AUTH
client_secret = '<the secret we got from GitHub>'

# OAuth endpoints given in the GitHub API documentation
authorization_base_url = 'https://github.com/login/oauth/authorize'
token_url = 'https://github.com/login/oauth/access_token'

github = OAuth2Session(client_id)

# Redirect user to GitHub for authorization
authorization_url, state = github.authorization_url(authorization_base_url)
print 'Please go here and authorize,', authorization_url

# Get the authorization verifier code from the callback url
redirect_response = raw_input('Paste the full redirect URL here:')

# Fetch the access token
access_token = github.fetch_token(token_url, client_secret=client_secret,
		authorization_response=redirect_response)
