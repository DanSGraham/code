#A program to collect Stock Price data and Headlines and store them to Text Files
#By Daniel Graham
#If a headline is posted on multiple feeds it shows up in the txt. Need to only keep first posting.

import urllib
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

    def __init__(self, headline, origin, post_time):

        self.headline = headline
        self.origin = origin
        self.time = post_time

    def getTime(self):
        return self.time

    def getHeadline(self):
        return self.headline

    def getOrigin(self):
        return self.origin

    def checkIfRelevant(self, company_list):
        return checker(self.headline, company_list)
        

class stock:

    """This class creates a stock object that can scrape it's price from the Nasdaq site"""
    
    def __init__(self, company, ticker):
        
        self.company = company
        self.ticker = ticker
 

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

def checker(headline, company_list):
    
    '''This function checks if a headline has a company in it. If so, it returns True and the companies in that headline'''
    
    companies_in_headline = []
    ToF = False
    for company in company_list:
        if company in headline and headline[-11:] != 'Google News':
            companies_in_headline.append(company)
            ToF = True
    return (ToF, companies_in_headline)

def scraper(url):

    """This program scrapes stock prices from nasdaq's website"""
    
    stockPricepage = urllib.urlopen(url)
    stockPricepagestring = stockPricepage.read()
    position1 = stockPricepagestring.find("""<div id="qwidget_lastsale" class="qwidget-dollar">""")
    position2 = stockPricepagestring.find("""<""", position1+50)
    stockPrice = stockPricepagestring[position1+50:position2]
    return stockPrice




def store():
    """This function scrapes stock and headline data and stores them to text documents for later use in the graph suite"""
    
    company_dictionary = companies_dictionary.companies_dict
    site_dictionary = headlines_dictionary.full_headline_dictionary
                       
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
        #while True:
        j = 0
        #while ((int(datetime.datetime.now().hour) >= 9 and int(datetime.datetime.now().minute) >= 30) or int(datetime.datetime.now().hour) >= 10) and int(datetime.datetime.now().hour) < 16:
        time.sleep(15)
        j += 1
        Stock_text_writer.stock_writer(header, stock_list)
        if j % 240 == 0:
            current_headlines = NewsScraper.scraper(header, company_dictionary , site_dictionary, known_headlines)
            for headline2 in current_headlines:
                 known_headlines.append(headline2)
            
    


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
