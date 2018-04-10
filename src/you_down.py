"""pytube"""
from bs4 import BeautifulSoup
import urllib
import requests
import webbrowser
import text_speech
import youtube_dl
import os
home = '/Home/scaars13'
def get_top_result(topic):
	try:
		text_speech.say("Finding"+topic)
		topic_url = topic.replace(' ','+')
		url= url = 'https://www.youtube.com/results?search_query='+topic_url
		r = requests.get(url)
		soup = BeautifulSoup(r.content, "html.parser")
		all_videos = soup.findAll('div', {'class': 'yt-lockup-video'})
		top_res = all_videos[0].find('a')['href']
		return top_res
	except:
		text_speech.say("Error Occured while finding a match")
		return -1

def stream_video(topic):
	try:
		top_res = get_top_result(topic)
		if(str(top_res) == "-1"):
			return -1
		#text_speech.say("Streaming Video In Your Browser")
		webbrowser.open('https://www.youtube.com'+top_res)
	except:
		text_speech.say("Sorry Video Could Not Be streamed")
def download_video(topic):
	try:
		os.chdir('../Downloads')
		top_res = get_top_result(topic)
		ydl_opts = {
        	         'format': 'bestvideo/best',
            	               'quiet': True,
               	            'restrictfilenames': True,
            	}

		ydl = youtube_dl.YoutubeDL()
		ydl.download(['https://www.youtube.com'+top_res])
		#except:
		os.chdir('../src')
	except:
		text_speech.say("Video Could not be Downloaded")
	#os.system()

def download_song(topic):
	#try:
	top_res = get_top_result(topic)		
	#os.chdir('../Downloads')
	ydl_opts = {
              'format': 'bestaudio/best',
              'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                           'preferredcodec': 'mp3',
                           'preferredquality': '192',
                           }],
                           'quiet': True,
                           'restrictfilenames': True,
                           'outtmpl': home+'Downloads/%(title)s.%(ext)s'
				}
	ydl = youtube_dl.YoutubeDL()
	ydl.download(['https://www.youtube.com'+top_res])
	#os.chdir('../src')
	#except:
	#	print("OOPS Song Could Not Be Downloaded")
#stream_video("Killing in the name")