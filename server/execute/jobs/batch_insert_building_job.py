 #-*- coding: utf-8 -*- 

from helper.zeepy_for_server_helper import ZeepyForServerHelper
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

def upload_json_data_in_one_directory(directory, filename):
    building_list = []

    print(f"json_data_add_location3/{directory}/{filename}")

    f = open(f"json_data_add_location3/{directory}/{filename}", "r", encoding="UTF8")
    json_data_list = json.load(f)
    building_type = ""

    if "다가구" in filename:
        return

    if "오피스텔" in filename:
        building_type = "OFFICETEL"
    elif "연립다세대" in filename:
        building_type = "ROWHOUSE"
    else:
        building_type = "UNKNOWN"
    
    sie = "서울특별시"

    if "세종특별자치시" in filename: 
        sie = "세종특별자치시"

    split_filename = filename[:-5].split("_")
    regex = "\(.*\)|\s-\s.*"

    for json_data in json_data_list:

        full_number_address = ""
        full_road_address = ""
        short_number_address = ""
        short_road_address = ""

        gue = split_filename[-1].replace(" ", "")
        dong = json_data['dong'].replace(" ", "") 
        bunji = json_data['jibun'].replace(" ", "")
        apart = json_data['apartment'].replace(" ", "")
        
        apartmentName = apart
        shortAddress = f"{sie} {gue}"

        if sie == "세종특별자치시":
            shortAddress = f"{sie}"

        area_code = int(json_data['area_code'])

        build_year = 0

        if json_data['build_year'] != '':
            build_year = int(json_data['build_year'])

        using_area = float(json_data['using_area'])

        if 'latitude' not in json_data or 'longitude' not in json_data:
            continue
        if json_data['full_address'] == "":
            continue

        latitude = float(json_data['latitude'])
        longitude = float(json_data['longitude'])
        address = json_data['full_address']

        deal_year = int(json_data['deal_year'])
        deal_month = int(json_data['deal_month'])
        deal_day = int(json_data['deal_day'])

        deal_date = int(time.mktime(datetime.strptime(f"{deal_year}-{deal_month}-{deal_day}", '%Y-%m-%d').timetuple())) * 1000
        floor = int(json_data['floor'])
        monthly_rent = int(json_data['monthly_rent'])
        deposit = int(json_data['deposit'].replace(",", ""))

        regex_address = re.sub(regex, '', address) # 정규식을 통해 괄호와 괄호안 문자열 제거
        replace_address = " ".join(regex_address.split())

        full_road_address = f"{replace_address} {apartmentName}"
        short_road_address_none_apart = replace_address.replace(shortAddress, "").strip()
        short_road_address = f"{short_road_address_none_apart} {apartmentName}"
        
        if sie != "세종특별자치시":
            full_number_address = f"{sie} {gue} {dong} {bunji} {apart}"
            short_number_address = f"{dong} {bunji} {apart}"
        else:
            full_number_address = f"{sie} {dong} {bunji} {apart}"
            short_number_address = f"{dong} {bunji} {apart}"

        full_road_address = full_road_address.replace("  ", " ")
        short_road_address = short_road_address.replace("  ", " ")
        full_number_address = full_number_address.replace("  ", " ")
        short_number_address = short_number_address.replace("  ", " ")

        full_road_address = full_road_address.replace("  ", " ")
        short_road_address = short_road_address.replace("  ", " ")
        full_number_address = full_number_address.replace("  ", " ")
        short_number_address = short_number_address.replace("  ", " ")

        full_road_address = full_road_address.replace("  ", " ")
        short_road_address = short_road_address.replace("  ", " ")
        full_number_address = full_number_address.replace("  ", " ")
        short_number_address = short_number_address.replace("  ", " ")

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

        building_list.append(building_data)

    return building_list
        

def bulk_building_in_directory_json_data():
    zeepy = ZeepyForServerHelper()
    directoies_about_molit_json = os.listdir("json_data_add_location3")
    building_list = []
    for directory in directoies_about_molit_json:
        print(directory)

        if directory == "error":
            break

        molit_jsons_name = os.listdir(f"json_data_add_location3/{directory}")

        for molit_json_name in molit_jsons_name:
            building_list += upload_json_data_in_one_directory(directory, molit_json_name)
    
    response_batch_insert_building = zeepy.batch_insert_building(building_list)
    response_batch_insert_building.close()

def main(): # 매인 함수
    bulk_building_in_directory_json_data()
    
if __name__ == "__main__":
	main()