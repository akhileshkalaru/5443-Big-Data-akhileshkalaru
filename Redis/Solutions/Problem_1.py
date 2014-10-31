import redis
import sys
import json
import string

def is_json(myjson):
	try:
		json_object=json.loads(myjson)
	except ValueError,e:
		return False
	return True
			
FileInfo=open('nutrition.json','r')
r=redis.StrictRedis(host='localhost',port=6379,db=0)
for line in FileInfo:
	if is_json(line):
		line = json.loads(filter(lambda x: x in string.printable, line))
		r.sadd("TestList",line['_id'])
print r.scard("TestList")