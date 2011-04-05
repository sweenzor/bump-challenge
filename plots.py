import pylab
import numpy
from matplotlib import mlab

file = open('part-00000.log')
lines = file.readlines()

count = []
for line in lines:
    count.append(int(line.split('\t')[1]))

x = pylab.sort(pylab.array(count))
n, bins, patches = pylab.hist(x[1:], 200, log=True)


pylab.plot(range(1,len(n)+1),n)


pylab.show()



