import pylab
import numpy
from matplotlib import mlab
from matplotlib import pyplot


file = open('mapreduced-data/matches.log')
lines = file.readlines()
file.close()

count = []
for line in lines:
    count.append(int(line.split('\t')[1]))

id_with_count = []
for line in lines:
    ids = line.strip().split('\t')
    id_with_count.append([int(ids[0]), int(ids[1])])


x = pylab.sort(pylab.array(count))
#n, bins, patches = pylab.hist(x, 200, log=True)
n, bins =  numpy.histogram(x,max(count))

fig = pyplot.figure()
ax = fig.add_subplot(111)

ax.semilogy(range(1,len(n)+1),n)
ax.set_xlim([0,30])
pyplot.show()



file = open('mapreduced-data/platform.log')
plat = file.readlines()
file.close

platform = {}
for line in plat:
    entry = line.strip().split('\t')
    platform[int(entry[0])]=entry[1]


count_android = []
count_ios = []
false = 0

for entry in id_with_count:
    try:
        if platform[entry[0]] == 'iOS':
            count_ios.append(entry[1])
    except:
        false += 1

    try:
        if platform[entry[0]] == 'Android':
            count_android.append(entry[1])
    except:
        false += 1


print len(count_android)
print len(count_ios)
print len(count)
print false

