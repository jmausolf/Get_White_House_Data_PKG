

import sys, csv, time, os, subprocess
sys.path.append('../Python_Scripts/')
sys.path.append('..')

from speech_urls import *
from readParent import *
from pages import *
from date import date
from CSVread import *
from Speech_parser import *







if __name__ == '__main__':

	"""
	#print "Len Dates", len(Dates)

	#os.makedirs('Speech_OS')

	#os.chdir('Speech_OS')
	os.chdir('bash_Speech')
	for URL in range(120, 130):
		speechURL = '\n'.join(map(str, read_speechURLs(URL)))
		#os.chdir('Speech_OS')
		time.sleep(0.5)
		WHT(speechURL)
    	#subprocess.call("cd ..", shell=True)
    	#os.system('cd ..')
    """


	#Get Number of Lines of Speech URLs


	os.chdir('bash_Speech')
	with open('speechurls.csv', 'rb') as urls_file:
		reader = csv.reader(urls_file)
		lines = list(reader)
		XSp = len(lines)
		print "Total requested speech urls:", XSp




	# Create Parsed Speeches
	for URL in range(0, XSp):
		speechURL = '\n'.join(map(str, read_speechURLs(URL)))
		time.sleep(0.5)
		WHT(speechURL)



