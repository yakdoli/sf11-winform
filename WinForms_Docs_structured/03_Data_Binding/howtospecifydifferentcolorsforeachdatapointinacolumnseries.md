---
title: howtospecifydifferentcolorsforeachdatapointinacolumnseries.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\howtospecifydifferentcolorsforeachdatapointinacolumnseries.md
created_at: 2025-07-03
---








  









## How to specify different colors for each data point in a Column Series? {#how-to-specify-different-colors-for-each-data-point-in-a-column-series style="tab-stops: 0pt"}

[] 

The color of the columns (points) in a Column Chart can be customized by handling the **PrepareStyle** event of the series.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                     |
| [series.PrepareStyle += [new] ChartPrepareStyleInfoHandler([this].ChartControlSeries_PrepareStyle);]                                                                                  |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                     |
| [protected][ [void] ChartControlSeries_PrepareStyle([object] sender, [ChartPrepareStyleInfoEventArgs] args)] |
|                                                                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                     |
| [ChartSeries][ series = sender [as] [ChartSeries];]                                                                            |
|                                                                                                                                                                                                                                                                     |
| [int][ r, g, b;]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                     |
| [switch][(args.Index)]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                     |
| [case][ 0:]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                     |
| [r = 222;b=245;g=123;]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                     |
| [break][;]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                     |
| [default][:]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                     |
| [r = 222;b=245;g=123;]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                     |
| [break][;]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                     |
| [}]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                     |
| [if][(series != [null])]                                                                                                                                  |
|                                                                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                     |
| [args.Style.Interior = [new] [BrushInfo]([GradientStyle].None,[Color].Black,[Color].FromArgb(r,g,b ) );]   |
|                                                                                                                                                                                                                                                                     |
| [args.Handled = [true];]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                     |
| [}]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                     |
| [}]                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                        |
| **[]**                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                        |
| [AddHandler][ series.PrepareStyle, [AddressOf] ChartControlSeries_PrepareStyle]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                        |
| [Protected][ [Sub] ChartControlSeries_PrepareStyle([ByVal] sender [As] [Object], [ByVal] args [As] ChartPrepareStyleInfoEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                        |
| [Dim][ series [As] ChartSeries = [CType](IIf([TypeOf] sender [Is] ChartSeries, sender, [Nothing]), ChartSeries)]                                         |
|                                                                                                                                                                                                                                                                                                                                                        |
| [Dim][ r, g, b [As] [Integer]]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                        |
| [Select][ [Case] args.Index]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                        |
| [Case][ 0]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                        |
| [r = 222]                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                        |
| [b = 245]                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                        |
| [g = 123]                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                        |
| [Case][ [Else]]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                        |
| [r = 222]                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                        |
| [b = 245]                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                        |
| [g = 123]                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                        |
| [End][ [Select]]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                        |
| [If][ [Not] series [Is] [Nothing] [Then]]                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                        |
| [args.Style.Interior = [New] BrushInfo(GradientStyle.None, Color.Black, Color.FromArgb(r, g, b))]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                        |
| [args.Handled = [True]]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                        |
| [End][ [If]]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub]]                                                                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p277} 

[]{#related-topics}

