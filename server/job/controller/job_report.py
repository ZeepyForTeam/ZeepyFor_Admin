 #-*- coding: utf-8 -*- 
from flask_restful import Resource, reqparse
from job.service.job_report_service import JobReportService
from flask_jwt_extended import jwt_required

class JobReport(Resource):
    def __init__(self):
        self.job_report_service = JobReportService()

    # 현재 스케줄링 되어 있는 잡 목록 조회 
    @jwt_required()
    def get(self):
        args = self.__make_get_arg()
        return self.job_report_service.get_all()

    '''
    Argument Create
    - private method
    '''

    def __make_get_arg(self):
        parser = reqparse.RequestParser()
        return parser.parse_args()