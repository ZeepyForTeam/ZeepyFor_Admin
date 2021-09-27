 #-*- coding: utf-8 -*- 
from flask_restful import Resource, reqparse
from job.service.job_service import JobService
from flask_jwt_extended import jwt_required

class Job(Resource):
    def __init__(self):
        self.job_service = JobService()

    # 현재 스케줄링 되어 있는 잡 목록 조회 
    @jwt_required()
    def get(self):
        args = self.__make_get_arg()
        return self.job_service.get_all()

    # 잡 등록
    @jwt_required()
    def post(self):
        args = self.__make_post_arg()
        return self.job_service.create(args)

    # 스케줄링 된 잡 삭제
    @jwt_required()
    def delete(self):
        args = self.__make_delete_arg()
        return self.job_service.delete_by_id(args)

    '''
    Argument Create
    - private method
    '''

    def __make_post_arg(self):
        parser = reqparse.RequestParser()
        parser.add_argument('type', type=str, required=True)
        parser.add_argument('schedule_time', type=int, required=True)
        return parser.parse_args()

    def __make_get_arg(self):
        parser = reqparse.RequestParser()
        return parser.parse_args()

    def __make_delete_arg(self):
        parser = reqparse.RequestParser()
        parser.add_argument('_id', type=str, required=True)
        return parser.parse_args()