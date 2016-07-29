# generates travel times between set of points 
# for a set number of departure times 
# and outputs to a csv table

# for analyzing how travel time varies at different times of day

import arcpy
from arcpy import env
import datetime
import time
import csv

# set paths
env.workspace = r"PATH.gdb"
env.overwriteOutput = True
arcpy.CheckOutExtension("Network")
network = r"PATH.gdb\network\network_ND"
ODpair = r"PATH\OD1" #start and end point to analyze

# evaluator
eval = "TravelTime_WithTransit"

# set times to run calc (e.g. 6am to 10am at every minute)
start_time = 6 # am
time_period = 4 # hours
intervals = 1 # minutes

time_ints = []

hour = start_time
while hour < (time_period + start_time):
    minute = 0
    while minute < (60):
        hm_time = []
        hm_time.append(hour)
        hm_time.append(minute)
        minute += intervals
        time_ints.append(hm_time)
    hour += 1

print time_ints


output_array = []

# run calc
for times in time_ints:

    # empty out row list
    route_result = []

    what_time = datetime.datetime(2016,4,29,times[0]+4,times[1],0) # April 29, 2016

    print what_time

    # make route layer - makes sure impedanceAttribute is correct spelling :)
    layer = arcpy.na.MakeRouteLayer(network, "Route", eval, "", "", "", eval, "ALLOW_UTURNS", "", '#', "", "TRUE_LINES_WITH_MEASURES", what_time)

    #Add stops
    arcpy.na.AddLocations('Route', 'Stops', ODpair, 'Name OBJECTID #', '5000 Meters', '#', 'Connectors_Stops2Streets NONE;Streets_UseThisOne SHAPE;TransitLines NONE;Stops NONE;Stops_Snapped2Streets NONE;GTFS_FD_ND_Junctions NONE', 'MATCH_TO_CLOSEST', 'CLEAR', 'SNAP', '0 Meters', 'EXCLUDE', 'Connectors_Stops2Streets #;Streets_UseThisOne #;TransitLines #;Stops #;Stops_Snapped2Streets #;GTFS_FD_ND_Junctions #')

    #Solve
    arcpy.na.Solve('Route', 'SKIP', 'TERMINATE', '#')

    fc = r'Route\Routes'

    rows = arcpy.SearchCursor(fc,"","","Total_" + eval,"Total_" + eval)

    # append times to out row list
    route_result.append(times[0])
    route_result.append(times[1])

    # grab out travel time from table using SearchCursor
    for row in rows:
    	route_result.append(row.Total_TravelTime_WithTransit)

    # append out row to out table
    output_array.append(route_result)

print output_array

# write to a csv
with open('out.csv', 'wb') as f:
    writer = csv.writer(f)
    for rowr in output_array:
        writer.writerows([rowr])
