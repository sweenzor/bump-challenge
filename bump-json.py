#!/usr/bin/python

import sys
import simplejson as json

#logs = open('bump10.log')
#lines = logs.readlines()

def main(argv):
  line = sys.stdin.readline()
  try:
    while line:
      if line.split(' ')[2]=="MATCH":
        dict1 = json.loads(line[28:])
        print "LongValueSum:" + dict1['userid1'] + "\t" + "1"
        #print "LongValueSum:" + dict1['userid2'] + "\t" + "1"
      line = sys.stdin.readline()
  except "end of file":
    return None
if __name__ == "__main__":
  main(sys.argv)
