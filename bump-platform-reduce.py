#!/usr/bin/python

import sys
import simplejson as json

def main(argv):
  count = {}
  line = sys.stdin.readline()
  try:
    while line:
      dict1 = json.loads(line.strip())
      #if dict1['head'] == "MATCH":
        #pass
 
      if dict1['head'] == "HELLO":
        id1 = dict1['userid']  
        if id1 in count:
          pass
          #count[id1]['platform'] = dict1['platform']
        else:
          count[id1] = dict1['platform']
 
      line = sys.stdin.readline()
  except:
    pass
  
  for uid in count:
    out = str(uid)+'\t'+count[uid]+'\n'
    sys.stdout.write(out)
    #else:
      #out = str(uid)+'\t'+str(len(count[uid]['matches']))+'\n'
      #sys.stdout.write(out)

if __name__ == "__main__":
  main(sys.argv)

