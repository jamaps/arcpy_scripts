# outputs feature class info to a csv tabl

import arcpy
import os
import time
import csv

begin_time = time.clock()

arcpy.env.workspace = ws = r"GDP PATH"
mrcsv = r"CSV PATH"

ls = [1,2,3]
writer = csv.writer(open(mrcsv, 'a'))
writer.writerow(["Feature","Feature_Count","Extents"])

c = 0
for fds in arcpy.ListDatasets('','feature') + ['']:
        for fc in arcpy.ListFeatureClasses('','',fds):
        	print fc
                c = arcpy.GetCount_management(fc)
                desc = arcpy.Describe(fc)
                extent = desc.extent
                ymax = extent.YMax
                ymin = extent.YMin
                xmax = extent.XMax
                xmin = extent.XMin
                row = [(fc),(c),(xmin),(xmax),(ymax),(ymin)]
                writer.writerow(row)
		c = c + 1

print "Feature Class Count:"
print c
print "--------------"

end_time = time.clock()
print "Elapsed Time:"
print (end_time - begin_time)
print "Seconds"
print "--------------"
print "Goodbye"
