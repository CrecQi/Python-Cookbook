from datetime import datetime, timedelta
def date_range(start, stop, step):
	while start < stop:
		yield start
		start += step

for day in date_range(datetime(2012,9,1), datetime(2012,10,1), timedelta(hours = 24)):
	print day
