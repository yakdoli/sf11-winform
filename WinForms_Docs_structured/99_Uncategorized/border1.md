---
title: border1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\border1.md
created_at: 2025-07-03
---






#### Border {#border style="tab-stops: 0pt"}

 

The user can also set the Border color and Border style for the chart series.

 


+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Details                                                                                                                                                                                                                                            |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Possible Values**                 | Any Color, Width, Style for the Borders                                                                                                                                                                      |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Default Value    **               | [·      ]**Color**  - Black                                                                                                                                                     |
|                                     |                                                                                                                                                                                                              |
|                                     | [·      ]**Width value** - 1                                                                                                                                                    |
|                                     |                                                                                                                                                                                                              |
|                                     | [·      ]**DashStyle** - Solid                                                                                                                                                  |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **2D / 3D Limitations**             | No                                                                                                                                                                                                           |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Applies to Chart Element**        | All series and points                                                                                                                                                                                        |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Applies to Chart Types**          | Pyramid, Funnel, Area, Bar, Bubble, Column Chart, Candle Chart, Renko chart, Three Line Break Chart, Box and Whisker Chart, Gantt Chart, Histogram Chart, Tornado Chart, Polar and Radar Chart and Pie Chart |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

The line type can be configured using the **ChartSeries.Style.Border** property as in the following example.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]                    ]**                                                                                                                                                        |
|                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                  |
|                                                                                                                                                                                                                                           |
| [// Set the border style required for the column chart.]                                                                                                                                |
|                                                                                                                                                                                                                                           |
| [series.Style.Border.Width = 3;]                                                                                                                                                        |
|                                                                                                                                                                                                                                           |
| [series.Style.Border.Color = ][Color][.][White;] |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                           |
| [// Set the Series style]                                                                                                                                                               |
|                                                                                                                                                                                                                                           |
| [series.Style.DisplayShadow = [true];]                                                                                                                                           |
|                                                                                                                                                                                                                                           |
| [series.Style.ShadowInterior = [new] Syncfusion.Drawing.[BrushInfo]([Color].White);]                                                   |
|                                                                                                                                                                                                                                           |
| [series.Style.ShadowOffset = [new] [Size](3, 3);]                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\' Set the border style required for the column chart.]                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [series.Style.Border.Width = 3]                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [series.Style.Border.Color = ][Color][.][White]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\' Set the Series style]                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [series.Style.DisplayShadow = True]                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [series.Style.ShadowInterior = ][New][ Syncfusion.Drawing.][BrushInfo][(][Color][.][White[)]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [series.Style.ShadowOffset = ][New][ Size(3, 3)]                                                                                                                                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

 

Figure 97**[: Border Lined Column Chart]**

 

To apply this on specific data points:

[] 

+--------------------------------------------------------------------------------------------------------------+
| **[\[C#\]                    ]**                           |
|                                                                                                              |
| **[]**                                                     |
|                                                                                                              |
| [//Sets border for the 1st point in 1st series]            |
|                                                                                                              |
| [series1.Styles\[0\].Border.Width = 3;]                                  |
|                                                                                                              |
| [series1.Styles\[0\].Border.Color = [Color].White;] |
|                                                                                                              |
| []                                                                       |
|                                                                                                              |
| [//Sets border for the 3rd point in 2nd series]            |
|                                                                                                              |
| [series2.Styles\[2\].Border.Width = 3;]                                  |
|                                                                                                              |
| [series2.Styles\[2\].Border.Color = [Color].White;] |
+--------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                |
|                                                                                                   |
| **[]**                                          |
|                                                                                                   |
| [\'Sets border for the 1st point in 1st series] |
|                                                                                                   |
| [series1.Styles(0).Border.Width = 3]                          |
|                                                                                                   |
| [series1.Styles(0).Border.Color = Color.White]                |
|                                                                                                   |
| []                                                            |
|                                                                                                   |
| [\'Sets border for the 3rd point in 2nd series] |
|                                                                                                   |
| [series2.Styles(2).Border.Width = 3]                          |
|                                                                                                   |
| [series2.Styles(2).Border.Color = Color.White]                |
+---------------------------------------------------------------------------------------------------+

[] 

{border="0"}

 

Figure 98: Individual Data Points with White Border

 

See Also

 

[Pyramid Chart]{.UGHyperlink}, [Funnel Chart]{.UGHyperlink}, [Area Charts]{.UGHyperlink}, [BarCharts]{.UGHyperlink}, [Bubble Chart]{.UGHyperlink}, [Column Chart]{.UGHyperlink},[ ][Candle Chart]{.UGHyperlink}, [Renko chart]{.UGHyperlink}, [Three Line Break Chart]{.UGHyperlink}, [Box and Whisker Chart]{.UGHyperlink}, [Gantt Chart]{.UGHyperlink}[,]{.UGHyperlink} [Histogram Chart]{.UGHyperlink}, [Tornado Chart]{.UGHyperlink}, [Polar and Radar Chart]{.UGHyperlink}, [Pie Chart]{.UGHyperlink}[]

 

[]{#p79} 

[]{#related-topics}

