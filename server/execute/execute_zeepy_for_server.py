 #-*- coding: utf-8 -*- 

from helper.zeepy_for_server_helper import ZeepyForServerHelper
from datetime import datetime
import os
import json
import time
from datetime import datetime

def upload_json_data_in_one_directory(directory, filename):
    zeepy = ZeepyForServerHelper()
    print(f"json_data_add_location2/{directory}/{filename}")
    f = open(f"json_data_add_location2/{directory}/{filename}", "r", encoding="UTF8")
    json_data_list = json.load(f)

    if "다가구" in filename:
        return
    
    sie = "서울특별시"

    if "세종특별자치시" in filename: 
        sie = "세종특별자치시"

    split_filename = filename[:-5].split("_")

    for json_data in json_data_list:
        location_string = ""

        

        gue = split_filename[-1].replace(" ", "")
        dong = json_data['dong'].replace(" ", "") 
        bunji = json_data['jibun'].replace(" ", "")
        apart = json_data['apartment'].replace(" ", "")
        
        apartmentName = apart
        shortAddress = f"{dong} {bunji}번지"

        area_code = int(json_data['area_code'])

        build_year = 0

        if json_data['build_year'] != '':
            build_year = int(json_data['build_year'])

        using_area = float(json_data['using_area'])

        if 'latitude' not in json_data or 'longitude' not in json_data:
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

        if sie != "세종특별자치시":
            location_string = f"{sie} {gue} {dong} {bunji} {apart}"
        else:
            location_string = f"{sie} {dong} {bunji} {apart}"

        building_data = {
            'buildYear' : build_year,
            'apartmentName' : apartmentName,
            'shortAddress' : shortAddress,
            'address' : address,
            'exclusivePrivateArea' : using_area,
            'areaCode' : area_code,
            'latitude' : latitude,
            'longitude' : longitude,
        }

        response_get_building = zeepy.get_building(location_string)

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
        

def upload_all_in_directory_json_data():
    directoies_about_molit_json = os.listdir("json_data_add_location2")
    for directory in directoies_about_molit_json:
        print(directory)
        molit_jsons_name = os.listdir(f"json_data_add_location2/{directory}")

        for molit_json_name in molit_jsons_name:
            upload_json_data_in_one_directory(directory, molit_json_name)
        time.sleep(5) # Socker Problem occured so, please use timer

def main(): # 매인 함수
    upload_all_in_directory_json_data()
    
if __name__ == "__main__":
	main()