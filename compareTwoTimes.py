import datetime

def isNowInTimePeriod(startTime, endTime, nowTime):
    if startTime < endTime:
        return nowTime >= startTime and nowTime <= endTime
    else: #Over midnight
        return nowTime >= startTime or nowTime <= endTime

startTime = "00:55:00"
endTime = "01:55:00"

startTime = datetime.datetime.strptime(startTime, '%H:%M:%S')
startTime = datetime.time(startTime.hour, startTime.minute,startTime.second)

endTime = datetime.datetime.strptime(endTime, '%H:%M:%S')
endTime = datetime.time(endTime.hour, endTime.minute, endTime.second)

nw = datetime.datetime.now().time()


print isNowInTimePeriod(startTime, endTime, nw)
