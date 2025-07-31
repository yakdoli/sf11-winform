---
title: chartareabounds1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\chartareabounds1.md
created_at: 2025-07-03
---








  









### Chart Area Bounds {#chart-area-bounds style="tab-stops: 0pt"}

 

Full Chart Area Bounds

 

Use the **Bounds** property to get the rectangular area comprising the chart area that includes the axis, axis titles and other sections.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                       |
| [this][.chartControl1.ChartAreaPaint += [new] System.Windows.Forms.[PaintEventHandler](chartControl1_ChartAreaPaint);] |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                       |
| [void][ chartControl1_ChartAreaPaint([object] sender, System.Windows.Forms.[PaintEventArgs] e)]                        |
|                                                                                                                                                                                                                                                       |
| [{]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                       |
| [    [Rectangle] axisBounds = [this].chartControl1.ChartArea.Bounds;]                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [   ][// Render a rectangle around this bounds]                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [    e.Graphics.DrawRectangle([Pens].Red, axisBounds);]                                                                                                                                      |
|                                                                                                                                                                                                                                                       |
| [}]                                                                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                     |
| [AddHandler][ [Me].chartControl1.ChartAreaPaint, [AddressOf] chartControl1_ChartAreaPaint]                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                     |
| [Private][ [Sub] chartControl1_ChartAreaPaint([ByVal] sender [As] [Object], [ByVal] e [As] System.Windows.Forms.PaintEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                     |
| [    [Dim] axisBounds [As] Rectangle = [Me].chartControl1.ChartArea.Bounds]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                     |
| [    [\' Render a rectangle around this bounds]]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                     |
| [    e.Graphics.DrawRectangle(Pens.Red, axisBounds)]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                     |
| [End][ [Sub]]                                                                                                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

 

Figure 363: Chart Area Bounds in Red

[] 

Chart Plot Area Bounds

 

Use the **RenderBounds** property to get the rectangular area comprising just the plot-area, bound by the axes.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                       |
| [this][.chartControl1.ChartAreaPaint += [new] System.Windows.Forms.[PaintEventHandler](chartControl1_ChartAreaPaint);] |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                       |
| [void][ chartControl1_ChartAreaPaint([object] sender, System.Windows.Forms.[PaintEventArgs] e)]                        |
|                                                                                                                                                                                                                                                       |
| [{]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                       |
| [    [Rectangle] axisBounds = [this].chartControl1.ChartArea.RenderBounds;]                                                                                             |
|                                                                                                                                                                                                                                                       |
| [    [// Render a rectangle around this bounds]]                                                                                                                                            |
|                                                                                                                                                                                                                                                       |
| [    e.Graphics.DrawRectangle([Pens].Red, axisBounds);]                                                                                                                                      |
|                                                                                                                                                                                                                                                       |
| [}]                                                                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                     |
| [AddHandler][ [Me].chartControl1.ChartAreaPaint, [AddressOf] chartControl1_ChartAreaPaint]                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                     |
| [Private][ [Sub] chartControl1_ChartAreaPaint([ByVal] sender [As] [Object], [ByVal] e [As] System.Windows.Forms.PaintEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                     |
| [    [Dim] axisBounds [As] Rectangle = [Me].chartControl1.ChartArea.RenderBounds]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                     |
| [    [\' Render a rectangle around this bounds]]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                     |
| [    e.Graphics.DrawRectangle(Pens.Red, axisBounds)]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                     |
| [End][ [Sub]]                                                                                                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

 

Figure 364: Chart Plot Area Bounds in Red

[]{#p266} 

[]{#related-topics}

