# -*- coding:utf8 -*-
from pymongo import MongoClient


def delete():
	try:
		# 建立连接
		client = MongoClient(host="localhost", port=27017)
		# 获得数据库
		db = client.practice
		# 删除文档一条
		# db.hui.delete_one({'name':'美'})
		# 删除文档多条
		db.hui.delete_many({'name': '美'})
	except Exception as e:
		print(e)
		
if __name__ == '__main__':
	# update()
	delete()