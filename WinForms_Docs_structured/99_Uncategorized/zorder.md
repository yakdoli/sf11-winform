---
title: zorder.md
original_path: WinForms_Docs/99_Uncategorized/zorder.md
created_at: 2025-08-05
---






#### ZOrder {#zorder style="tab-stops: 0pt"}

[] 

Specifies the order in which the objects are arranged and controls the visibility when one is placed over the other.

By default, the ZOrder for series are assigned based on the order in which they are added to the Series collection.

[] 


+--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Details                                                                                                                                                                                                                                         |
+--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Possible Values          | Any integer value                                                                                                                                                                                                    |
+--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Default Value            | The order that we add the series in the chart control.                                                                                                                                                               |
+--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2D / 3D Limitations      | No                                                                                                                                                                                                                   |
+--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Applies to Chart Element | Any Series                                                                                                                                                                                                           |
+--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Applies to Chart Types   | Gantt Chart, Histogram chart, Tornado Chart, Combination Chart, Box and Whisker Chart, Area Charts,Polar And Radar Chart, BarCharts, Column Charts, Bubble Charts, Candle Charts, Hilo Charts, Hilo Open Close Chart |
+--------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


**[]** 

Here is sample code snippet using ZOrder.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                       |
|                                                                                                                                                      |
| **[]**                                                                                             |
|                                                                                                                                                      |
| [this][.ChartWebControl1.Series\[0\].ZOrder = 0;] |
|                                                                                                                                                      |
| [this][.ChartWebControl1.Series\[1\].ZOrder = 1;] |
+------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                      |
|                                                                                                                                                         |
| **[]**                                                                                                |
|                                                                                                                                                         |
| [Private Me][.ChartWebControl1.Series(0).ZOrder = 0] |
|                                                                                                                                                         |
| [Private Me][.ChartWebControl1.Series(1).ZOrder = 1] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

**[]** 

***[]*** 

Figure 224: Series 1 ZOrder = 0, Series 2 ZOrder = 1

**[]** 

{border="0"}

**[]** 

***[]*** 

Figure 225: Series 1 ZOrder = 1, Series 2 ZOrder = 0

**[]** 

Rearranging the Series using ZOrder property

[] 

The chart series can be rearranged at run-time using ZOrder property as follows. The chart needs to be redrawn in order to reflect ZOrder property changes. we cannot call redrawing for every series ZOrder changes. In order to overcome this, we should change the order of the series in between the begin update and end update statements as follows.\
\

+----------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                               |
|                                                                                                                                              |
| []                                                                                         |
|                                                                                                                                              |
| [this][.ChartWebControl1.BeginUpdate();]                |
|                                                                                                                                              |
| [this][.ChartWebControl1.Model.Series\[0\].ZOrder = 2;] |
|                                                                                                                                              |
| [this][.ChartWebControl1.Model.Series\[1\].ZOrder = 1;] |
|                                                                                                                                              |
| [this][.ChartWebControl1.Model.Series\[2\].ZOrder = 0;] |
|                                                                                                                                              |
| [this][.ChartWebControl1.EndUpdate();]                  |
+----------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                        |
|                                                                                                                                           |
| **[]**                                                                                  |
|                                                                                                                                           |
| [Me][.ChartWebControl1.BeginUpdate()]                |
|                                                                                                                                           |
| [Me][.ChartWebControl1.Model.Series\[0\].ZOrder = 2] |
|                                                                                                                                           |
| [Me][.ChartWebControl1.Model.Series\[1\].ZOrder = 1] |
|                                                                                                                                           |
| [Me][.ChartWebControl1.Model.Series\[2\].ZOrder = 0] |
|                                                                                                                                           |
| [Me][.ChartWebControl1.EndUpdate()]                  |
+-------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

**[]** 

***[]*** 

Figure 226: Chart with Rearranged Series

**[]** 

See Also

[] 

[Pyramid Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Funnel Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Area Charts]{.UGHyperlink}[, ]{.UGHyperlink}[Bar Charts]{.UGHyperlink}[, ]{.UGHyperlink}[Bubble Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Column Charts]{.UGHyperlink}[, ]{.UGHyperlink}[Candle Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Renko chart]{.UGHyperlink}[, ]{.UGHyperlink}[Three Line Break Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Box and Whisker Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Gantt Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Histogram Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Tornado Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Polar and Radar Chart]{.UGHyperlink}[, ]{.UGHyperlink}[Pie Chart]{.UGHyperlink}[]{.UGHyperlink}

[]{#p170} 

[]{#related-topics}

