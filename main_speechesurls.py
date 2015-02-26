#from date import *

import sys, csv
from speech_urls import *
from readParent import *
from pages import *
from date import date
from CSVread import *
from WHT_pull_print import *






#req_URLs("2010/09", "2011/05") #Dates are different


if __name__ == '__main__':
	Dates = sys.argv[1:]
	#print "Len Dates", len(Dates)

	print "Dates are", Dates
	#print "Date1", Dates[0]
	#print "Date2", Dates[1]
	#date2 = sys.argv[2:3]


	#assert len(Dates) != 2, "Error: Only one date provided, pleave provide two dates."

	assert Dates, "Error: Please provide two dates in the form 'YYYY/MM'    'YYYY/MM' ."
	#assert Dates[1], "Error: Please provide exactly two dates 'YYYY/MM' 'YYYY/MM' ."


	
	#Define initial parent URLs in Specified Date Range
	parent_urls = req_URLs(Dates[0], Dates[1])

	"""
	date1 = Dates[0]
	date2 = Dates[1]

	a = date(date1)
	b = date(date2)"""

	print "___"*30

	print read_reqURLs(3)

	#Get Number of Lines of Requested URLs
	with open('requested_parentURLs.csv', 'rb') as urls_file:
		reader = csv.reader(urls_file)
		lines = list(reader)
		XR = len(lines)
		

	# Create CSV of Subpage URLS 
	for URL in range(0, XR):
		rURL = '\n'.join(map(str, read_reqURLs(URL)))
		sub_pages_URLs(rURL)



	#Get Number of Lines of Subpages URLs
	with open('subpages.csv', 'rb') as urls_file:
		reader = csv.reader(urls_file)
		lines = list(reader)
		XS = len(lines)
		print XS



	# Create CSV of Speech URLS
	for URL in range(0, XS):
		subURL = '\n'.join(map(str, read_subURLs(URL)))
		speech_urls(subURL)



	#Get Number of Lines of Speech URLs
	with open('speechurls.csv', 'rb') as urls_file:
		reader = csv.reader(urls_file)
		lines = list(reader)
		XSp = len(lines)
		print XS



	
	# Create Parsed Speeches
	for URL in range(0, 5):
		speechURL = '\n'.join(map(str, read_speechURLs(URL)))
		WHT(speechURL)
	



