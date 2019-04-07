# -*- coding: utf-8 -*-
#import json

#from pyjob.items import PyjobItem


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class PyjobPipeline(object):
    def process_item(self, item, spider):
        return item

#class PyjobItemJSONEncoder(json.JSONEncoder):
#    def default(self, o):
#        if isinstance(o, PyjobItem):
#            return {
#                "title": o["title"],
#                "company": o["company"],
#                "location": o["location"]
#            }
#
#        return super(PyjobItemJSONEncoder, self).default(o)

#class PyjobPipeline(object):
#    def __init__(self):
#        self.items = []
#
#    def process_item(self, item, spider):
#        self.items.append(item)
#        return item
#
#    def close_spider(self, spider):
#        with open("pyjob_list.json", mode="w") as f:
#            json.dump(self.items, f, cls=PyjobItemJSONEncoder)
