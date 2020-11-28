from .modules.os.mac.apps.open import applications
from .modules.time import times
from .respondzowiie import respond

def digital_assistant(data):
    global listening
    if 'time' in data:
        times(data)
    elif 'teams' in data:
        respond("opening teams now")
        applications(data)
    else:
        respond("Sorry I did not understand")
