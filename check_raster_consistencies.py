# checking raster consistencies

# this script loops through a group of rasters in a directory
# it prints their spatial reference system and number of bands
# it then prints whether all the rasters have the same number of bands and spatial reference system

# the purpose of this script is to check these consistencies between rasters before building a mosaic dataset
# if they are not consistent, then extra steps will be necessary before creating a mosaic dataset

# script last updated by Jeff Allen on August 14, 2015


import arcpy

arcpy.env.workspace = PATH HERE
list_of_rasters = arcpy.ListDatasets()

desc = arcpy.Describe(list_of_rasters[0])
og_num_bands = desc.bandCount
og_spatial_ref = (desc.spatialReference).name

print "___"

raster_count = 0

for raster in list_of_rasters:
	file_path = arcpy.env.workspace + "\\" + raster
	desc = arcpy.Describe(file_path)
	spatial_ref = desc.spatialReference
	print raster
	print "Spatial Reference: %s" %spatial_ref.name
	print "Number of bands: %d" %desc.bandCount
	print "___"
	raster_count = raster_count + 1
	if desc.bandCount == og_num_bands:
		bands_answer = "yes, %d" %og_num_bands
	else:
		bands_answer = "no"
	if spatial_ref.name == og_spatial_ref:
		ref_answer = "yes, %s" %spatial_ref.name
	else:
		ref_answer = "no"
	
print "Number of rasters checked: %d" %dataset_count
print "Do all rasters have the same number of bands? %s" %bands_answer
print "Do all rasters have the same spatial reference? %s" %ref_answer


