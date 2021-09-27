 #-*- coding: utf-8 -*-
from domain.review import Review 
from enum import Enum
import sys # System
import pandas as pd
import numpy as np
import math
import os

class Mode(Enum):
    XLSX = 1
    CSV = 2

class ExcelParseHelper:
    def __init__(self):
        self.mode = Mode.CSV
        self.file = "json_data/1차 (서대문구, 마포구)3.csv"
        self.sheet = ""
        self.review = Review()

    def __str__(self):
        return "excel_parser_helper"

    def is_nan(self, x): # NAN 값 제거
        return isinstance(x, float) and math.isnan(x)

    def read_sheet_csv(self):
        table = pd.read_csv(self.file)
        table = np.array(table)
        # print(table)
        return table

    def read_sheet_xlsx(self): # sheet 읽기
        table = pd.read_excel(self.file, sheet_name = self.sheet, header = 0)
        table = np.array(table)
        # print(table)
        return table
    
    def short_text_type(self, table): # 세로 읽기
        result= []
        for j_row in range(len(table)):
            tmp = []
            if self.is_nan(table[j_row][0]):
                break
            for i_col in range(len(table[0])):
                #   print(table[j_row][i_col])
                if self.is_nan(table[j_row][i_col]):
                    tmp.append("")
                else:
                    if type(table[j_row][i_col]) is str :
                        tmp.append(table[j_row][i_col].replace("'",""))
                    else:
                        tmp.append(table[j_row][i_col])
            result.append(tmp)
            
        return result

    def read_make_format(self):
        print("sheet: ", self.sheet)
        if self.mode == Mode.CSV:
            table = self.read_sheet_csv()
        else:
            table = self.read_sheet_xlsx()

        result = self.short_text_type(table)
        return result

    def parse_excel_review_data(self):
        # 국토교통부_아파트 전월세 자료 XML 데이터 파싱 함수
        result = self.read_make_format()
        rows = []

        for i in range(1, len(result)):
            shell = result[i]
            # print(shell)
            nickname = shell[0]
            building_name = shell[1]
            address = shell[2]
            communcationTendency = self.review.communicationTendency[shell[3]] 
            lessorGender = self.review.lessorGender[shell[4]] 
            lessorAge = self.review.lessorAge[shell[5]] 
            lessorReview = shell[6]
            roomCount = self.review.roomCount[shell[7]] 
            soundInsulation = self.review.soundInsulation[shell[8]] 
            pest = self.review.pest[shell[9]] 
            lightning = self.review.lightning[shell[10]] 
            waterPressure = self.review.waterPressure[shell[11]] 
            furnitures = shell[12]
            furnitures = furnitures.replace(" ", "")
            furnitures = furnitures.split(",")
            furnitures = self.review.return_furniture_list(furnitures)
            review = shell[13]
            totalEvaluation = self.review.totalEvaluation[shell[14]] 
            
            rows.append({
                "address":address,
                "communcationTendency":communcationTendency,
                "lessorGender":lessorGender,
                "lessorAge":lessorAge,
                "lessorReview":lessorReview,
                "roomCount":roomCount,
                "soundInsulation":soundInsulation,
                "pest":pest,
                "lightning":lightning,
                "waterPressure":waterPressure,
                "furnitures":furnitures,
                "review":review,
                "totalEvaluation":totalEvaluation
            })

        return rows


a = ExcelParseHelper()
b = a.parse_excel_review_data()
print(b)