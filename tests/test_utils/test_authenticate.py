import unittest
import unittest.mock as mock
from .utils.authenticate import Authenticate


TOKEN = 'afd53032060c50872c19e884c35e4ae00c046f73'
USER = 'raphaeljunior'


def mocked_requests_get(*args, **kwargs):
    return {'json': {
        "login": "Raphaeljunior",
        "id": 6213945,
        "node_id": "MDQ6VXNlcjYyMTM5NDU=",
        "avatar_url": "https://avatars0.githubusercontent.com/u/6213945?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/Raphaeljunior",
        "html_url": "https://github.com/Raphaeljunior",
        "followers_url": "https://api.github.com/users/Raphaeljunior/followers",
        "following_url": "https://api.github.com/users/Raphaeljunior/following{/other_user}",
        "gists_url": "https://api.github.com/users/Raphaeljunior/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/Raphaeljunior/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/Raphaeljunior/subscriptions",
        "organizations_url": "https://api.github.com/users/Raphaeljunior/orgs",
        "repos_url": "https://api.github.com/users/Raphaeljunior/repos",
        "events_url": "https://api.github.com/users/Raphaeljunior/events{/privacy}",
        "received_events_url": "https://api.github.com/users/Raphaeljunior/received_events",
        "type": "User",
        "site_admin": False,
        "name": None,
        "company": None,
        "blog": "",
        "location": None,
        "email": None,
        "hireable": None,
        "bio": None,
        "public_repos": 120,
        "public_gists": 1,
        "followers": 7,
        "following": 10,
        "created_at": "2013-12-18T11:31:17Z",
        "updated_at": "2018-10-26T15:13:40Z",
        "private_gists": 3,
        "total_private_repos": 8,
        "owned_private_repos": 8,
        "disk_usage": 167702,
        "collaborators": 2,
        "two_factor_authentication": False,
        "plan": {
            "name": "developer",
            "space": 976562499,
            "collaborators": 0,
            "private_repos": 9999
        }
    }}


class TestAuthenticate(unittest.TestCase):

    @mock.patch('requests.get', mocked_requests_get)
    def test_get_profile(self):
        authenticate = Authenticate(TOKEN, USER)
        authenticate.get_profile()
        self.assertDictEqual(authenticate.profile, mocked_requests_get())
