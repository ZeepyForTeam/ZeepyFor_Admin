 #-*- coding: utf-8 -*- 
from flask import jsonify
from repository.user_db_handler import UserDBHandler
from helper.mongo_data_parser import MongoDataParser
from bson.objectid import ObjectId

class UserService:
    def __init__(self):
        self.user_repository = UserDBHandler()
        self.parse = MongoDataParser()

    def create(self, args):
        response = jsonify()
        data = self.user_repository.find_item_one({"email" : args.email})

        if data != None:
            response = jsonify(message="email is already exists")
            response.status_code = 400
            return response

        _id = self.user_repository.insert_item_one(args)
        response.status_code = 201
        response.headers['location'] = f"/api/users/{str(_id)}"
        response.autocorrect_location_header = False
        return response
    
    def delete_by_email(self, args):
        self.user_repository.delete_item_one({"email" : args.email})
        response = jsonify()
        response.status_code = 204
        return response