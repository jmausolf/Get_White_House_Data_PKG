

import sys, csv, time, os, subprocess
sys.path.append('../Python_Scripts/')
sys.path.append('..')

from speech_urls import *
from readParent import *
from pages import *
from date import date
from CSVread import *
from Speech_parser import *
from Speech_parser2 import *





if __name__ == '__main__':


	#Get Number of Lines of Speech URLs
	os.chdir('bash_Speech')
	with open('speechurls.csv', 'rb') as urls_file:
		reader = csv.reader(urls_file)
		lines = list(reader)
		XSp = len(lines)
		print "Total requested speech urls:", XSp


	# Create Parsed Speeches
	#for URL in range(0, XSp):
	for URL in range(549, 553):
		speechURL = '\n'.join(map(str, read_speechURLs(URL)))
		time.sleep(0.5)
		try:
			#Try the 1st Parser, Works Most Speeches
			WHT(speechURL)
		except:
			#Try the 2nd Parser, Works when Parser 1 Fails
			WHT2(speechURL)



