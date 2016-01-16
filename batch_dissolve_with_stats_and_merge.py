# dissolves shps based on field
# keeps stats of other fields
# then updates field names with addfield, calculatefield, and deletefield
# finally, it merges the results into one shp

import arcpy
import os
import time

begin_time = time.clock()

# set input shp directory and output path
arcpy.env.workspace = r"PATH
output_location = r"PATH"

count = 0

# list of stats to keep when dissolving
statistics_fields = [["CMA", "FIRST"], ["CT", "FIRST"],["CMA_ID",'FIRST'],["CT_ID","FIRST"]]

# loop through files, dissolving each using the stats fields
for f in arcpy.ListFiles('*.shp'):
	print f
	out_file = output_location + "\dissolve_" + f
	print out_file
	# arcpy.RepairGeometry_management ("%s" %f)
	arcpy.Dissolve_management(f, out_file, "CMACTUID", statistics_fields, "MULTI_PART", "DISSOLVE_LINES")	
	count = count + 1
	
print count


mid_time = time.clock()

print "time:"
print (mid_time - begin_time)

#-------------------------------------


arcpy.env.workspace = output_location

count2 = 0

for d in arcpy.ListFiles('*.shp'):
	
	print d
	
	arcpy.AddField_management(d, "CMA", "SHORT")
	arcpy.CalculateField_management(d, "CMA", "!FIRST_CMA!", "PYTHON_9.3", "")
	arcpy.DeleteField_management(d, "FIRST_CMA")
	
	arcpy.AddField_management(d, "CT", "SHORT")
	arcpy.CalculateField_management(d, "CT", "!FIRST_CT!", "PYTHON_9.3", "")
	arcpy.DeleteField_management(d, "FIRST_CT")
	
	arcpy.AddField_management(d, "CMA_ID", "TEXT", "", "", 3)
	arcpy.CalculateField_management(d, "CMA_ID", "!FIRST_CMA_!", "PYTHON_9.3", "")
	arcpy.DeleteField_management(d, "FIRST_CMA_")
	
	arcpy.AddField_management(d, "CT_ID", "TEXT", "", "", 3)
	arcpy.CalculateField_management(d, "CT_ID", "!FIRST_CT_I!", "PYTHON_9.3", "")
	arcpy.DeleteField_management(d, "FIRST_CT_I")
	
	arcpy.AddField_management(d, "CMA_CT_ID", "TEXT", "", "", 6)
	arcpy.CalculateField_management(d, "CMA_CT_ID", "!CMACTUID!", "PYTHON_9.3", "")
	arcpy.DeleteField_management(d, "CMACTUID")
		
	count2 = count2 + 1

print count2

if count == count2:
	print ":)"
else:
	print ":("

#-----------------------------------------------------

arcpy.env.workspace = output_location

count3 = 0
merge_list = []

# loop through output appending shps to merge list
for x in arcpy.ListFiles('*.shp'):
	print x
	merge_list.append(x)
	count3 = count3 + 1

# if number of dissolved shps equals the number of input shps, merge the dissolved shps into one shp
if (count2 - count3) == 0:
	merge_output = r"merge.shp"
	arcpy.Merge_management(merge_list, merge_output)

print "------------------"


end_time = time.clock()


print "time:"
print (end_time - begin_time)



