---
title: appearanceandstructureofthecontrol.md
original_path: WinForms_Docs/02_Concepts/appearanceandstructureofthecontrol.md
created_at: 2025-08-05
---








  









## Appearance and Structure of the Control {#appearance-and-structure-of-the-control style="tab-stops: 0pt"}

 

Essential Map Control contains the following structures:

 

{border="0"}

Figure 7: Maps Control Structure

{border="0"}

Figure 8: Essential Maps Control's Structure

 

 

Map Control:

MapControl is the base class, which consists of several layers namely the Navigation Layer that contains the Navigation control, the ShapeFileLayer that loads the shape files and the Latitude and Longitude Viewer that displays the corresponding co-ordinates. It receives user inputs [and translates them into actions and commands on other layers.]

 

ShapeFileLayers:

ShapeFileLayer is the most important component of MapControl. It provides a mechanism to upload the shape files, which essentially form the content of the Maps. A shapefile is a digital vector storage format for storing geometric location and associated attribute information. Shapefiles spatially describe geometries such as points, polylines[, and polygons.]

 

Latitude Longitude Viewer:

The Latitude/Longitude Viewer is useful to determine the latitude and the longitude coordinates of the portion of the map, which is being pointed to by the mouse. It will usually be displayed on the top left corner of the control.

 

Navigation Control:

Navigation control is used to Zoom and Pan the Map Control. With Navigation Control, the map can be navigated in all directions. With Navigation control, ZoomLevel can also be set. Navigation Control can be set to Top, Right, Bottom or Left of the MapControl

 

 

[]{#related-topics}

