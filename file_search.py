import webbrowser
import os
def find_all(name, path):
	result = []
	for root, dirs, files in os.walk(path):
   		if name in files:
			match = os.path.join(root, name)
			result.append(match)
			webbrowser.open(match)
	print(len(result))
	return result
#find_all("free-soul.jpg","/home")