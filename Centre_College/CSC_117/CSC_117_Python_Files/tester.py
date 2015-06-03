
import urllib
import stockPriceScraper
import string

def main():
    url = 'http://www.nasdaq.com/symbol/' + string.lower('Goog')
    return stockPriceScraper.scraper(url)
