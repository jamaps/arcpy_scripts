# loops through shps, checks if shps have same number of fields and spatial refs, if so, it merges them

import arcpy

arcpy.env.workspace = ws = r'PATH'
count = 0
x = 0
z = 0 
merge_list = []
for f in arcpy.ListFiles('*.shp'):
	print f
	count = count + 1
	fields = arcpy.ListFields(f)
	lc = 0
	for field in fields:
		print field.name
		lc = lc + 1
	if lc == 8:
		print "hooray"
	else:
		print "boohoo"
		x = x + 1
	desc = arcpy.Describe(f)
	spatialRef = desc.spatialReference
	x = spatialRef.Name
	print x
	if x == "GCS_GRS_1980":
		print "hooray"
	else:
		z = z + 1
	merge_list.append(f)

if z == 0 and x == 0:	
	merge_output = r"PATH.shp"
	arcpy.Merge_management(merge_list, merge_output)
