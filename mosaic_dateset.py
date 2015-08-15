# script for building a mosaic dataset, adding rasters, and export files

# still under construction
#   Jeff Allen - August 15, 2015

import arcpy

arcpy.env.workspace = "c:/workspace"

#create mosaic
arcpy.CreateMosaicDataset_management("c:/workspace/CreateMD.gdb",\
                                    "Mosaic Dataset Name", "Projection.prj",\
                                    "Number of bands", "8_BIT_UNSIGNED")

#build footprints to yes
how????

#add rasters to mosaic
#need to check parameters
arcpy.AddRastersToMosaicDataset_management(
     mdname,  rastype, inpath, updatecs, updatebnd, updateovr,
     maxlevel, maxcs, maxdim, spatialref, inputdatafilter,
     subfolder, duplicate, buildpy, calcstats, 
     buildthumb, comments, forcesr)
     
#save as layer files
#need to remove footprints from viewport
#check absolute or relative
arcpy.SaveToLayerFile_management("studyquadsLyr", "C:/output/studyquadsLyr.lyr", "ABSOLUTE")
