 #-*- coding: utf-8 -*- 

class MongoDataParser:
    def parse_many(self, datas):
        result = []
        for data in datas:
            data['_id'] = str(data['_id'])
            result.append(data)
        return result

    def parse_many_no_op_id(self, datas):
        result = []
        for data in datas:
            result.append(data)
        return result

    def parse_one(self, data):
        result = data
        data._id = str(data._id)
        return result