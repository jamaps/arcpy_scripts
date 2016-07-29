# generates OD matrix for travel times

# check out arcpy doc for more info


import arcpy
from arcpy import env
import time


script_start = time.time()

env.workspace = r"E:\jeff\food\transit_may.gdb"
env.overwriteOutput = True
arcpy.CheckOutExtension("Network")
network = r"E:\jeff\food\transit_may.gdb\transit_may\transit_may_ND"

origins = r"E:\jeff\RealTime\temp.gdb\Origin1"
destinations = r"E:\Jeff\tor\points_for_street_dest_1.shp"
out_folder = r"E:\Jeff\tor"
# time to run the calc at
what_time = datetime.datetime(2016,5,25,5,0,0) # May 25, 2016

#Create OD Matrix for the time that is next in the time step
arcpy.MakeODCostMatrixLayer_na(network, 'OD Cost Matrix', 'TravelTime_WithTransit', 99999, '#', '#', 'ALLOW_UTURNS', '#', 'NO_HIERARCHY', '#', 'STRAIGHT_LINES', what_time)

#Add origin points
arcpy.AddLocations_na('OD Cost Matrix', 'Origins', origins, 'Name DAuid #', '5000 Meters', '#', 'Connectors_Stops2Streets NONE;Streets_UseThisOne SHAPE;TransitLines NONE;Stops NONE;Stops_Snapped2Streets NONE;GTFS_FD_ND_Junctions NONE', 'MATCH_TO_CLOSEST', 'APPEND', 'SNAP', '0 Meters', 'EXCLUDE', 'Connectors_Stops2Streets #;Streets_UseThisOne #;TransitLines #;Stops #;Stops_Snapped2Streets #;GTFS_FD_ND_Junctions #')

#Add destination points
arcpy.AddLocations_na('OD Cost Matrix', 'Destinations', destinations, 'Name GEO_ID #', '5000 Meters', '#', 'Connectors_Stops2Streets NONE;Streets_UseThisOne SHAPE;TransitLines NONE;Stops NONE;Stops_Snapped2Streets NONE;GTFS_FD_ND_Junctions NONE', 'MATCH_TO_CLOSEST', 'APPEND', 'SNAP', '0 Meters', 'EXCLUDE', 'Connectors_Stops2Streets #;Streets_UseThisOne #;TransitLines #;Stops #;Stops_Snapped2Streets #;GTFS_FD_ND_Junctions #')

#Solve OD Matrix for the time step
arcpy.Solve_na('OD Cost Matrix', 'SKIP', 'TERMINATE', '#')

fc = r'OD Cost Matrix\Lines'

print fc

# out table location and name
arcpy.TableToTable_conversion(fc, out_folder, "rex_kip")

print('done solving')
print('+++++++++++++')
print (time.time() - script_start)
