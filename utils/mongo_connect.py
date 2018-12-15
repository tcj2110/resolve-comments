import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pymongo  # noqa


class MongoConnect:

    def __init__(self):
        self.client = pymongo.MongoClient(
            "mongodb://arsalaanansari:resolve_comments1\
            @ds041404.mlab.com:41404/resolve-comments")

    # Checks MongoDB database for whether user
    def remember_cred(self, username):
        self.db = self.client['resolve-comments']
        rem = self.db.user_remember
        data = rem.find_one({"user": username})
        print(data)
