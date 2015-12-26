# prints number of unique CTUIDs in each shp

import arcpy

arcpy.env.workspace = ws = r"PATH"

print "------------------------------"

for f in arcpy.ListFiles('*.shp'):
    	print f
    	row_x = 0
    	rows = arcpy.SearchCursor(f,"","","CTUID; CT_NAME","CTUID")
    	count = 0
	for row in rows:
		if row_x != row.CTUID:
		count = count + 1
		row_x = row.CTUID
	print count
	print "------------------------------"

print "number of shps checked:"
print total_count
