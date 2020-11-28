from .modules.time import times
from .respondliz import respond

def digital_assistant(data):
    global listening
    times(data)

    if "how are you" in data:
        listening = True
        respond("I am well")
