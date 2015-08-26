import arcpy

arcpy.env.workspace = r"\\PATH.gdb"

n = "FILE_NAME"

# 3 - save as layer file
arcpy.SaveToLayerFile_management("%s" %n, "\\PATH\%s.lyr" %n, "ABSOLUTE")

# 4 - change dataframe projection to web aux

# 5 - change border size to 8.5 x 8.5

# 6 - remove frame

# 7 - change paper size to 8.5 x 8.5

# 8 - save as mxd

# 9 - export image
