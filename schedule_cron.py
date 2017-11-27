from crontab import CronTab 


my_cron = CronTab(user='shauncox')

for job in my_cron:
	print (job)
