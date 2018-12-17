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
        return self.profile

    def load_repos(self):
        params = {
            "visibility": "all",
            "affiliation": "owner, collaborator, organization_member",
            "sort": "pushed",
            "direction": "asc"
        }
        response = requests.get(
            git_constants.REPOS,
            auth=(
                self.username,
                self.token),
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
        response = requests.get(
            url,
            auth=(
                self.username,
                self.token),
            params=params)
        return response.json()

    def get_pr_reviews(self, owner, repo, pr_id):
        url = 'https://api.github.com/repos/:owner/:repo/pulls/:number/reviews'
        # list = []
        url = "https://api.github.com/repos/:" + str(owner) + "/:" + str(repo)
        url += "/pulls/:" + str(pr_id) + "/reviews"

        params = {}
        response = requests.get(

        ''' response = requests.get(

            url,
            auth=(
                self.username,
                self.token),
            params=params)
        return response.json() '''

    def get_pr_comments(self, owner, repo, pr_id):
        url = git_constants.GITHUB_REPO + \
            ("%s/%s/pulls/%s/comments" % (owner, repo, pr_id))
        params = {
            "sort": "created",
            "direction": "desc"
        }
        print(url)
        response = requests.get(url, auth=(self.username, self.token), params=params)
        return response.json()

    ##Kevin edit 12/16

    def get_repo_issues(self, owner, repo):

        ##implemented = False

        url = ' https://api.github.com/repos/:owner/:repo/issues'
        url = git_constants.GITHUB_REPO + \
              ("/repos/%s/%s/issues" % (owner , repo))
        params = {
            "filter": "all",
            "sort": "created",
            "direction": "desc"

        }
        response = requests.get(url, auth=(self.username, self.token), params=params)
        return response.json()

    def update_repo_issues(self, owner, repo, number, title, body , assignee, state , milestone, labels, assignees):
        #assumes user has push access
        #title and body are title, contents of the issues
        url = 'https://api.github.com/repos/:owner/:repo/issues/:number'
        url = git_constants.GITHUB_REPO + \
              ("repos/%s/%s/issues/%s" % (owner, repo, number))

        params = {
            "title":title,
            "body":body ,
            "assignee":assignee,
            "state":state,
            "milestone":milestone,
            "labels":labels,
            "assignees": assignees,
        }
        response = requests.patch(url, auth=(self.username, self.token), params=params)
        return response.json()
    #close issues
    #very similar to update, the only change is the parameter
    #for 'state' should be closed
    def close_repo_issues(self ,owner, repo, number, title, body , assignee, state  , milestone, labels, assignees ):
        url = 'https://api.github.com/repos/:owner/:repo/issues/:number'
        url = git_constants.GITHUB_REPO + \
              ("repos/%s/%s/issues/%s" % (owner, repo, number))
        assert (state =="closed")
        params = {
            "title": title,
            "body": body,
            "assignee": assignee,
            "state": "closed",
            "milestone": milestone,
            "labels": labels,
            "assignees": assignees,
        }
        response = requests.patch(url, auth=(self.username, self.token), params=params)
        return response.json()

    """Given a review comment, comment, review number, 
    thread ID, update the GitHub API with new comments. """
    def post_pr_comments(self, owner ,repo, number ,commit_id, comment_body ,event,comments ):
        ##needs further testing
        #body must not be empty if event=="REQUEST_CHANGES" or event=="COMMENT"
        if (event=="REQUEST_CHANGES"):
            assert (comment_body != "")
        if (event=="COMMENT"):
            assert (comment_body != "")
        url ='https://api.github.com/repos/:owner/:repo/pulls/:number/reviews'
        url = git_constants.GITHUB_REPO + \
              ("repos/%s/%s/pulls/%s/reviews" % (owner, repo, number))
        params = {
            "commit_id":commit_id ,
            "comment_body":comment_body ,
            "event": event,
            "comments" : comments,
        }
        response = requests.post(url, auth=(self.username, self.token), params=params)

        params = {
            "state": "all",
            "sort": "updated",
            "direction": "desc"
        }
        url = git_constants.GITHUB_REPO + ("%s/%s/issues" % (owner, repo))
        response = requests.get(
            url,
            auth=(
                self.username,
                self.token),
            params=params)

        return response.json()
