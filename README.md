# <I>Linking fishes to multiple metrics of coral reef structural complexity using three-dimensional technology</I>

González-Rivero M <sup>1,2*</sup>, Harborne A R <sup>2,3,5</sup>, Herrera-Reveles A <sup>4</sup>, Bozec Y M <sup>5,2</sup>, Rogers A <sup>5</sup>, Friedman A <sup>6,7</sup>, Ganase A <sup>1,2,5</sup> and Hoegh-Guldberg O <sup>1,2,5</sup>1. The Global Change Institute, The University of Queensland, St Lucia. Queensland, Australia 40722. Australian Research Council Centre of Excellence for Coral Reef Studies, The University of Queensland, St Lucia, Queensland, Australia 40723. Department of Biological Sciences, Florida International University, North Miami, Florida 331814. Instituto de Zoología y Ecología Tropical, Universidad Central de Venezuela. Caracas, Distrito Capital, Venezuela 10515. School of Biological Sciences, The University of Queensland, St Lucia. Queensland, Australia 40726. Greybits Engineering, Sydney, New South Wales, Australia 20067 The Australian Centre for Field Robotics, University of Sydney, New South Wales, Australia 2006*correspondence author, e-mail: m.gonzalezrivero@uq.edu.au 
## Summary
This repository contains supplementary material to the the manuscript submitted to Nature Scientific Reports under the title: " Linking fishes to multiple metrics of structural complexity using three-dimensional technologies". This manuscript is currently under review (from 02 June 2017). 

The supplementary manterial comprise of the original data, methodological protocols and statistical models employed in this study. 

Here is an example of the 3D reconstructions of reef substrate:
<div class="sketchfab-embed-wrapper"><iframe width="640" height="480" src="https://sketchfab.com/models/7a7ece235db24be4b3766da017272d6e/embed" frameborder="0" allowvr allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" onmousewheel=""></iframe>

<p style="font-size: 13px; font-weight: normal; margin: 5px; color: #4A4A4A;">
    <a href="https://sketchfab.com/models/7a7ece235db24be4b3766da017272d6e?utm_medium=embed&utm_source=website&utm_campain=share-popup" target="_blank" style="font-weight: bold; color: #1CAAD9;">mesophotic_quadrat</a>
    by <a href="https://sketchfab.com/magr?utm_medium=embed&utm_source=website&utm_campain=share-popup" target="_blank" style="font-weight: bold; color: #1CAAD9;">Manuel Gonzalez-Rivero</a>
    on <a href="https://sketchfab.com?utm_medium=embed&utm_source=website&utm_campain=share-popup" target="_blank" style="font-weight: bold; color: #1CAAD9;">Sketchfab</a>
</p>
</div>


## Structure of the repository

###Summarised Data: 
This folder contain a .R list file with three main levels of data and derived analyses from this study. The main levels of this list file correspond to each studied species:

* <B>Spartitus</B> (<I>Stegastes partituts</I>)
* <B>Splanifrons</B> (<I>Stegastes planifrons</I>)
* <B>Ccyanea</B> (<I>Chromis cyanea</I>)

Within each species-level, data and outputs from statistical analyses is further segregated by the mothodological approaches and the data itself:

* <B>data</B>: corresponding the compiled data of fish abundance and structural complexity metrics for each grid-cell within each plot and reef site. For this data the following nomenclature applies: 
	- fov = Viewshed
	- garea = Grazing Surface Area
	- n.cr = Densinty of crevices
	- gsty = Rugosity
	- ab = fish abundance
	- size = average fish size
* Partitioned Structural Complexity (<B>sc</B>)
* Rugosity index (<B>rgsty</B>)

For each method (sc or rgsty), four main elements are provided in this file:

* <B>model.sel</B>: model selection table where each of the iterations of models with different combination of explanatory variables is listed and ranked according to AIC values. The table has been order from selected model and decresing in selection ranking. 
* <B>s.model</B>: selecte glm model for explaining the abundance of the given species.
* <B>first.models</B>: list of the first models where delta AIC is less than 2.
* <B>R2m</B>: marginal R2
* <B>R2c</B>: conditional R2
* <B>dR2m.g</B>: delta of R2m after perturbation analysis where grazing surface area was perturbed.
* <B>dR2m.f</B>: delta of R2m after perturbation analysis where viewshed was perturbed.
* <B>dR2m.c</B>: delta of R2m after perturbation analysis where density of crevices was perturbed.
* <B>vimp.g</B>: variable importance for grazing surface area.
* <B>vimp.f</B>: variable importance for viewshed.
* <B>vimp.c</B>: varibale importance for density of crevices.

###Protocols:
This section includes the scripts and protocols for calculating Viewshed and the Rugosity Index from the 3D data.

###Terrain Data:
This section include two datasets from the the photogrammetric reconstrictions of each reef plot:

* <B>Mosaic</B>: Stiched images into a ortorectified and georeferences mosaic used for determining grazing surface area and the density of crevices.
* <B>Mesh</B>: data derived from three-dimesnional reconstruction of the reef (e.g., navegation, point-cloud, mesh, images).

Samples of these reconstructions can be visualised from the following repository 3D data: https://sketchfab.com/magr/models.

Also, this section included the derived datasets:

* <B>Viewshed</B>: A compilation of the viewshed for every simulated fish in the terrain.
* <B>Benthic classification</B>: a 2D classifciation of the benthic coverage derived from the manual classifciation of the photomosaics. 
* <B>Crevices</B>: a vector for the location of each of the crevices identified from the photomosaic.
* <B>Plots</B>: vector dataset delineating each of the gridcells within the plots. 






