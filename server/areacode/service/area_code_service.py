 #-*- coding: utf-8 -*- 
from flask import jsonify
from repository.area_code_db_handler import AreaCodeDBHandler
from helper.mongo_data_parser import MongoDataParser
from bson.objectid import ObjectId

class AreaCodeService:
    def __init__(self):
        self.area_code_repository = AreaCodeDBHandler()
        self.parse = MongoDataParser()

    def get_all(self):
        data = self.area_code_repository.find_item()
        response = jsonify(self.parse.parse_many(data))
        response.status_code = 200
        return response

    def create(self, args):
        _id = self.area_code_repository.insert_item_one(args)
        response = jsonify()
        response.status_code = 201
        response.headers['location'] = f"/api/codes/{str(_id)}"
        response.autocorrect_location_header = False
        return response
    
    def delete_by_id(self, args):
        self.area_code_repository.delete_item_one({"_id" : ObjectId(args._id)})
        response = jsonify()
        response.status_code = 204
        return response