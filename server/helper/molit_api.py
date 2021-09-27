 #-*- coding: utf-8 -*- 

from urllib import parse, request
from config.settings import Settings

class MolitApi:
    def __init__(self):
        # 국토교통부 API Key
        self.molit_api_key = Settings.return_molit_api_key()
        # 국토교통부_아파트 전월세 API URL
        self.molit_api_apartment_url = "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptRent" 
        # 국토교통부_오피스텔 전월세 API URL
        self.molit_api_officetels_url = "http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcOffiRent"
        # 국토교통부_단독/다가구 전월세 API URL
        self.molit_api_family_url = "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcSHRent"
        # 국토교통부_연립다세대 전월세 API URL
        self.molit_api_alliance_url = "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcRHRent"

    def __str__(self):
        return "molit_api"
    
    def get_molit_api_apartment_data(self, area_code, deal_ymd):
        # 국토교통부_아파트 전월세 API 조회 함수
        url_params = dict()
        url_params["DEAL_YMD"] = deal_ymd
        url_params["LAWD_CD"] = f"{area_code['SIDO_CODE']}{area_code['SIGUNGU_CODE']}"
        url_params["serviceKey"] = self.molit_api_key

        encode_url_params = parse.urlencode(url_params, doseq=True)
        print(encode_url_params)

        response = request.urlopen(self.molit_api_apartment_url + "?" + encode_url_params).read()
        return response

    def get_molit_api_officetels_data(self, area_code, deal_ymd):
        # 국토교통부_오피스텔 전월세 API 조회 함수
        url_params = dict()
        url_params["DEAL_YMD"] = deal_ymd
        url_params["LAWD_CD"] = f"{area_code['SIDO_CODE']}{area_code['SIGUNGU_CODE']}"
        url_params["serviceKey"] = self.molit_api_key

        encode_url_params = parse.urlencode(url_params, doseq=True)
        print(encode_url_params)

        response = request.urlopen(self.molit_api_officetels_url + "?" + encode_url_params).read()
        return response

    def get_molit_api_family_data(self, area_code, deal_ymd):
        # 국토교통부_단독/다가구 전월세 API 조회 함수
        url_params = dict()
        url_params["DEAL_YMD"] = deal_ymd
        url_params["LAWD_CD"] = f"{area_code['SIDO_CODE']}{area_code['SIGUNGU_CODE']}"
        url_params["serviceKey"] = self.molit_api_key

        encode_url_params = parse.urlencode(url_params, doseq=True)
        print(encode_url_params)

        response = request.urlopen(self.molit_api_family_url + "?" + encode_url_params).read()
        return response

    def get_molit_api_alliance_data(self, area_code, deal_ymd):
        # 국토교통부_연립다세대 전월세 API 조회 함수
        url_params = dict()
        url_params["DEAL_YMD"] = deal_ymd
        url_params["LAWD_CD"] = f"{area_code['SIDO_CODE']}{area_code['SIGUNGU_CODE']}"
        url_params["serviceKey"] = self.molit_api_key

        encode_url_params = parse.urlencode(url_params, doseq=True)
        print(encode_url_params)

        response = request.urlopen(self.molit_api_alliance_url + "?" + encode_url_params).read()
        return response