---
title: chartregionevents.md
original_path: WinForms_Docs/04_Controls/Chart/chartregionevents.md
created_at: 2025-08-05
---








  









### Chart Region Events {#chart-region-events style="tab-stops: 0pt"}

[] 

ChartRegionLink event in ASP.NET

[] 

This event lets you provide custom links to different regions of a chart.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                              |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                                             |
| [protected][ [string] ChartWebControl1_ChartRegionLink([object] sender, ChartRegion region)] |
|                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                     |
|                                                                                                                                                                                                                             |
| [    //Setting link for Chart area]                                                                                                                                       |
|                                                                                                                                                                                                                             |
| [    [if](region.Description==[\"ChartArea region\"])]                                                                                      |
|                                                                                                                                                                                                                             |
| [        [return] [\"Default.aspx\"];]                                                                                                      |
|                                                                                                                                                                                                                             |
| [    //Setting link for Chart control]                                                                                                                                    |
|                                                                                                                                                                                                                             |
| [    [else] [if](region.Description==[\"ChartControl Region\"])]                                                       |
|                                                                                                                                                                                                                             |
| [        [return] [\"Default2.aspx\"];]                                                                                                     |
|                                                                                                                                                                                                                             |
| [    //Setting link for specific data points]                                                                                                                             |
|                                                                                                                                                                                                                             |
| [    [else] [if](region.PointIndex == 1 && region.SeriesIndex == 0) ]                                                                         |
|                                                                                                                                                                                                                             |
| [        [return] [\"Default3.aspx\"];]                                                                                                     |
|                                                                                                                                                                                                                             |
| [    [else]]                                                                                                                                                       |
|                                                                                                                                                                                                                             |
| [        [return] [\"http://www.syncfusion.com\"];]                                                                                         |
|                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| [Protected][ [Function] ChartWebControl1_ChartRegionLink([ByVal] sender [As] [Object], [ByVal] region [As] ChartRegion) [As] [String]] |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| [   [ \'Setting link for Chart area]]                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| [    [If] region.Description = [\"ChartArea region\"] [Then]]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| [        [Return] [\"Default.aspx\"]]                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| [   [ \'Setting link for Chart control]]                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| [    [ElseIf] region.Description = [\"ChartControl Region\"] [Then]]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| [        [Return] [\"Default2.aspx\"]]                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| [    [\'Setting link for specific data points]]                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| [    [ElseIf] region.PointIndex = 1 And region.SeriesIndex = 0 [Then ]]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| [        [Return] [\"Default3.aspx\"]]                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| [    [Else]]                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| [        [Return] [\"http://www.syncfusion.com\"]]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| [    [End] [If]]                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| [End][ [Function]]                                                                                                                                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p261} 

[]{#related-topics}

