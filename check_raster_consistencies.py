#################################
# checking raster consistencies #
#################################

# this script loops through a group of rasters in a directory
# it checks if any of the rasters are corrupt
# it prints their spatial reference system and number of bands
# it then prints whether all the rasters have the same number of bands and spatial reference system

# the purpose is to check these consistencies between rasters before building a mosaic dataset
# if they are not consistent, then extra steps will be necessary before creating a mosaic dataset

# last updated by Jeff Allen on September 11, 2015

import arcpy

arcpy.env.workspace = r"\\192-86\DFSRoot\Data\allenj\Desktop\test\New Folder"
list_of_rasters = arcpy.ListDatasets()

desc = arcpy.Describe(list_of_rasters[0])
og_num_bands = desc.bandCount
og_spatial_ref = (desc.spatialReference).name
bands_answer = "yes"
ref_answer = "yes"
corrupt = "no"
corrupt_rasters = []
raster_count = 0

print "___"

for raster in list_of_rasters:
	try:
		file_path = arcpy.env.workspace + "\\" + raster
		desc = arcpy.Describe(file_path)
		spatial_ref = desc.spatialReference
		print raster
		print "Spatial Reference: %s" %spatial_ref.name
		print "Number of bands: %d" %desc.bandCount
		print "___"
		if desc.bandCount == og_num_bands:
			bands = "%d" %og_num_bands 
		else:
			bands_answer = "no"
		if spatial_ref.name == og_spatial_ref:
			ref = "%s" %spatial_ref.name
		else:
			ref_answer = "no"
	except:
		print raster
		print "CORRUPT"
		corrupt = "yes"
		corrupt_rasters.append(raster)
		print "___"
	raster_count = raster_count + 1	
print "Number of rasters checked: %d" %raster_count

if corrupt == "no":
	if bands_answer == "yes":
		print "All rasters have the same number of bands, %s :)" %bands
	else:
		print "Rasters do NOT have the same number of bands :("
	if ref_answer == "yes" and spatial_ref.name == "Unknown":
		print "Spatial reference is Unknown for all rasters.  Will probably need to batch define."
	elif ref_answer == "no":
		print "Rasters do NOT have the same spatial reference :("
	else:
		print "All rasters have the same spatial reference, %s :)" %ref
else:
	if len(corrupt_rasters) > 1:
		print "There are %i corrupt rasters:" %len(corrupt_rasters)
	else:
		print "There is %i corrupt raster:" %len(corrupt_rasters)	
	for x in corrupt_rasters:
		print x
