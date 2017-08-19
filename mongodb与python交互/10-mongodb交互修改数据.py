# -*- coding:utf8 -*-
from pymongo import MongoClient


def update():
	try:
		# 建立连接
		client = MongoClient(host="localhost", port=27017)
		# 获得数据库
		db = client.practice
		# 更新文档一条
		# db.hui.update_one({'name':'王敏慧'},{'$set':{'name':"磊"}})
		# 更新文档多条
		db.hui.update_many({'name': '王敏慧'},{'$set':{'name':"美"}})
	except Exception as e:
		print(e)
		
if __name__ == '__main__':
	update()