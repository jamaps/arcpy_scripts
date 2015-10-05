# batch exports feature classes from a directory (including gdb's) to an output foler

import arcpy
from arcpy import env

env.workspace = r"PATH.gdb"
output_location = "C:\\Users\\.............\\Output_Folder\\"

FeatureList = arcpy.ListFeatureClasses()
n = 0
for Feature in FeatureList:
	arcpy.FeatureClassToFeatureClass_conversion(Feature, output_location, Feature)
	n = n + 1
print "Number of features exported: %i" %n
