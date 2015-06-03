##Stock Market Program V2


import urllib

def stockPriceScraper(url):

    ##This method scrapes CNN money for the price of a stock given as the url.
    stockMarket = urllib.urlopen(url)
    stockMarketText = stockMarket.read()
    position1 = stockMarketText.find("""<span stream="last_282560" streamFormat="ToHundredth""")
    position2 = stockMarketText.find("""</span><div class="wsod_quoteLabel">""")
    print stockMarketText[position1 + 75:position2]


stockPriceScraper("http://money.cnn.com/quote/quote.html?symb=VRTX")
    

def headlineScraper(url, websiteName):
    website = urllib.urlopen(url)
    source = website.read()
    headlines = []
    while True:
        
        if websiteName == "CNN":
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
            
        if websiteName == "New York Times":
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

        if websiteName == "Fox News":
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
            
        if websiteName == "NBC":
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

        if websiteName == "Google News":
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

        if websiteName == "Wall Street Journal":
            
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

        source = source.replace(source[:del_position + 8], "")
        



