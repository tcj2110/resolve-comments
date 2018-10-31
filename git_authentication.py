import subprocess
import requests
import json
#subprocess.check_output(['ls','-l']) #all that is technically needed...
##print subprocess.check_output(['ls','-l'])
#print subprocess.check_output([ 'curl','-u','kmejia:705cb4fc9b90fdc93c441e4d39573dff38fa6f2d','https://api.github.com/user'])
"""
get comments
get repo 
"""

##the two lines below are my authentication credentials
def run():
    username = 'kmejia'
    token = '705cb4fc9b90fdc93c441e4d39573dff38fa6f2d'
    r = requests.get('https://api.github.com/user', auth=(username, token)).json()
    """
    for key in r.keys():
        print(str(key)+":"+ str(r[key]) )
    """
    return r
##print r["login"]
#print r.status_code
##print r.login