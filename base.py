import sublime_plugin
import sublime
import sys
import os
from subprocess import call, STDOUT, check_output
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import authenticate  # noqa: E402
import pref  # noqa: E402


# Global variable for plugin preferences

preferences = {"window_size": 0.33, "issue_pr": 1}


# Class provides the entrypoint for the plugin.
# All helper functions are external to
# allow for easy unit testing.


class InsertPanelCommand(sublime_plugin.TextCommand):

    # Entrypoint for application

    def run(self, edit):
        username_input()


# Text command to open preference menu


class PreferencesCommand(sublime_plugin.TextCommand):

    # Method returns screen size in print statement
    # When complete will insert screen preference to mongo

    def run(self, edit):
        preference_mode = True
        username_input(preference_mode)


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
        toggle = pref.PreferenceToggle()
        toggle.window_preference(user)
    else:
        gen_comment_list(token, user, auth)
    return True


#  Manager function that uses helper functions to show
#  comments in side popup


def extract_path():
    env_var = sublime.active_window().extract_variables()
    if('file_path' in env_var):
        path = env_var['file_path']
    else:
        return None
    if call(["git", "branch"], stderr=STDOUT,
            stdout=open(os.devnull, 'w'), cwd=path) == 0:
        root = check_output(["git", "rev-parse", "--show-toplevel"], cwd=path)
        path = root.rstrip()
    os.chdir(path)
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
    global preferences
    path = extract_path()
    if(not path):
        error_message("Error: file not found in git repository")
        return
    org, repo = path
    data_store = load_quick_panel_data(
        auth, org, repo)
    pref_toggle = pref.PreferenceToggle()
    preferences = pref_toggle.load_window_preference(user)
    sublime.active_window().show_quick_panel(data_store[:-1], on_click, 1, 2)


# Method loads Github pull_requests data by authenticating the user and token.
# After authentication plugin retrieves pull request data based on org name
# and repo name.

def load_quick_panel_data(auth, org, repo):

    data = []

    if(preferences['issue_pr'] == 1 or preferences['issue_pr'] == 2):
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
            state = req['state']
            url = req['html_url']
            content = [title, body, user, "Pull Request", state, url]
            data.append(content)
    elif(preferences['issue_pr'] == 0 or preferences['issue_pr'] == 2):
        issues = auth.get_repo_issues(org, repo)
        if('message' in issues and
            (issues['message'] == 'Bad credentials' or
                issues['message'] == 'Not Found')):
            error_message("Error: " + issues['message'])
            return []
        for issue in issues:
            title = issue['title']
            body = issue['body']
            user = issue['user']['login']
            state = issue['state']
            url = issue['html_url']
            content = [title, body, user, "Issue", state, url]
            data.append(content)

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
        if len(sublime.active_window().views_in_group(nGroup)) == 0:
            sublime.active_window().focus_group(nGroup)
            createdView = sublime.active_window().new_file()
            createdView.add_phantom(
                "test", createdView.sel()[0], gen_comment_html(
                    data_store[index]), sublime.LAYOUT_BLOCK,
                lambda href: sublime.run_command(
                    'open_url', {'url': href}))
        elif(nGroup == 1):
            sublime.active_window().focus_group(nGroup)
            createdView = sublime.active_window().active_view_in_group(nGroup)
            createdView.add_phantom(
                "test", createdView.sel()[0], gen_comment_html(
                    data_store[index]), sublime.LAYOUT_BLOCK,
                lambda href: sublime.run_command(
                    'open_url', {'url': href}))


def on_phantom_click(href):
    print("DID WE REACH IT")


def gen_comment_html(data):
    html_arr = [
        "<style> ul { display: flex; flex-direction \
        : column; flex-wrap: wrap;} </style>",
        "<ul>"]
    html_arr.append("<h3>" + data[0] + "</h3>")
    for i in range(1, len(data) - 1):
        li = "<li>" + data[i] + "</li>"
        html_arr.append(li)
    link = "Click <a href='" + data[-1] + \
        "'>here</a> to go to Pull Request Link "
    html_arr.append(
        "<li>" + link + "</li>")
    html_arr.append("</ul>")

    html_str = "".join(html_arr)
    return html_str


def error_message(e_mes):
    sublime.active_window().show_input_panel(
        caption="Error Prompt",
        initial_text=e_mes,
        on_done=None,
        on_change=None,
        on_cancel=None)
