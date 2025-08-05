---
title: enablezoominginxandyaxis.md
original_path: WinForms_Docs/99_Uncategorized/enablezoominginxandyaxis.md
created_at: 2025-08-05
---








  









## Enable Zooming in X and Y axis? {#enable-zooming-in-x-and-y-axis style="tab-stops: 0pt"}

[] 

In order to enable the zooming factor, initially set   EnableXZooming and EnableYZooming property  to *true* and later on, set the value for the ZoomFactor property in X and Y axis.

**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                          |
|                                                                                                                                                                                              |
| [this][. olapChart1.EnableXZooming = [true];]                                      |
|                                                                                                                                                                                              |
| [this][. olapChart1.EnableXZooming = [true];]                                      |
|                                                                                                                                                                                              |
| [this][. olapChart1.PrimaryXAxis.ZoomFactor = 1.0;]                                                     |
|                                                                                                                                                                                              |
| [this][. olapChart1.PrimaryYAxis.ZoomFactor = 1.0;][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**[]                                                                                      |
|                                                                                                                                                                                          |
| [Me][.olapChart1.EnableXZooming = [True]]                                      |
|                                                                                                                                                                                          |
| [Me][.olapChart1.EnableXZooming = [True]]                                      |
|                                                                                                                                                                                          |
| [Me][.olapChart1.PrimaryXAxis.ZoomFactor = 1.0]                                                     |
|                                                                                                                                                                                          |
| [Me.][olapChart1.PrimaryYAxis.ZoomFactor = 1.0][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

{border="0"}

 

Figure 54: Zooming

 

[]{#related-topics}

