 #-*- coding: utf-8 -*- 

import xml.etree.ElementTree as ET

class XmlParseHelper:
    def __init__(self):
        self.type = [
            "국토교통부_아파트_전월세_자료",
            "국토교통부_오피스텔_전월세_신고_조회_서비스",
            "국토교통부_단독_다가구_전월세_자료",
            "국토교통부_연립다세대_전월세_자료"
        ]

    def __str__(self):
        return "xml_parser_helper"

    def return_validate_text_of_XML(self, node, xml_tag):
        result_string = ""
        if node.find(xml_tag) is not None:
            result_string = node.find(xml_tag).text
        else:
            result_string = ""
        return result_string

    def parse_molit_api_apartment_xml(self, response):
        # 국토교통부_아파트 전월세 자료 XML 데이터 파싱 함수
        xtree = ET.fromstring(response)
        rows = []
        for node in xtree.iter("item"):
            build_year = self.return_validate_text_of_XML(node, "건축년도")
            deal_year = self.return_validate_text_of_XML(node, "년")
            dong = self.return_validate_text_of_XML(node, "법정동")
            deposit = self.return_validate_text_of_XML(node, "보증금액")
            apartment = self.return_validate_text_of_XML(node, "아파트")
            deal_month = self.return_validate_text_of_XML(node, "월")
            deal_day = self.return_validate_text_of_XML(node, "일")
            using_area = self.return_validate_text_of_XML(node, "전용면적")
            jibun = self.return_validate_text_of_XML(node, "지번")
            area_code = self.return_validate_text_of_XML(node, "지역코드")
            floor = self.return_validate_text_of_XML(node, "층")
            
            rows.append({
                "build_year":build_year,
                "deal_year":deal_year,
                "dong":dong,
                "deposit":deposit,
                "apartment":apartment,
                "deal_month":deal_month,
                "deal_day":deal_day,
                "using_area":using_area,
                "jibun":jibun,
                "area_code":area_code,
                "floor":floor
            })

        return rows

    def parse_molit_api_officetels_xml(self, response):
    # 국토교통부_오피스텔 전월세 신고 조회 자료 XML 데이터 파싱 함수
        xtree = ET.fromstring(response)
        rows = []
        for node in xtree.iter("item"):
            build_year = self.return_validate_text_of_XML(node, "건축년도")
            deal_year = self.return_validate_text_of_XML(node, "년")
            apartment = self.return_validate_text_of_XML(node, "단지")
            dong = self.return_validate_text_of_XML(node, "법정동")
            deposit = self.return_validate_text_of_XML(node, "보증금")
            sigungu = self.return_validate_text_of_XML(node, "시군구")
            deal_month = self.return_validate_text_of_XML(node, "월")
            monthly_rent = self.return_validate_text_of_XML(node, "월세")
            deal_day = self.return_validate_text_of_XML(node, "일")
            using_area = self.return_validate_text_of_XML(node, "전용면적")
            jibun = self.return_validate_text_of_XML(node, "지번")
            area_code = self.return_validate_text_of_XML(node, "지역코드")
            floor = self.return_validate_text_of_XML(node, "층")

            rows.append({
                "build_year":build_year,
                "deal_year":deal_year,
                "dong":dong,
                "deposit":deposit,
                "apartment":apartment,
                "sigungu":sigungu,
                "deal_month":deal_month,
                "monthly_rent":monthly_rent,
                "deal_day":deal_day,
                "using_area":using_area,
                "jibun":jibun,
                "area_code":area_code,
                "floor":floor
            })

        return rows

    def parse_molit_api_family_xml(self, response):
    # 국토교통부_단독/다가구 전월세 자료 XML 데이터 파싱 함수
        xtree = ET.fromstring(response)
        rows = []
        for node in xtree.iter("item"):
            build_year = self.return_validate_text_of_XML(node, "건축년도")
            using_area = self.return_validate_text_of_XML(node, "계약면적")
            deal_year = self.return_validate_text_of_XML(node, "년")
            dong = self.return_validate_text_of_XML(node, "법정동")
            deposit = self.return_validate_text_of_XML(node, "보증금액")
            deal_month = self.return_validate_text_of_XML(node, "월")
            monthly_rent = self.return_validate_text_of_XML(node, "월세금액")
            deal_day = self.return_validate_text_of_XML(node, "일")
            area_code = self.return_validate_text_of_XML(node, "지역코드")

            rows.append({
                "build_year":build_year,
                "deal_year":deal_year,
                "dong":dong,
                "deposit":deposit,
                "deal_month":deal_month,
                "monthly_rent":monthly_rent,
                "deal_day":deal_day,
                "using_area":using_area,
                "area_code":area_code
            })

        return rows

    def parse_molit_api_alliance_xml(self, response):
    # 국토교통부_연립다세대 전월세 자료 XML 데이터 파싱 함수
        # print(response)
        xtree = ET.fromstring(response)
        rows = []
        for node in xtree.iter("item"):
            build_year = self.return_validate_text_of_XML(node, "건축년도")
            deal_year = self.return_validate_text_of_XML(node, "년")
            dong = self.return_validate_text_of_XML(node, "법정동")
            deposit = self.return_validate_text_of_XML(node, "보증금액")
            apartment = self.return_validate_text_of_XML(node, "연립다세대")
            deal_month = self.return_validate_text_of_XML(node, "월")
            monthly_rent = self.return_validate_text_of_XML(node, "월세금액")
            deal_day = self.return_validate_text_of_XML(node, "일")
            using_area = self.return_validate_text_of_XML(node, "전용면적")
            jibun = self.return_validate_text_of_XML(node, "지번")
            area_code = self.return_validate_text_of_XML(node, "지역코드")
            floor = self.return_validate_text_of_XML(node, "층")

            rows.append({
                "build_year":build_year,
                "deal_year":deal_year,
                "dong":dong,
                "deposit":deposit,
                "apartment":apartment,
                "deal_month":deal_month,
                "monthly_rent":monthly_rent,
                "deal_day":deal_day,
                "using_area":using_area,
                "jibun":jibun,
                "area_code":area_code,
                "floor":floor
            })

        return rows