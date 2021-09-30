 #-*- coding: utf-8 -*- 

from pytz import utc
from repository.job_report_db_handler import JobReportDBHandler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.events import (
    EVENT_SCHEDULER_START, EVENT_SCHEDULER_SHUTDOWN, EVENT_JOBSTORE_ADDED, 
    EVENT_JOBSTORE_REMOVED, EVENT_JOB_ADDED, EVENT_JOB_REMOVED, 
    EVENT_JOB_MODIFIED, EVENT_JOB_EXECUTED, EVENT_JOB_ERROR, EVENT_JOB_MISSED)
from job.scheduler.scheduler_event_listener import (
    scheduler_start_listener, scheduler_shutdown_listener, job_added_listener, 
    job_removed_listener, job_modified_listener, job_executed_listener, 
    job_error_listener, job_missed_listener)

class Scheduler:
    def __init__(self):
        jobstores = {
            'default': MongoDBJobStore(
                database='zeepy_db', 
                collection='jobs', 
                host='db', 
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
        
        self.scheduler.add_listener(scheduler_start_listener, EVENT_SCHEDULER_START)
        self.scheduler.add_listener(scheduler_shutdown_listener, EVENT_SCHEDULER_SHUTDOWN)
        self.scheduler.add_listener(job_added_listener, EVENT_JOB_ADDED)
        self.scheduler.add_listener(job_missed_listener, EVENT_JOB_MISSED)
        self.scheduler.add_listener(job_executed_listener, EVENT_JOB_EXECUTED)
        self.scheduler.add_listener(job_removed_listener, EVENT_JOB_REMOVED)
        self.scheduler.add_listener(job_error_listener, EVENT_JOB_ERROR)
        self.scheduler.add_listener(job_modified_listener, EVENT_JOB_MODIFIED)
    
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