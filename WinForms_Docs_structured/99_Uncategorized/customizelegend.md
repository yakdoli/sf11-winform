---
title: customizelegend.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\customizelegend.md
created_at: 2025-07-03
---








  









## Customize Legend? {#customize-legend style="tab-stops: 0pt"}

 

The customization of the legend such as placement, position, alignment and representation are done using the properties given in the following code snippets:

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                 |
|                                                                                                                                                                                                        |
| [this][.olapChart1.LegendsPlacement = ChartPlacement.Outside;]                                                    |
|                                                                                                                                                                                                        |
| [this][.olapChart1.Legend.Alignment = ChartAlignment.Center;][] |
|                                                                                                                                                                                                        |
| [this][.olapChart1.Legend.Position = ChartDock.Top;][]          |
|                                                                                                                                                                                                        |
| [this][.olapChart1.Legend.RepresentationType = ChartLegendRepresentationType.Circle;]                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**[]                                                                                                              |
|                                                                                                                                                                                                     |
| [Me][.olapChart1.LegendsPlacement = ChartPlacement.Outside]                                                    |
|                                                                                                                                                                                                     |
| [Me][.olapChart1.Legend.Alignment = ChartAlignment.Center][] |
|                                                                                                                                                                                                     |
| [Me][.olapChart1.Legend.Position = ChartDock.Top][]          |
|                                                                                                                                                                                                     |
| [Me][.olapChart1.Legend.RepresentationType = ChartLegendRepresentationType.Circle]                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

 

Figure 65: Legend Customization

[]{#related-topics}

