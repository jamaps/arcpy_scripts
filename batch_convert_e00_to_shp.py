import arcpy
import os

#-----------------------------------
# converts e00 to shp - run in arcmap python window
#-----------------------------------

# Workspace for interchange files
arcpy.env.workspace = ws = r'PATH'


os.chdir(ws)
os.getcwd()


# loop e00, convert to coverage, and put into custom folders
for f in arcpy.ListFiles('*.E00'):
	print f
	sp = f.split('.')[0]
	print sp
	os.mkdir("%s\coverage_%s" %(ws,sp))
	arcpy.ImportFromE00_conversion(f, ("%s\coverage_%s" %(ws,sp)), sp)
	print 'Converted %s' %f
	
# add to data frame and rename
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd,"*")[0]

for d in arcpy.ListFiles('coverage*'):
	print "%s\%s" %(ws,d)
	arcpy.env.workspace = "%s\%s" %(ws,d)
	for dataset in arcpy.ListDatasets():
		print dataset
		print ws
		c = ws + r'\%s\%s' %(d,dataset) + r'\polygon'
		print c
		newlayer = arcpy.mapping.Layer(c)
		arcpy.mapping.AddLayer(df, newlayer,"BOTTOM")

		layers = arcpy.mapping.ListLayers(mxd)

		for lyr in layers:
			if lyr.name == "polygon":
				lyr.name = dataset
	
	arcpy.env.workspace = ws

	
arcpy.RefreshTOC()


# convert to shapefiles and put in a new directory
os.mkdir("all_shp_outputs")
for l in df:
    print l
    arcpy.FeatureClassToFeatureClass_conversion(l, "%s/all_shp_outputs" %ws, "%s.shp" %l)
    arcpy.mapping.RemoveLayer(df, l)


    layers = arcpy.mapping.ListLayers(mxd)

    for lyr in layers:
        if lyr.name == "polygon":
            lyr.name = dataset

arcpy.RefreshTOC()

# convert to feature classes
for l in df:
    print l
    arcpy.FeatureClassToFeatureClass_conversion(l, ws, "zzz_%s.shp" %l)
    arcpy.mapping.RemoveLayer(df, l)
