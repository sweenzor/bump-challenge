import pylab
import numpy
from matplotlib import mlab

file = open('part-00000.log')
lines = file.readlines()

count = []
for line in lines:
    count.append(int(line.split('\t')[1]))

x = pylab.array(count)
n, bins, patches = pylab.hist(x, 200, log=True)
pylab.plot(n)

#pylab.plot(x,[idx for idx, value in enumerate(x)])

#poly = numpy.poly1d(numpy.polyfit([idx for idx, value in enumerate(x)],x,5))
#pylab.plot(x, poly(x), '-k', linewidth=2)



mu = pylab.mean(x)
sigma = pylab.std(x)
bincenters = 0.5*(bins[1:]+bins[:-1])
# add a 'best fit' line for the normal PDF
y = mlab.normpdf( bincenters, mu, sigma )
pylab.plot(bincenters, y, 'r--', linewidth=1)



pylab.show()



