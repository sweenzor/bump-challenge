#!/usr/bin/python

import sys
import simplejson as json

def extract(d, keys):
  return dict((k, d[k]) for k in keys if k in d)

def main(argv):

  sys.stdout.write("HI omg")
  sys.stdout.flush()

  line = sys.stdin.readline()
  try:
    while line:

      print >> sys.stderr, "LINE: *" + line.split(' ')[2] + "*"
      if line.split(' ')[2]=="MATCH":
        print >> sys.stderr, "HELLO 1"

        dict1 = json.loads(line[28:])
        dict2 = {}
        dict2.update(extract(dict1,['userid1','userid2']))
        dict2['head'] = 'MATCH'


        #print json.dumps(dict2, sort_keys=True)
        sys.stdout.write(json.dumps(dict2, sort_keys=True))
        #sys.stdout.flush()
        
        #dict3 = {}
        #dict3['userid1'] = dict1['userid2']
        #dict3['userid2'] = dict1['userid1']
        #dict3['head'] = 'MATCH'
        #print dict3
 

      if line.split(' ')[2]=="HELLO":
        print >> sys.stderr, "HELLO 2"
        #print >> sys.stderr, " WHAT"
        dict1 = json.loads(line[28:])
        dict2 = {}
        dict2.update(extract(dict1,['userid']))
        dict2.update(extract(dict1['app_version'],['platform']))
        dict2['head'] = 'HELLO'
        
        #print "WHAT WHAT"

        #print json.dumps(dict2, sort_keys=True)
        sys.stdout.write(json.dumps(dict2, sort_keys=True))
        #sys.stdout.flush()

      line = sys.stdin.readline()

  except:
    pass

  print >> sys.stderr, "I'M DYING"

if __name__ == "__main__":
  main(sys.argv)
