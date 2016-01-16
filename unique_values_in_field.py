# prints the number of unique values for a specific field for each shp in a folder

# esri documentation for SearchCursor at
# http://resources.arcgis.com/en/help/main/10.1/index.html#//018v00000050000000

import arcpy

# set path to working folder
arcpy.env.workspace = r"PATH"

print "------------------------------"

total_count = 0

# loop through shapefiles in the working folder
for f in arcpy.ListFiles('*.shp'):
	
	# sort by "CT" field (check linked esri documentation if needed)
	rows = arcpy.SearchCursor(f,"","","CT","CT")
	
	row_x = 0
	count = 0
	
	# loop through rows and count unique values in "CT" field
	for row in rows:
		if row_x != row.CT:
			count = count + 1
		row_x = row.CT
	
	# print result for each shp
	print f
	print count
	
	total_count = total_count + 1

#
# all this assumes that a value of '0' is unwanted towards the final count
#

print "------------------------------"
print "number of shps checked:"
print total_count
