# script which loops through folder of shps, checks geometry, dissolves each to one feature, and merges the dissolved into one shp

# ArcPy dissolve documentation
# http://pro.arcgis.com/en/pro-app/tool-reference/data-management/dissolve.htm

# ArcPy merge documentation
# http://pro.arcgis.com/en/pro-app/tool-reference/data-management/merge.htm

import arcpy
import os

# set input shp directory and output path
arcpy.env.workspace = r"PATH"
output_location = r"PATH"

count = 0

# loop through files, dissolving each to one feature, checking the geometry in the process
for f in arcpy.ListFiles('*.shp'):
	print f
	out_file = output_location + "\dissolve_" + f
	print out_file
	arcpy.RepairGeometry_management ("%s" %f)
	arcpy.Dissolve_management(f, out_file, "", "", "MULTI_PART", "DISSOLVE_LINES")
	count = count + 1

print count

# !
# can end the script here if you just want to dissolve
# !

# change workspace to output folder
arcpy.env.workspace = output_location

count2 = 0
merge_list = []

# loop through output appending shps to merge list
for d in arcpy.ListFiles('*.shp'):
	print d
	merge_list.append(d)
	count2 = count2 + 1

# if number of dissolved shps equals the number of input shps, merge the dissolved shps into one shp
if (count2 - count) == 0:
	merge_output = r"PATH.shp"
	arcpy.Merge_management(merge_list, merge_output)

print "------------------"
