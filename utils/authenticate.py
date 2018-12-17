import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import requests  # noqa: E402
import constants as git_constants  # noqa: E402


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
            url,
            auth=(
                self.username,
                self.token),
            params=params)
        return response.json()

    def get_pr_comments(self, owner, repo, pr_id):
        url = git_constants.GITHUB_REPO + \
            ("%s/%s/pulls/%s/comments" % (owner, repo, pr_id))
        params = {
            "sort": "created",
            "direction": "desc"
        }

        response = requests.get(
            url,
            auth=(
                self.username,
                self.token),
            params=params)
        print("RESPONSE")
        print(response.json())
        return response.json()

    # list all the issues, given a repository name and correct credentials
    def get_repo_issues(self, owner, repo):
        params = {
            # "state": "all",
            # "sort": "updated",
            # "direction": "desc"
        }
        url = git_constants.GITHUB_REPO + ("%s/%s/issues" % (owner, repo))
        response = requests.get(
            url,
            auth=(
                self.username,
                self.token),
            params=params)

        return response.json()

    # given a specific issue, we can list all the comments
    def get_comments_on_issue(self, owner, repo, number):
        # url='https://api.github.com/repos/:owner/:repo/issues/:number/comments'
        params = {
        }
        url = git_constants.GITHUB_REPO + \
            ("%s/%s/issues/%s/comments" % (owner, repo, number))
        response = requests.get(
            url,
            auth=(
                self.username,
                self.token),
            params=params)
        return response.json()

    def post_issue_comment(self, owner, repo, number, body):
        assert("body!=""")
        params = {
            "body": body
        }
        url = git_constants.GITHUB_REPO + \
            ("%s/%s/issues/%s/comments" % (owner, repo, number))
        response = requests.get(
            url,
            auth=(
                self.username,
                self.token),
            params=params)
        return response.json()

    def post_pr_comment(
            self,
            owner,
            repo,
            number,
            body,
            commit_id,
            path,
            position):
        # note: all paramaters are required and position must be an integer
        params = {
            "body": body,
            "commit_id": commit_id,
            "path": path,
            "position": position
        }
        url = git_constants.GITHUB_REPO + \
            ("%s/%s/pulls/%s/comments" % (owner, repo, number))
        response = requests.post(
            url,
            auth=(
                self.username,
                self.token),
            params=params)
        return response.json()

    def edit_pr_comment(self, owner, repo, comment_id, body):
        # url=https://api.github.com/repos/:owner/:repo/pulls/comments/:comment_id
        # note: body is required
        params = {
            "body": body
        }
        url = git_constants.GITHUB_REPO + \
            ("%s/%s/pulls/comments/%s" % (owner, repo, comment_id))
        response = requests.patch(
            url,
            auth=(
                self.username,
                self.token),
            params=params)
        return response.json()

    def del_pr_comment(self, owner, repo, comment_id):
        # url
        # ='https://api.github.com/repos/:owner/:repo/pulls/comments/:comment_id

        params = {}
        url = git_constants.GITHUB_REPO + \
            ("%s/%s/pulls/comments/%s" % (owner, repo, comment_id))
        response = requests.delete(
            url,
            auth=(
                self.username,
                self.token),
            params=params)
        # below should return 204
        return response.status_code()


# TOKEN = 'stuy.2063'
# USER = 'kmejia'
# x = Authenticate(TOKEN, USER)
# pr = x.get_repo_issues( 'RaphaelJunior', 'resolve-comments')
# print(pr)
#
# pr2 = x.get_comments_on_issue( 'RaphaelJunior', 'resolve-comments' , 20)
# print(pr2)
#
