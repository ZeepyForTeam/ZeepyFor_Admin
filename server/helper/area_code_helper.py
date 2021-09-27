 #-*- coding: utf-8 -*- 

import pandas as pd
import json

class AreaCodeHelper:
    def __init__(self):
        # 전체 지역코드 모음 CSV
        self.area_code_filename = "area_code_data/국토교통부_등록번호용 지역코드_20191231.csv"
        # 초기 지역 코드: 마포구 서대문구 강북구 성북구 동대문구 중랑구 노원구 도봉구
        self.area_init_code_json_filename = "area_code_data/area_init_code.json"

    def __str__(self):
        return "area_code_helper"

    def get_area_code_from_csv(self): # 전국 지역 코드 반환 함수(CSV)
        data = pd.read_csv(self.area_code_filename, encoding="CP949")
        code_sido = data["SIDO"].tolist()
        code_sigungu = data["SIGUNGU"].tolist()
        code_address = data["ORGN_NM"].tolist()
        code_total = []
        for i in range(len(code_sido)): 
            if code_sigungu[i] > 99:
                code_total.append([code_sido[i], code_sigungu[i], code_address[i]])
        return code_total

    def get_seoul_area_code_from_csv(self): # 서울시 지역 코드 반환 함수(CSV)
        data = pd.read_csv(self.area_code_filename, encoding="CP949")
        code_sido = data["SIDO"].tolist()
        code_sigungu = data["SIGUNGU"].tolist()
        code_address = data["ORGN_NM"].tolist()
        code_total = []
        for i in range(22): 
            if code_sigungu[i] > 99:
                code_total.append([code_sido[i], code_sigungu[i], code_address[i]])
        return code_total

    def get_setting_area_code_from_json(self): # 특정 지역 코드 반환 함수(json)
        with open(self.area_init_code_json_filename, "r", encoding="UTF8") as f:
            json_data = json.load(f)
            return json_data

    def get_area_code_to_json(self): # 지역코드 json 반환 함수
        data = pd.read_csv(self.area_code_filename, encoding="CP949")
        code_sido = data["SIDO"].tolist()
        code_sigungu = data["SIGUNGU"].tolist()
        code_address = data["ORGN_NM"].tolist()
        code_total = []

        for i in range(len(code_sido)): 
            code_total.append({
                    "SIDO_CODE" : code_sido[i], 
                    "SIGUNGU_CODE" : code_sigungu[i], 
                    "ADDRESS_NAME" : code_address[i]
                    })
        return code_total