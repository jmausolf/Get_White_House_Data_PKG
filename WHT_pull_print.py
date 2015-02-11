


def WHT(url):
    """Prints Text Output for a given URL from Whitehouse Speeches and Remarks"""
    
    import urllib2,sys
    from bs4 import BeautifulSoup

    #ptext = []
    soup = BeautifulSoup(urllib2.urlopen(url).read())


    # Get Release
    Release = soup.find("div", {"class":"release"})
    release = Release.get_text()

    # Get Date
    Date = soup.find("div", {"class":"date"})
    date = Date.get_text()

    # Get Paragraph Body
    content = soup.find("div", {"id":"content"})
    paragraph = ["".join(x.findAll(text=True)) for x in content.findAll("p")]
    paragraph_body = "\n\n%s" % ("\n\n".join(paragraph))

    #ptext.append((date, release, paragraph_body))

    #return ptext
    f = open("Obama_speech_test.txt", 'w')
    f.write(date.encode('utf-8'))
    f.write(release.encode('utf-8'))
    f.write(paragraph_body.encode('utf-8'))
    f.close


url = "http://www.whitehouse.gov/the-press-office/2014/10/30/remarks-first-lady-grassroots-campaign-event-democratic-candidate-govern"

WHT(url)


