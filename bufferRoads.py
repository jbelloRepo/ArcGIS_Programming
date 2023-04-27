"""
Set interpreter to: C:\Python27\ArcGIS10.7
"""
from inspect import Attribute
from os import access
import arcpy
# Set geoprocessing environments
arcpy.env.workspace = r"PythonGP\PythonGP\Data\SanJuan.gdb"
arcpy.env.overwriteOutput = True

# Set parameter used to join the BufferDistance table to the Road feature class
# print(arcpy.Usage("JoinField_management"))
inFeatures = "Roads"
inField = "ROUTE_TYPE"
joinTable = "BufferDistance"
joinField = "ROUTE_TYPE"
 
# Join table to feature class
arcpy.JoinField_management(inFeatures, inField, joinTable, joinField)

# Set parameter for the buffer Road feature class
# print(arcpy.Usage("Buffer_analysis"))
outBuffers = "RoadBuffers"
buffField = "DISTANCE"

# Buffer the roads based on DISTANCE Attribute
arcpy.Buffer_analysis(inFeatures, outBuffers, buffField)
print("Hello, world")