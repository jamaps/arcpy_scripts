import arcpy
import os
import time

begin_time = time.clock()

arcpy.env.workspace = ws = r"PATH"

shp = "data_desc_points.shp"

out_folder_MC = r"PATH"
out_folder_SD = r"PATH"

fieldList = arcpy.ListFields(shp)


# output MCs and SDs

count = 0
for field in fieldList:
  if field.name == "FID"or field.name == "Shape":
    print "skip %s" %field.name
  else:
    print field.name
    out_MeanCentre_shp = out_folder_MC + "\MeanCentre_%s.shp" %field.name
    arcpy.MeanCenter_stats(shp, out_MeanCentre_shp, field.name, "#", "#")
    
    out_StandDist_shp = out_folder_SD + "\StandDist_%s.shp" %field.name
    arcpy.StandardDistance_stats(shp, out_StandDist_shp, "1_STANDARD_DEVIATION", field.name, "#")
    
    count = count + 1

print count



# code MC with years and mode

arcpy.env.workspace = out_folder_MC
  
  #adding fields
count2 = 0
for f in arcpy.ListFiles('*.shp'):
  print f
  arcpy.AddField_management(f, "MODE", "TEXT", "", "", 2)
  arcpy.AddField_management(f, "YEAR", "TEXT", "", "", 4)
  count2 = count2 + 1
print count2
  
  #adding data to fields
count3 = 0
for f in arcpy.ListFiles('*.shp'):
  if "Bike" in f:
     M = "B"
     arcpy.CalculateField_management(f, "MODE", "'" + M + "'","PYTHON_9.3")
  if "Tra" in f:
     M = "T"
     arcpy.CalculateField_management(f, "MODE", "'" + M + "'","PYTHON_9.3")
  if "Drive" in f:
     M = "D"
     arcpy.CalculateField_management(f, "MODE", "'" + M + "'","PYTHON_9.3")
  if "Walk" in f:
     M = "W"
     arcpy.CalculateField_management(f, "MODE", "'" + M + "'","PYTHON_9.3")
  if "2011" in f:
     Y = "2011"
     arcpy.CalculateField_management(f, "YEAR", "'" + Y + "'","PYTHON_9.3")
  if "2006" in f:
     Y = "2006"
     arcpy.CalculateField_management(f, "YEAR", "'" + Y + "'","PYTHON_9.3")
  if "2001" in f:
     Y = "2001"
     arcpy.CalculateField_management(f, "YEAR", "'" + Y + "'","PYTHON_9.3")
  if "96" in f:
     Y = "96"
     arcpy.CalculateField_management(f, "YEAR", "'" + Y + "'","PYTHON_9.3")
  count3 = count3 + 1
print count3

# merging MCs
count4 = 0
merge_list = []
for q in arcpy.ListFiles('*.shp'):
  print q
  merge_list.append(q)
  count4 = count4 + 1
print merge_list
merge_output = out_folder_MC + "\merged_MeanCentres.shp"
arcpy.Merge_management(merge_list, merge_output)


# add codes to SD

arcpy.env.workspace = out_folder_SD

count6 = 0
for x in arcpy.ListFiles('*.shp'):
  print x
  arcpy.AddField_management(x, "MODE", "TEXT", "", "", 2)
  arcpy.AddField_management(x, "YEAR", "TEXT", "", "", 4)
  count6 = count6 + 1
print count6

count5 = 0
for d in arcpy.ListFiles('*.shp'):
  if "Bike" in d:
     M = "B"
     arcpy.CalculateField_management(d, "MODE", "'" + M + "'","PYTHON_9.3")
  if "Tra" in d:
     M = "T"
     arcpy.CalculateField_management(d, "MODE", "'" + M + "'","PYTHON_9.3")
  if "Drive" in d:
     M = "D"
     arcpy.CalculateField_management(d, "MODE", "'" + M + "'","PYTHON_9.3")
  if "Walk" in d:
     M = "W"
     arcpy.CalculateField_management(d, "MODE", "'" + M + "'","PYTHON_9.3")
  if "2011" in d:
     Y = "2011"
     arcpy.CalculateField_management(d, "YEAR", "'" + Y + "'","PYTHON_9.3")
  if "2006" in d:
     Y = "2006"
     arcpy.CalculateField_management(d, "YEAR", "'" + Y + "'","PYTHON_9.3")
  if "2001" in d:
     Y = "2001"
     arcpy.CalculateField_management(d, "YEAR", "'" + Y + "'","PYTHON_9.3")
  if "96" in d:
     Y = "96"
     arcpy.CalculateField_management(d, "YEAR", "'" + Y + "'","PYTHON_9.3")
  count5 = count5 + 1

print count5

# merging SD
count7 = 0
merge_list = []
for z in arcpy.ListFiles('*.shp'):
  print z
  merge_list.append(z)
  count7 = count7 + 1
print merge_list
merge_output = out_folder_SD + "\merged_StandDistances.shp"
arcpy.Merge_management(merge_list, merge_output)

end_time = time.clock()
print "Elapsed Time:"
print (end_time - begin_time)
print "Seconds"
print "--------------"

print ":)"
  
