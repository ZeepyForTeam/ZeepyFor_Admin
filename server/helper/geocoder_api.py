 #-*- coding: utf-8 -*- 

import requests
from urllib import parse, request
from config.settings import Settings

class GeocoderApi:
    def __init__(self):
        self.geocoder_api_url = "http://api.vworld.kr/req/address"
        self.geocoder_api_key = Settings.return_geocoder_api_key()
     
    def get_geocoder_api_address_to_location(self, address):
        # GEOCODER API 조회 함수
        url_params = dict()
        url_params["service"] = "address"
        url_params["request"] = "getcoord"
        url_params["version"] = "2.0"
        url_params["crs"] = "epsg:4326"
        url_params["address"] = address
        url_params["refine"] = "true"
        url_params["simple"] = "false"
        url_params["format"] = "json"
        url_params["type"] = "road"
        url_params["key"] = self.geocoder_api_key

        encode_url_params = parse.urlencode(url_params, doseq=True)
        response = requests.get(url=self.geocoder_api_url + "?" + encode_url_params)
        result = {}
        try:
            result = response.json()
        except:
            result = {}
            
        return result