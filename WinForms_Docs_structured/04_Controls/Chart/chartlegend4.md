---
title: chartlegend4.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\chartlegend4.md
created_at: 2025-07-03
---








  









### Chart Legend {#chart-legend style="tab-stops: 0pt"}

 

Legend is the one that displays all the series information that is plotted on the chart.

The Chart Legends can be used to give information about the series in chart control. Chart Legend has CheckBoxVisibility property.  If this property value is *Visible*, then the particular series will be displayed in the chart control. If the check box is unchecked, then the series will be in the *Hidden* state. 

The Legend has collections of series namely LegendLabel data and its template. We can position the legends using the Dock position of the DockPanel. The following code illustrates adding a legend to the chart area.

**[]** 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[XAML\]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **[\<][syncfusion][:][ChartArea.Legends][\>]**                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **[ ][\<][syncfusion][:][ChartLegend][ CheckboxVisibility][=\"Visible\"][ IconVisibility][=\"Visible\"/\>]** |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **[\</][syncfusion][:][ChartArea.Legends][\>]**                                                                                                                                                                                                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                          |
| **[Chart][ chart = ][new][ ][Chart][();]**                |
|                                                                                                                                                                                                                                                                                                                                                                          |
| **[ChartArea][ area = ][new][ ][ChartArea][();]**         |
|                                                                                                                                                                                                                                                                                                                                                                          |
| **[ChartLegends][ legend = ][new][ ][ChartLegends][();]** |
|                                                                                                                                                                                                                                                                                                                                                                          |
| **[legend.CheckboxVisibility = ][Visibility][.Visible;]**                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                          |
| **[legend.IconVisibility = ][Visibility][.Visible;]**                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                          |
| **[area.Legends = legend;]**                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                          |
| **[chart.Areas.Add(area);]**                                                                                                                                                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

**[]** 

Run the code. The following output is displayed.

**[]** 

{border="0"}

 

Figure 104 : Chart Legend**[]**

**[]** 

Some important settings of chart legend are discussed in detail, under the following topic.

**[]** 

More:







