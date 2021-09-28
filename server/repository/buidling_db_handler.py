 #-*- coding: utf-8 -*- 
from pymongo import MongoClient
from pymongo.cursor import CursorType

class BuildingDBHandler:
    def __init__(self):
        host = "localhost"
        port = "27017"
        self.db_name = "zeepy_db"
        self.collection_name = "building"
        self.client = MongoClient(host, int(port))[self.db_name][self.collection_name]

    def insert_item_one(self, data):
        result = self.client.insert_one(data).inserted_id
        return result

    def insert_item_many(self, datas):
        result = self.client.insert_many(datas).inserted_ids
        return result

    def save_item_one(self, data):
        self.client.save(data)

    def save_item_many(self, datas):
        for data in datas:
            self.client.save(data)

    def find_item_one(self, condition=None):
        result = self.client.find_one(condition)
        return result

    def find_item(self, condition=None):
        result = self.client.find(condition, no_cursor_timeout=True, cursor_type=CursorType.EXHAUST)
        return result
    
    def find_item_pagenate(self, page, condition=None):
        limit = 50
        offset = (page - 1) * limit
        result = self.client.find(condition, no_cursor_timeout=True, cursor_type=CursorType.NON_TAILABLE).limit(limit).skip(offset)
        return result
    
    def count_items(self, condition=None):
        result = self.client.find(condition, no_cursor_timeout=True, cursor_type=CursorType.EXHAUST)
        return result.count()

    def delete_item_one(self, condition=None):
        result = self.client.delete_one(condition)
        return result

    def delete_item_many(self, condition=None):
        result = self.client.delete_many(condition)
        return result

    def update_item_one(self, condition=None, update_value=None):
        result = self.client.update_one(filter=condition, update=update_value)
        return result

    def update_item_many(self, condition=None, update_value=None):
        result = self.client.update_many(filter=condition, update=update_value)
        return result

    def text_search(self, text=None):
        result = self.client.find({"$text": {"$search": text}})
        return result