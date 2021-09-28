 #-*- coding: utf-8 -*- 
from helper.kakao_geocoder_api import KakaoGeocoderApi # GEOCODER API 클래스
from datetime import datetime
import os
import json

class KakaoGeocoderExecuter:
    def __init__(self):
        # 캐싱 할 디렉토리
        self.cache_directory = "json_data_add_location3"
        # JSON 읽을 디렉토리
        self.read_directory = "json_data_2021_05"
        # JSON 저장할 디렉토리
        self.write_directory = "json_data_2021_05_add_location"

    def edit_molit_json_use_geocoder_api(self, directory, filename, cache_address_map, count):
        if "다가구" in filename:
            return

        geocoder = KakaoGeocoderApi()

        print(f"{self.read_directory}/{directory}/{filename}")
        f = open(f"{self.read_directory}/{directory}/{filename}", "r", encoding="UTF8")
        json_data_list = json.load(f)
        
        sie = "서울특별시"

        if "세종특별자치시" in filename: 
            sie = "세종특별자치시"

        split_filename = filename[:-5].split("_")
        before_location_string = ""
        location = {}
        full_address = ""
        for json_data in json_data_list:
            if "latitude" in json_data:
                continue

            location_string = ""
            gue = split_filename[-1].replace(" ", "")
            dong = json_data['dong'].replace(" ", "")
            jibun = json_data['jibun'].replace(" ", "")
            apart = json_data['apartment'].replace(" ", "")

            if sie != "세종특별자치시":
                # if "다가구" in filename:
                #     location_string = f"{sie} {split_filename[-1]} {json_data['dong']} {json_data['jibun']}"
                location_string = f"{sie} {gue} {dong} {jibun} {apart}"
            else:
                # if "다가구" in filename:
                #     location_string = f"{sie} {json_data['dong']} {json_data['jibun']}"
                location_string = f"{sie} {dong} {jibun} {apart}"
            
            if location_string in cache_address_map:
                # 캐시 맵에 데이터가 있는 경우
                location = cache_address_map[location_string]
                json_data["latitude"] = location["latitude"]
                json_data["longitude"] = location["longitude"]
                json_data["full_address"] = location["full_address"]
                json_data["kakao"] = False
            else:
                # 캐시 맵에 데이터가 없는 경우
                # 카카오 API 호출
                count += 1
                print(count)

                response = geocoder.get_kakao_geocoder_api_address_to_location(location_string)
                location = False

                try :
                    location = response["documents"]
                except :
                    print(f"error: ${location_string}")
                    
                before_location_string = location_string
            
                if location == False:
                    continue
                if len(location) == 0:
                    continue
                # 데이터 삽입
                if location[0]["road_address"] != None:
                    json_data["latitude"] = location[0]["y"]
                    json_data["longitude"] = location[0]["x"]
                    json_data["full_address"] = location[0]["road_address"]["address_name"]
                else:
                    json_data["latitude"] = location[0]["y"]
                    json_data["longitude"] = location[0]["x"]
                    json_data["full_address"] = ""

                json_data["kakao"] = True
                json_data["etc"] = location
                # 캐시 맵 생신
                cache_address_map[location_string] = {}
                cache_address_map[location_string]["latitude"] = json_data["latitude"]
                cache_address_map[location_string]["longitude"] = json_data["longitude"] 
                cache_address_map[location_string]["full_address"] = json_data["full_address"]

        f = open(f"{self.write_directory}/{directory}/{filename}", "w", encoding="UTF8")
        f.write(json.dumps(json_data_list, indent=2, ensure_ascii=False))
        f.close()
        return count

    def make_cache_address_map(self):
        print("#### Start Make Cache Map Address ####")
        cache_address_map = {}

        directoies_about_molit_json = os.listdir(self.cache_directory)
        for directory in directoies_about_molit_json:
            molit_jsons_name = os.listdir(f"{self.cache_directory}/{directory}")

            if directory == "error":
                break

            for molit_json_name in molit_jsons_name:
                if "다가구" in molit_json_name:
                    return

                print(f"{self.cache_directory}/{directory}/{molit_json_name}")
                f = open(f"{self.cache_directory}/{directory}/{molit_json_name}", "r", encoding="UTF8")
                json_data_list = json.load(f)
                
                sie = "서울특별시"

                if "세종특별자치시" in molit_json_name: 
                    sie = "세종특별자치시"

                split_filename = molit_json_name[:-5].split("_")

                for json_data in json_data_list:
                    if "latitude" not in json_data:
                        continue

                    location_string = ""
                    gue = split_filename[-1].replace(" ", "")
                    dong = json_data['dong'].replace(" ", "")
                    jibun = json_data['jibun'].replace(" ", "")
                    apart = json_data['apartment'].replace(" ", "")

                    if sie != "세종특별자치시":
                        location_string = f"{sie} {gue} {dong} {jibun} {apart}"
                    else:
                        location_string = f"{sie} {dong} {jibun} {apart}"

                    cache_address_map[location_string] = json_data
        print("#### End Make Cache Map Address ####")
        return cache_address_map

    def edit_molit_json_add_location_data_used_kakao_geocoder_api_and_save_files(self): # GEOCODER API 사용 함수
        count = 0
        cache_address_map = self.make_cache_address_map()
        directoies_about_molit_json = os.listdir(self.read_directory)
        for directory in directoies_about_molit_json:
            print(directory)
            if directory == "error":
                break

            if os.path.isdir(f"{self.write_directory}/{directory}") == False: # 디렉토리 체크
                os.mkdir(f"{self.write_directory}/{directory}")

            molit_jsons_name = os.listdir(f"{self.read_directory}/{directory}")

            for molit_json_name in molit_jsons_name:
                count = self.edit_molit_json_use_geocoder_api(directory, molit_json_name, cache_address_map, count)

def main(): # 매인 함수
    execute_kakao_geocoder = ExecuteKakaoGeocoder()
    execute_kakao_geocoder.edit_molit_json_add_location_data_used_kakao_geocoder_api_and_save_files()
    
if __name__ == "__main__":
	main()


'''
{
  "meta": {
    "total_count": 4,
    "pageable_count": 4,
    "is_end": true
  },
  "documents": [
    {
      "address_name": "전북 익산시 부송동 100",
      "y": "35.97664845766847",
      "x": "126.99597295767953",
      "address_type": "REGION_ADDR",
      "address": {
        "address_name": "전북 익산시 부송동 100",
        "region_1depth_name": "전북",
        "region_2depth_name": "익산시",
        "region_3depth_name": "부송동",
        "region_3depth_h_name": "삼성동",
        "h_code": "4514069000",
        "b_code": "4514013400",
        "mountain_yn": "N",
        "main_address_no": "100",
        "sub_address_no": "",
        "x": "126.99597295767953",
        "y": "35.97664845766847"
      },
      "road_address": {
        "address_name": "전북 익산시 망산길 11-17",
        "region_1depth_name": "전북",
        "region_2depth_name": "익산시",
        "region_3depth_name": "부송동",
        "road_name": "망산길",
        "underground_yn": "N",
        "main_building_no": "11",
        "sub_building_no": "17",
        "building_name": "",
        "zone_no": "54547",
        "y": "35.976749396987046",
        "x": "126.99599512792346"
      }
    },
    ...
  ]
}
'''