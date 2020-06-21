#google
from googlesearch import search
import webbrowser as wb
import text_speech

def play():
	text_speech.say("What do you want to listen:")
	song = raw_input()
	query="play "+song+" sound cloud"
	for url in search(query , tld="com", num=1, stop=1, pause=2):
		wb.open_new_tab(url)
    
     

