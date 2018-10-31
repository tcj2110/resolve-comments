##tester for git_authenticate
from git_authenticate import run

##below should print 'all entrees in dictionary'
rr = run()
for key in rr.keys():
    print(str(key)+":"+ str(rr[key]) )