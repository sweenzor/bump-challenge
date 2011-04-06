import pylab
import numpy
from matplotlib import mlab
from matplotlib import pyplot


file = open('part-00001.log')
lines = file.readlines()

count = []
for line in lines:
    count.append(int(line.split('\t')[1]))

x = pylab.sort(pylab.array(count))
n, bins, patches = pylab.hist(x, 200, log=True)
n, bins =  numpy.histogram(x,max(count))

fig = pyplot.figure()
ax = fig.add_subplot(111)

ax.semilogy(range(1,len(n)+1),n)
pyplot.show()



