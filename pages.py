
def pages(url):
    """Returns the number of additional pages for a given parent URL"""
    
    import urllib2,sys
    from bs4 import BeautifulSoup

    #Base Page
    soup = BeautifulSoup(urllib2.urlopen(url).read())
	
    #Page Counter
    page_counter = soup.find("div", {"class":"item-list"})
    paragraph = ["".join(x.findAll(text=True)) for x in page_counter.findAll("li", {"class":"pager-item"})]
    
    print len(paragraph)

    return len(paragraph)

#pages("http://www.whitehouse.gov/briefing-room/Speeches-and-Remarks/2010/09")

#pages("http://www.whitehouse.gov/briefing-room/Speeches-and-Remarks/2011/04")



def sub_pages_URLs(parent_url):

	base_url = parent_url+"?page="

	# Number of Pages
	total_pages = pages(parent_url)

	for i in range(0, total_pages+1):
		print base_url+str(i)


#sub_pages_URLs("http://www.whitehouse.gov/briefing-room/Speeches-and-Remarks/2010/09")

sub_pages_URLs("http://www.whitehouse.gov/briefing-room/Speeches-and-Remarks/2009/09")




