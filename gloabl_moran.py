import arcpy
arcpy.env.workspace = r"C:\Users\allenje4\Desktop\GGRC32 Lab 4 Files\GGRC32 Lab 4 Files\Local Statistics Data"
m = 
arcpy.SpatialAutocorrelation_stats("pop_sci.shp", "PDens2011","NO_REPORT", "CONTIGUITY_EDGES_CORNERS", "#",)

