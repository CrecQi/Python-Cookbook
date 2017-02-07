from datetime import datetime, timedelta
import sys
def date_range(start, stop, step):
	while start < stop:
		yield start
		start += step

print "Input dates like 2012,9,1:\n"
time_0 = int(input("The start date:"))
time_1 = int(input("The first day of the next month:"))
for day in date_range(datetime(time_0), datetime(time_1), timedelta(hours = 24)):
	print day
