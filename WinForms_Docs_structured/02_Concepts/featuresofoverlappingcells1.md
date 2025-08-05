---
title: featuresofoverlappingcells1.md
original_path: WinForms_Docs/02_Concepts/featuresofoverlappingcells1.md
created_at: 2025-08-05
---






##### Features of Overlapping Cells {#features-of-overlapping-cells style="tab-stops: 0pt"}

###### 4.1.2.4.1.1 Overlapping Cells {#overlapping-cells style="tab-stops: 0pt"}

To overlap the cell when it is not in edit mode and calculate according to the flooding and length of the text.

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                             |
|                                                                                                                                                                                                                              |
| [C#]                                                                                                                                                                        |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                              |
| [this][.grid.Model.Options.FloatCellMode = [GridFloatCellsMode].OnDemandCalculation;] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

###### 4.1.2.4.1.2 Flooding {#flooding style="tab-stops: 0pt"}

To prevent the overlapping of previous cells.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                     |
|                                                                                                                                                                                      |
| [C#]                                                                                                                                |
|                                                                                                                                                                                      |
| []                                                                                                                     |
|                                                                                                                                                                                      |
| [this][.grid.Model.Options.FloodCell = [false];] |
|                                                                                                                                                                                      |
|                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

###### 4.1.2.4.1.3 Floating {#floating style="tab-stops: 0pt"}

To enable floating cell behavior by calculating while editing the text.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                             |
|                                                                                                                                                                                              |
| [C#]                                                                                                                                        |
|                                                                                                                                                                                              |
| []                                                                                                                             |
|                                                                                                                                                                                              |
| [this][.grid.Model.Options.EnableFloatingCell = [true];] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[[]]{.UGHyperlink} 

 

 

[]{#related-topics}

