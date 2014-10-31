import redis
import string
import json
import sys

r = redis.Redis(host='localhost', port=6379, db=0)
r.flushdb()
f = open('nutrition.json','r')

for line in f:
    line = json.loads(filter(lambda x: x in string.printable, line))
    for nut in line['nutrients']:
        r.zincrby('HashTab',nut['tagname'],1)
LenZList=r.zcard('HashTab')
listVals=r.zrange('HashTab',LenZList-5,LenZList)
for test in listVals:
	print test
	print r.zscore('HashTab',test)