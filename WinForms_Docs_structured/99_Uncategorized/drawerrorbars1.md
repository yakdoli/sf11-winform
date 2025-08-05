---
title: drawerrorbars1.md
original_path: WinForms_Docs/99_Uncategorized/drawerrorbars1.md
created_at: 2025-08-05
---






#### DrawErrorBars {#drawerrorbars style="tab-stops: 0pt"}

 

Error Bars are used to indicate a degree of uncertainty in the plotted data through a bar indicating an \"error range\".

 

The 2nd y value is used to indicate the error range. For example, a value of 5 indicates an error range of -5 to +5 from the specified y value.

 


+-------------------------------------+-----------------------------------------+
|                                                                               |
|                                                                               |
| Details                                                                       |
+-------------------------------------+-----------------------------------------+
| **Possible Values**                 | True or False                           |
+-------------------------------------+-----------------------------------------+
| **Default Value    **               | **False**                               |
+-------------------------------------+-----------------------------------------+
| **2D / 3D Limitations**             | No                                      |
+-------------------------------------+-----------------------------------------+
| **Applies to Chart Element**        | All series                              |
+-------------------------------------+-----------------------------------------+
| **Applies to Chart Types**          | Column Chart, Line Chart and HiLo Chart |
+-------------------------------------+-----------------------------------------+


 

