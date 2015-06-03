#A program to collect Stock Price data and Headlines and store them to Text Files
#By Daniel Graham


import urllib
import datetime
import NewsScraper
import headline_checker
import stockPriceScraper
import string
import time
import write_headlinetxt
import Stock_text_writer



class newsSite:

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
        return headline_checker.checker(self.headline, company_list)
        

class stock:

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
        stock.price = stockPriceScraper.scraper(url)
        return stockPriceScraper.scraper(url)




def main():
    company_dictionary = {'Google': 'Goog', 'Amazon':'AMZN', 'Best Buy': 'BBY', 'Sony': 'SNE', 'Microsoft': 'MSFT', 'Tesla Motors': 'TSLA'}
    site_dictionary = {'CNN Top Stories' : 'http://rss.cnn.com/rss/cnn_topstories.rss', 'Huffington Post Full': 'http://feeds.huffingtonpost.com/huffingtonpost/raw_feed', 'New York Times Homepage': 'http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'}
    stock_list = []
    known_headlines = []
    for key in company_dictionary:
        new_stock = stock(key, company_dictionary[key])
        stock_list.append(new_stock)  
    header = '%s/%s/%s\n' % (datetime.datetime.now().day, datetime.datetime.now().month, datetime.datetime.now().year) 
    while ((int(datetime.datetime.now().hour) >= 9 and int(datetime.datetime.now().minute) >= 30) or int(datetime.datetime.now().hour) >= 10) and int(datetime.datetime.now().hour) < 16:
        time.sleep(60)
        Stock_text_writer.stock_writer(header, stock_list)
        current_headlines = NewsScraper.scraper(header, company_dictionary , site_dictionary, known_headlines)
        for headline2 in current_headlines:
            known_headlines.append(headline2)
        print known_headlines
    


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
