import os
import eel
from Engine.feature import *
from Engine.command import *

eel.init("www")

playAssistantSound()

os.system('Start msedge.exe --app="http://localhost:8000/index.html"')

eel.start('index.html',mode=None, host='localhost',block=True)