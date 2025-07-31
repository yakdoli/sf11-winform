---
title: elementborders1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\elementborders1.md
created_at: 2025-07-03
---






#### ElementBorders {#elementborders style="tab-stops: 0pt"}

 

Gets / sets the border settings for elements associated with the chart point. You can specify the inner and outer border. It is currently used only by symbols rendered by the ChartPoint (inherited from ChartStyleInfo).

 


+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                       |
| Details                                                                                                                                                                                                                               |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Possible Values**                 | Border setting object                                                                                                                                                                           |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Default Value    **               | [·      ]**Weight** -- Thin                                                                                                                                        |
|                                     |                                                                                                                                                                                                 |
|                                     | [·      ]**Width value** -- 1                                                                                                                                      |
|                                     |                                                                                                                                                                                                 |
|                                     | [·      ]**Style** - Standard                                                                                                                                      |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **2D / 3D Limitations**             | No                                                                                                                                                                                              |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Applies to Chart Element**        | All series and points                                                                                                                                                                           |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Applies to Chart Types**          | Area Charts, Bar Charts, Bubble Chart, Column Charts, Line  Charts, Candle Chart, Renko chart, Three Line Break Chart, Box and Whisker Chart, Gantt Chart, Tornado Chart, Polar and Radar Chart |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

Here is some sample code.

 

Series Wide Setting

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                         |
|                                                                                                                                                                                                        |
| **[]**                                                                                                                                               |
|                                                                                                                                                                                                        |
| [// Setting Symbol for the ChartSeries]                                                                                                              |
|                                                                                                                                                                                                        |
| [this][.chartControl1.Series\[0\].Style.Symbol.Color = [Color].Yellow;]                      |
|                                                                                                                                                                                                        |
| [this][.chartControl1.Series\[0\].Style.Symbol.Shape = [ChartSymbolShape].InvertedTriangle;] |
|                                                                                                                                                                                                        |
| [// Setting ElementBorder for a symbol]                                                                                                              |
|                                                                                                                                                                                                        |
| [ChartBordersInfo][ cbi = [new] [ChartBordersInfo]();]                  |
|                                                                                                                                                                                                        |
| [cbi.Outer = [new] [ChartBorder]([ChartBorderStyle].Solid, [Color].White);]    |
|                                                                                                                                                                                                        |
| [cbi.Inner = [new] [ChartBorder]([ChartBorderStyle].DashDot, [Color].Cyan);]   |
|                                                                                                                                                                                                        |
| [this][.chartControl1.Series\[0\].Style.ElementBorders = cbi;]                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
|                                                                                                                                                                                                   |
| [ \' Setting Symbol for the ChartSeries]                                                                                                        |
|                                                                                                                                                                                                   |
| [Me][.chartControl1.Series(0).Style.Symbol.Color = [Color].Yellow]                      |
|                                                                                                                                                                                                   |
| [Me][.chartControl1.Series(0).Style.Symbol.Shape = [ChartSymbolShape].InvertedTriangle] |
|                                                                                                                                                                                                   |
| [ \' Setting ElementBorder for a symbol]                                                                                                        |
|                                                                                                                                                                                                   |
| [cbi As [ChartBordersInfo] = New [ChartBordersInfo]()]                                                              |
|                                                                                                                                                                                                   |
| [cbi.Outer = [New] [ChartBorder]([ChartBorderStyle].Solid, Color.White)]                       |
|                                                                                                                                                                                                   |
| [cbi.Inner = [New] ChartBorder(ChartBorderStyle.DashDot, Color.Cyan)]                                                                    |
|                                                                                                                                                                                                   |
| [Me][.chartControl1.Series(0).Style.ElementBorders = cbi]                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

**[]** 

Figure 121: Column Chart with ElementBorder

 

Specific Data Point Setting

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                              |
|                                                                                                                                                             |
| []                                                                                                                      |
|                                                                                                                                                             |
| [//Specifying element border for the first data point Styles(0), second data point Styles(1) and so on..] |
|                                                                                                                                                             |
| [this][.chartControl1.Series\[0\].Styles\[0\].ElementBorders = cbi;]   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                          |
|                                                                                                                                                             |
| []                                                                                                                      |
|                                                                                                                                                             |
| [\'Specifying element border for the first data point Styles(0), second data point Styles(1) and so on..] |
|                                                                                                                                                             |
| [this][.chartControl1.Series(0).Styles(0).ElementBorders = cbi]        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

See Also

 

[Area Charts]{.UGHyperlink},[ ]{.UGHyperlink}[Bar Charts]{.UGHyperlink}, [Bubble Chart]{.UGHyperlink}, [Column Charts]{.UGHyperlink}, [Line Charts]{.UGHyperlink}, [Candle Chart]{.UGHyperlink}, [Renko chart]{.UGHyperlink}, [Three Line Break Chart]{.UGHyperlink},

[Box and Whisker Chart]{.UGHyperlink}, [Gantt Chart]{.UGHyperlink}, [Tornado Chart]{.UGHyperlink}, [Polar and Radar Chart]{.UGHyperlink}[]

 

[]{#p95} 

[]{#related-topics}

