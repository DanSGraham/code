from urllib import urlopen

import write_headlinetxt

import dataCollection

import time

import timeConverter

# Companies is the string I am searching for, Websites is a list of urls that I want to scrape,
#header is today's date, and current_headlines are the already stored headlines.

def scraper(companys, websites):
    '''This function scrapes news sites for relevant headlines'''
    headlines = []
    for key in websites:
        url = websites[key]
        html = urlopen(url)
        source = html.read()
        # The key for the scraper = "ends with </title>"
        #time.sleep(5) #maybe unneccessary
        while True:
            if key[0:3] == 'CNN':
                if '</title>' in source:  #looks until no more headlines
                    position1 = source.find('<title>')
                    position2 = source.find('</title>', position1)
                    del_position = source.find('</title>', position2)
                    headline1 = source[position1+7:position2]
                    published_position1 = source.find('<pubDate>', position1)
                    published_position2 = source.find("""</pubDate>""", published_position1)
                    published = source[published_position1+9:published_position2]
                else:
                    break
            if key[0:3] == 'Huf':
                #POSTS ARE TIMED TO UTC TIME(SAME AS GMT)
                if '</title>' in source:  #looks until no more headlines
                    position1 = source.find('<title>')
                    position2 = source.find('</title>', position1)
                    del_position = source.find('</title>', position2)
                    headline1 = source[position1+16:position2-3]
                    published_position1 = source.find('<pubDate>', position1)
                    published_position2 = source.find("""</pubDate>""", published_position1)
                    published = source[published_position1+9:published_position2-6]
                    if published[-1] != 'T':
                        published = published + ' UTC'
                else:
                    break
            if key[0:3] == 'New':
                if '</title>' in source:  #looks until no more headlines
                    position1 = source.find('<title>')
                    position2 = source.find('</title>', position1)
                    del_position = source.find('</title>', position2)
                    headline1 = source[position1+7:position2]
                    published_position1 = source.find('<pubDate>', position1)
                    published_position2 = source.find("""</pubDate>""", published_position1)
                    published = source[published_position1+9:published_position2]
                else:
                    break
            if key[0:3] == 'Fox':
                if '</title>' in source:  #looks until no more headlines
                    position1 = source.find('<title>')
                    position2 = source.find('</title>', position1)
                    del_position = source.find('</title>', position2)
                    if key == 'Fox News Latest Headlines':
                        headline1 = source[position1+16:position2-3]
                    else:
                        headline1 = source[position1+7:position2]
                    published_position1 = source.find('<pubDate>', position1)
                    published_position2 = source.find("""</pubDate>""", published_position1)
                    published = source[published_position1+9:published_position2]
                else:
                    break
            if key[0:3] == 'NBC':
                if '</title>' in source:  #looks until no more headlines
                    position1 = source.find('<title>')
                    position2 = source.find('</title>', position1)
                    del_position = source.find('</title>', position2)
                    headline1 = source[position1+7:position2]
                    published_position1 = source.find('<pubDate>', position1)
                    published_position2 = source.find("""</pubDate>""", published_position1)
                    published = source[published_position1+9:published_position2]
                else:
                    break
            if key[0:3] == 'Goo':
                if '</title>' in source:  #looks until no more headlines
                    position1 = source.find('<title>')
                    position2 = source.find('</title>', position1)
                    del_position = source.find('</title>', position2)
                    headline1 = source[position1+7:position2]
                    published_position1 = source.find('<pubDate>', position1)
                    published_position2 = source.find("""</pubDate>""", published_position1)
                    published = source[published_position1+9:published_position2]
                else:
                    break
            if key[0:3] == 'For':
                if '</title>' in source:  #looks until no more headlines
                    position1 = source.find('<title>')
                    position2 = source.find('</title>', position1)
                    del_position = source.find('</title>', position2)
                    headline1 = source[position1+7:position2]
                    published_position1 = source.find('<pubDate>', position1)
                    published_position2 = source.find("""</pubDate>""", published_position1)
                    published = source[published_position1+9:published_position2]
                    if published[-5:] == '-0500':
                        published = published[:-6] + ' EST'
                    elif published[-1] != 'T':
                        published = published + ' EST'
                else:
                    break

            if key[0:3] == 'Fin':
                if '</title>' in source:  #looks until no more headlines
                    position1 = source.find('<title>')
                    position2 = source.find('</title>', position1)
                    del_position = source.find('</title>', position2)
                    headline1 = source[position1+7:position2]
                    published_position1 = source.find('<pubDate>', position1)
                    published_position2 = source.find("""</pubDate>""", published_position1)
                    published = source[published_position1+9:published_position2]
                else:
                    break

            if key[0:3] == 'Wal':
                if '</title>' in source:  #looks until no more headlines
                    position1 = source.find('<title>')
                    position2 = source.find('</title>', position1)
                    del_position = source.find('</title>', position2)
                    headline1 = source[position1+7:position2]
                    published_position1 = source.find('<pubDate>', position1)
                    published_position2 = source.find("""</pubDate>""", published_position1)
                    published = source[published_position1+9:published_position2]
                else:
                    break

            if key[0:3] == 'Dig':
                if '</title>' in source:  #looks until no more headlines
                    position1 = source.find('<title>')
                    position2 = source.find('</title>', position1)
                    del_position = source.find('</title>', position2)
                    headline1 = source[position1+7:position2]
                    print headline1
                    published_position1 = source.find('<pubDate>', position1)
                    published_position2 = source.find("""</pubDate>""", published_position1)
                    published = source[published_position1+9:published_position2]
                    if published[-1] != 'T':
                        published = published[:-6] + ' GMT'

                

                    #Huff Po had an extra -500 at the end of all of their titles, and no time zone identifier so I had to make an exception in the scraper
            source = source.replace(source[:del_position+8], '')
            new_published = published
            new_headline = dataCollection.headline(headline1, key, new_published)
            new_headline.checkIfRelevant(companys)
            if(new_headline.isRelevant()):
                headlines.append(new_headline)
            
    return headlines
