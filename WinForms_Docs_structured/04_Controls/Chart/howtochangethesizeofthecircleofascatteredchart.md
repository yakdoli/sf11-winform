---
title: howtochangethesizeofthecircleofascatteredchart.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\howtochangethesizeofthecircleofascatteredchart.md
created_at: 2025-07-03
---








  









## How to change the size of the circle of a Scattered Chart? {#how-to-change-the-size-of-the-circle-of-a-scattered-chart style="tab-stops: 0pt"}

[] 

You can change the circle size of a Scattered Chart by changing the symbol size of the of **ChartStyleInfo**.

**[]** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                          |
|                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                |
|                                                                                                                                                                                                                         |
| [void][ series2_PrepareStyle([object] sender, [ChartPrepareStyleInfoEventArgs] args)] |
|                                                                                                                                                                                                                         |
| [{]                                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [ChartSeries][ series = sender [as] [ChartSeries];]                                |
|                                                                                                                                                                                                                         |
| [if][ (series != [null])]                                                                                     |
|                                                                                                                                                                                                                         |
| [{]                                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [args.Style.Text = [string].Format([\"{0}\"], series.Points\[args.Index\].YValues\[0\]);]                                              |
|                                                                                                                                                                                                                         |
| [args.Style.Symbol.Shape = [ChartSymbolShape].Circle;]                                                                                                      |
|                                                                                                                                                                                                                         |
| [// Change the size of the symbol.]                                                                                                                                   |
|                                                                                                                                                                                                                         |
| [args.Style.Symbol.Size = [new] [Size](50, 50);]                                                                                       |
|                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                           |
| [Private][ [Sub] series2_PrepareStyle([ByVal] sender [As] [Object], [ByVal] args [As] ChartPrepareStyleInfoEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                           |
| [Dim][ series [As] ChartSeries = [CType](IIf([TypeOf] sender [Is] ChartSeries, sender, [Nothing]), ChartSeries)]                            |
|                                                                                                                                                                                                                                                                                                                                           |
| [If][ [Not] series [Is] [Nothing] [Then]]                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                           |
| [args.Style.Text = [String].Format([\"{0}\"], series.Points(args.Index).YValues(0))]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                           |
| [args.Style.Symbol.Shape = ChartSymbolShape.Circle]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                           |
| [\' Change the size of the symbol.]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                           |
| [args.Style.Symbol.Size = [New] Size(50, 50)]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                           |
| [End][ [If]]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                           |
| [End][ [Sub]]                                                                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p274} 

[]{#related-topics}

