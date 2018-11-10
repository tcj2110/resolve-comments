
# from .utils import authenticate
import sublime_plugin
import sublime
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

TOKEN = 'Nanosoft1*'
USER = 'raphaeljunior'


class InsertPanelCommand(sublime_plugin.TextCommand):

    # Sets cursor location for comments side panel
    # to be positioned correctly
    # Returns: Original cursor location
    def set_cursor(self):
        selections = self.view.sel()
        try:
            cursor = selections[0]
            self.view.sel().clear()
            # self.view.show_at_center(sublime.Region(0,0))
            self.view.sel().add(sublime.Region(0, 0))
            return cursor
        except IndexError:
            return (0, 0)

    # Resets cursor to users original position

    def reset_cursor(self, cursor):
        print(cursor)
        self.view.sel().add(sublime.Region(cursor))

    # Placeholder method for fetching comment data
    # Will be replaced with Github API comment data
    # Returns data in list format
    def load_comment_data(self):
        # auth = authenticate.Authenticate(TOKEN, USER)
        # auth.load_repos()
        # repos = auth.repos
        # print(repos)
        # pr_comments = auth.get_pr_comments('ADI-Labs', 'culpa2', 2)
        # print(pr_comments)
        data = [["Arsalaan", "wow"]] * 4
        return data

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
        data = self.load_comment_data()
        self.view.window().show_quick_panel(data, self.on_click, 1, 2)

    # Entrypoint for plugin

    def run(self, edit):
        self.gen_comment_list()
