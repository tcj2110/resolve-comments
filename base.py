
import sublime_plugin
# import sublime
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import authenticate  # noqa: E402

TOKEN = 'Nanosoft1*'
USER = 'raphaeljunior'


class InsertPanelCommand(sublime_plugin.TextCommand):

    # Method opens up input window and prompts user for token and username

    def user_token_input(self):
        self.view.window().show_input_panel(
            caption="Credential Prompt",
            initial_text="Username:",
            on_done=None,
            on_change=None,
            on_cancel=None)

        return TOKEN, USER

    # Generates simple list HTML for comment data
    # Returns: HTML

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

    def on_click(self, index):
        if(index == -1):
            return -1

    #  Manager function that uses helper functions to show
    #  comments in side popup

    def gen_comment_list(self):
        data = load_quick_panel_data(self.token, self.user)
        self.view.window().show_quick_panel(data, self.on_click, 1, 2)

    # Entrypoint for plugin

    def run(self, edit):
        self.token, self.user = self.user_token_input()
        self.gen_comment_list()

# Placeholder method for fetching comment data
# Will be replaced with Github API comment data
# Returns data in list format


def load_quick_panel_data(token, user):
    auth = authenticate.Authenticate(token, user)
    # auth.load_repos()
    # repos = auth.repos
    # print(repos)
    data = []
    pull_requests = auth.get_pull_requests('Raphaeljunior', 'resolve-comments')
    for req in pull_requests:
        title = req['title']
        body = req['body']
        content = [title, body]
        data.append(content)
    return data
