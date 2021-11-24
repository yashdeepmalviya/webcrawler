# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


import pymongo
from pymongo import MongoClient


class QuotetutorialPipeline(object):


    def __init__(self):
        connection = pymongo.MongoClient(
            'localhost',
            27017
        )

    # connection = pymongo.MongoClient("mongodb+srv://admin:admin123@cluster0.w0ugn.mongodb.net/Yashdeep?retryWrites=true&w=majority")
    #        db = connection["Yashdeep"]
    #        self.collection = db["netaporter"]


        db = connection["Yashdeep"]
        self.collection = db["netaporter"]

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item

