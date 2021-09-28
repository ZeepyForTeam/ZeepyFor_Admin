 #-*- coding: utf-8 -*- 

from helper.molit_api import MolitApi # MOLIT API 클래스
from helper.xml_parse_helper import XmlParseHelper # XML 파싱 클래스
from helper.area_code_helper import AreaCodeHelper # 지역코드 제작 클래스
from repository.buidling_db_handler import BuildingDBHandler
from datetime import datetime
import os
import json

class MolitExecuter:
    def __init__(self):
        # API 호출 종류
        self.apartment = False
        self.officetels = True
        self.family = False
        self.alliance = True
        self.building_repository = BuildingDBHandler()
        # JSON 저장 디렉토리 설정
        self.directory = "json_data_2021_05"

    def is_pass_my_date_to_current_date(self, my_date_year, my_date_month, current_date_year, current_date_month): # 현재 날짜 비교 함수
        if current_date_year > my_date_year:
            return True
        elif current_date_month > my_date_month:
            return True
        else:
            return False

    def make_my_date_string(self, my_date_year, my_date_month): # 날짜 스트링 변환 함수
        my_date_string = str(my_date_year)
        if my_date_month < 10:
            my_date_string += "0" + str(my_date_month)
        else:
            my_date_string += str(my_date_month)
        return my_date_string

    def make_file(self, json_data, area_code_json, my_date_string, tag): # 파일 작성 함수
        # 파일 작성
        f = open(f"{self.directory}/{my_date_string}/{tag}_{area_code_json['SIDO_CODE']}_{area_code_json['SIGUNGU_CODE']}_{area_code_json['ADDRESS_NAME']}.json", "w", encoding="UTF8")
        f.write(json.dumps(json_data, indent=2, ensure_ascii=False))
        f.close()

    def molit_api_cron_job(self): # 부동산 API 사용 함수
        apartment = self.apartment
        officetels = self.officetels
        family = self.family
        alliance = self.alliance

        molit = MolitApi() # API HELPER
        xml_parser = XmlParseHelper() # XML PARSER HELPER
        area_code = AreaCodeHelper() # AREA CODE HELPER

        area_code_json = area_code.get_setting_area_code_from_json()

        my_date_year = datetime.today().year ## 비교 요청 첫번째 년도
        my_date_month = datetime.today().month ## 비교 요청 첫번째 달수

        my_date_string = self.make_my_date_string(my_date_year, my_date_month)
        
        building_upload_list = []
        for area_code in area_code_json:
            print(area_code)
            if apartment is not None and apartment is True:
                # 아파트 API CALL
                apartment_data = molit.get_molit_api_apartment_data(area_code, my_date_string)
                apartment_json = xml_parser.parse_molit_api_officetels_xml(apartment_data)
                filename = f"{xml_parser.type[0]}_{area_code['SIDO_CODE']}_{area_code['SIGUNGU_CODE']}_{area_code['ADDRESS_NAME']}"
                filtered_apartment_json = self.filtering_json_data(filename, apartment_json)
                building_upload_list += filtered_apartment_json

            if officetels is not None and officetels is True:
                # 오피스텔 API CALL
                officetels_data = molit.get_molit_api_officetels_data(area_code, my_date_string)
                officetels_json = xml_parser.parse_molit_api_officetels_xml(officetels_data)
                filename = f"{xml_parser.type[1]}_{area_code['SIDO_CODE']}_{area_code['SIGUNGU_CODE']}_{area_code['ADDRESS_NAME']}"
                filtered_officetels_json = self.filtering_json_data(filename, apartment_json)
                building_upload_list += filtered_officetels_json

            if family is not None and family is True:
                # 단독/다가구 API CALL
                family_data = molit.get_molit_api_family_data(area_code, my_date_string)
                family_json = xml_parser.parse_molit_api_family_xml(family_data)
                filename = f"{xml_parser.type[2]}_{area_code['SIDO_CODE']}_{area_code['SIGUNGU_CODE']}_{area_code['ADDRESS_NAME']}"
                filtered_family_json = self.filtering_json_data(filename, apartment_json)
                building_upload_list += filtered_family_json

            if alliance is not None and alliance is True:
                # 연립다세대 전월세 API CALL
                alliance_data = molit.get_molit_api_alliance_data(area_code, my_date_string)
                alliance_json = xml_parser.parse_molit_api_alliance_xml(alliance_data)
                filename = f"{xml_parser.type[3]}_{area_code['SIDO_CODE']}_{area_code['SIGUNGU_CODE']}_{area_code['ADDRESS_NAME']}"
                filtered_alliance_json = self.filtering_json_data(filename, apartment_json)
                building_upload_list += filtered_alliance_json

        self.building_repository.insert_item_many(building_upload_list)

    def molit_api_compare_date_job(self, start_year, start_month, end_year, end_month): # 부동산 API 사용 함수
        apartment = self.apartment
        officetels = self.officetels
        family = self.family
        alliance = self.alliance

        molit = MolitApi() # API HELPER
        xml_parser = XmlParseHelper() # XML PARSER HELPER
        area_code = AreaCodeHelper() # AREA CODE HELPER

        area_code_json = area_code.get_setting_area_code_from_json()

        ## 아규먼트 필터링 ######################
        if start_year > datetime.today().year:
            return False

        if end_year > datetime.today().year:
            return False

        if start_year > end_year:
            return False
        
        if start_year == end_year and start_month > end_month:
            return False

        if start_month > 12 or start_month < 1:
            return False

        if end_month > 12 or end_month < 1:
            return False
        ####################################

        my_date_year = start_year ## 비교 요청 첫번째 년도
        my_date_month = start_month ## 비교 요청 첫번째 달수
        current_date_year = end_year ## 비교 마지막 요청 년도
        current_date_month = end_month ## 비교 마지막 요청 달수
        
        while self.is_pass_my_date_to_current_date(my_date_year, my_date_month, current_date_year, current_date_month):
            my_date_string = self.make_my_date_string(my_date_year, my_date_month)
            
            for area_code in area_code_json:
                if apartment is not None and apartment is True:
                    # 아파트 API CALL
                    apartment_data = molit.get_molit_api_apartment_data(area_code, my_date_string)
                    apartment_json = xml_parser.parse_molit_api_officetels_xml(apartment_data)
                    self.make_file(apartment_json, area_code, my_date_string, xml_parser.type[0])

                if officetels is not None and officetels is True:
                    # 오피스텔 API CALL
                    officetels_data = molit.get_molit_api_officetels_data(area_code, my_date_string)
                    officetels_json = xml_parser.parse_molit_api_officetels_xml(officetels_data)
                    self.make_file(officetels_json, area_code, my_date_string, xml_parser.type[1])

                if family is not None and family is True:
                    # 단독/다가구 API CALL
                    family_data = molit.get_molit_api_family_data(area_code, my_date_string)
                    family_json = xml_parser.parse_molit_api_family_xml(family_data)
                    self.make_file(family_json, area_code, my_date_string, xml_parser.type[2])

                if alliance is not None and alliance is True:
                    # 연립다세대 전월세 API CALL
                    alliance_data = molit.get_molit_api_alliance_data(area_code, my_date_string)
                    alliance_json = xml_parser.parse_molit_api_alliance_xml(alliance_data)
                    self.make_file(alliance_json, area_code, my_date_string, xml_parser.type[3])
            
            if my_date_month >= 12:
                my_date_year += 1
                my_date_month = 1
            else:
                my_date_month += 1

    def filtering_json_data(self, filename, json_data_list):
        building_list = []
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

        split_filename = filename.split("_")
        regex = "\(.*\)|\s-\s.*"

        for json_data in json_data_list:
            full_number_address = ""
            short_number_address = ""

            gue = split_filename[-1].replace(" ", "")
            dong = json_data['dong'].replace(" ", "") 
            bunji = json_data['jibun'].replace(" ", "")
            apart = json_data['apartment'].replace(" ", "")

            shortAddress = f"{sie} {gue}"

            if sie == "세종특별자치시":
                shortAddress = f"{sie}"

            if sie != "세종특별자치시":
                full_number_address = f"{sie} {gue} {dong} {bunji} {apart}"
                short_number_address = f"{dong} {bunji} {apart}"
            else:
                full_number_address = f"{sie} {dong} {bunji} {apart}"
                short_number_address = f"{dong} {bunji} {apart}"
            
            full_number_address = full_number_address.replace("  ", " ")
            short_number_address = short_number_address.replace("  ", " ")

            full_number_address = full_number_address.replace("  ", " ")
            short_number_address = short_number_address.replace("  ", " ")

            full_number_address = full_number_address.replace("  ", " ")
            short_number_address = short_number_address.replace("  ", " ")

            json_data["type"] = building_type
            if "build_year" in json_data and json_data["build_year"] != "":
                json_data["build_year"] = int(json_data["build_year"].replace(",",""))
            json_data["deal_year"] = int(json_data["deal_year"].replace(",",""))
            json_data["deposit"] = float(json_data["deposit"].replace(",",""))
            json_data["deal_month"] = int(json_data["deal_month"].replace(",",""))
            json_data["monthly_rent"] = int(json_data["monthly_rent"].replace(",",""))
            json_data["deal_day"] = int(json_data["deal_day"].replace(",",""))
            json_data["using_area"] = float(json_data["using_area"].replace(",",""))
            json_data["area_code"] = int(json_data["area_code"].replace(",",""))
            json_data["full_number_address"] = full_number_address
            json_data["short_number_address"] = short_number_address
            json_data["short_address"] = shortAddress
            json_data["floor"] = int(json_data["floor"].replace(",",""))
            
            building_list.append(json_data)

        return building_list