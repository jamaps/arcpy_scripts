# this script creates new fields and generates values based on converting numbers of other fields to strings for each shp in a folder

# it uses arcpy.da.UpdateCursor:
# http://pro.arcgis.com/en/pro-app/arcpy/data-access/updatecursor-class.htm


import arcpy


arcpy.env.workspace = r"PATH"

# function that converts numbers to 3 char strings
def fun(x):
	if (x < 10):
		return '00' + str(x)
	elif (x < 100):
		return '0' + str(x)
	else:
		return str(x)


count = 0

for s in arcpy.ListFiles('*.shp'):

	print s

	# add new fields
	arcpy.AddField_management(s, "CMA_ID", "TEXT", "", "", 3)
	arcpy.AddField_management(s, "CT_ID", "TEXT", "", "", 3)
	arcpy.AddField_management(s, "CMACTUID", "TEXT", "", "", 6)

	# create a list of fields to be edited
	fields = ["CT","CT_ID","CMA","CMA_ID","CMACTUID"]

	# update fields using the fun function
	with arcpy.da.UpdateCursor(s, fields) as cursor:
		for row in cursor:
			row[1] = fun(row[0])
			row[3] = fun(row[2])
			row[4] = row[3] + row[1]
			cursor.updateRow(row)

	count = count + 1


print "------------------------------"
print "number of shps updated:"
print count
