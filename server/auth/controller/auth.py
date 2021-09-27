 #-*- coding: utf-8 -*- 
from flask_restful import Resource, reqparse
from auth.service.auth_service import AuthService

class Auth(Resource):
    def __init__(self):
        self.auth_service = AuthService()

    # 로그인
    def post(self):
        args = self.__make_post_arg()
        return self.auth_service.login(args)

    '''
    Argument Create
    - private method
    '''

    def __make_post_arg(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        return parser.parse_args()