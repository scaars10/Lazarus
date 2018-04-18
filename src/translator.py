from googletrans import Translator,LANGUAGES
import text_speech

def translate():
	trans=Translator()
	text_speech.say("Enter a string in any language")
	in_str=raw_input()
	out_str=trans.translate(in_str)
	print "The input language is: "+LANGUAGES[out_str.src] + "\nIts translation in English: " + out_str.text
