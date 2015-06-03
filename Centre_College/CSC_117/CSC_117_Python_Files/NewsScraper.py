from urllib import urlopen

import write_headlinetxt

import storeData

import time

def scraper(header, companys, websites, current_headlines):
    '''This function scrapes news sites for relevant headlines'''
    
    for key in websites:
        url = websites[key]
        html = urlopen(url)
        source = html.read()
        # The key for the scraper = "ends with </title> >"
        time.sleep(5)
        headlines = []
        while True:
            if '</title>' in source:  #looks until no more headlines
                position1 = source.find('<title>')
                if url == 'http://news.google.com/news?pz=1&cf=all&ned=us&hl=en&output=rss':
                    position2 = source.find(' -',position1)
                else:
                    position2 = source.find('</title>', position1)
                del_position = source.find('</title>', position2)
                headline1 = source[position1+7:position2]
                published_position1 = source.find('<pubDate>', position1)
                published_position2 = source.find("""</pubDate>""", published_position1)
                published = source[published_position1+9:published_position2]

                #Finds position of headline in the feed, then stores it and the time  date info to string objects
                #if published[-3:-1] == 'GMT':
                    #published[-12:-11] = int(published[-12:-11]) +

                if url == 'http://rss.cnn.com/rss/cnn_topstories.rss':
                    published = published[-12:-4]

                    #Huff Po had an extra -500 at the end of all of their titles so I had to make an exception in the scraper
                    
                if url == 'http://www.huffingtonpost.com/feeds/verticals/business/index.xml':
                    published = published[-14:-6]
                source = source.replace(source[:del_position+8], '')

                #Checks if the headline has already been stored
                if not headline1 in current_headlines:
                    new_headline = storeData.headline(headline1, key, published)
                    if new_headline.checkIfRelevant(companys.keys())[0]:
                        for company1 in new_headline.checkIfRelevant(companys.keys())[1]:
                            write_headlinetxt.headline_text_writer(header, company1, new_headline)
                        headlines.append(new_headline.getHeadline())                
            else:
                break
            
    return headlines




