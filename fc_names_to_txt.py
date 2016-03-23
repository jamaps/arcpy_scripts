import arcpy
from arcpy import env

env.workspace = r"PATH.sde"
FeatureList = arcpy.ListFeatureClasses()
names = []
n = 0

for fc in FeatureList:
    if "PART" in fc:
        print fc
        print fc[8:]
        n += 1
        names.append(fc[8:])
print n

text_file = open("text_file_name.txt", "w")

names.sort()

for name in names:
    text_file.write(name)
    text_file.write('\n')
text_file.close()
