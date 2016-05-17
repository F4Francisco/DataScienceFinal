#FPerez

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from linear_algebra import sum_of_squares, dot
import math
import csv

N = 2
NY12_13 = (10405, 24769)
NY14_15 = (22313, 31998)
NY15 = []
NY14 = []
NY13 = []
NY12 = []

with open('NYC2012.csv', 'rb') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')

    for row in reader:
        NY12.append(row["CONTRIBUTING FACTOR VEHICLE 1"])
#        if row[0] == ["01/02/2015"]

print "2012 Crashes:",len(NY12)

with open('NYC2013.csv', 'rb') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')

    for row in reader:
        NY13.append(row["CONTRIBUTING FACTOR VEHICLE 1"])
#        if row[0] == ["01/02/2015"]

print "2013 Crashes:",len(NY13)

with open('NYC2014.csv', 'rb') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')

    for row in reader:
        NY14.append(row["CONTRIBUTING FACTOR VEHICLE 1"])
#        if row[0] == ["01/02/2015"]

print "2014 Crashes:",len(NY14)

with open('NYC2015.csv', 'rb') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')

    for row in reader:
        NY15.append(row["CONTRIBUTING FACTOR VEHICLE 1"])
#        if row[0] == ["01/02/2015"]

print "2015 Crashes:" ,len(NY15)





##################################################
NY = [10405,22314,24771,32001]
NJ = [3383,3657,3885,5234]
year = [2012,2013,2014,2015]


def variance(x):
    """assumes x has at least two elements"""
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)

def mean(x):
    return sum(x) / len(x)

def standard_deviation(x):
    return math.sqrt(variance(x))

def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)

def de_mean(x):
    """translate x by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0

def scale(stateList, plt, lab,col):
     """
     Takes a list, label, and color and creates a scatter plot
     of the percentage change with respect to the first entry
     in the list.
     """
     baseNum = stateList[0]
     scaled= [i*10/baseNum-10 for i in stateList]
     plt.scatter(year, scaled, label=lab, c = col, s=75)


scale(NY,plt,"NY", "blue")
scale(NJ,plt,"NJ", "red")

print("The Correlation between NY & NJ is:")
print correlation(NY,NJ)


plt.title("Number of Accidents in NYC & NJ 2012-2015")
plt.xlabel('Years')
plt.xlim(2012,2016)
plt.ylabel('Percent Change')
plt.xlim(2012,2016)
plt.legend()


print("The Correlation between before & after is:")
print correlation(NY12_13,NY14_15)
ind = np.arange(N)  # the x locations for the groups
width = 0.50       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, NY12_13, width, color='r', yerr=0)
rects2 = ax.bar(ind + width, NY14_15, width, color='r', yerr=0)

# add some text for labels, title and axes ticks
ax.set_ylabel('Number of Crashes')
ax.set_title('Collsions Before & After Vision Zero')
ax.set_xticks(ind + width)
ax.set_xticklabels(('12-13', '14-15'))
ax.set_xlabel('Years')



def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()