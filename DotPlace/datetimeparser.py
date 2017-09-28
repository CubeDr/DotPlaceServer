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
	return int(time[12:16])

def month(time):
	return int(time[8:10])

def date(time):
	return int(time[5:7])

def hour(time):
	return int(time[17:19])

def minute(time):
	return int(time[20:22])

def second(time):
	return int(time[23:25])
