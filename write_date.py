#!/bin/env python
from crontab import CronTab
import datetime


with open('date_info.txt', 'a') as output:
	output.write( '\n' + str(datetime.datetime.now()) )