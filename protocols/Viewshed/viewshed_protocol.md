#TERRAIN ANALYSIS FOR FISH PLOTS 
## Pre-processing data

* data: data.xyz from the file 'total_mesh.mat' within the folder for each plot. 

> <B>NOTE</B>: X=Y AND Y=X in this dataset.

* Transform z values to depth. Multiply third column by -1. This way ARCGIS will read the terrain correctly.
* Write txt file 
* Add XY data to arcgis. Specify spatial reference following centroid meridian and Lat at origin values from raster layer (mosaic).
* Create Tin (3D analyst/ Data Management)
* Create TINraster file (3D Analysit/Conversion/TIN to Raster). Specify sampling distance: cell size

## Viewshed analysis
Viewshed calculates the area viewed by a observer given a set of parameters (e.g., altitude of observer, focal view, etc). Viewshed somehow resembles the openness of a given quadrats in the plot, and can be used to estimate how much shelter does each quadrat provides to preys from visual exposure to predators.

###Steps:

* Generate TINraster for each plot
* Generate random point locations on the raster for each quadrats (Data Management / Create Random Points)
		2a. Constrain features: quadrats (shapefile)
		2b. Number of points: 100 (number of observers per quadrat)
		3b. Minimum allowed Distance: 0.10 (10cm)
* Define observer attributes and generate table observer.txt with lat and long for each random point, as well as parameters for viewshed

 | Observer Parameter | Value | Description |
 |-----|-------|-----|
 | OFFSETA | 0.1| Altitude of the observer from the substrate |
 | OFFSETB | 0.1| Altitude of the targetfrom the substrate |
 | RADIUS1 | 0 | Minimum radius of the target |
 | RADIUS2 | 3| Maximum sight/detection distance|
 |VERT1 & VERT2| [180, -180]| Field of view of the observer| 
 |AZIMUTH1 $ AZIMUTH2| [0, 360] | Angular view in the horizontal plane| 


* Set up and run script to generate multiple raster files for the viewshed of each observer.

	 `viewshed_multipleobs.py`
	 
* Run script to compile the viewshed data in one table:

	`viewshed_compile_results.py`  

* Select attributes where value is 1 and create a new table using the following script:

	`cleanup_viewshed_table.py`
	
* Join this table (ID) to corresponding obs shapefile (FID)
* Convert count data to area and percentage area. (reference area is 29.609 m2). Summary stats are based on cell counts. Using the cell size from the tinras file, calculate the area of each cell and multiply this by each column.

> <B>NOTE</B>: CID does not equals to the quadrat ID, rather to the OBJECT ID. Need to join the data to get the QID. 

* Compile data to one summary table for analysis. This table should include Reef (A,B), plotID (1-3), QID (1-9)
	