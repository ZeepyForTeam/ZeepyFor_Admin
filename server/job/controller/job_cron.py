 #-*- coding: utf-8 -*- 
from flask_restful import Resource, reqparse
from job.service.job_service import JobService
from flask_jwt_extended import jwt_required

class JobCron(Resource):
    def __init__(self):
        self.job_service = JobService()
    # 잡 등록
    # @jwt_required()
    def post(self):
        args = self.__make_post_arg()
        return self.job_service.set_cron_schedule(args)

    '''
    Argument Create
    - private method
    '''

    def __make_post_arg(self):
        parser = reqparse.RequestParser()
        parser.add_argument('nickname', type=str, required=True)
        parser.add_argument('run_type', type=str, required=True)
        parser.add_argument('cron_day', type=str, required=True)
        parser.add_argument('cron_hour', type=str, required=True)
        parser.add_argument('cron_minute', type=str, required=False, default="0")
        return parser.parse_args()