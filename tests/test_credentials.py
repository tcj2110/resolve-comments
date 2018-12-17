import os
import sublime
import sys
from unittest import TestCase
version = sublime.version()
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
test_credentials = sys.modules["git_comments.base"]
from utils import authenticate  # noqa: E402


# Tests if panel data is shown correctly if both username and password are
# correct


class TestUserCorrectTokenCorrect(TestCase):
    def mock_auth(self):
        return True

    def test_user_correct_token_correct(self):
        test_auth = test_credentials.check_auth(
            'Nanosoft1*', 'raphaeljunior', False)
        self.assertEqual(test_auth, self.mock_auth())

# Tests if there is an error when username is incorrect but token is correct


class TestUserIncorrectTokenCorrect(TestCase):
    def mock_auth(self):
        return {
            'documentation_url': 'https://developer.github.com/v3',
            'message': 'Bad credentials'}

    def test_user_incorrect_token_correct(self):
        test_auth = test_credentials.check_auth(
            'Nanosoft1*', 'Incorrect', False)
        self.assertDictEqual(test_auth, self.mock_auth())


# Tests if there is an error when username is incorrect but token is correct


class TestUserCorrectTokenIncorrect(TestCase):
    def mock_auth(self):
        return {
            'documentation_url': 'https://developer.github.com/v3',
            'message': 'Bad credentials'}

    def test_user_correct_token_incorrect(self):
        test_auth = test_credentials.check_auth(
            'Incorrect', 'raphaeljunior', False)
        self.assertDictEqual(test_auth, self.mock_auth())


# Tests if there is an error when username is left empty


class TestUserEmpty(TestCase):
    def mock_auth(self):
        return "Error: Username or Token Left Blank"

    def test_user_empty(self):
        test_auth = test_credentials.check_auth('Nanosoft1*', '', False)
        self.assertEqual(test_auth, self.mock_auth())


# Tests if there is an error when token is left empty


class TestTokenEmpty(TestCase):
    def mock_auth(self):
        return "Error: Username or Token Left Blank"

    def test_token_empty(self):
        test_auth = test_credentials.check_auth('', 'raphaeljunior', False)
        self.assertEqual(test_auth, self.mock_auth())


# Tests if panel data is shown correctly if both repo and org are
# correct


class TestRepoCorrectOrgCorrect(TestCase):
    def mock_panel_list(self):
        mock_panel_list = [
            ['Set up db schema and created models', '',
             'Raphaeljunior', 'Pull Request : closed'],
            ['Setup database', '', 'Raphaeljunior', 'Pull Request: closed']]
        return mock_panel_list

    def test_repo_correct_org_correct(self):
        auth = authenticate.Authenticate('Nanosoft1*', 'raphaeljunior')
        panel_data = test_credentials.load_quick_panel_data(
            auth, 'ADI-Labs', 'culpa2')
        self.assertListEqual(panel_data, self.mock_panel_list())

# Tests if there is an error when repo is incorrect but org is correct


class TestRepoCorrectOrgIncorrect(TestCase):
    def mock_panel_list(self):
        mock_panel_list = []
        return mock_panel_list

    def test_repo_correct_org_incorrect(self):
        auth = authenticate.Authenticate('Nanosoft1*', 'raphaeljunior')
        panel_data = test_credentials.load_quick_panel_data(
            auth, 'Incorrect', 'culpa2')
        self.assertListEqual(panel_data, self.mock_panel_list())

# Tests if there is an error when repo is incorrect but org is correct


class TestRepoIncorrectOrgCorrect(TestCase):
    def mock_panel_list(self):
        mock_panel_list = []
        return mock_panel_list

    def test_repo_incorrect_org_correct(self):
        auth = authenticate.Authenticate('Nanosoft1*', 'raphaeljunior')
        panel_data = test_credentials.load_quick_panel_data(
            auth, 'ADI-Labs', 'Incorrect')
        self.assertListEqual(panel_data, self.mock_panel_list())

# Tests if there is an error when repo is left empty


class TestOrgEmpty(TestCase):
    def mock_panel_list(self):
        mock_panel_list = []
        return mock_panel_list

    def test_org_empty(self):
        auth = authenticate.Authenticate('Nanosoft1*', 'raphaeljunior')
        panel_data = test_credentials.load_quick_panel_data(
            auth, '', 'culpa2')
        self.assertListEqual(panel_data, self.mock_panel_list())

# Tests if there is an error when org is left empty


class TestRepoEmpty(TestCase):
    def mock_panel_list(self):
        mock_panel_list = []
        return mock_panel_list

    def test_repo_empty(self):
        auth = authenticate.Authenticate('Nanosoft1*', 'raphaeljunior')
        panel_data = test_credentials.load_quick_panel_data(
            auth, 'ADI-Labs', '')
        self.assertListEqual(panel_data, self.mock_panel_list())
