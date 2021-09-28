 #-*- coding: utf-8 -*- 

from helper.zeepy_for_server_helper import ZeepyForServerHelper
from repository.buidling_db_handler import BuildingDBHandler
from helper.mongo_data_parser import MongoDataParser
from datetime import datetime
import os
import json
import time
import re
from datetime import datetime

'''
일반 인서트 방식
- 빌딩, 빌딩 거래 내역 인서트
- 빌딩 한개당 한번의 API 호출
- 테스트 용 익스큐터
'''

def upload_building_in_zeepy(building_list):

    zeepy = ZeepyForServerHelper()
    regex = "\(.*\)|\s-\s.*"

    for building in building_list:

        if 'latitude' not in building or 'longitude' not in building:
            continue

        if 'full_address' not in building or building['full_address'] == "":
            continue

        full_road_address = ""
        short_road_address = ""
        
        build_year = 0

        if building['build_year'] != '':
            build_year = building['build_year']
        
        apartmentName = building['apartment'].replace(" ", "")
        shortAddress = building['short_address']
        full_number_address = building['full_number_address']  
        short_number_address = building['short_number_address']
        building_type = building['type']
        area_code = building['area_code']
        using_area = building['using_area']
        latitude = building['latitude']
        longitude = building['longitude']
        address = building['full_address']

        deal_year = building['deal_year']
        deal_month = building['deal_month']
        deal_day = building['deal_day']

        deal_date = int(time.mktime(datetime.strptime(f"{deal_year}-{deal_month}-{deal_day}", '%Y-%m-%d').timetuple())) * 1000
        floor = building['floor']
        monthly_rent = building['monthly_rent']
        deposit = building['deposit']

        regex_address = re.sub(regex, '', address) # 정규식을 통해 괄호와 괄호안 문자열 제거
        replace_address = " ".join(regex_address.split())

        full_road_address = f"{replace_address} {apartmentName}"

        short_road_address_none_apart = replace_address.replace(shortAddress, "").strip()
        short_road_address = f"{short_road_address_none_apart} {apartmentName}"

        full_road_address = full_road_address.replace("  ", " ")
        short_road_address = short_road_address.replace("  ", " ")

        full_road_address = full_road_address.replace("  ", " ")
        short_road_address = short_road_address.replace("  ", " ")

        full_road_address = full_road_address.replace("  ", " ")
        short_road_address = short_road_address.replace("  ", " ")

        building_data = {
            'buildYear' : build_year,
            'apartmentName' : apartmentName,
            'shortAddress' : shortAddress,
            'fullRoadNameAddress' : full_road_address,
            'shortRoadNameAddress' : short_road_address,
            'fullNumberAddress' : full_number_address,
            'shortNumberAddress' : short_number_address,
            'exclusivePrivateArea' : using_area,
            'areaCode' : area_code,
            'latitude' : latitude,
            'longitude' : longitude,
            'buildingType' : building_type,
        }

        response_get_building = zeepy.get_building(full_number_address)

        if response_get_building.status_code == 404:
            response_upload = zeepy.upload_building(building_data)
            split_location = response_upload.headers['Location'].split("/")
            building_id = int(split_location[3])
            response_upload.close()
        else:
            building_id = json.loads(response_get_building.content)["id"]

        response_get_building.close()

        building_deal_data = {
            'buildingId' : building_id,
            'dealDate' : deal_date,
            'deposit' : deposit,
            'monthlyRent' : monthly_rent,
            'dealCost' : 0,
            'floor' : floor
        }

        response_get_building_deal = zeepy.get_building_deal(building_id, floor)

        if response_get_building_deal.status_code == 404:
            response_last = zeepy.upload_building_deal(building_deal_data)
            response_last.close()
        else:
            _id = json.loads(response_get_building_deal.content)["id"]
            response_last = zeepy.update_building_deal(building_deal_data, _id)
            response_last.close()

        response_get_building_deal.close()
        time.sleep(1)

def insert_building_job(start_year, start_month):
    parse = MongoDataParser()
    building_repository = BuildingDBHandler()
    building_find_list = building_repository.find_item(
        {"deal_year" : start_year, 'deal_month': start_month}
    )
    building_parse_list = parse.parse_many_no_op_id(building_find_list)
    upload_building_in_zeepy(building_parse_list)

def insert_building_cron_job(start_year, start_month):
    parse = MongoDataParser()
    building_repository = BuildingDBHandler()
    current_date_year = datetime.today().year ## 비교 요청 첫번째 년도
    current_date_month = datetime.today().month ## 비교 요청 첫번째 달수
    building_find_list = building_repository.find_item(
        {"deal_year" : current_date_year, 'deal_month': current_date_month}
    )
    building_parse_list = parse.parse_many_no_op_id(building_find_list)
    upload_building_in_zeepy(building_parse_list)