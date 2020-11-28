from time import ctime
from activities.respondzowiie import respond
def times(data):
    if "time" in data:
        listening = True
        respond(ctime())
