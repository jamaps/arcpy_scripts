#--------------------------------------#
# batch converts e00 to shp - 
# need to run in arcmap python window
#--------------------------------------#

# ArcPy convert from e00 documentation
# https://desktop.arcgis.com/en/desktop/latest/tools/conversion-toolbox/import-from-e00.htm

import arcpy
import os

# set workspace for e00 files
arcpy.env.workspace = ws = r'D:\Census\e00_test'
os.chdir(ws)
os.getcwd()

#
# e00 to coverage...
#

# loop e00s in workspace, convert to coverage, and put into custom folders for each
for f in arcpy.ListFiles('*.E00'):
	print f
	# take just name, without the extension
	sp = f.split('.')[0]
	print sp
	# make new directory
	os.mkdir("%s\coverage_%s" %(ws,sp))
	# convert to coverage and put in new directory
	arcpy.ImportFromE00_conversion(f, ("%s\coverage_%s" %(ws,sp)), sp)
	print 'Converted %s' %f

#
# rename coverage and add to data frame
#
	
# set working data frame and current MXD
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd,"*")[0]

# loop through coverage and add to data frame
for d in arcpy.ListFiles('coverage*'):
	print "%s\%s" %(ws,d)
	arcpy.env.workspace = "%s\%s" %(ws,d)
	for dataset in arcpy.ListDatasets():
		print dataset
		print ws
		# path to polygon layer in the coverage
		c = ws + r'\%s\%s' %(d,dataset) + r'\polygon'
		print c
		# add to the data frame
		newlayer = arcpy.mapping.Layer(c)
		arcpy.mapping.AddLayer(df, newlayer,"BOTTOM")
		layers = arcpy.mapping.ListLayers(mxd)
		# change layer from polygon to actual layer name 
		for lyr in layers:
			if lyr.name == "polygon":
				lyr.name = dataset

	arcpy.env.workspace = ws

arcpy.RefreshTOC()

#
# convert to coverage to shp and put in a new directory 
#

# make new directory
os.mkdir("all_shp_outputs")
# loop through coverages in data frame and export to shp in new directory
for l in df:
    print l
	# convert to shp in new directory
    arcpy.FeatureClassToFeatureClass_conversion(l, "%s/all_shp_outputs" %ws, "%s.shp" %l)
    arcpy.mapping.RemoveLayer(df, l)

    layers = arcpy.mapping.ListLayers(mxd)

    for lyr in layers:
        if lyr.name == "polygon":
            lyr.name = dataset

arcpy.RefreshTOC()

