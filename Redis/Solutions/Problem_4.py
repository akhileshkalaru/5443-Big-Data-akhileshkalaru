import redis
import string
import json
import sys

r = redis.Redis(host='localhost', port=6379, db=0)
r.flushdb()
f = open('nutrition.json','r')

for line in f:
	line = json.loads(filter(lambda x: x in string.printable, line))
	for FoodItmVal in line['nutrients']:
		r.zincrby('TagVals',FoodItmVal['tagname'],1)
	r.sadd('LineVals',line['_id'])
Set5Count=r.scard('LineVals')
Food_Item = 'PROCNT'
FoodItmScr=r.zscore('TagVals',Food_Item)
print FoodItmScr
print Set5Count
print float(FoodItmScr)*100/float(Set5Count)