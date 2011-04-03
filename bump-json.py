import json

logs = open('bump10.log')
lines = logs.readlines()
for line in lines:
    if line.split(' ')[2]=="MATCH":
        dict1 = json.loads(line[28:])
        print dict1['userid1']
        print dict1['userid2']
