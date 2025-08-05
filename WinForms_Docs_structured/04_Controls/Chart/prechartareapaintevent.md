---
title: prechartareapaintevent.md
original_path: WinForms_Docs/04_Controls/Chart/prechartareapaintevent.md
created_at: 2025-08-05
---








  









### PreChartAreaPaint Event {#prechartareapaint-event style="tab-stops: 0pt"}

 

**PreChartAreaPaint** event is raised before the chart area is painted.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                  |
| [this][.chartControl1.PreChartAreaPaint += [new] System.Windows.Forms.PaintEventHandler([this].chartControl1_PreChartAreaPaint);] |
|                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                  |
| [private][ [void] chartControl1_PreChartAreaPaint([object] sender, PaintEventArgs e)]                                             |
|                                                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                  |
| [       [this].chartControl1.BackColor = Color.Yellow;       ]                                                                                                                                          |
|                                                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p276} 

[]{#related-topics}

