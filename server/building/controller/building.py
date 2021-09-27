 #-*- coding: utf-8 -*- 
from flask_restful import Resource, reqparse
from building.service.building_service import BuildingService
from flask_jwt_extended import jwt_required

class Building(Resource):
    def __init__(self):
        self.building_service = BuildingService()

    # 현재 저장되어 있는 빌딩 관련 정보 반환 
    @jwt_required()
    def get(self):
        args = self.__make_get_arg()
        return self.building_service.get_pagenate(args)

    # 빌딩 단일 업로드
    def post(self):
        args = self.__make_post_arg()
        return self.building_service.create(args)

    #빌딩 단일 삭제
    @jwt_required()
    def delete(self):
        args = self.__make_delete_arg()
        return self.building_service.delete_by_id(args)

    '''
    Argument Create
    - private method
    '''

    def __make_post_arg(self):
        parser = reqparse.RequestParser()
        parser.add_argument('build_year', type=int, required=False)
        parser.add_argument('deal_year', type=int, required=True)
        parser.add_argument('dong', type=str, required=True)
        parser.add_argument('deposit', type=float, required=True)
        parser.add_argument('apartment', type=str, required=True)
        parser.add_argument('sigungu', type=str, required=False)
        parser.add_argument('deal_month', type=int, required=True)
        parser.add_argument('monthly_rent', type=int, required=True)
        parser.add_argument('deal_day', type=int, required=True)
        parser.add_argument('using_area', type=float, required=True)
        parser.add_argument('jibun', type=str, required=True)
        parser.add_argument('area_code', type=int, required=True)
        parser.add_argument('floor', type=int, required=True)
        parser.add_argument('latitude', type=float, required=False)
        parser.add_argument('longitude', type=float, required=False)
        parser.add_argument('full_address', type=str, required=False)
        parser.add_argument('type', type=str, required=True)
        parser.add_argument('kakao', type=bool, required=False)
        parser.add_argument('etc', type=list, required=False)
        return parser.parse_args()

    def __make_get_arg(self):
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, required=True)
        return parser.parse_args()

    def __make_delete_arg(self):
        parser = reqparse.RequestParser()
        parser.add_argument('_id', type=str, required=True)
        return parser.parse_args()