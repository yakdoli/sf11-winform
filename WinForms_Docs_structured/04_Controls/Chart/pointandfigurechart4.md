---
title: pointandfigurechart4.md
original_path: WinForms_Docs/04_Controls/Chart/pointandfigurechart4.md
created_at: 2025-08-05
---






#### Point and Figure Chart {#point-and-figure-chart style="tab-stops: 0pt"}

[]{#p53}[] 

Point and Figure chart consists of columns of X\'s and O\'s that represent filtered price movements over time. Their distinctive look may be alien at first to people who are more familiar with traditional price bar charts, but once people learn the basics of Point and Figure charts, they usually become familiar. It uses a series of X\'s and O\'s to determine price trends where the X\'s represent an upward trend and the O\'s represent a downward trend.

[] 

The following are the attached properties of the Point and Figure chart.

**[]** 


  ------------------- ------------------------- ---------------------------------------------------------------------
  Attached Property   Type                      Description
  ReversalAmount      double                    Gets and sets the reversal amount. The default value is 1.
  FigureCost          double                    Gets and sets the figure cost.
  StartFrom           ChartPointAndFigureType   Gets and sets the start point value for the Point and Figure chart.
  ------------------- ------------------------- ---------------------------------------------------------------------


[] 

The following code example illustrates how to create a Point and Figure Chart.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[XAML\]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<][syncfusion][:][ChartSeries][ Type][=\"PointAndFigure\"][ Label][=\"April\"][ Interior][=\"Blue\"][ Stroke][=\"Black\"][ StrokeThickness][=\"2\"] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [DataSource][=\"{][StaticResource][ data1][}\"][ BindingPathX][=\"StockDate\"][ BindingPathsY][=\"High, Low\"\>]                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\</][syncfusion][:][ChartSeries][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                  |
|                                                                                                                                                                                                                                      |
| [ChartArea][ area = [new] [ChartArea]();]                                                       |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                      |
| [// Creating Point and Figure Chart.]                                                                                                                                              |
|                                                                                                                                                                                                                                      |
| [ChartSeries][ series = [new] [ChartSeries]();]                                                 |
|                                                                                                                                                                                                                                      |
| [series.Type = [ChartTypes].PointAndFigure;]                                                                                                                             |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                      |
| [// Initializing chart data.]                                                                                                                                                      |
|                                                                                                                                                                                                                                      |
| [series.DataSource = [this].Resources\[[\"data1\"]\] [as] StockInfoData;]                                                      |
|                                                                                                                                                                                                                                      |
| [series.BindingPathX = [\"StockDate\"];]                                                                                                                                 |
|                                                                                                                                                                                                                                      |
| [series.BindingPathsY = [new] [List]\<[string]\>() { [\"High\"], [\"Low\"] };] |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                      |
| [area.Series.Add(series);]                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

 

Figure 50 : Point and Figure Chart[]

 

[]{#related-topics}

