---
title: howtochangetheexistingvaluesofthechartpointsinchartwebcontrol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\howtochangetheexistingvaluesofthechartpointsinchartwebcontrol.md
created_at: 2025-07-03
---








  









## How to change the existing value(s) of the Chart Points in ChartWebControl? {#how-to-change-the-existing-values-of-the-chart-points-in-chartwebcontrol style="tab-stops: 0pt"}

[] 

You can access any of the points through the Series and Points collections.

 

The following code demonstrates this.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                           |
|                                                                                                                                                          |
| **[]**                                                                                                 |
|                                                                                                                                                          |
| [this][.ChartWebControl1.BeginUpdate();]                            |
|                                                                                                                                                          |
| [this][.ChartWebControl1.Series\[0\].Points\[0\].X=1;]              |
|                                                                                                                                                          |
| [this][.ChartWebControl1.Series\[0\].Points\[0\].YValues\[0\]=190;] |
|                                                                                                                                                          |
| [this][.ChartWebControl1.EndUpdate();]                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                 |
|                                                                                                                                                    |
| **[]**                                                                                           |
|                                                                                                                                                    |
| [Me][.ChartWebControl1.BeginUpdate() ]                        |
|                                                                                                                                                    |
| [Me][.ChartWebControl1.Series(0).Points(0).X = 1 ]            |
|                                                                                                                                                    |
| [Me][.ChartWebControl1.Series(0).Points(0).YValues(0) = 190 ] |
|                                                                                                                                                    |
| [Me][.ChartWebControl1.EndUpdate()]                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p279} 

[]{#related-topics}

