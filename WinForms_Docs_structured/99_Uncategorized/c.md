---
title: c.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\c.md
created_at: 2025-07-03
---








  









### [\[C#\]]

[] 

[//ChartRegionDoubleClick Event]

[this][.chartControl1.ChartRegionDoubleClick += [new] Syncfusion.Windows.Forms.Chart.ChartRegionMouseEventHandler([this].chartControl1_ChartRegionDoubleClick);]

[] 

[private][ [void] chartControl1_ChartRegionDoubleClick([object] sender, ChartRegionMouseEventArgs e)]

[{]

[    [if] ([this].chkRegionDoubleClick.Checked)]

[    {]

[        [if] (e.Region.SeriesIndex == 0)]

[        {]

[            OutputText(String.Format([\"Double Click over Series 1 Column {0} Point : {1}\"], e.Region.PointIndex,e.Point));]

[            ShowChartRegion([\"ChartSeries\"]);]

[        }]

[        [else]]

[        {]

[            OutputText(String.Format([\"Double Click over {0}\"], e.Region.Description.ToString()));]

[            ShowChartRegion(e.Region.Description.ToString());]

[        }]

[] 

[    }]

[}]

[] 

[//Usage of Button property in ChartRegionMouseDown Event]

[void][ chartControl1_ChartRegionMouseDown([object] sender, [ChartRegionMouseEventArgs] e)]

[{]

[  [if](e.Button==[MouseButtons].Right)]

[     [Console].WriteLine([\"Chart Region Mouse Down:=\"]+e.Point.ToString());]

[}]

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB][.NET][\]]**                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                   |
| [\'ChartRegionDoubleClick Event]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                   |
| [AddHandler][ [Me].chartControl1.ChartRegionDoubleClick, [AddressOf] [Me].chartControl1_ChartRegionDoubleClick]                                                                               |
|                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                   |
| [Private][ [Sub] chartControl1_ChartRegionDoubleClick([ByVal] sender [As] [Object], [ByVal] e [As] ChartRegionMouseEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                   |
| [    [If] [Me].chkRegionDoubleClick.Checked [Then]]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                   |
| [        [If] e.Region.SeriesIndex = 0 [Then]]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                   |
| [            OutputText(\[String\].Format([\"Double Click over Series 1 Column {0} Point : {1}\"], e.Region.PointIndex, e.Point))]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                   |
| [            ShowChartRegion([\"ChartSeries\"])]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                   |
| [        [Else]]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                   |
| [            OutputText(\[String\].Format([\"Double Click over {0}\"], e.Region.Description.ToString()))]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                   |
| [            ShowChartRegion(e.Region.Description.ToString())]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                   |
| [        [End] [If]]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                   |
| [    [End] [If]]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                   |
| [End][ [Sub]]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                   |
| [\'Usage of Button property in ChartRegionMouseDown Event]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                   |
| [Private Sub ][chartControl1_ChartRegionMouseDown([ByVal] sender [As] [Object], [ByVal] e [As] ChartRegionMouseEventArgs)]                          |
|                                                                                                                                                                                                                                                                                                                                                   |
| [  [    If ][e.Button = MouseButtons.Right ][Then]]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                   |
| [        ][Console][.WriteLine([\"Chart Region Mouse Down:=\"]+e.Point.ToString())]                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                   |
| [    End If]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                   |
| [End Sub]                                                                                                                                                                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p268} 

[]{#related-topics}

