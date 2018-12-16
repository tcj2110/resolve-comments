import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pymongo  # noqa : E402


class MongoConnect:

    def __init__(self):
        self.client = pymongo.MongoClient(
            "mongodb://arsalaanansari:resolve_comments1\
            @ds041404.mlab.com:41404/resolve-comments")
        self.db = self.client['resolve-comments']
        self.window_pref = [
            "Compact : 1/3 Screen",
            "Normal: 1/2 Screen",
            "Large: 2/3 Screen"]

    # Adds user preferences to preferences mongoDB collection

    def insert_pref(self, data):
        self.pref = self.db.preferences
        post_id = self.pref.insert_one(data).inserted_id
        return post_id

    def remember_cred(self, username):
        rem = self.db.user_remember
        data = rem.find_one({"user": username})
        print(data)
