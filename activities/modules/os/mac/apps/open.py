import os

def applications(data):
    if 'teams' in data:
        os.system("/usr/bin/open -W -n -a /Applications/Microsoft\ Teams.app")
