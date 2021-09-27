 #-*- coding: utf-8 -*- 
from flask_restful import Resource, reqparse
from molit.service.molit_service import MolitService

class Molit(Resource):
    def __init__(self):
        self.molit_service = MolitService()

    def get(self):
        return self.molit_service.get_jobs()

    def post(self):
        args = self.__make_post_arg()
        return self.molit_service.create(args)
    
    def delete(self):
        args = self.__make_delete_arg()
        return self.molit_service.delete_by_id(args)

    '''
    Argument Create
    - private method
    '''

    def __make_post_arg(self):
        parser = reqparse.RequestParser()
        parser.add_argument('start_year', type=int, required=True) 
        parser.add_argument('start_month', type=int, required=True) 
        parser.add_argument('end_year', type=int, required=True) 
        parser.add_argument('end_month', type=int, required=True) 

        parser.add_argument('apartment', type=bool, required=False) ## 아파트 전월세 잡 여부
        parser.add_argument('officetels', type=bool, required=False) ## 오피스텔 전월세 잡 여부
        parser.add_argument('family', type=bool, required=False) ## 단독/다가구 전월세 잡 여부
        parser.add_argument('alliance', type=bool, required=False) ## 연립다세대 전월세 잡 여부
        return parser.parse_args()

    def __make_get_arg(self):
        parser = reqparse.RequestParser()
        return parser.parse_args()

    def __make_delete_arg(self):
        parser = reqparse.RequestParser()
        parser.add_argument('job_id', type=str, required=True)
        return parser.parse_args()