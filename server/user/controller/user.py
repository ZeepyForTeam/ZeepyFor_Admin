 #-*- coding: utf-8 -*- 
from flask_restful import Resource, reqparse
from user.service.user_service import UserService

class User(Resource):
    def __init__(self):
        self.user_service = UserService()

    # 회원가입
    def post(self):
        args = self.__make_post_arg()
        return self.user_service.create(args)

    # 아이디 삭제
    def delete(self):
        args = self.__make_delete_arg()
        return self.user_service.delete_by_email(args)

    '''
    Argument Create
    - private method
    '''

    def __make_post_arg(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        parser.add_argument('nickname', type=str, required=True)
        return parser.parse_args()

    def __make_delete_arg(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True)
        return parser.parse_args()