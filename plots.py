import pylab
import numpy
from matplotlib import mlab
from matplotlib import pyplot

# Graph Histogram as line

fig = pyplot.figure()
ax = fig.add_subplot(111)

def histo(count,x_lim,data_label):

    x = pylab.sort(pylab.array(count))
    #n, bins, patches = pylab.hist(x, 200, log=True)
    n, bins =  numpy.histogram(x,max(count))

    ax.semilogy(range(1,len(n)+1),n, label=data_label)
    ax.set_xlim([0,x_lim])
    #pyplot.show()
    return n


# Process "Matches" log

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

# Process "Platform" log

file = open('mapreduced-data/platform.log')
plat = file.readlines()
file.close

platform = {}
for line in plat:
    entry = line.strip().split('\t')
    platform[int(entry[0])]=entry[1]



# Split matches by platform

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


print 'number of android bumps: ', len(count_android)
print 'number of ios bumps: ', len(count_ios)
print 'total bumps: ', len(count)
print 'bumps without platform match: ', false


#histo(count,30,'Total')
android_bins = histo(count_android,30,'Android')
ios_bins = histo(count_ios,30,'iOS')
pyplot.ylabel('User Count per Bin')
pyplot.xlabel('Number of Bumps (Bins)')
pyplot.title('Unique Bumps by Platform')
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)
#pyplot.show()




def normalize_histo(bins):
    max_bin = max(bins)
    new_bin = []
    for bin1 in bins:
        new_bin.append(float(bin1)/float(max_bin))
    return new_bin

ios_bins = normalize_histo(ios_bins)
android_bins = normalize_histo(android_bins)

fig2 = pyplot.figure()
ax2 = fig2.add_subplot(111)

ax2.semilogy(range(1,len(android_bins)+1),android_bins,label='Android')
ax2.semilogy(range(1,len(ios_bins)+1),ios_bins,label='iOS')
ax2.set_xlim([0,30])
pyplot.title('Normalized by platform population')
handles, labels = ax2.get_legend_handles_labels()
ax2.legend(handles, labels)



pyplot.show()

