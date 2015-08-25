# script for building a mosaic dataset and adding rasters

# still under construction
# Jeff Allen - August 25, 2015

import arcpy

arcpy.env.workspace = r"PATH_NAME"

mosaic_dataset_name = "______________"
projection = "___________.prj"
bands = "3"

#create mosaic
arcpy.CreateMosaicDataset_management("Mosaic.gdb",\
                                    mosaic_dataset_name, projection,\
                                    "3", "8_BIT_UNSIGNED")

arcpy.SetMosaicDatasetProperties_management(
    "c:/workspace/mdproperties.gdb/Mosaic Dataset Name", clip_to_footprints="CLIP"
    )

# add rasters to mosaic
# need to check parameters
arcpy.AddRastersToMosaicDataset_management(
     mdname,  rastype, inpath, updatecs, updatebnd, updateovr,
     maxlevel, maxcs, maxdim, spatialref, inputdatafilter,
     subfolder, duplicate, buildpy, calcstats,
     buildthumb, comments, forcesr)
