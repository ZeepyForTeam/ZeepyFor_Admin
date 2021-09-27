 #-*- coding: utf-8 -*- 
from helper.geocoder_api import GeocoderApi # GEOCODER API 클래스

from datetime import datetime
import os
import json

def edit_molit_json_use_geocoder_api(directory, filename):
    if "다가구" in filename:
        return

    geocoder = GeocoderApi()

    print(f"json_data/{directory}/{filename}")
    f = open(f"json_data/{directory}/{filename}", "r", encoding="UTF8")
    json_data_list = json.load(f)
    
    sie = "서울특별시"

    if "세종특별자치시" in filename: 
        sie = "세종특별자치시"

    split_filename = filename[:-5].split("_")
    before_location_string = ""
    location = {}
    full_address = ""
    for json_data in json_data_list:
        location_string = ""
        gue = split_filename[-1].replace(" ", "")
        dong = json_data['dong'].replace(" ", "")
        jibun = json_data['jibun'].replace(" ", "")
        apart = json_data['apartment'].replace(" ", "")

        if sie != "세종특별자치시":
            # if "다가구" in filename:
            #     location_string = f"{sie} {split_filename[-1]} {json_data['dong']} {json_data['jibun']}"
            location_string = f"{sie} {gue} {dong} {apart}"
        else:
            # if "다가구" in filename:
            #     location_string = f"{sie} {json_data['dong']} {json_data['jibun']}"
            location_string = f"{sie} {dong} {apart}"

        if location_string != before_location_string:
            response = geocoder.get_geocoder_api_address_to_location(location_string)
            location = False
            full_address = ""
            try :
                location = response["response"]["result"]["point"]
                full_address = response["response"]["refined"]["text"]
            except :
                print(f"error: ${location_string}")
                
            before_location_string = location_string
        
        if location == False:
            continue
        
        json_data["latitude"] = location["y"]
        json_data["longitude"] = location["x"]
        json_data["full_address"] = full_address

    f = open(f"json_data_add_location2/{directory}/{filename}", "w", encoding="UTF8")
    f.write(json.dumps(json_data_list, indent=2, ensure_ascii=False))
    f.close()

def edit_molit_json_add_location_data_used_geocoder_api_and_save_files(): # GEOCODER API 사용 함수
    directoies_about_molit_json = os.listdir("json_data")
    for directory in directoies_about_molit_json:
        print(directory)

        if os.path.isdir(f"json_data_add_location2/{directory}") == False: # 디렉토리 체크
            os.mkdir(f"json_data_add_location2/{directory}")

        molit_jsons_name = os.listdir(f"json_data/{directory}")

        for molit_json_name in molit_jsons_name:
            edit_molit_json_use_geocoder_api(directory, molit_json_name)

def main(): # 매인 함수
    edit_molit_json_add_location_data_used_geocoder_api_and_save_files()
    
if __name__ == "__main__":
	main()


'''
{
    'response': {
        'service': {'name': 'address', 'version': '2.0', 'operation': 'getcoord', 'time': '105(ms)'}, 
        'status': 'OK', 
        'input': {'type': 'road', 'address': '서울특별시 동대문구  용두동 엘림'}, 
        'refined': {
            'text': '서울특별시 동대문구 왕산로19길 57 (용두동,엘림맨션)', 
            'structure': {
                'level0': '대한민국', 
                'level1': '서울특별시', 
                'level2': '동대문구', 
                'level3': '용두동', 
                'level4L': '왕산로19길', 
                'level4LC': '', 
                'level4A': '용신동', 
                'level4AC': '1123053600', 
                'level5': '57', 
                'detail': '엘림맨션'
            }
        }, 
        'result': {
            'crs': 'EPSG:4326', 
            'point': {'x': '127.031725314', 'y': '37.580684077'}
        }
    }
}
서울특별시 동대문구  용두동 (102-190)
'''