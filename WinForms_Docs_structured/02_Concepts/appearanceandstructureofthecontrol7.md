---
title: appearanceandstructureofthecontrol7.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\appearanceandstructureofthecontrol7.md
created_at: 2025-07-03
---








  









## Appearance and Structure of the Control {#appearance-and-structure-of-the-control style="tab-stops: 0pt"}

 

Essential Map Control contains the following structures:

 

{border="0"}

Figure 9: Maps Control Structure

 

 

{border="0"}

Figure 10: Essential Maps Control's Structure

 

 

 

 

Map Control:

MapControl is the base class, which consists of several layers namely the *ShapeFileLayer* that loads the shape. It receives user inputs [and translates them into actions and commands on other layers.]

 

ShapeFileLayers:

The *ShapeFileLayer* is the most important component of MapControl. It provides a mechanism to upload the shape files, which essentially form the content of the Maps. A *shapefile* is a digital vector storage format for storing geometric location and associated attribute information. *Shapefiles* spatially describe geometries such as points, polylines[, and polygons.]

 

[]{#related-topics}

