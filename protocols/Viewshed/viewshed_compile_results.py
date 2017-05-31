# Author: Manuel Gonzalez-Rivero
#Date: June 2016 
#Propurse: Write VATs To Table
#Description: This script will write the values and cell counts from all the VAT's in a folder to a dbf table.

# Parameter 1 = Workspace where rasters and are stored (workspace; required,input,no)
# Parameter 2 = Workspace where the output table will be stored. If left blank, outTableWS will be inRasterWS. (workspace; optional,input,no)
# Parameter 2 = dbf name (string; required,input,no)
# Adapted from Luke Pinner July 2006 http://forums.esri.com/Thread.asp?c=93&f=988&t=196596

 

# Import system modules

import sys, os.path
sys.path.insert(0, 'PATH_TO_ARCGIS_BIN')
import  arcgisscripting

# Create the Geoprocessor object

gp = arcgisscripting.create()

 
#Input workspace

inRasterWS ="PATH_TO_VIEWSHED_RASTER"
 
#Output Workspace

outTableWS = "PATH_TO_OUTPUT_FOLDER"

if outTableWS == "#":

  outTableWS = inRasterWS

#Output Table

outTable = "NAME_OF_SUMMARISED_TABLE_TO_OUTPUT"


#Output Table

outTable = gp.CreateTable(outTableWS, outTable + ".dbf") 

gp.AddField(outTable,"NAME","TEXT", "", "", "13")

gp.AddField(outTable,"VALUE","DOUBLE", "16", "0")

gp.AddField(outTable,"COUNT","DOUBLE", "16", "0")

#gp.CreateTable w/out a template FC adds a default field to dbfs - Name:Field1 Type:Integer

try: gp.deletefield (outTable, "FIELD1")

except: pass


# Set the workspace. List all of the GRIDs

gp.Workspace= inRasterWS

grids = gp.ListRasters()

# Reset the enumeration to make sure the first object is returned

grids.reset()

# Get the first feature class name

grid = grids.next()

while grid: # While the raster name is not empty

    print "Processing grid: " +grid

    try:

        vat = gp.SearchCursor(grid)

        rec = vat.Next()

        outRows = gp.InsertCursor(outTable)

        while rec:

            outRow = outRows.NewRow()

            outRow.SetValue("NAME", grid)

            outRow.SetValue("VALUE", rec.value)

            outRow.SetValue("COUNT", rec.count)

            outRows.InsertRow(outRow)

            rec = vat.Next()

    except:

        msg = "Unable to access %s.vat\nRun buildvat %s \nfrom Spatial Analyst Raster Calculator or ArcInfo GRID" % (grid,grid)

        print msg

        gp.AddMessage(msg)

    grid = grids.next()
 
