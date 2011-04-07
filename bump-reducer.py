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
        count[id1] = 1 
        count[id2] = 2 
        #if id1 in count:
          #try:
            #count[id1]['matches'][id2] = count.get(id1).get('matches').get(id2,0) + 1
          #except:
            #count[id1] = {'matches':{id2:1}}
      
        #if id2 in count:
          #try:
            #count[id2]['matches'][id1] = count.get(id2).get('matches').get(id1,0) + 1
          #except:
            #count[id2] = {'matches':{id1:1}}

        print count
      line = sys.stdin.readline()
  except:
    pass
if __name__ == "__main__":
  main(sys.argv)

