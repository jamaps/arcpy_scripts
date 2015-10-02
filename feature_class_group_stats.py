# loops through a group of feature classes and calculates basic stats about the number of features in each feature class

import arcpy
from arcpy import env

env.workspace = r"PATH"

# calculate number of features for each feature class and append to a list
FeatureList = arcpy.ListFeatureClasses()
countlist = []
n = 0
for Feature in FeatureList:
	result = arcpy.GetCount_management(Feature)
	count = int(result.getOutput(0))
	countlist.append(count)
	n = n + 1

# calculate stats
total = math.fsum(countlist)
average = total / n
sumsq = 0
for c in countlist:
	sqdif = (average - c)**2
	sumsq = sqdif + sumsq
variance = sumsq / n
standard_deviation = variance ** 0.5

# print results
print countlist
print "Number of vector layers (feature classes): %f" %n
print "Total number of features: %f" %total
print "Average number of features per feature class: %f" %average
print "Variance of features per feature class: %f" %variance
print "Standard Deviation of features per feature class: %f" %standard_deviation
