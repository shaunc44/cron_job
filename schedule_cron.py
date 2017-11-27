#!/bin/env python
from crontab import CronTab 


my_cron = CronTab(user='shauncox')

job = my_cron.new(
		command = 'python3 /Users/shauncox/cron_job/write_date.py', 
		# command = 'python3 write_date.py', 
		comment = 'date_info'
	)
job.minute.every(1)

# my_cron.remove_all()

my_cron.write()