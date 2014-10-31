import csv
import json

csvfile = open('GpsFilePoints.csv', 'r')
jsonfile = open('Output.json', 'w')

fieldnames = ("UserID","FieldID","PointID","Lat","Lng","Ele","Time","Course","Hdop","Sat","Filtered")

reader = csv.reader(csvfile, fieldnames)
out = json.dumps( [ row for row in reader ] )
jsonfile.write(out)
