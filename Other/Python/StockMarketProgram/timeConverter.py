#A program to convert time to EST
#By Daniel Graham

import convertTimeToSeconds
import time

January = 31
February = 28
March = 31
April = 30
May = 31
June = 30
July = 31
August = 31
September = 30
October = 31
November = 30
December = 31
months_list = [January, February, March, April, May, June, July, August, September, October, November, December]
months_string = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
days_of_week = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

#ISSUE WITH TIME CONVERSION. CHECK EACH SITE FOR BUGS.
def converter(time_string):
    if time_string[-3:] == 'EST' or time_string[-3:] == 'EDT':
        return time_string
    else:
        time_in_seconds = convertTimeToSeconds.convert_to_seconds(time_string[-12:-4])
        if time_string[-3:] == 'GMT' or time_string[-3:] == 'UTC':
            new_time = time_in_seconds - 5*3600
            if new_time < 0:
                day_of_week = days_of_week[days_of_week.index(time_string[0:3])-1]
                day_of_month = int(time_string[5:7]) - 1
                if day_of_month <= 0:
                    month = months_string[months_string.index(time_string[8:11]) - 1]
                    if month == 'Dec':
                        year = int(time_string[12:16]) - 1
                    else:
                        year = int(time_string[12:16])
                    day_of_month = months_list[months_string.index(month)]
                else:
                    year = int(time_string[12:16])
                    month = time_string[8:11]
                new_time = 24*3600 + new_time
                EST_time = convertTimeToSeconds.convert_to_regtime(new_time)
            else:
                day_of_week = time_string[0:3]
                day_of_month = int(time_string[5:7])
                month = time_string[8:11]
                year = int(time_string[12:16])
                EST_time = convertTimeToSeconds.convert_to_regtime(new_time)
                
            return day_of_week + ', ' + str(day_of_month) + ' ' + month + ' ' + str(year) + ' ' + EST_time + ' ' + 'EST'
