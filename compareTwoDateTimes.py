import datetime
now = datetime.datetime.now()
print now.year, now.month, now.day, now.hour, now.minute, now.second


def isNowInTimePeriod(startTime, endTime, nowTime):
    if startTime < endTime:
        return nowTime >= startTime and nowTime <= endTime
    else: #Over midnight
        return nowTime >= startTime or nowTime <= endTime

#set the date and time format
date_format = "%Y-%m-%d %H:%M:%S"
str1 = "2019-07-17 00:55:00"
str2 = "2019-07-17 01:55:00"

#convert string to actual date and time
time1  = datetime.datetime.strptime(str1, date_format)
time2  = datetime.datetime.strptime(str2, date_format)
 
#find the difference between two dates
diff = time2 - time1

nw = datetime.datetime.now()
# total seconds difference
print isNowInTimePeriod(time1, time2, nw)


'''
start_time = '13::55::26'
end_time = '14::55::26'
start_time_obj = datetime.datetime.strptime(start_time, '%H::%M::%S').time()
end_time_obj = datetime.datetime.strptime(end_time, '%H::%M::%S').time()
print(start_time_obj)
print(end_time_obj)
print type(start_time_obj)
'''
