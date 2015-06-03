from urllib import urlopen

def scraper(url):

    if url == 'https://news.google.com/':
        headlines = []
        newswebpage = urlopen(url)
        newspagestring = newswebpage.read()

        while True:
            if '''<span class="titletext">''' in newspagestring:
                position1 = newspagestring.find('''<span class="titletext">''')
                position2 = newspagestring.find('''</span>''', position1)
                headline = newspagestring[position1 + 24:position2]
                headlines.append(headline)
                newspagestring=newspagestring.replace(newspagestring[:position2],' ')        
            else: 
                break
        return headlines

