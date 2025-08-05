---
title: hittestradius.md
original_path: WinForms_Docs/99_Uncategorized/hittestradius.md
created_at: 2025-08-05
---






#### HitTestRadius {#hittestradius style="tab-stops: 0pt"}

**[]** 

HitTestRadius property controls the circle around this point, which will be considered within the bounds of this point for hit-testing purposes. The ChartRegion events such as ChartRegionClick, ChartRegionMouseDown, ChartRegionMouseHover, ChartRegionMouseLeave, ChartRegionMouseMove and ChartRegionMouseEnter, are being affected by this property.

[] 


+--------------------------+--------------------------------+
| Details                                                   |
+--------------------------+--------------------------------+
| Possible Values          | A double values                |
+--------------------------+--------------------------------+
| Default Value            | 7.5                            |
+--------------------------+--------------------------------+
| 2D / 3D Limitations      | None                           |
+--------------------------+--------------------------------+
| Applies to Chart Element | All series                     |
+--------------------------+--------------------------------+
| Applies to Chart Types   | Line Chart and Step Line Chart |
+--------------------------+--------------------------------+


**[]** 

Here is some sample code.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                          |
| [// Specifies the circle radius around the point for HitTest]                                                                                                                                          |
|                                                                                                                                                                                                                                                          |
| [this][.ChartWebControl1.Series\[0\].Style.HitTestRadius = 20;]                                                                                                     |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                          |
| [// ChartClick Event will be fired if clicked within the above circle]                                                                                                                                 |
|                                                                                                                                                                                                                                                          |
| [void][ ChartWebControl1_ChartRegionClick([object] sender, Syncfusion.Windows.Forms.Chart.[ChartRegionMouseEventArgs] e)] |
|                                                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                          |
| [  // Message appears when User hits the test radius region ]                                                                                                                                          |
|                                                                                                                                                                                                                                                          |
| [  [if] (e.Region.IsChartPoint)]                                                                                                                                                                |
|                                                                                                                                                                                                                                                          |
| [  {     ]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                          |
| [    MessageBox][.Show([\"Point is Hit\"]);]                                                                                                 |
|                                                                                                                                                                                                                                                          |
| [  }]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [\' Specifies the circle radius around the point for HitTest]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [Me][.ChartWebControl1.Series(0).Style.HitTestRadius = 20]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [\' ChartClick Event will be fired if clicked within the above circle]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [Private][ [Sub] ChartWebControl1_ChartRegionClick([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Windows.Forms.Chart.ChartRegionMouseEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [  \' Message appears when User hits the test radius region ]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [  [If] e.Region.IsChartPoint [Then]]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [      MessageBox.Show(\"Point is Hit\")]                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [  [End] [If]]                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                               |
| [End][ [Sub]]                                                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

**[]** 

Figure 144: Chart with HitTestRadius set to \"20\"

**[]** 

See Also

[] 

[Line Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Step Line Chart]{.UGHyperlink}[, ]{.UGHyperlink}[ChartRegionClick Events]{.UGHyperlink}[]{.UGHyperlink}

[]{#p115} 

[]{#related-topics}

