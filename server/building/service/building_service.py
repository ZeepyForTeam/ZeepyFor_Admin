 #-*- coding: utf-8 -*- 
from flask import jsonify
from repository.buidling_db_handler import BuildingDBHandler
from helper.mongo_data_parser import MongoDataParser
from bson.objectid import ObjectId

class BuildingService:
    def __init__(self):
        self.building_repository = BuildingDBHandler()
        self.parse = MongoDataParser()

    def get_pagenate(self, args):
        page = 1
        if "page" in args:
            page = args.page

        total = self.building_repository.count_items()
        data = self.building_repository.find_item_pagenate(page, None)
        response = jsonify(body=self.parse.parse_many(data), page=page, offset=50, total=total, totalPage=((total // 50) + 1))
        response.status_code = 200
        return response

    def create(self, args):
        _id = self.building_repository.insert_item_one(args)
        response = jsonify()
        response.status_code = 201
        response.headers['location'] = f"/api/buildings/{str(_id)}"
        response.autocorrect_location_header = False
        return response
    
    def create_many(self, args):
        self.building_repository.insert_item_many(args)
        response = jsonify(message="success")
        response.status_code = 200
        return response
    
    def delete_by_id(self, args):
        self.building_repository.delete_item_one({"_id" : ObjectId(args._id)})
        response = jsonify()
        response.status_code = 204
        return response