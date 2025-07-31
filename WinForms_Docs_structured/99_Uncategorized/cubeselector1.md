---
title: cubeselector1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\cubeselector1.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






    


### Cube Selector {#cube-selector style="tab-stops: 0pt"}

 

Definition

OLAP data sources contain multiple cubes and in this case, the cube selector lets you to browse all the available cubes and user can select accordingly.

{border="0"} []

Figure 12: Cube Selector

On Cube Selection Change

Once we change the cube all controls will get refreshed.

[·      ]The Cube Dimension browser will get populated with cube.

[·      ]The Axis element builder will come empty.

[·      ]The OLAP Chart and OLAP Grid will become plain without any data.

[·      ]The report list will have an empty report without any elements in it.

[]{#_Showing_CubeSelector} **[]**  

Showing CubeSelector

Users can toggle the visibility of CubeSelector using this property. This property will accept a Boolean value (true/false) and based on this value sets the visibility of CubeSelector.

**[]**  

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                |
|                                                                                                                                                             |
| []                                                                                                                      |
|                                                                                                                                                             |
| [this] [.olapClient1.ShowCubeSelector = [false];] |
|                                                                                                                                                             |
| []                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]**  

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[VB\]]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                        |
| [   ]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                        |
| [Me] [.olapClient1.] [ShowCubeSelector] [ = [False]] |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

