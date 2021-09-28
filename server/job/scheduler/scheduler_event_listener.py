 #-*- coding: utf-8 -*- 

from repository.job_report_db_handler import JobReportDBHandler
import datetime

def scheduler_start_listener(event):
    event_data_list = event.job_id.split("/")
    insert_job_report("EVENT_SCHEDULER_START", event_data_list, "")

def scheduler_shutdown_listener(event):
    event_data_list = event.job_id.split("/")
    insert_job_report("EVENT_SCHEDULER_SHUTDOWN", event_data_list, "")

def job_added_listener(event):
    event_data_list = event.job_id.split("/")
    insert_job_report("EVENT_JOB_ADDED", event_data_list, "")

def job_removed_listener(event):
    event_data_list = event.job_id.split("/")
    insert_job_report("EVENT_JOB_REMOVED", event_data_list, "")

def job_modified_listener(event):
    event_data_list = event.job_id.split("/")
    insert_job_report("EVENT_JOB_MODIFIED", event_data_list, "")

def job_executed_listener(event):
    event_data_list = event.job_id.split("/")
    insert_job_report("EVENT_JOB_EXECUTED", event_data_list, "")

def job_error_listener(event): 
    event_data_list = event.job_id.split("/")
    insert_job_report("EVENT_JOB_ERROR", event_data_list, event.traceback)

def job_missed_listener(event):
    event_data_list = event.job_id.split("/")
    insert_job_report("EVENT_JOB_MISSED", event_data_list, "")

def insert_job_report(event_code, event_data_list, trace_back):
    job_report_repository = JobReportDBHandler()
    job_report_repository.insert_item_one(
        {
            "event_code": event_code,
            "nickname": event_data_list[0],
            "job_first_add_time": event_data_list[1],
            "run_type": event_data_list[2],
            "job_type": event_data_list[3],
            "trace_back": trace_back,
            "event_time": datetime.datetime.now()
        }
    )