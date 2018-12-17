import os
import sys
import sublime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils import mongo_connect  # noqa: E402

# Class that stores methods to toggle plugin preferences


class PreferenceToggle:

    def __init__(self):
        self.mongo_client = mongo_connect.MongoConnect()
        self.mongo_pref = {}

    def issue_click(self, index):
        if(index == -1):
            return -1
        else:
            self.mongo_pref['issue_pr'] = index
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
        mongo_pref = self.mongo_client.load_pref(user)
        return {
            'window_size': mongo_pref['window_size'],
            'issue_pr': mongo_pref['issue_pr']}
