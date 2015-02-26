def WHT(url):
    """Prints Text Output for a given URL from Whitehouse Speeches and Remarks"""
    
    import urllib2,sys
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(urllib2.urlopen(url).read())


    # Get Date
    Date = soup.find("div", {"class":"date"})
    raw_date = Date.get_text()
    date = raw_date.replace(' ', '', 12)

    # Get Release
    Release = soup.find("div", {"class":"release"})
    raw_release = Release.get_text()
    release = raw_release.replace(' ', '', 12)+"\n\n"

    # Get Title
    Title = soup.find("h1", {"property":"dc:title"})
    title = Title.get_text()

    
    # Get Paragraph Body
    content = soup.find("div", {"id":"content"})
    paragraph = ["".join(x.findAll(text=True)) for x in content.findAll("p")]
    paragraph_body = "\n\n%s" % ("\n\n".join(paragraph))


    #Get File ID - Date & Time
    #Date
    year_id = url[43:47]
    month_id = url[48:50]
    day_id = url[51:53]
    date_id = year_id+'-'+month_id+'-'+day_id
    #Time
    time = ["".join(x.findAll(text=True)) for x in content.findAll("p")]
    start = time[3]
    time_string0 = start[0:10]
    time_string1 = time_string0.replace(':', '')
    time_string2 = time_string1.replace('.', '')
    time_string3 = time_string2.replace("\n", '')
    time_id = time_string3.replace(' ', '')



    #Save Text File
    f = open(date_id+"_"+time_id+".txt", 'w')
    f.write(date.encode('utf-8'))
    f.write(release.encode('utf-8'))
    f.write(title.encode('utf-8'))
    f.write(paragraph_body.encode('utf-8'))
    f.close


##Test URLS
#url = "http://www.whitehouse.gov/the-press-office/2014/10/30/remarks-first-lady-grassroots-campaign-event-democratic-candidate-govern"
#url = "http://www.whitehouse.gov/the-press-office/2014/01/22/remarks-president-meeting-presidential-commission-election-administratio"
#url = "http://www.whitehouse.gov/the-press-office/2015/02/11/remarks-president-americas-leadership-ebola-fight"

#WHT(url)


