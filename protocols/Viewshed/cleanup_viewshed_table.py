#Author: Manuel Gonzalez-Rivero
#Date: June 2016
#Purpose: to reshape and cleaup data from viewshed analysis for the purpuse of this study

import sys, os.path
sys.path.insert(0, 'PATH_TO_ARCHGIS')
import arcpy
import os
import  arcgisscripting
from arcpy import env
arcpy.ResetEnvironments()
wks="PATH_TO WORKING_DIR"
env.workspace = wks
tableList=arcpy.ListTables()

for table in tableList:
	inTable = table
	outTable = "%s\\vwshd\\%s" % (wks, table)
	tempTableView = "%s_TableView" %(inTable)
	expression = arcpy.AddFieldDelimiters(tempTableView, "Value") + " = 0"
	# Execute CopyRows to make a new copy of the table
	arcpy.CopyRows_management(inTable, outTable)

	# Execute MakeTableView
	arcpy.MakeTableView_management(outTable, tempTableView)

	# Execute SelectLayerByAttribute to determine which rows to delete
	arcpy.SelectLayerByAttribute_management(tempTableView, "NEW_SELECTION", expression)

	# Execute GetCount and if some features have been selected, then execute
	#  DeleteRows to remove the selected rows.
	if int(arcpy.GetCount_management(tempTableView).getOutput(0)) > 0:
		arcpy.DeleteRows_management(tempTableView)
	# Create ID field
	arcpy.AddField_management(tempTableView,"ID","SHORT")
	features = arcpy.UpdateCursor(tempTableView)
	for feature in features:
		feature.ID=feature.NAME
		features.updateRow(feature)
del feature, features
	

