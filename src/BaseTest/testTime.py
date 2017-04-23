import datetime
import math
import time

day1 = time.strptime("20170223", "%Y%m%d")
print "day1: year=%s, month=%s, day=%s" % (day1[0], day1[1], day1[2])

day2 = time.strptime("20170305", "%Y%m%d")
print "day2: year=%s, month=%s, day=%s" % (day1[0], day1[1], day1[2])

date1 = datetime.datetime(day1[0], day1[1], day1[2])
date2 = datetime.datetime(day2[0], day2[1], day2[2])

print "interval of date1 and date2 is %d" % (date2 - date1).days

print math.log(2, math.e)
