#A program to check headlines from different websites and return a list of headlines that are relevant.
#By Daniel Graham

import NewsScraper
import headline_checker
import datetime
import urllib
import string
import time
from StockPriceCalculator import newsSite
from StockPriceCalculator import headline


def headlinelist(company_list):
    newsSiteList = []
    relevant_headlines = []
    relevant_headlines_status = 'Empty'
    newsSiteDictionary = {'Google News':'https://news.google.com/', 'New York Times' : 'http://www.nytimes.com/', 'CNN': 'http://www.cnn.com/', 'Yahoo News': 'http://news.yahoo.com/', 'Huffington Post': 'http://www.huffingtonpost.com/'}
    for key in newsSiteDictionary:
        site_object = newsSite(newsSiteDictionary[key], key)
        newsSiteList.append(site_object)

    for site in newsSiteList:
        headlines = site.getHeadlines()
        time.sleep(1)
        for headline1 in headlines:
            no_append = False
            siteHeadline = headline(headline1, site.getURL())
            if 'on Google+' in headline1:  #a tag on the front page of google news everytime
                no_append = True
            if siteHeadline.checkIfRelevant(company_list)[0] and relevant_headlines_status == 'Empty':
                relevant_headlines.append(siteHeadline)
                relevant_headlines_status = 'Not Empty'
            if relevant_headlines_status != 'Empty':
                for headline2 in relevant_headlines:
                    if headline1 == headline2.getHeadline():
                        no_append = True
            if not no_append and siteHeadline.checkIfRelevant(company_list)[0]:
                relevant_headlines.append(siteHeadline)


    return relevant_headlines    


