#A program to collect Stock Price data and Headlines and store them to Text Files
#By Daniel Graham

#TODO
#CURRENTLY SCRAPES HEADLINES SUCCESSFULLY AND STORES THEM IN A list. Next is to convert published data into seconds and check stock price scraping(CONVERT TIMEZONES AND USE A DATETIME OBJECT). Once everything scrapes correctly, time to store in a txt file. Finally display the data on a graph.
import urllib
from pytz import
import calendar
import datetime
import NewsScraper
import string
import time
import write_headlinetxt
import Stock_text_writer
import companies_dictionary
import headlines_dictionary

class newsSite:

    """This class creates a newsSite object with a getHeadlines method to scrape headlines"""

    def __init__(self, url, name):
        
        self.url = url
        self.name = name

    def getName(self):
        return self.name

    def getURL(self):
        return self.url
    
    def getHeadlines(self):
        return NewsScraper.scraper(self.url)
        
    def __str__(self):
        return "The news site is " + self.name + ", at" + self.url

class headline:

    """This class creates a headline object which can check if it is relevant to the company list"""

    monthDict = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "June": 6, "July": 7, "Aug": 8, "Sept": 9, "Oct": 10, "Nov": 11, "Dec": 12}
    
    def __init__(self, headline, origin, post_time):
        self.headline = headline
        self.companiesInHeadline = []
        self.relevant = False
        self.origin = origin
        self.time = post_time
        try:
            timeDateList = self.time.split()
            year = int(timeDateList[3])
            month = self.monthDict[timeDateList[2]]
            day = int(timeDateList[1])
            timeList = timeDateList[4].split(":")
            hour = timeList[0]
            minute = timeList[1]
            second = timeList[2]
            timeZone = timeDateList[5]
            hlDateTime = datetime.datetime(year, month, day, hour, minute, second
            
        except:
            print "Something went wrong with date conversion"
            

    def getTime(self):
        return self.time


    def getCompaniesInHeadline(self):
        return self.companiesInHeadline
    
    def getHeadline(self):
        return self.headline

    def getOrigin(self):
        return self.origin

    def checkIfRelevant(self, company_list):
        companies_in_headline = []
        for company in company_list:
            if company in self.headline and self.headline[-11:] != 'Google News':
                self.companiesInHeadline.append(company)
                self.relevant = True

    def isRelevant(self):
        return self.relevant
        

class stock:

    """This class creates a stock object that can scrape it's price from the Nasdaq site"""
    
    def __init__(self, company, ticker):
        
        self.company = company
        self.ticker = ticker
        self.time = datetime.datetime.now()

    def getCompany(self):
        return self.company

    def getTicker(self):
        return self.ticker


    def getTime(self):
        return ("%s:%s:%s" % (datetime.datetime.now().hour, datetime.datetime.now().minute, datetime.datetime.now().second))
    
    def getPrice(self):
        url = 'http://www.nasdaq.com/symbol/' + str(string.lower(self.ticker))
        stock.price = scraper(url)
        return scraper(url)


def scraper(url):

    """This program scrapes stock prices from nasdaq's website. NOTE: NASDAQ NO LONGER WORKS. IDK WHY SAYS I DO NOT HAVE ACCESS."""
    
    stockPricepage = urllib.urlopen(url)
    stockPricepagestring = stockPricepage.read()
    position1 = stockPricepagestring.find("""<div id="qwidget_lastsale" class="qwidget-dollar">""")
    position2 = stockPricepagestring.find("""<""", position1+50)
    print stockPricepagestring
    stockPrice = stockPricepagestring[position1+50:position2]
    return stockPrice




def store():
    """This function scrapes stock and headline data and stores them to text documents for later use in the graph suite"""
    
    company_dictionary = companies_dictionary.companies_dict
    site_dictionary = headlines_dictionary.full_headline_dictionary
    #site_dictionary = {'CNN Top Stories' : 'http://rss.cnn.com/rss/cnn_topstories.rss',\
                      #'New York Times Homepage': 'http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml', 'CNN Most Popular': 'http://rss.cnn.com/rss/cnn_mostpopular.rss'\
                       #,'CNN Money': 'http://rss.cnn.com/rss/money_latest.rss', 'CNN Technology': 'http://rss.cnn.com/rss/cnn_tech.rss', 'CNN Recently Updated' : 'http://rss.cnn.com/rss/cnn_latest.rss'\
                       #,'Huffington Post Technology': 'http://www.huffingtonpost.com/feeds/verticals/technology/index.xml', 'New York Times Business': 'http://rss.nytimes.com/services/xml/rss/nyt/Business.xml',\
                       #'New York Times Technology': 'http://rss.nytimes.com/services/xml/rss/nyt/Technology.xml'}
    ###These two dictionaries are where new stocks or sites to scrape may be added

    day = datetime.datetime.now().day
    stock_list = []
    known_headlines = []
    
    for key in company_dictionary:
        new_stock = stock(key, company_dictionary[key])
        stock_list.append(new_stock)
    while True:
        header = '%s/%s/%s\n' % (datetime.datetime.now().day, datetime.datetime.now().month, datetime.datetime.now().year)
    ##This program only runs during stock trading hours, when price changes may be tracked.
        while True:
        #while ((int(datetime.datetime.now().hour) >= 9 and int(datetime.datetime.now().minute) >= 30) or int(datetime.datetime.now().hour) >= 10) and int(datetime.datetime.now().hour) < 16:
            time.sleep(1)
            #Stock_text_writer.stock_writer(header, stock_list)
            current_headlines = NewsScraper.scraper(company_dictionary , site_dictionary)
            for headline2 in current_headlines:
                append = True
                for headline3 in known_headlines:
                    if headline2.getHeadline() == headline3.getHeadline():
                        append = False
                if append:
                    
                    print headline2.getHeadline()
                    print headline2.getTime()
                    print headline2.getCompaniesInHeadline()
                    known_headlines.append(headline2)
            print "done"
            
    


#Progam can become smart. After gathering headline data. learn to make prediction about future stock price due to current headlines and knowledge of previous headlines and their keywords. 
#Instead of getting a headline and recording the price of the stock, the program will get headline and predict the change in price. Then return it's accuracy. 

###Two categories of news sites:
##    #Top news sites
##    #Top financial news sites
##
##
##
###List of companies I will track
##Google
##Hallmark
##GE
##Facebook
##Instagram
##Twitter
##Car Companies
##others
##
###Maybe split up by category and if the category comes up in news track the whole category?
