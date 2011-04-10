#!/usr/bin/python

import sys
import simplejson as json

def extract(d, keys):
  return dict((k, d[k]) for k in keys if k in d)

def main(argv):

  line = sys.stdin.readline()
  try:
    while line:
    
      if line.split(' ')[2]=="MATCH":
        dict1 = json.loads(line[28:])
        dict2 = {}
        dict2.update(extract(dict1,['userid1','userid2']))
        dict2['head'] = 'MATCH'

        sys.stdout.write(json.dumps(dict2, sort_keys=True)+'\n')
        

      if line.split(' ')[2]=="HELLO":
        dict1 = json.loads(line[28:])
        dict2 = {}
        dict2.update(extract(dict1,['userid']))
        dict2.update(extract(dict1['app_version'],['platform']))
        dict2['head'] = 'HELLO'

        sys.stdout.write(json.dumps(dict2, sort_keys=True)+'\n')

      line = sys.stdin.readline()

  except:
    pass

if __name__ == "__main__":
  main(sys.argv)
