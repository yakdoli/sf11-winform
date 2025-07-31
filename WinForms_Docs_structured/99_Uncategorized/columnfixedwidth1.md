---
title: columnfixedwidth1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\columnfixedwidth1.md
created_at: 2025-07-03
---






#### ColumnFixedWidth {#columnfixedwidth style="tab-stops: 0pt"}

[] 

Specifies the width of each column when [ColumnWidthMode]{.UGHyperlink} is set to FixedWidthMode.

 


+------------------------------+-------------------------------------------------+
| Details                                                                        |
+------------------------------+-------------------------------------------------+
| **Possible Values**          | An integer value                                |
+------------------------------+-------------------------------------------------+
| **Default Value    **        | **20**                                          |
+------------------------------+-------------------------------------------------+
| **2D / 3D Limitations**      | None                                            |
+------------------------------+-------------------------------------------------+
| **Applies to Chart Element** | All Series                                      |
+------------------------------+-------------------------------------------------+
| **Applies to Chart Types**   | Column Charts, BoxAndWhiskerChart, Candle Chart |
+------------------------------+-------------------------------------------------+


 

Here is some sample code.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                     |
|                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                           |
|                                                                                                                                                                                                                    |
| [ChartSeries][ series1 = [new] [ChartSeries]([\"Series\"]);] |
|                                                                                                                                                                                                                    |
| [series1.Points.Add(1, [new] [double]\[\] { 24});]                                                                                   |
|                                                                                                                                                                                                                    |
| [series1.Points.Add(2, [new] [double]\[\] { 36});]                                                                                   |
|                                                                                                                                                                                                                    |
| [series1.Points.Add(3, [new] [double]\[\] { 48});]                                                                                   |
|                                                                                                                                                                                                                    |
| [chartControl1.Series.Add(series1);]                                                                                                                                           |
|                                                                                                                                                                                                                    |
| [chartControl1.ColumnWidthMode = [ChartColumnWidthMode].FixedWidthMode;]                                                                                  |
|                                                                                                                                                                                                                    |
| [chartControl1.ColumnFixedWidth = 45;]                                                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                  |
| [Dim][ series1 [As] [ChartSeries] = [New] ChartSeries(\"[Series]\")] |
|                                                                                                                                                                                                                                                  |
| [series1.Points.Add(1, [New] [Double]() { 24})]                                                                                                                    |
|                                                                                                                                                                                                                                                  |
| [series1.Points.Add(2, [New] [Double]() { 36})]                                                                                                                    |
|                                                                                                                                                                                                                                                  |
| [series1.Points.Add(3, [New] [Double]() { 48})]                                                                                                                    |
|                                                                                                                                                                                                                                                  |
| [chartControl1.Series.Add(series1) ]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                  |
| [chartControl1.ColumnWidthMode = ChartColumnWidthMode.FixedWidthMode ]                                                                                                                                       |
|                                                                                                                                                                                                                                                  |
| [chartControl1.ColumnFixedWidth = 45 ]                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 


[{border="0"}]Note: The ColumnFixedWidth property can be overridden by specifying a second y value in the data point. See [ColumnWidthMode]{.UGHyperlink}[ ]{.UGHyperlink}for a sample.


 

{border="0"}

 

Figure 106: ColumnChart with ColumnFixedWidth = \"45\"

 

See Also

 

[Column charts]{.UGHyperlink}, [BoxAndWhiskerChart]{.UGHyperlink}, [ColumnWidthMode]{.UGHyperlink}, [Candle Charts]{.UGHyperlink}[]

 

[]{#p83} 

[]{#related-topics}

