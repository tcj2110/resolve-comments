import sublime_plugin
import sublime
import sys
import os
from subprocess import call, STDOUT, check_output
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import mongo_connect  # noqa: E402
from utils import authenticate  # noqa: E402


# Global variable for plugin preferences

preferences = {"window_size": 0.33, "issue_compact": False}


# Class provides the entrypoint for the plugin.
# All helper functions are external to
# allow for easy unit testing.


class InsertPanelCommand(sublime_plugin.TextCommand):

    # Entrypoint for application

    def run(self, edit):
        mongo_client = mongo_connect.MongoConnect()
        print(mongo_client)
        username_input()


# Text command to open preference menu


class PreferencesCommand(sublime_plugin.TextCommand):

    # Method returns screen size in print statement
    # When complete will insert screen preference to mongo

    def run(self, edit):
        preference_mode = True
        username_input(preference_mode)


# Class that stores methods to toggle plugin preferences
class PreferenceToggle:

    def __init__(self):
        self.mongo_client = mongo_connect.MongoConnect()
        self.mongo_pref = {}

    def issue_click(self, index):
        if(index == -1):
            return -1
        elif(index == 0):
            self.mongo_pref['issue_compact'] = True
        else:
            self.mongo_pref['issue_compact'] = False
        self.mongo_client.insert_pref(self.mongo_pref)

    def issue_pref(self):
        sublime.active_window().show_quick_panel(
            self.mongo_client.issue_pref, self.issue_click, 1, 2)

    def window_click(self, index):
        if(index == -1):
            return -1
        elif(index == 0):
            self.mongo_pref = {"user": self.user, "window_size": 0.33}
        elif(index == 1):
            self.mongo_pref = {"user": self.user, "window_size": 0.50}
        else:
            self.mongo_pref = {"user": self.user, "window_size": 0.66}
        self.issue_pref()

    def window_preference(self, user):
        self.user = user
        sublime.active_window().show_quick_panel(
            self.mongo_client.window_pref, self.window_click, 1, 2)

    def load_window_preference(self, user):
        global preferences
        preferences['window_size'] = self.mongo_client.load_pref(user)


# Method opens up input window and prompts username.
# When user presses enter on_done function calls
# token_input.


def username_input(mode=False):
    def on_done(user_string):
        user = user_string.strip()
        token_input(user, mode)

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

def token_input(user, mode):
    def on_done(token_string):
        token = token_string.strip()
        check_auth(token, user, mode)

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


def check_auth(token, user, mode):
    if(user == "" or token == ""):
        error_message("Error: Username or Token Left Blank")
        return "Error: Username or Token Left Blank"
    auth = authenticate.Authenticate(token, user)
    profile = auth.get_profile()
    if('message' in profile):
        error_message("Error: Bad Credentials")
        print(profile)
        return profile
    if(mode):
        toggle = PreferenceToggle()
        toggle.window_preference(user)
    else:
        gen_comment_list(token, user, auth)
    return True


#  Manager function that uses helper functions to show
#  comments in side popup


def extract_path():
    env_var = sublime.active_window().extract_variables()
    # file = env_var['file']
    if('file_path' in env_var):
        path = env_var['file_path']
    else:
        return None
    if call(["git", "branch"], stderr=STDOUT,
            stdout=open(os.devnull, 'w'), cwd=path) == 0:
        root = check_output(["git", "rev-parse", "--show-toplevel"], cwd=path)
        path = root.rstrip()
    os.chdir(path)
    # Write exception case for opening file that may not exist
    with open('./.git/config') as f:
        url = f.read().splitlines()[6]
        if(url[7] == 'g'):
            github_path = url[22:-4]
        else:
            github_path = url[26:-4]
    org, repo = github_path.split('/')
    return (org, repo)


def gen_comment_list(token, user, auth):
    global data_store
    path = extract_path()
    if(not path):
        error_message("Error: file not found in git repository")
        return
    org, repo = path
    data_store = load_quick_panel_data(
        auth, org, repo)
    pref_toggle = PreferenceToggle()
    pref_toggle.load_window_preference(user)
    sublime.active_window().show_quick_panel(data_store, on_click, 1, 2)


# Method loads Github pull_requests data by authenticating the user and token.
# After authentication plugin retrieves pull request data based on org name
# and repo name.

def load_quick_panel_data(auth, org, repo):

    data = []
    pull_requests = auth.get_pull_requests(org, repo)
    if('message' in pull_requests and
            (pull_requests['message'] == 'Bad credentials' or
                pull_requests['message'] == 'Not Found')):
        error_message("Error: " + pull_requests['message'])
        return []
    for req in pull_requests:
        title = req['title']
        body = req['body']
        user = req['user']['login']
        content = [title, body, user]
        data.append(content)
    '''issues = auth.get_repo_issues(org, repo)
    print(issues)
    if('message' in issues and
        (issues['message'] == 'Bad credentials' or
            issues['message'] == 'Not Found')):
        error_message("Error: " + issues['message'])
        return []
    for issue in issues:
        title = issue['title']
        body = issue['body']
        user = issue['user']['login']
        content = [title, body, user]
        data.append(content) '''

    return data


# Method that responds to clicking quickpanel item


def on_click(index):
    if(index == -1):
        return -1

    sublime.active_window().set_layout({
        "cols": [
            0.0, preferences['window_size'], 1.0], "rows": [
            0.0, 1.0], "cells": [
            [
                0, 0, 1, 1], [
                1, 0, 2, 1]]})
    for nGroup in range(sublime.active_window().num_groups()):
        print(nGroup)
        if len(sublime.active_window().views_in_group(nGroup)) == 0:
            print(nGroup)
            sublime.active_window().focus_group(nGroup)
            createdView = sublime.active_window().new_file()
            # createdView.erase_phantoms("test")
            '''for i in range(len(data_store)):
                createdView.add_phantom(
                    "test", createdView.sel()[0], gen_comment_html(
                        data_store[i]), sublime.LAYOUT_BLOCK)'''
            createdView.add_phantom(
                "test", createdView.sel()[0], gen_comment_html(
                    data_store[index]), sublime.LAYOUT_BLOCK)
        elif(nGroup == 1):
            sublime.active_window().focus_group(nGroup)
            createdView = sublime.active_window().active_view_in_group(nGroup)
            createdView.add_phantom(
                "test", createdView.sel()[0], gen_comment_html(
                    data_store[index]), sublime.LAYOUT_BLOCK)


def gen_comment_html(data):
    html_arr = [
        "<style> ul { display: flex; flex-direction \
        : column; flex-wrap: wrap;} </style>",
        "<ul>"]
    html_arr.append("<h3>" + data[0] + "</h3>")
    if(not preferences['issue_compact']):
        for i in range(1, len(data)):
            li = "<li>" + data[i] + "</li>"
            html_arr.append(li)
        html_arr.append("</ul>")
        html_arr.append(
            "Click <a href='http://www.yahoo.com'>here</a> to go to yahoo.")
    html_str = "".join(html_arr)
    return html_str


def error_message(e_mes):
    sublime.active_window().show_input_panel(
        caption="Error Prompt",
        initial_text=e_mes,
        on_done=None,
        on_change=None,
        on_cancel=None)
