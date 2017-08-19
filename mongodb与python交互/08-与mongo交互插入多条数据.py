# -*- coding:utf-8 -*-
from pymongo import *


def insert():
	# 获取链接对象
	client = MongoClient(host='localhost', port=27017)
	# 获取数据库
	db = client.practice
	# 获取集合对象
	db.hui.insert({'name': '王敏慧'})
	db.hui.insert_many([{'name': '郭'}, {'name': '梦'}, {'age': 18}])
	

if __name__ == "__main__":
	insert()