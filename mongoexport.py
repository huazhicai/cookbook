# -*- coding:utf-8 -*-
import re
import json
from pymongo import MongoClient

URI = 'mongodb://aiit-zhyl:zhyl123456@10.8.6.106:27017'
DB = 'aiit_zhyl_cache'
COLLECTION = 'lungcancer'
LIMIT = 0
FIELDS = 'zhyl11001.zhyl11002,zhyl200001.zhyl201001.zhyl201011,zhyl200001.zhyl201001.zhyl201019,zhyl200001.zhyl201001.zhyl201020.zhyl201021,zhyl200001.zhyl201001.zhyl201020.zhyl201022'
FIELDS = re.split(r',|\.', FIELDS)
flag = 'file'
filter_field = 'zhyl201011'
inhospital_no = []


class Exporter(object):
    def __init__(self):
        client = MongoClient(URI)
        db = client[DB]
        self.collection = db[COLLECTION]

    def filter_data_by_hospital_num(self, data):
        if data['zhyl11001']['zhyl11002'] not in inhospital_no:
            return True

    def read_csv(self):
        with open('diagnoseData.json', 'r', encoding='utf-8') as f:
            for line in f:
                yield json.loads(line)

    def filter_data_by_field(self, data, field):
        """过滤不存在某个字段的doc"""
        if isinstance(data, dict):
            for key, val in data.items():
                if key == field:
                    return True
                if isinstance(val, (dict, list)):
                    ret = self.filter_data_by_field(val, field)
                    if ret: return ret
        elif isinstance(data, list):
            for item in data:
                ret = self.filter_data_by_field(item, field)
                if ret: return ret
        else:
            raise Exception(data)

    def search(self):
        for doc in self.read_csv():
            self.recursive_filter(doc)
            if self.filter_data_by_field(doc, filter_field):
                self.serialization(str(doc))

    def find(self):
        if LIMIT:
            data = self.collection.find().limit(LIMIT)
        else:
            data = self.collection.find()
        for doc in data:
            self.recursive_filter(doc)
            self.serialization(str(doc))

    def recursive_filter(self, data):
        if isinstance(data, dict):
            for key in list(data.keys()):
                if key not in FIELDS:
                    data.pop(key)
                    continue
                if isinstance(data[key], (list, dict)):
                    self.recursive_filter(data[key])
        elif isinstance(data, list):
            for item in data:
                self.recursive_filter(item)
        else:
            raise Exception(data)

    def serialization(self, text):
        with open('exportData.json', 'a', encoding='utf-8') as f:
            f.write(text + '\n')


if __name__ == '__main__':
    exporter = Exporter()
    # exporter.find()
    exporter.search()
