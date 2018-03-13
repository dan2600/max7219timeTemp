from urllib2 import urlopen
from datetime import datetime, timedelta
def getDateTime():
	res = urlopen('http://just-the-time.appspot.com/')
	time_str = res.read().strip()
	datetimeOB = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
	datetimeOB = datetimeOB - timedelta(hours=4)
	return datetimeOB