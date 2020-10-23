from crontab import CronTab
cron = CronTab(user='root')
job = cron.new(command='python /home/pi/roos/updater.py')
job.minute.on(0)
job.hour.on(0)
cron.write()
