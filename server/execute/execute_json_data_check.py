 #-*- coding: utf-8 -*- 
from datetime import datetime
import os
import json

def length_checker(directory, filename): # JSON 데이터 길이 계산 함수
    f = open(f"json_data_add_location3/{directory}/{filename}", "r", encoding="UTF8")
    json_data_list = json.load(f)
    return len(json_data_list)

def iterate_length_checker(): # 전체 JSON 데이터 길이 계산 함수
    directoies_about_molit_json = os.listdir("json_data_add_location3")
    length = 0
    for directory in directoies_about_molit_json:
        if directory == "error":
            continue
        molit_jsons_name = os.listdir(f"json_data_add_location3/{directory}")
        for molit_json_name in molit_jsons_name:
            length += length_checker(directory, molit_json_name)

    return length

def main(): # 매인 함수
    total_length = iterate_length_checker()
    print(total_length)

if __name__ == "__main__":
	main()