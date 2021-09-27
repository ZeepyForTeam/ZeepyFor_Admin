 #-*- coding: utf-8 -*- 
from flask_restful import Resource, reqparse
from flask import request
from building.service.building_service import BuildingService
from flask_jwt_extended import jwt_required

class BuildingBatch(Resource):
    def __init__(self):
        self.building_service = BuildingService()

    # 빌딩 단일 업로드
    def post(self):
        args = self.__make_post_arg()
        return self.building_service.create_many(args)

    '''
    Argument Create
    - private method
    '''

    def __make_post_arg(self):
        return request.get_json()