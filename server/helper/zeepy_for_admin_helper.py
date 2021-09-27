 #-*- coding: utf-8 -*- 

import requests
import json

class ZeepyForAdminHelper:
    def __init__(self):
        self.zeepy_for_admin_url = "http://localhost:5001"

    def upload_building(self, data):
        url = self.zeepy_for_admin_url + "/api/buildings"
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        return response

    def batch_insert_building(self, data):
        url = self.zeepy_for_admin_url + "/api/buildings/batch"
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        return response
