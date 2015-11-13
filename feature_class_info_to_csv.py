import arcpy
import os
import time
import csv


begin_time = time.clock()

arcpy.env.workspace = ws = r"\\192-86\DFSRoot\Data\allenj\Desktop\gdb\test.gdb"
mrcsv = r"\\192-86\DFSRoot\Data\allenj\Desktop\gdb\write.csv"


ls = [1,2,3]
writer = csv.writer(open(mrcsv, 'a'))
writer.writerow(["Feature","Feature_Count","Extents"])

c = 0
for fds in arcpy.ListDatasets('','feature') + ['']:
        for fc in arcpy.ListFeatureClasses('','',fds):
        	print fc
                x = fc
                y = arcpy.GetCount_management(fc)
                z = "meow"
                row = [(x),(y),(z)]
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
