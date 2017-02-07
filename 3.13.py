from datetime import datetime, date, timedelta
import calendar

def get_month_range(start_date = None):
	if start_date is None:
		start_date = date.today().replace(day = 1)
		_, days_in_month = calendar.monthrange(start_date.year, start_date.month) #list for Month of the year and Days of the month
		end_date = start_date + timedelta(days = days_in_month)-a_day  #timedelta function transfers an 'int' into a 'datetime.date' instance
		return start_date, end_date  #Both are 'datetime.date' instances

a_day = timedelta(days=1)  #represents a one-day time
first_day, last_day = get_month_range()
while first_day <= last_day:
	print first_day
	first_day += a_day
