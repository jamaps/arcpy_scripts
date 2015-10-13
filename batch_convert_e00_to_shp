import arcpy
arcpy.env.overwriteOutput = True

#-----------------------------------
# converts e00 to shp - run in arcmap python window
#-----------------------------------

# Workspace for interchange files
arcpy.env.workspace = ws = r'PATH'

# loop e00 and convert to folders
for f in arcpy.ListFiles('*.e00'):
    print f
    print f.split('.')[0]
    arcpy.ImportFromE00_conversion(f, ws, f.split('.')[0])
    print 'Converted %s' %f

# add to data frame and rename
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd,"*")[0]
for dataset in arcpy.ListDatasets():
    print dataset
    print ws
    c = ws + r'\%s' %dataset + r'\polygon'
    print c
    newlayer = arcpy.mapping.Layer(c)
    arcpy.mapping.AddLayer(df, newlayer,"BOTTOM")

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
