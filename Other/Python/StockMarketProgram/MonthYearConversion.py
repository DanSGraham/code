#A program to convert Day and Month information into numerals
#By Daniel Graham


months_string = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def translate(date_string):
    day = int(date_string[5:7])
    month = date_string[8:11]
    month_number = months_string.index(month) + 1
    year = int(date_string[12:16])
    number_time = '%02d/%02d/%04d' % (day, month_number, year)
    return number_time

