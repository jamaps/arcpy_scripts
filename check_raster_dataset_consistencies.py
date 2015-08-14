# checking raster consistencies before building mosaic datasets

import arcpy

arcpy.env.workspace = PATH HERE
list_of_rasters = arcpy.ListDatasets()

desc = arcpy.Describe(list_of_datasets[0])
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

# script updated by Jeff Allen on August 14, 2015


