import sublime
import sys
from unittest import TestCase

version = sublime.version()

test_credentials = sys.modules["git_comments.base"]

# Tests if panel data is shown correctly if both username and password are
# correct


class TestUserCorrectTokenCorrect(TestCase):
    def mock_panel_list(self):
        mock_panel_list = [
            ['Set up db schema and created models', '', 'Raphaeljunior'],
            ['Setup database', '', 'Raphaeljunior']]
        return mock_panel_list

    def test_user_correct_token_correct(self):
        panel_data = test_credentials.load_quick_panel_data(
            'Nanosoft1*', 'raphaeljunior', 'ADI-Labs', 'culpa2')
        self.assertListEqual(panel_data, self.mock_panel_list())

# Tests if there is an error when username is incorrect but token is correct


class TestUserIncorrectTokenCorrect(TestCase):
    def mock_panel_list(self):
        mock_panel_list = []
        return mock_panel_list

    def test_user_incorrect_token_correct(self):
        panel_data = test_credentials.load_quick_panel_data(
            'Nanosoft1*', 'Incorrect', 'ADI-Labs', 'culpa2')
        self.assertListEqual(panel_data, self.mock_panel_list())

# Tests if there is an error when username is incorrect but token is correct


class TestUserCorrectTokenIncorrect(TestCase):
    def mock_panel_list(self):
        mock_panel_list = []
        return mock_panel_list

    def test_user_correct_token_incorrect(self):
        panel_data = test_credentials.load_quick_panel_data(
            'Incorrect', 'raphaeljunior', 'ADI-Labs', 'culpa2')
        self.assertListEqual(panel_data, self.mock_panel_list())

# Tests if there is an error when username is left empty


class TestUserEmpty(TestCase):
    def mock_panel_list(self):
        mock_panel_list = []
        return mock_panel_list

    def test_user_empty(self):
        panel_data = test_credentials.load_quick_panel_data(
            'Nanosoft1*', '', 'ADI-Labs', 'culpa2')
        self.assertListEqual(panel_data, self.mock_panel_list())

# Tests if there is an error when token is left empty


class TestTokenEmpty(TestCase):
    def mock_panel_list(self):
        mock_panel_list = []
        return mock_panel_list

    def test_token_empty(self):
        panel_data = test_credentials.load_quick_panel_data(
            '', 'raphaeljunior', 'ADI-Labs', 'culpa2')
        self.assertListEqual(panel_data, self.mock_panel_list())
