from date import date

def read_parentURLs(i):
	"""Reads the URLs from the Parent URLs CSV"""
	import csv
	with open('parentURLs.csv', 'rb') as urls_file:
		reader = csv.reader(urls_file)
		lines = list(reader)
		URL = lines[i]
		return URL




def req_URLs(date1, date2):
	"""Returns the requested parent URL's for speeches and remarks in a 
	given date range. Date1 = "YYYY/MM" Date2 = "YYYY/MM"""

	a = date(date1)
	b = date(date2)

	if a==b:
		print '\n'.join(map(str, read_parentURLs(a)))

	elif a != b:
		for URL in range(a, b+1):
			#print read_parentURLs(URL)
			print '\n'.join(map(str, read_parentURLs(URL)))


# Test Requested Parent Date URLS's
#req_URLs("2011/01", "2011/01") #Dates are the same
#req_URLs("2010/09", "2011/05") #Dates are different
req_URLs("2009/01", "2015/03") #Dates are different
