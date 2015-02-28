import sys, csv, time, os, subprocess
sys.path.append('../Python_Scripts/')
sys.path.append('..')

from speech_urls import *
from readParent import *
from pages import *
from date import date
from CSVread import *
from Speech_parser1 import *
from Speech_parser2 import *


if __name__ == '__main__':

## ____________ President Speeches _____________ ##

	# Get CSV Lines - President
	os.chdir('bash_Speech')
	os.chdir('Speech_President')
	with open('__president_urls.csv', 'rU') as urls_file:
		reader = csv.reader(urls_file)
		lines = list(reader)
		Xpotus = len(lines)
		print "Total requested speech urls:", Xpotus


	# Create Parsed Speeches - President
	for URL in range(0, Xpotus):
	#for URL in range(0, 5):
		speechURL = '\n'.join(map(str, read_presidentURLs(URL)))
		time.sleep(0.5)
		try:
			WHT(speechURL)
		except:
			WHT2(speechURL)


## ____________ Vice-President Speeches _____________ ##

	try:
		# Get CSV Lines - Vice-President
		os.chdir(os.pardir)
		os.chdir('Speech_Vice_President')
		with open('__vice_president_urls.csv', 'rU') as urls_file:
			reader = csv.reader(urls_file)
			lines = list(reader)
			Xvp = len(lines)
			print "Total requested speech urls:", Xvp

		# Create Parsed Speeches - Vice-President
		for URL in range(0, Xvp):
		#for URL in range(0, 3):
			speechURL = '\n'.join(map(str, read_vice_presidentURLs(URL)))
			time.sleep(0.5)
			try:
				WHT(speechURL)
			except:
				WHT2(speechURL)
	except:
		print "No Vice-President Speeches Found, Pass."
		pass


## ____________ First-Lady Speeches _____________ ##

	try:
		# Get CSV Lines - First Lady
		os.chdir(os.pardir)
		os.chdir('Speech_First_Lady')
		with open('__first-lady_urls.csv', 'rU') as urls_file:
			reader = csv.reader(urls_file)
			lines = list(reader)
			Xflotus = len(lines)
			print "Total requested speech urls:", Xflotus

		# Create Parsed Speeches - First Lady
		for URL in range(0, Xflotus):
		#for URL in range(0, 14):
			speechURL = '\n'.join(map(str, read_first_ladyURLs(URL)))
			time.sleep(0.5)
			try:
				WHT(speechURL)
			except:
				WHT2(speechURL)
	except:
		print "No First-Lady Speeches Found, Pass."
		pass


## ____________ Second-Lady Speeches _____________ ##

	try: 
		# Get CSV Lines - Second Lady
		os.chdir(os.pardir)
		os.chdir('Speech_Second_Lady')
		with open('__second-lady_urls.csv', 'rU') as urls_file:
			reader = csv.reader(urls_file)
			lines = list(reader)
			Xsl = len(lines)
			print "Total requested speech urls:", Xsl
		print "back up again"

		# Create Parsed Speeches - Second Lady
		for URL in range(0, Xsl):
			speechURL = '\n'.join(map(str, read_second_ladyURLs(URL)))
			time.sleep(0.5)
			try:
				WHT(speechURL)
			except:
				WHT2(speechURL)
	except:
		print "No Second-Lady Speeches Found, Pass."
		pass


## ____________ Other Speeches _____________ ##

	try:
		# Get CSV Lines - Other
		os.chdir(os.pardir)
		os.chdir('Speech_Other')
		with open('__other_urls.csv', 'rU') as urls_file:
			reader = csv.reader(urls_file)
			lines = list(reader)
			Xother = len(lines)
			print "Total requested speech urls:", Xother

		# Create Parsed Speeches - Other
		for URL in range(0, Xother):
		#for URL in range(0, 2):
			speechURL = '\n'.join(map(str, read_otherURLs(URL)))
			time.sleep(0.5)
			try:
				WHT(speechURL)
			except:
				WHT2(speechURL)
	except:
		print "No Other Speeches Found, Pass."
		pass



