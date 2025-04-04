# terminal - > pip install pyttsx
# python.wxw -m pip install --upgrade pip

import pyttsx3
engine = pyttsx3.init() #initialize the TTS engine
engine.setProperty('rate', 150) # default is around 200
engine.setProperty('volume', 0.8) # default is around 80%

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #change the voice to female

engine.say("WELL WELL WELL HOW THE TURNTABLES")
engine.runAndWait() #speak the text