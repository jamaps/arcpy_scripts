# script which loops through folder of shps, checks geometry, dissolves each to one feature, and merges the dissolved into one shp
# built for creating a shp of census metropolitan areas from single files of census tracts for each urban area
# can also add dissolve fields to dissolve to and dissolve stats - check arcpy documentation for this

import arcpy
import os

arcpy.env.workspace = r"PATH"
count = 0
output_location = r"PATH"

for f in arcpy.ListFiles('*.shp'):
	print f
	out_file = output_location + "\cma_" + f
	print out_file
	arcpy.RepairGeometry_management ("%s" %f)
	arcpy.Dissolve_management(f, out_file, "", "", "MULTI_PART", "DISSOLVE_LINES")
	count = count + 1

print count	

arcpy.env.workspace = output_location

count2 = 0
merge_list = []
for d in arcpy.ListFiles('*.shp'):
	print d
	merge_list.append(d)
	count2 = count2 + 1

print merge_list
print count2 - count

merge_output = r"PATH.shp"
arcpy.Merge_management(merge_list, merge_output)
