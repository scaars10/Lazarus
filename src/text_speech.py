"""requirements 
gtts
os
mpg321 (not py)
"""
from gtts import gTTS
import os
import sys
def say(text):

	language = "en"
	try:
		tts = gTTS(text=text, lang = language)
		tts.save("geek_aud.mp3")
		os.system("mpg321 geek_aud.mp3")
		os.remove("geek_aud.mp3")
	except:
		print("Error occured while converting text to speech. ")
