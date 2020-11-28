from time import ctime
from activities.respondliz import respond
def times(data):
    if "time" in data:
        listening = True
        respond(ctime())
