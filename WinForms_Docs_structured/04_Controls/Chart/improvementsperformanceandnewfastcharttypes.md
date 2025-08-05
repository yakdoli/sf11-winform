---
title: improvementsperformanceandnewfastcharttypes.md
original_path: WinForms_Docs/04_Controls/Chart/improvementsperformanceandnewfastcharttypes.md
created_at: 2025-08-05
---






#### Improvements Performance and New fast chart types  {#improvements-performance-and-new-fast-chart-types style="tab-stops: 0pt"}

**[]** 

Fast Column and Fast Scatter Charts are similar to Column and Scatter charts respectively. It uses vertical bars (called columns) and scattered circles (called ellipse) to display different values of one or more items.

The advantages of Fast Charts:

[·      ]Loads faster than other charts

[·      ]Ensures high performance for displaying data.

[·      ]They can be used as real time charts to render huge number of data points.

Use Case Scenarios

It can be used for rendering large number of points like Stock Market Analysis.

[] 

Adding FastScatter to an Application

FastScatter and FastColumn Chart types can be added using the property Type in ChartSeries.

**[]** 

+-------------------------------------------------------------------------------------------------------------------+
| [\[XAML\]][ ] |
|                                                                                                                   |
| **[]**                                                          |
|                                                                                                                   |
| [//Add FastScatter chart type to the series.]                   |
|                                                                                                                   |
| [  \<sync:ChartSeries  Type=\"FastScatter\" /\>]                |
|                                                                                                                   |
| **[]**                                                          |
+-------------------------------------------------------------------------------------------------------------------+

**[]** 

+------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                       |
|                                                                                                                  |
| []                                                             |
|                                                                                                                  |
| [//Add FastScatter chart type to the series.]                  |
|                                                                                                                  |
| []                                                             |
|                                                                                                                  |
| [Chart1.Areas\[0\].Series\[0\].Type = ChartTypes.FastScatter;] |
|                                                                                                                  |
| **[]**                                                         |
+------------------------------------------------------------------------------------------------------------------+

 

 

{border="0"}

Figure 52: FastScatter

**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[[XAML]\]][ ]                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| [//Add FastColumn chart type to the series.]                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| [  ][\<][sync][:][ChartSeries][ [ Type][=\"FastColumn\" /\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                                                                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+-----------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                |
|                                                                                                                             |
| []                                                                                      |
|                                                                                                                             |
| [//Add FastColumn chart type to the series.]                              |
|                                                                                                                             |
| []                                                                                      |
|                                                                                                                             |
| [Chart1.Areas\[0\].Series\[0\].Type = [ChartTypes].FastColumn;] |
|                                                                                                                             |
| **[]**                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 53: FastColumn

 

Sample Link

A sample application that illustrates FastChart is distributed along with the Essential Chart Silverlight installation and can be found at:

\<sample installation location\>\\Syncfusion\\EssentialStudio\\8.3.0.22\\Silverlight\\Syncfusion.Chart.Silverlight.Samples\\Samples\\Chart Gallery\\FastChartTypes.xaml

[]{#related-topics}

