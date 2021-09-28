
# 스케줄러
from pytz import utc
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.executors.pool import ThreadPoolExecutor

class Scheduler:
    def __init__(self):
        jobstores = {
            'default': MongoDBJobStore(
                database='zeepy_db', 
                collection='jobs', 
                host='localhost', 
                port=27017
            )
        }  

        executors = {
            'default': ThreadPoolExecutor(20)
        }

        job_defaults = {
            'coalesce': False,
            'max_instances': 3
        }

        self.scheduler = BackgroundScheduler(
            jobstores=jobstores, 
            executors=executors, 
            job_defaults=job_defaults, 
            timezone=utc
        )
        self.scheduler.start()
        
    
    def return_current_pending_jobs(self):
        return self.scheduler.get_jobs()
    
    def remove_job(self, job_id):
        self.scheduler.remove_job(job_id)
    
    def add_job_one_time(self, execute_job_func, job_id, datetime, args=[]):
        self.scheduler.add_job(
            execute_job_func, 
            'date', 
            run_date=datetime, 
            id=job_id, 
            timezone="Asia/Seoul",
            args=args
        )

    def add_job_interval(self, execute_job_func, job_id, interval_week):
        self.scheduler.add_job(
            execute_job_func, 
            'interval', 
            weeks=interval_week, 
            id=job_id
        )
    
    def add_job_cron_all_month(self, execute_job_func, job_id, cron_day, cron_hour, cron_minute):
        self.scheduler.add_job(
            execute_job_func, 
            'cron', 
            month='1-12',  
            day=cron_day, 
            hour=cron_hour,
            minute=cron_minute, 
            id=job_id,
            timezone="Asia/Seoul"
        )