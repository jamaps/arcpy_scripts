#goes through a folder of shps and prints how many unique values are in a specific field if values in another field are > 0


import arcpy

arcpy.env.workspace = ws = r"PATH"

print "------------------------------"

for f in arcpy.ListFiles('*.shp'):
	print f
	rows = arcpy.SearchCursor(f,"","","CTUID; CT_NAME","CTUID")
	count = 0
	for row in rows:
		if float(row.CT_NAME) > 0:
			row_x = "0"
			count = count + 1
			print "no 0s"
		else:
			row_x = row.CTUID
			print "yes 0s"
		break
	for row in rows:
		if row_x != row.CTUID:
			count = count + 1
		row_x = row.CTUID
	print count
	print "------------------------------"
