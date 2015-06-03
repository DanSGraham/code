from urllib import urlopen

#USES AN END TAG IDENTIFIER FOR POSITION

def scraper():

    
    html = urlopen('http://news.yahoo.com/')

    source = html.read()

    key = "ends with </a> but the character before the </a> is not >"

    headlines = []
    while True:
        if '</a>' in source:
            position2 = source.find('</a>')
            position1 = source.rfind('>',0,position2)
            headline = source[position1+1:position2]
            if headline != '' and headline != ' ' and headline != '  ' and headline != '   ' and headline != '    ':
                headlines.append(headline)
            source = source.replace(source[:position2+4], '')

        else:
            break
    return headlines
