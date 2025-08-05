---
title: chartareabounds.md
original_path: WinForms_Docs/04_Controls/Chart/chartareabounds.md
created_at: 2025-08-05
---








  









### Chart Area Bounds {#chart-area-bounds style="tab-stops: 0pt"}

**[]** 

Full Chart Area Bounds

**[]** 

Use the **Bounds** property to get the rectangular area comprising the chart area that includes the axis, axis titles and other sections.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                             |
| [this][.ChartWebControl1.ChartAreaPaint += [new] System.Windows.Forms.[PaintEventHandler](ChartWebControl1_ChartAreaPaint);] |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                             |
| [void][ ChartWebControl1_ChartAreaPaint([object] sender, System.Windows.Forms.[PaintEventArgs] e)]                           |
|                                                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                             |
| [    [Rectangle] axisBounds = [this].ChartWebControl1.ChartWebArea.Bounds;]                                                                                                   |
|                                                                                                                                                                                                                                                             |
| [   // Render a rectangle around this bounds]                                                                                                                                                             |
|                                                                                                                                                                                                                                                             |
| [    e.Graphics.DrawRectangle([Pens].Red, axisBounds);]                                                                                                                                            |
|                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                        |
| **[]**                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                        |
| [AddHandler][ [Me].ChartWebControl1.ChartAreaPaint, [AddressOf] ChartWebControl1_ChartAreaPaint]                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                        |
| [Private][ [Sub] ChartWebControl1_ChartAreaPaint([ByVal] sender [As] [Object], [ByVal] e [As] System.Windows.Forms.PaintEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                        |
| [    [Dim] axisBounds [As] Rectangle = [Me].ChartWebControl1.ChartWebArea.Bounds]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                        |
| [    [\' Render a rectangle around this bounds]]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                        |
| [    e.Graphics.DrawRectangle(Pens.Red, axisBounds)]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub]]                                                                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

**[]** 

Figure 319: Chart Area Bounds in Red

[] 

Chart Plot Area Bounds

**[]** 

Use the **RenderBounds** property to get the rectangular area comprising just the plot-area, bound by the axes.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                             |
| [this][.ChartWebControl1.ChartAreaPaint += [new] System.Windows.Forms.[PaintEventHandler](ChartWebControl1_ChartAreaPaint);] |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                             |
| [void][ ChartWebControl1_ChartAreaPaint([object] sender, System.Windows.Forms.[PaintEventArgs] e)]                           |
|                                                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                             |
| [    [Rectangle] axisBounds = [this].ChartWebControl1.ChartWebArea.RenderBounds;]                                                                                             |
|                                                                                                                                                                                                                                                             |
| [    [// Render a rectangle around this bounds]]                                                                                                                                                  |
|                                                                                                                                                                                                                                                             |
| [    e.Graphics.DrawRectangle([Pens].Red, axisBounds);]                                                                                                                                            |
|                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                        |
| **[]**                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                        |
| [AddHandler][ [Me].ChartWebControl1.ChartAreaPaint, [AddressOf] ChartWebControl1_ChartAreaPaint]                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                        |
| [Private][ [Sub] ChartWebControl1_ChartAreaPaint([ByVal] sender [As] [Object], [ByVal] e [As] System.Windows.Forms.PaintEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                        |
| [    [Dim] axisBounds [As] Rectangle = [Me].ChartWebControl1.ChartWebArea.RenderBounds]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                        |
| [    [\' Render a rectangle around this bounds]]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                        |
| [    e.Graphics.DrawRectangle(Pens.Red, axisBounds)]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub]]                                                                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 320: Chart Plot Area Bounds in Red

 

[]{#p272} 

[]{#related-topics}

