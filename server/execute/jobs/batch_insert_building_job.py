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
배치 인서트 방식
- 빌딩 인서트
- API 호출 한번
- 배포용 용 익스큐터
'''
def make_buidings_dict():
    result = {}
    zeepy = ZeepyForServerHelper()
    response_get_building = zeepy.get_buildings()
    building_list = json.loads(response_get_building.content)
    for building in building_list:
        result[building["fullNumberAddress"]] = building["id"]
    return result

def bulk_insert_building_in_zeepy(building_list):
    zeepy_building_list = []

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


        zeepy_building_list.append(building_data)

    return zeepy_building_list

def bulk_insert_building_deal_in_zeepy(building_list, building_dict):
    zeepy_building_deal_list = []

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

        if full_number_address not in building_dict:
            continue

        building_data = {
            'buildingId' : building_dict[full_number_address],
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
            'dealDate' : deal_date,
            'deposit' : deposit,
            'monthlyRent' : monthly_rent,
            'dealCost' : 0,
            'floor' : floor
        }

        zeepy_building_deal_list.append(building_data)

    return zeepy_building_deal_list

def loop_to_get_all_building_list(building_repository, parse):
    total = building_repository.count_items()
    total_page=((total // 50) + 1)
    result = []
    for page in range(1, total_page + 1):
        data = building_repository.find_item_pagenate(page, None)
        result += parse.parse_many_no_op_id(data)
    return result

def batch_insert_all_building_job():
    zeepy = ZeepyForServerHelper()
    parse = MongoDataParser()
    building_repository = BuildingDBHandler()
    building_parse_list = loop_to_get_all_building_list(building_repository, parse)
    ## 건물 데이터 삽입
    building_list = bulk_insert_building_in_zeepy(building_parse_list)
    response_batch_insert_building = zeepy.batch_insert_building(building_list)
    response_batch_insert_building.close()
    ## 건물 거래 정보 삽입
    building_dict = make_buidings_dict()
    building_deal_list = bulk_insert_building_deal_in_zeepy(building_parse_list, building_dict)
    response_batch_insert_building = zeepy.batch_insert_building_deal(building_deal_list)
    response_batch_insert_building.close()

def batch_insert_building_job(start_year, start_month):
    zeepy = ZeepyForServerHelper()
    parse = MongoDataParser()
    building_repository = BuildingDBHandler()

    building_find_list = building_repository.find_item(
        {"deal_year" : start_year, 'deal_month': start_month}
    )
    building_parse_list = parse.parse_many_no_op_id(building_find_list)
    ## 건물 데이터 삽입
    building_list = bulk_insert_building_in_zeepy(building_parse_list)
    response_batch_insert_building = zeepy.batch_insert_building(building_list)
    response_batch_insert_building.close()
    ## 건물 거래 정보 삽입
    building_dict = make_buidings_dict()
    building_deal_list = bulk_insert_building_deal_in_zeepy(building_parse_list, building_dict)
    response_batch_insert_building = zeepy.batch_insert_building_deal(building_deal_list)
    response_batch_insert_building.close()

def batch_insert_building_cron_job():
    zeepy = ZeepyForServerHelper()
    parse = MongoDataParser()
    building_repository = BuildingDBHandler()
    current_date_year = datetime.today().year ## 비교 요청 첫번째 년도
    current_date_month = datetime.today().month ## 비교 요청 첫번째 달수

    building_find_list = building_repository.find_item(
        {"deal_year" : current_date_year, 'deal_month': current_date_month}
    )
    building_parse_list = parse.parse_many_no_op_id(building_find_list)
    ## 건물 데이터 삽입
    building_list = bulk_insert_building_in_zeepy(building_parse_list)
    response_batch_insert_building = zeepy.batch_insert_building(building_list)
    response_batch_insert_building.close()
    ## 건물 거래 정보 삽입
    building_dict = make_buidings_dict()
    building_deal_list = bulk_insert_building_deal_in_zeepy(building_parse_list, building_dict)
    response_batch_insert_building = zeepy.batch_insert_building_deal(building_deal_list)
    response_batch_insert_building.close()