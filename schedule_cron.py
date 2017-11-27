from crontab import CronTab 


my_cron = CronTab(user='shauncox')
job = my_cron.new(command='python3 /Users/shauncox/cron_job/write_date.py')
job.minute.every(1)

my_cron.write()