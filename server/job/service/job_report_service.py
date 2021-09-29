 #-*- coding: utf-8 -*- 
from flask import jsonify
from repository.job_report_db_handler import JobReportDBHandler
from helper.mongo_data_parser import MongoDataParser
from bson.objectid import ObjectId
import datetime

class JobReportService:
    def __init__(self):
        self.job_report_repository = JobReportDBHandler()
        self.parse = MongoDataParser()

    def get_all(self):
        data = self.job_report_repository.find_item()
        response = jsonify(self.parse.parse_many(data))
        response.status_code = 200
        return response