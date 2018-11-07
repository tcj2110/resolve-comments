import requests
from utils import constants as git_constants
from github import Github

# Check if an access token exists and if not create one
# Initialize a github class object with the access token
class Plugin:
    def __init__(self):
        if self.has_run():
            access_token = open("auth.txt")
        else:
            print("Visit this link to generate your access token: ")
            print("Be sure to enable all desired scopes")
            print("https://github.com/settings/tokens/new")
            access_token = raw_input("Paste the access token you received: ")

            file = open("auth.txt", "w+")
            file.write(access_token)
            file.close()

        self.github = Github(access_token)

    def has_run(self):
        return os.files.exists(auth)

# This is how we can use the above with pull requests
class PullRequests():
    def show(self):
        pulls = Plugin.github.get_pulls(state='open',
                                        sort='created',
                                        base='master')
        all_pulls = []
        for p in pulls.get_num_pages():
            all_pulls.append(Plugin.github.get_pulls(state='open',
                                                     sort='created',
                                                     base='master',
                                                     page=p))

    def comments(self):
        return Plugin.github.get_pulls(state='open',
                                       sort='created',
                                       base='master').get_comments()

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

#        # for later in the semester, this function will return a list
#        implemented = False
#        return list

    def get_pr_comments(self, owner, repo, pr_id):
#<<<<<<< HEAD
#        implemented = False
#        url = 'https://api.github.com/repos/:owner/:repo/pulls/:number/reviews'
        #returns a list of comments
#        url = "https://api.github.com/repos/:" + str(owner)+  "/:" +str(repo)
#        url+=  "/pulls/:"+str(pr_id)+"/reviews"
#=======
#        url = git_constants.GITHUB_REPO + ("%s/%s/pulls/%s/comments" % (owner, repo, pr_id))
#        params = {
#            "sort": "created",
#            "direction": "desc"
#        }
#        print(url)
#>>>>>>> c9a694db5a9fb87b0c346f5fb00e7fa4ae3a8a10
#        response = requests.get(url, auth=(self.username, self.token), params=params)
#        return response.json()

    def get_repo_issues(self, owner, repo):
        implemented = False
        url = ' https://api.github.com/repos/:owner/:repo/issues'
