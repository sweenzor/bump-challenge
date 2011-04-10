#!/usr/bin/python

import sys
import simplejson as json

def main(argv):
  count = {}
  line = sys.stdin.readline()
  try:
    while line:
      dict1 = json.loads(line.strip())
      if dict1['head'] == "MATCH":
        id1 = dict1['userid1']
        id2 = dict1['userid2']
        
        if id1 in count:
          count[id1]['matches'][id2] = count.get(id1).get('matches').get(id2,0) + 1
        else:
          count[id1] = {'matches':{id2:1}}
      
        if id2 in count:
          count[id2]['matches'][id1] = count.get(id2).get('matches').get(id1,0) + 1
        else:
          count[id2] = {'matches':{id1:1}}
      
      if dict1['head'] == "HELLO":
        id1 = dict1['userid']  
        try:
          count[id1]['platform'] = dict1['platform']
        except:
          pass       
 
      line = sys.stdin.readline()
  except:
    pass
  
  for uid in count:
    if 'platform' in count[uid]:
      out = str(uid)+'\t'+str(len(count[uid]['matches']))+'\t'+count[uid]['platform']+'\n'
      sys.stdout.write(out)
    else:
      out = str(uid)+'\t'+str(len(count[uid]['matches']))+'\n'
      sys.stdout.write(out)

if __name__ == "__main__":
  main(sys.argv)

