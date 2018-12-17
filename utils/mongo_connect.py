import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pymongo  # noqa : E402


class MongoConnect:

    def __init__(self):
        url = ("mongodb://arsalaanansari:resolve_comments1@"
               "ds041404.mlab.com:41404/resolve-comments")
        self.client = pymongo.MongoClient(url)
        self.db = self.client['resolve-comments']
        self.window_pref = [
            "Side Window Compact : 1/3 Screen",
            "Side Window Normal: 1/2 Screen",
            "Side Window Large: 2/3 Screen"]
        self.issue_pref = [
            "Show Issues",
            "Show Pull Requests",
            "Show Both"]

    # Adds user preferences to preferences mongoDB collection

    def insert_pref(self, data):
        self.pref = self.db.preferences
        self.pref.update_one({"user": data["user"]}, {
                             "$set": {"window_size": data['window_size'],
                                      "issue_pr": data['issue_pr']}},
                             upsert=True)

    def load_pref(self, user):
        self.pref = self.db.preferences
        res = self.pref.find_one({"user": user})
        return {'window_size': res['window_size'], 'issue_pr': res['issue_pr']}
