# -*- coding:utf8 -*-
from pymongo import MongoClient


def select():
	try:
		# 建立连接
		client = MongoClient(host='localhost', port=27017)
		# 获取数据库
		db = client.practice
		# 完成查询,获得返回值
		result = db.hui.find_one()
		print(result)
		for temp in result:
			print(temp)
	except Exception as e:
		print(e)
		
if __name__ == '__main__':
	select()