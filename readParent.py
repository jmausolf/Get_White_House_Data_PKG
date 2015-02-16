def read_parentURLs(i):
	import csv
	with open('parentURLs.csv', 'rb') as urls_file:
		reader = csv.reader(urls_file)
		lines = list(reader)
		URL = lines[i]
		return URL



def req_URLs(i):
	for URL in range(1, i):
		#print read_parentURLs(URL)
		print '\n'.join(map(str, read_parentURLs(URL)))


req_URLs(5)

