import os
import arcpy

# takes all PAL.shp and merges into one shp
# and takes all ARC.shp and merges into another shp
# for taking converted coverges into a workable output format

in_dir = r"PATH"
s = p = 0

merge_street = r"PATH\streets.shp"
merge_blocks = r"PATH\blocks.shp"

merge_list_street = []
merge_list_blocks = []

for root, dirs, files in os.walk(in_dir):
    for file in files:
        if file.endswith("ARC.shp"):
      			fp = (os.path.join(root, file))
      			s += 1
      			merge_list_street.append(fp)

for root, dirs, files in os.walk(in_dir):
    for file in files:
        if file.endswith("PAL.shp"):
      			fp = (os.path.join(root, file))
      			p += 1
      			merge_list_blocks.append(fp)
			
arcpy.Merge_management(merge_list_street, merge_street)
arcpy.Merge_management(merge_list_blocks, merge_blocks)

print s
print p
print (":)")
