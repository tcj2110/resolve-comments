
import sublime_plugin
import sublime
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import authenticate  # noqa: E402

TOKEN = 'Nanosoft1*'
USER = 'Raphaeljunior'

# Class provides the entrypoint for the plugin.
# All helper functions are external to
# allow for easy unit testing.


class InsertPanelCommand(sublime_plugin.TextCommand):

    # Generates simple list HTML for comment data
    '''
    def gen_comment_html(self):
        data = self.load_comment_data()
        html_arr = [
            "<style> ul { height: 100px; display: flex; flex-direction \
            : column; flex-wrap: wrap;} </style>",
            "<ul>"]
        for body in data:
            li = "<li>" + body + "</li>"
            html_arr.append(li)
        html_arr.append("</ul>")
        html_str = "".join(html_arr)
        return html_str
    '''

    # Entrypoint for plugin

    def run(self, edit):
        username_input()


# Method opens up input window and prompts username.
# When user presses enter on_done function calls
# token_input.

def username_input():
    def on_done(user_string):
        user = user_string.strip()
        token_input(user)

    def on_change(user_string):
        pass

    def on_cancel(user_string):
        print("User cancelled input")

    sublime.active_window().show_input_panel(
        caption="Username:",
        initial_text="",
        on_done=on_done,
        on_change=on_change,
        on_cancel=on_cancel)


# Method opens up input window and prompts token.
# When user presses enter on_done function calls
# gen_comment_list.

def token_input(user):
    def on_done(token_string):
        token = token_string.strip()
        gen_comment_list(token, user)

    def on_change(token_string):
        pass

    def on_cancel(token_string):
        print("User cancelled input")

    sublime.active_window().show_input_panel(
        caption="Token:",
        initial_text="",
        on_done=on_done,
        on_change=on_change,
        on_cancel=on_cancel)

#  Manager function that uses helper functions to show
#  comments in side popup


def gen_comment_list(token, user):
    data = load_quick_panel_data(
        token, user, 'Raphaeljunior', 'resolve-comments')
    sublime.active_window().show_quick_panel(data, on_click, 1, 2)

# Method that responds to clicking quickpanel item


def on_click(index):
    if(index == -1):
        return -1


# Method loads Github pull_requests data by authenticating the user and token.
# After authentication plugin retrieves pull request data based on org name
# and repo name.


def load_quick_panel_data(token, user, org, repo):

    if(user == "" or token == ""):
        error_message("Error: Username or Token Left Blank")
        return []
    auth = authenticate.Authenticate(token, user)
    data = []
    pull_requests = auth.get_pull_requests(org, repo)
    if('message' in pull_requests and
            pull_requests['message'] == 'Bad credentials'):
        error_message("Error: Username or Token Invalid")
        return []
    for req in pull_requests:
        title = req['title']
        body = req['body']
        user = req['user']['login']
        content = [title, body, user]
        data.append(content)
    return data


def error_message(e_mes):
    sublime.active_window().show_input_panel(
        caption="Error Prompt",
        initial_text=e_mes,
        on_done=None,
        on_change=None,
        on_cancel=None)
