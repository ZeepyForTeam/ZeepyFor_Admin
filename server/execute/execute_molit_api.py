 #-*- coding: utf-8 -*- 

from helper.molit_api import MolitApi # MOLIT API 클래스
from helper.xml_parse_helper import XmlParseHelper # XML 파싱 클래스
from helper.area_code_helper import AreaCodeHelper # 지역코드 제작 클래스
from datetime import datetime
import os
import json

class MolitExecuter:
    def __init__(self):
        self.start_year = 2021
        self.start_month = 5
        self.end_year = 2021
        self.end_month = 9
        self.apartment = False
        self.officetels = True
        self.family = False
        self.alliance = True
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

    def make_area_code_json_to_file(self): # 지역코드 json 파일 제작 함수
        molit = MolitApi() # API HELPER
        area_code_json = molit.get_area_code_to_json()

        f = open(f"area_code.json", "w", encoding="UTF8")
        f.write(json.dumps(area_code_json, indent=2, ensure_ascii=False))
        f.close()

    def save_to_file_setting_date_to_current_date_of_molit_data(self): # 부동산 API 사용 함수
        start_year = self.start_year
        start_month = self.start_month
        end_year = self.end_year
        end_month = self.end_month
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
        
        # current_date_year = datetime.today().year ## 비교 마지막 요청 년도
        # current_date_month = datetime.today().month ## 비교 마지막 요청 달수

        while self.is_pass_my_date_to_current_date(my_date_year, my_date_month, current_date_year, current_date_month):
            my_date_string = self.make_my_date_string(my_date_year, my_date_month)
            print(my_date_string)

            if os.path.isdir(f"{self.directory}/{my_date_string}") == False: # 디렉토리 체크
                os.mkdir(f"{self.directory}/{my_date_string}")
            
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

def main(): # 매인 함수
    molit_executer = MolitExecuter()
    molit_executer.save_to_file_setting_date_to_current_date_of_molit_data()
    
if __name__ == "__main__":
	main()