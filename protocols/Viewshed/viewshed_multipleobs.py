
# Author:  Josh Livni & Matt Stevenson
# Date: Nov. 5, 2009
# Purpose: creates separate point shapefiles from an observer shapefile, then runs Viewshed on each individual point
#############################################################

# Import the arcgisscripting module

import sys
sys.path.insert(0, 'C:\\Program Files (x86)\\ArcGIS\\Desktop10.2\\bin')
import arcgisscripting  #ADD SYS MODULE FOR ARGUMENTS

# Create the Geoprocessor object
gp = arcgisscripting.create()
gp.overwriteoutput = 1

wks = "D:\\Rugosity_plots\\Rugosity_data\\Viewshed_analysis\\viewshed_ws\\B2"
data = "D:\\Rugosity_plots\\Rugosity_data\\Viewshed_analysis\\observers\\B2Obs.shp"

# Set the workspace
gp.workspace = wks
in_raster = "D:\\Rugosity_plots\\Rugosity_data\\Viewshed_analysis\\tin_rasters\\b2tinras"

gp.CheckOutExtension("Spatial")

# Set up cursor
cur = gp.SearchCursor(data)
row = cur.Next()
while row <> None:
    i = str(row.FID)
    print "Processing site: " +i  #ADD SOME MESSAGES
    #Select_analysis <in_features> <out_feature_class> {where_clause}
    gp.Select_analysis(data, "point_"+i+".shp", "\"FID\" = "+i+"")
    
    #we now theoretically have written out a shape?
    out_raster = "%s\\output\\%s" % (wks, i)
    in_shape = '%s\\point_%s.shp' % (wks, i)
    
    print in_raster, in_shape, out_raster
    #this writes out a new raster for us
    gp.Viewshed_sa(in_raster, in_shape, out_raster)
    
    gp.MakeRasterLayer_management(out_raster, "gridlayer")
    inRows = gp.SearchCursor("gridlayer")
    inRow = inRows.Next()
        
    row = cur.Next()
del cur
print "Done!"
del gp 
gp.CheckInExtension("Spatial")
f.close()
