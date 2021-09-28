 #-*- coding: utf-8 -*- 
from flask import jsonify
from repository.job_db_handler import JobDBHandler
from job.scheduler.scheduler import Scheduler
from execute.executer import Executer
from execute.jobs.molit_api_job import (molit_api_cron_job, molit_api_job)
from execute.jobs.kakao_geocoder_job import (kakao_geocoder_api_cron_job, kakao_geocoder_api_job)
from execute.jobs.insert_building_job import (insert_building_cron_job, insert_building_job)
from execute.jobs.batch_insert_building_job import (batch_insert_building_cron_job, batch_insert_building_job, batch_insert_all_building_job)
from helper.mongo_data_parser import MongoDataParser
from bson.objectid import ObjectId
import datetime

class JobService:
    def __init__(self):
        self.scheduler = Scheduler()
        self.executer = Executer()
        self.job_repository = JobDBHandler()
        self.parse = MongoDataParser()

    def get_all(self, args):
        data = self.job_repository.find_item()
        response = jsonify(self.parse.parse_many(data))
        response.status_code = 200
        return response

    def set_date_schedule(self, args):
        # JOB TYPE
        run_type = args.run_type
        nickname = args.nickname
        # JOB ARGUMENT
        start_year = args.arg_start_year
        start_month = args.arg_start_month
        end_year = args.arg_end_year
        end_month = args.arg_end_month
        # SCHEDULER PARAMS
        current_time = datetime.datetime.now()
        next_time = datetime.datetime.strptime(args.run_date, "%Y-%m-%d %H:%M:%S")
        job_id = f"{nickname}/{run_type}/date/{str(current_time)}"

        if run_type == "MOLIT":
            self.scheduler.add_job_one_time(
                molit_api_job,
                job_id,
                next_time,
                [start_year, start_month, end_year, end_month]
            )
        elif run_type == "KAKAO":
            self.scheduler.add_job_one_time(
                kakao_geocoder_api_job,
                job_id,
                next_time,
                [start_year, start_month]
            )
        elif run_type == "VWORLD":
            self.scheduler.add_job_one_time(
                self.executer.vworld_geocoder_jobs,
                job_id,
                next_time
            )
        elif run_type == "ZEEPY_BATCH_BUILDING":
            self.scheduler.add_job_one_time(
                batch_insert_building_job,
                job_id,
                next_time,
                [start_year, start_month]
            )
        elif run_type == "ZEEPY_BUILDING":
            self.scheduler.add_job_one_time(
                insert_building_job,
                job_id,
                next_time,
                [start_year, start_month]
            )
        else:
            response = jsonify(message="run_type is mismatching. check your parameters")
            response.status_code = 400
            return response
        
        response = jsonify(message="complete scheduled jobs")
        response.status_code = 200
        return response
    
    def set_cron_schedule(self, args):
        run_type = args.run_type
        nickname = args.nickname
        current_time = datetime.datetime.now()
        cron_day = args.cron_day
        cron_hour = args.cron_hour
        cron_minute = args.cron_minute
        job_id = f"{nickname}/{run_type}/cron/{str(current_time)}"

        if run_type == "MOLIT":
            self.scheduler.add_job_cron_all_month(
                molit_api_cron_job,
                job_id,
                cron_day,
                cron_hour,
                cron_minute
            )
        elif run_type == "KAKAO":
            self.scheduler.add_job_cron_all_month(
                kakao_geocoder_api_cron_job,
                job_id,
                cron_day,
                cron_hour,
                cron_minute
            )
        elif run_type == "VWORLD":
            self.scheduler.add_job_cron_all_month(
                self.executer.vworld_geocoder_jobs,
                job_id,
                cron_day,
                cron_hour,
                cron_minute
            )
        elif run_type == "ZEEPY_BATCH_BUILDING":
            self.scheduler.add_job_cron_all_month(
                batch_insert_building_cron_job,
                job_id,
                cron_day,
                cron_hour,
                cron_minute
            )
        elif run_type == "ZEEPY_BUILDING":
            self.scheduler.add_job_cron_all_month(
                insert_building_cron_job,
                job_id,
                cron_day,
                cron_hour,
                cron_minute
            )
        else:
            response = jsonify(message="type is mismatching. check your parameters")
            response.status_code = 400
            return response
        
        response = jsonify(message="complete scheduled jobs")
        response.status_code = 200
        return response
    
    def delete_schedule(self, args):
        self.job_repository.delete_item_one({"_id" : ObjectId(args._id)})
        response = jsonify()
        response.status_code = 204
        return response