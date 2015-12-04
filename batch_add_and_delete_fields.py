# ex script for adding/deleting the same fields to multiple shps in a folder

import arcpy

arcpy.env.workspace = ws = r"PATH"

count = 0

for f in arcpy.ListFiles('*.shp'):
	print f
	
	#deleting fields
	arcpy.DeleteField_management(f, ["AREA","PERIMETER"])
	
	#adding fields
	arcpy.AddField_management(f, "CT_NAME", "TEXT", "", "", 7)
	arcpy.AddField_management(f, "CTUID", "TEXT", "", "", 11)
	
	count = count + 1

print count

# refer to arc documentation for more info
