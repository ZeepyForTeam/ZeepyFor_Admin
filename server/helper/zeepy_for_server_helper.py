 #-*- coding: utf-8 -*- 
from config.settings import Settings
import requests
import json

class ZeepyForServerHelper:
    def __init__(self):
        # self.zeepy_for_server_url = "http://13.125.168.182:8080"
        self.token = ""
        self.zeepy_for_server_url = "http://localhost:8080"
        self.email = Settings.return_zeepy_admin_email()
        self.password = Settings.return_zeepy_admin_password()

    def __refresh_token(self):
        url = self.zeepy_for_server_url + "/api/auth/login"
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        data = {"email": self.email, "password": self.password}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        token_body = json.loads(response.content)
        self.token = token_body["accessToken"]

    def upload_building(self, data):
        self.__refresh_token()
        url = self.zeepy_for_server_url + "/api/buildings"
        headers = {'Content-Type': 'application/json; charset=utf-8', "X-AUTH-TOKEN": self.token}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        return response

    def batch_insert_building(self, data):
        self.__refresh_token()
        url = self.zeepy_for_server_url + "/api/buildings/batch"
        headers = {'Content-Type': 'application/json; charset=utf-8', "X-AUTH-TOKEN": self.token}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        return response

    def batch_insert_building_deal(self, data):
        self.__refresh_token()
        url = self.zeepy_for_server_url + "/api/deals/batch"
        headers = {'Content-Type': 'application/json; charset=utf-8', "X-AUTH-TOKEN": self.token}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        return response

    def upload_building_deal(self, data):
        self.__refresh_token()
        url = self.zeepy_for_server_url + "/api/deals"
        headers = {'Content-Type': 'application/json; charset=utf-8', "X-AUTH-TOKEN": self.token}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        return response
    
    def update_building_deal(self, data, _id):
        self.__refresh_token()
        url = self.zeepy_for_server_url + "/api/deals/" + str(_id)
        headers = {'Content-Type': 'application/json; charset=utf-8', "X-AUTH-TOKEN": self.token}
        response = requests.put(url, data=json.dumps(data), headers=headers)
        return response

    def get_building(self, address):
        self.__refresh_token()
        url = self.zeepy_for_server_url + "/api/buildings/address" + "?address=" + address 
        headers = {'Content-Type': 'application/json; charset=utf-8', "X-AUTH-TOKEN": self.token}
        response = requests.get(url, headers=headers)
        return response

    def get_buildings(self):
        self.__refresh_token()
        url = self.zeepy_for_server_url + "/api/buildings/all" 
        headers = {'Content-Type': 'application/json; charset=utf-8', "X-AUTH-TOKEN": self.token}
        response = requests.get(url, headers=headers)
        return response

    def get_building_deal(self, _id, floor):
        self.__refresh_token()
        url = self.zeepy_for_server_url + "/api/deals/floors" + "?floor=" + str(floor) + "&id=" + str(_id) 
        headers = {'Content-Type': 'application/json; charset=utf-8', "X-AUTH-TOKEN": self.token}
        response = requests.get(url, headers=headers)
        return response
