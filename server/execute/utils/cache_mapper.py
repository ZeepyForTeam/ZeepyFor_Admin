 #-*- coding: utf-8 -*- 
from repository.buidling_db_handler import BuildingDBHandler
from helper.mongo_data_parser import MongoDataParser
from datetime import datetime
import os
import json

class CacheMapper:
    def __init__(self):
        self.building_repository = BuildingDBHandler()
        self.parse = MongoDataParser()

    def return_cache_address_map(self):
        cache_address_map = {}
        building_find_list = self.building_repository.find_item()
        building_list= self.parse.parse_many(building_find_list)
        
        for building in building_list:
            if "latitude" not in building:
                continue

            location_string = building["full_number_address"]

            cache_address_map[location_string] = building
        return cache_address_map