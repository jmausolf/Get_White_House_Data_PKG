def getURL(year, month):

	#http://www.whitehouse.gov/briefing-room/Speeches-and-Remarks/YYYY/MM
	base_url = "http://www.whitehouse.gov/briefing-room/Speeches-and-Remarks/"+year+"/"+month
	print base_url
#getURL("2011", "05")


def getyrURL(year):
	base_url = "http://www.whitehouse.gov/briefing-room/Speeches-and-Remarks/"+year+"/"
	return base_url
#getyrURL("2011")




def getparentURLs(yr1=2009, yr2=2015, month1=1, month2=12):

	import itertools

	years = ['2009', '2010', '2011', '2012', '2013', '2014', '2015']
	months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

	index_yr1 = yr1-2009
	index_yr2 = yr2-2009
	index_mo1 = month1-1
	index_mo2 = month2-1


	req_years = years[index_yr1:index_yr2+1]
	req_months = months[index_mo1:index_mo2+1]

	#print(list(itertools.product(req_years, req_months)))

	x = (list(itertools.product(req_years, req_months)))

	#print x[0:12]

	"""
	for year in years:
		urls = getyrURL(year)
		for month in months:
			full_url = urls+month
			print full_url"""

	"""
	parent_urls = []
	for year in years:
		urls = getyrURL(year)
		for month in months:
			full_url = urls+month
			parent_urls.append(full_url)"""

	#print parent_urls[12:24]

	f = open('parentURLs.csv', 'w')
	try:
		f.write(u'PARENT_URLS\n')
		for year in req_years:
			urls = getyrURL(year)
			for month in req_months:
				full_url = urls+month
				f.write(u'%s\n' % (full_url))
		#f.write(u'"%s\n"' % (parent_urls))
	finally:
		f.close()





#getparentURLs()
#problem is that the years are all messed up and doesn't go from start period to end period
#other problem is if all, getting future dates.
# WH lists future dates with class="view-empty" <p>There are no speeches and remarks for this time period.</p>
#getparentURLs(2009, 2013, 1, 12)



"""

def getparentURLs_df(yr1=2009, yr2=2015, month1=1, month2=12):

	import itertools
	import pandas as pd 
	import numpy as np 
	import csv

	years = ['2009', '2010', '2011', '2012', '2013', '2014', '2015']
	months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

	index_yr1 = yr1-2009
	index_yr2 = yr2-2009
	index_mo1 = month1-1
	index_mo2 = month2-1


	req_years = years[index_yr1:index_yr2+1]
	req_months = months[index_mo1:index_mo2+1]

	#print(list(itertools.product(req_years, req_months)))

	x = (list(itertools.product(req_years, req_months)))

	#print x[0:12]



	#print parent_urls[12:24]

	f = open('parentURLs.txt', 'wr')
	try:
		f.write(u'PARENT_URLS\n')
		for year in req_years:
			urls = getyrURL(year)
			for month in req_months:
				full_url = urls+month
				f.write(u'%s\n' % (full_url))
		#f.write(u'"%s\n"' % (parent_urls))
	finally:
		f.close()

	
	import csv
	with open('parentURLs.csv', 'rb') as urls_file:
		reader = csv.reader(urls_file)
		lines = list(reader)
		first_10 = lines[0:10]

		print first_10 """

	

	"""
	f = open('first10.csv', 'w')
	try:
		parent_urls_df = pd.read_csv("parentURLs.csv")
		first_10 = parent_urls_df.ix[0:10]
		f.write(u'%s\n' % (first_10))
	finally:
		f.close()"""

	"""
	import csv
	with open("parentURLs.csv", 'rb') as f:
		rdr = csv.reader(f)
		lines = list(rdr)
		for i in lines:
			first_10 = lines[1:10]
		print first_10


	f = open('first10.csv', 'w')
	try:
		f.write(u'%s\n' % (first_10))
	finally:
		f.close()"""



#getparentURLs_df()










