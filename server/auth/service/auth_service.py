 #-*- coding: utf-8 -*- 
from flask import jsonify
from repository.user_db_handler import UserDBHandler
from helper.mongo_data_parser import MongoDataParser
from bson.objectid import ObjectId
from flask_jwt_extended import create_access_token

class AuthService:
    def __init__(self):
        self.user_repository = UserDBHandler()
        self.parse = MongoDataParser()

    def login(self, args):
        response = jsonify()
        data = self.user_repository.find_item_one({"email" : args.email, "password" : args.password})

        if data == None:
            response.status_code = 401
            return response
        
        nickname = data["nickname"]
        access_token = create_access_token(identity=str(args.email))

        response = jsonify(access_token=access_token, nickname=nickname)
        response.status_code = 200
        return response