"""
This is a program to assist me in data scraping. Given certain tags to
look for the program will strip data from a website and store it in a
text file.
"""

#By Daniel Graham


class DataHog:
	
	def __init__(self, html_to_scrape):
		self.scrape_site = html_to_scrape
