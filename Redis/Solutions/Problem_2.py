import redis
import sys
import json
import string


r=redis.StrictRedis(host='localhost',port=6379,db=0)
r.flushdb()
def is_json(myjson):
	try:
		json_object=json.loads(myjson)
	except ValueError,e:
		return False
	return True

FileInfo=open('nutrition.json','r')

for line in FileInfo:
	if is_json(line):
		line = json.loads(filter(lambda x: x in string.printable, line))
		nuts=line['nutrients']
		for nut in nuts:
			r.sadd("MyList",nut['_id'])
print r.scard("MyList")