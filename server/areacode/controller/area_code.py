 #-*- coding: utf-8 -*- 
from flask_restful import Resource, reqparse
from areacode.service.area_code_service import AreaCodeService
from flask_jwt_extended import jwt_required

class AreaCode(Resource):
    def __init__(self):
        self.area_code_service = AreaCodeService()

    @jwt_required()
    def get(self):
        return self.area_code_service.get_all()

    @jwt_required()
    def post(self):
        args = self.make_post_arg()
        return self.area_code_service.create(args)

    @jwt_required()
    def delete(self, id):
        args = self.make_delete_arg()
        return self.area_code_service.delete_by_id(args)

    def make_post_arg(self):
        parser = reqparse.RequestParser()
        parser.add_argument('SIDO_CODE', type=int, required=True)
        parser.add_argument('SIGUNGU_CODE', type=int, required=True)
        parser.add_argument('ADDRESS_NAME', type=str, required=True)
        return parser.parse_args()

    def make_get_arg(self):
        parser = reqparse.RequestParser()
        return parser.parse_args()

    def make_delete_arg(self):
        parser = reqparse.RequestParser()
        parser.add_argument('_id', type=str, required=True)
        return parser.parse_args()