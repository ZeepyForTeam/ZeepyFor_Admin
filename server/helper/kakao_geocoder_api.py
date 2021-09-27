 #-*- coding: utf-8 -*- 

import requests
from urllib import parse, request
from config.settings import Settings

class KakaoGeocoderApi:
    def __init__(self):
        self.kakao_geocoder_api_url = "https://dapi.kakao.com/v2/local/search/address.json"
        self.kakao_geocoder_api_key = Settings.return_kakao_api_key()
     
    def get_kakao_geocoder_api_address_to_location(self, address):
        # GEOCODER API 조회 함수
        headers = {'Authorization': f"KakaoAK {self.kakao_geocoder_api_key}"}
        url_params = dict()
        url_params["query"] = address

        encode_url_params = parse.urlencode(url_params, doseq=True)
        response = requests.get(url=self.kakao_geocoder_api_url + "?" + encode_url_params, headers=headers)
        result = {}
        try:
            result = response.json()
        except:
            result = {}
            
        return result