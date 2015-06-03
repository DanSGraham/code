from urllib import urlopen
import time
import datetime


#USES AN END TAG IDENTIFIER FOR POSITION (</a>)

def nytimesScraper():
    html = urlopen('http://www.nytimes.com/')

    source = html.read()

    key = "ends with </a> but the character before the </a> is not >"

    headlines = []
    while True:
        if '</a>' in source:
            
            position2 = source.find('</a>')
            position1 = source.rfind('>',0,position2)
            headline = source[position1+1:position2]
            if headline != '':
                headlines.append(headline)
            source = source.replace(source[:position2+4], '')

        else:
            break

    return headlines

def googlenewsScraper():

    headlines = []
    newswebpage = urlopen("https://news.google.com/?ar=1385422357")
    newspagestring = newswebpage.read()

    while True:
        if '''<span class="titletext">''' in newspagestring:
            position1 = newspagestring.find('''<span class="titletext">''')
            position2 = newspagestring.find('''</span>''', position1)
            headline = newspagestring[position1 + 24:position2]
            headlines.append(headline)
            newspagestring=newspagestring.replace(newspagestring[:position2],' ')        
        else: 
            break
    return headlines

#For some reason it doesn't remove every headline that doesn't have google in it.
def main():
    nytimes_headlines = 1
    googlenews_headlines = 1
    googleHeadlines = {}
    nytimesHeadlines = {}
    company = 'Google'
    while True:
        time.sleep(3)
        if nytimesScraper() != nytimes_headlines:
            nytimesHeadlines[str(datetime.datetime.now())] = nytimesScraper()
            nytimes_headlines = nytimesScraper()
        if googlenewsScraper() != googlenews_headlines:
            googleHeadlines[str(datetime.datetime.now())] = googlenewsScraper()
            googlenews_headlines = googlenewsScraper()
        break
    

    for key in googleHeadlines:
        headlinelist = []
        for headline in googleHeadlines[key]:
            if company in headline:
                headlinelist.append(headline)

        googleHeadlines[key] = headlinelist

    for key in nytimesHeadlines:
        headlinelist = []
        for headline in nytimesHeadlines[key]:
            if not company in headline:
                headlinelist.remove(headline)
        nytimesHeadlines[key] = headlinelist
                

main()
