#still working

import arcpy

arcpy.env.workspace = ws = r"PATH"

shp = "pop_sci.shp"

fieldList = arcpy.ListFields(shp)

for field in fieldList:
  print field.name

m = arcpy.SpatialAutocorrelation_stats(shp, "PDens2011","NO_REPORT", "CONTIGUITY_EDGES_CORNERS", "#",)
print m[0]
print m[1]
print m[2]
