 #-*- coding: utf-8 -*- 
from helper.kakao_geocoder_api import KakaoGeocoderApi # GEOCODER API 클래스
from execute.utils.cache_mapper import CacheMapper
from repository.buidling_db_handler import BuildingDBHandler
from helper.mongo_data_parser import MongoDataParser
from datetime import datetime
import os
import json

def edit_molit_json_use_geocoder_api(building_list, cache_address_map):
    geocoder = KakaoGeocoderApi()
    location = {}

    for building in building_list:
        if "latitude" in building:
            continue

        location_string = building["full_number_address"]

        if location_string in cache_address_map:
            # 캐시 맵에 데이터가 있는 경우
            location = cache_address_map[location_string]
            building["latitude"] = location["latitude"]
            building["longitude"] = location["longitude"]
            building["full_address"] = location["full_address"]
        else:
            # 캐시 맵에 데이터가 없는 경우
            # 카카오 API 호출

            response = geocoder.get_kakao_geocoder_api_address_to_location(location_string)
            location = False

            try :
                location = response["documents"]
            except :
                print(f"error: ${location_string}")
        
            if location == False:
                continue
            if len(location) == 0:
                continue
            # 데이터 삽입
            if location[0]["road_address"] != None:
                building["latitude"] = location[0]["y"]
                building["longitude"] = location[0]["x"]
                building["full_address"] = location[0]["road_address"]["address_name"]
            else:
                building["latitude"] = location[0]["y"]
                building["longitude"] = location[0]["x"]
                building["full_address"] = ""

            building["kakao"] = True
            building["etc"] = location
            # 캐시 맵 생신
            cache_address_map[location_string] = {}
            cache_address_map[location_string]["latitude"] = building["latitude"]
            cache_address_map[location_string]["longitude"] = building["longitude"] 
            cache_address_map[location_string]["full_address"] = building["full_address"]

    return building_list

def kakao_geocoder_api_job(start_year, start_month): # GEOCODER API 사용 함수
    parse = MongoDataParser()
    cache_mapper = CacheMapper()
    building_repository = BuildingDBHandler()
    building_find_list = building_repository.find_item(
        {"deal_year" : start_year, 'deal_month': start_month}
    )
    building_parse_list = parse.parse_many_no_op_id(building_find_list)
    cache_address_map = cache_mapper.return_cache_address_map()
    building_list = edit_molit_json_use_geocoder_api(building_parse_list, cache_address_map)
    building_repository.save_item_many(building_list)
    print("END")

def kakao_geocoder_api_cron_job(): # GEOCODER API 사용 함수
    parse = MongoDataParser()
    current_date_year = datetime.today().year ## 비교 요청 첫번째 년도
    current_date_month = datetime.today().month ## 비교 요청 첫번째 달수
    cache_mapper = CacheMapper()
    building_repository = BuildingDBHandler()
    building_find_list = building_repository.find_item(
        {"deal_year" : current_date_year, 'deal_month': current_date_month}
    )
    building_parse_list = parse.parse_many_no_op_id(building_find_list)
    cache_address_map = cache_mapper.return_cache_address_map()
    building_list = edit_molit_json_use_geocoder_api(building_parse_list, cache_address_map)
    building_repository.save_item_many(building_list)
    print("END")
