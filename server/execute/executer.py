 #-*- coding: utf-8 -*- 
import os 

class Executer:
    def __init__(self):
        self.type = ["MOLIT", "VWORLD", "KAKAO", "ZEEPY_BATCH_BUILDING", "ZEEPY_BUILDING"]

    def molit_jobs(self):
        print("molit_geocoder_jobs")

    def kakao_geocoder_jobs(self):
        print("kakao_geocoder_jobs")
    
    def vworld_geocoder_jobs(self):
        print("vworld_geocoder_jobs")
    
    def zeepy_building_insert_jobs(self):
        print("zeepy_normal_insert_jobs")
    
    def zeepy_building_batch_insert_jobs(self):
        print("zeepy_building_batch_insert_jobs")