Here is some sample code.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                             |
| [ [// Generating Series]]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                             |
| [ChartSeries][ series = [this].chartControl1.Model.NewSeries([\"Sales\"], [ChartSeriesType].Column);] |
|                                                                                                                                                                                                                                                             |
| [ [// 2nd Y value indicates the error range]]                                                                                                                                                     |
|                                                                                                                                                                                                                                                             |
| [series.Points.Add(1, [new] [double]\[\] { 20, 5 });]                                                                                                                         |
|                                                                                                                                                                                                                                                             |
| [series.Points.Add(2, [new] [double]\[\] { 70, 6 });]                                                                                                                         |
|                                                                                                                                                                                                                                                             |
| [series.Points.Add(3, [new] [double]\[\] { 10, 3 });]                                                                                                                         |
|                                                                                                                                                                                                                                                             |
| [series.Points.Add(4, [new] [double]\[\] { 40, 6 });]                                                                                                                         |
|                                                                                                                                                                                                                                                             |
| [series.Text = series.Name;]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                             |
| [// Adding Series to the Chart]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                             |
| [this][.chartControl1.Series.Add(series);]                                                                                                                             |
|                                                                                                                                                                                                                                                             |
| [// Specifies the Error Bar in Column chart.]                                                                                                                                                             |
|                                                                                                                                                                                                                                                             |
| [this][.chartControl1.Series\[0\].DrawErrorBars = [true];]                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **[ ]**[\' Generating Series]                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [series As ][ChartSeries][ = ][Me][.chartControl1.Model.NewSeries(][\"Sales\"][, ][ChartSeriesType][.Column)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [ [\' 2nd Y value indicates the error range]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [series.Points.Add(1,][ New Double][() { 20, 5 })]                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [series.Points.Add(2, ][New Double][() { 70, 6 })]                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [series.Points.Add(3, ][New Double][() { 10, 3 })]                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [series.Points.Add(4, ][New Double][() { 40, 6 })]                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [series.Text = series.Name]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\' Adding Series to the Chart]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Me][.chartControl1.Series.Add(series)]                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\' Specifies the Error Bar in Column chart.]                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Private Me.chartControl1.Series(0).DrawErrorBars = ][True]                                                                                                                                                                                                                                                                                                                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

 

Figure 116: ColumnChart with ErrorBars

 

{border="0"}

 

Figure 117: Line Chart with ErrorBars and ErrorBarsSymbolShape=\"Diamond\"

 

ErrorBar Orientation

 

Orientation of the ErrorBars can be specified in the **ErrorBars.Orientation** property. It can be *Vertical* or *Horizontal*.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [//Creates a New Series]                                                                                                                                    |
|                                                                                                                                                                                                               |
| [ChartSeries][ s1 = [new] [ChartSeries]([\"series\"]);] |
|                                                                                                                                                                                                               |
| [//Points for the Series]                                                                                                                                   |
|                                                                                                                                                                                                               |
| [s1.Points.Add(10, [new] [double]\[\] {20, 2, 2});]                                                                             |
|                                                                                                                                                                                                               |
| [s1.Points.Add(20, [new] [double]\[\] {70, 2, 2});]                                                                             |
|                                                                                                                                                                                                               |
| [s1.Points.Add(30, [new] [double]\[\] {10, 2, 2});]                                                                             |
|                                                                                                                                                                                                               |
| [s1.Points.Add(40, [new] [double]\[\] {40, 2, 2});]                                                                             |
|                                                                                                                                                                                                               |
| [s1.Points.Add(40, [new] [double]\[\] {40, 2, 2});]                                                                             |
|                                                                                                                                                                                                               |
| [s1.Text = s1.Name;]                                                                                                                                                      |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [//Type of Series]                                                                                                                                          |
|                                                                                                                                                                                                               |
| [s1.Type = [ChartSeriesType].Line;]                                                                                                                  |
|                                                                                                                                                                                                               |
| [s1.ConfigItems.ErrorBars.Enabled = [true];]                                                                                                         |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [// Set the orientation to horizontal]                                                                                                                      |
|                                                                                                                                                                                                               |
| [s1.ConfigItems.ErrorBars.Orientation = [ChartOrientation].Horizontal;]                                                                              |
|                                                                                                                                                                                                               |
| [s1.ConfigItems.ErrorBars.SymbolShape = [ChartSymbolShape].None;]                                                                                    |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [s1.Style.Interior = [new] Syncfusion.Drawing.[BrushInfo]([Color].Red);]                                   |
|                                                                                                                                                                                                               |
| [this][.chartControl1.PrimaryXAxis.DrawGrid = [false];]                                             |
|                                                                                                                                                                                                               |
| [this][.chartControl1.PrimaryYAxis.DrawGrid = [false];]                                             |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [this][.chartControl1.Series.Add(s1);]                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                    |
|                                                                                                                                                                                                       |
| **[]**                                                                                                                                              |
|                                                                                                                                                                                                       |
| [\'Creates a New Series ]                                                                                                                           |
|                                                                                                                                                                                                       |
| [Dim][ s1 [As] [New] ChartSeries([\"series\"])] |
|                                                                                                                                                                                                       |
| [\'Points for the Series ]                                                                                                                          |
|                                                                                                                                                                                                       |
| [s1.Points.Add(10, [New] [Double]() {20, 2, 2}) ]                                                                       |
|                                                                                                                                                                                                       |
| [s1.Points.Add(20, [New] [Double]() {70, 2, 2}) ]                                                                       |
|                                                                                                                                                                                                       |
| [s1.Points.Add(30, [New] [Double]() {10, 2, 2}) ]                                                                       |
|                                                                                                                                                                                                       |
| [s1.Points.Add(40, [New] [Double]() {40, 2, 2}) ]                                                                       |
|                                                                                                                                                                                                       |
| [s1.Points.Add(40, [New] [Double]() {40, 2, 2}) ]                                                                       |
|                                                                                                                                                                                                       |
| [s1.Text = s1.Name ]                                                                                                                                              |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [\'Type of Series ]                                                                                                                                 |
|                                                                                                                                                                                                       |
| [s1.Type = ChartSeriesType.Line ]                                                                                                                                 |
|                                                                                                                                                                                                       |
| [s1.ConfigItems.ErrorBars.Enabled = [True] ]                                                                                                 |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [\' Set the orientation to horizontal ]                                                                                                             |
|                                                                                                                                                                                                       |
| [s1.ConfigItems.ErrorBars.Orientation = ChartOrientation.Horizontal ]                                                                                             |
|                                                                                                                                                                                                       |
| [s1.ConfigItems.ErrorBars.SymbolShape = ChartSymbolShape.None ]                                                                                                   |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [s1.Style.Interior = [New] Syncfusion.Drawing.BrushInfo(Color.Red) ]                                                                         |
|                                                                                                                                                                                                       |
| [Me][.chartControl1.PrimaryXAxis.DrawGrid = [False] ]                                       |
|                                                                                                                                                                                                       |
| [Me][.chartControl1.PrimaryYAxis.DrawGrid = [False] ]                                       |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [Me][.chartControl1.Series.Add(s1) ]                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

 

Figure 118: Errorbar Orientation = \"Horizontal\"

 

See Also

 

[Line Chart]{.UGHyperlink}, [Column Chart]{.UGHyperlink},[ ][Hi Lo Chart]{.UGHyperlink}, [ErrorBarsSymbolShape]{.UGHyperlink}[]

 

[]{#p91} 

[]{#related-topics}

