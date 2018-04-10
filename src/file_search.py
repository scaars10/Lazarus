import webbrowser
import os
import text_speech
def find_all(name, path):
	result = []
	for root, dirs, files in os.walk(path):
   		if name in files:
			match = os.path.join(root, name)
			result.append(match)
			webbrowser.open(match)
	text_speech.say(str(len(result))+" results found.")
	return result
#find_all("exp_sky.jpg","/home")