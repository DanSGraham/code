import datetime
import urllib
import time

#THIS code should activate during the regular trading day. Takes stock price information and turns it into text data that then writes to a text document.
#Program to be run each day to record stock prices.
company = "Google"
file_name = company + "StockPrices.txt"
text_file = open(file_name, 'a')
current_datetime = datetime.datetime.now()

header = ("%s/%s/%s\n" % (current_datetime.day, current_datetime.month, current_datetime.year))
dayDict ={1:'abc'}
prev_time = 1
time_stopped = " "
time_returned = " "
body_string = " "
j = 0
while ((int(datetime.datetime.now().hour) >= 9 and int(datetime.datetime.now().minute) >= 30) or int(datetime.datetime.now().hour) >= 10) and int(datetime.datetime.now().hour) < 16: 
    time.sleep(5)
    try:
        stockPricepage = urllib.urlopen("http://www.nasdaq.com/symbol/goog")
        if time_stopped != ' ' and time_returned != ' ' and time_stopped != prev_time_stopped:
            header = header + time_stopped + time_returned
            prev_time_stopped = time_stopped
            
        stockPricepagestring = stockPricepage.read()

        position1 = stockPricepagestring.find("""<div id="qwidget_lastsale" class="qwidget-dollar">""")
        position2 = stockPricepagestring.find("""<""", position1+50)
        stockPrice = stockPricepagestring[position1+50:position2]
        if dayDict[prev_time] != stockPrice:
            print stockPrice
            dayDict[str(datetime.datetime.now())] = stockPrice
            prev_time = str(datetime.datetime.now())

    except:
        if j == 0:
            time_stopped = "## Time Stopped %s:%s:%s\n" % (current_datetime.hour, current_datetime.minute, current_datetime.second)
            j = 1
        else:
            time_returned = "## Time Returned %s:%s:%s\n" % (current_datetime.hour, current_datetime.minute, current_datetime.second)

del dayDict[1]        
for key in dayDict:
    body_string = body_string + key + ':' + dayDict[key] + ', '

print body_string
print header
text_file.write(header+body_string)
text_file.close()
