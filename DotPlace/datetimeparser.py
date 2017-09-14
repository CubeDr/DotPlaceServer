import datetime

def parseDatetime(time):
	print('parsing ' + time)
	return datetime.datetime(
		year(time),
		month(time),
		date(time),
		hour(time),
		minute(time),
		second(time)
	)

def year(time):
	return int(time[0:4])

def month(time):
	return int(time[5:7])

def date(time):
	return int(time[8:10])

def hour(time):
	return int(time[11:13])

def minute(time):
	return int(time[14:16])

def second(time):
	return int(time[17:19])