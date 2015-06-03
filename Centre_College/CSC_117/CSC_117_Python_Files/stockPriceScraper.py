import urllib


def scraper(url):

    """This program scrapes stock prices from nasdaq's website"""
    
    stockPricepage = urllib.urlopen(url)
    stockPricepagestring = stockPricepage.read()
    position1 = stockPricepagestring.find("""<div id="qwidget_lastsale" class="qwidget-dollar">""")
    position2 = stockPricepagestring.find("""<""", position1+50)
    stockPrice = stockPricepagestring[position1+50:position2]
    return stockPrice
