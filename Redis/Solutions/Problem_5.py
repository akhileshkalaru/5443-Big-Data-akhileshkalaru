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
			
f=open('nutrition.json','r')
r=redis.StrictRedis(host='localhost',port=6379,db=0)
r.flushdb()
for line in f:
	if is_json(line):
		line = json.loads(filter(lambda x: x in string.printable, line))
		count=0;
		StrVal=""
		for Nutrients  in line['nutrients']:
			r.sadd("MyListID",Nutrients['_id'])
			r.hset("MyHashID",Nutrients['_id'],Nutrients)
			r.sadd("TagNameSet",Nutrients['tagname'])
			r.hset("TagNameHash",Nutrients['tagname'],Nutrients)
		print StrVal
		r.hset("MainColl",line['_id'],StrVal)
print r.scard("MyListID")
print r.hlen("MyHashID")
print r.scard("TagNameSet")
print r.hlen("TagNameHash")
print r.info()