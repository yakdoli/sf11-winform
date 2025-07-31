---
title: multipleaxes.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\multipleaxes.md
created_at: 2025-07-03
---








  









### Multiple Axes {#multiple-axes style="tab-stops: 0pt"}

[] 

Often you will have to plot multiple series on a single chart, each in it\'s own X or Y axis. You will then need to add an X or Y axis to the chart in addition to the already existing PrimaryXAxis and PrimaryYAxis. You can do this by instantiating a **ChartAxis** and adding it to the **Axes** collection. Then specify the newly created axis as the X or Y axis of a particular series.

The following are the steps to include a new axis to the chart.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                              |
| [// Create a new instance of the chart axis.]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                              |
| [private][ ChartAxis secXAxis = ][new][ ChartAxis();]                  |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                              |
| [// Add the secondary axis to the chart axis collection.]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                              |
| [this][.][ChartWebControl1[.Axes.Add(][this][.secXAxis);]]           |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                              |
| [// Specify this axis to be the axis for an existing series]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                              |
| [this][.][ChartWebControl1[.Series\[1\].XAxis = ][this][.secXAxis;]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [\' Create a new instance of the chart axis.]                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [Private][ secXAxis ][As][ ChartAxis = ][New][ ChartAxis()] |
|                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [\' Add the secondary axis to the chart axis collection.]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [Me][.][ChartWebControl1[.Axes.Add(][Me][.secXAxis)]]                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [\' Specify this axis to be the axis for an existing series]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                      |
| [Me][.][ChartWebControl1[.Series(1).XAxis = ][Me][.secXAxis]]                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 244: Chart Web control with a 2nd X-Axis (-2 to 8) stacked below the Primary X-Axis

[] 

Opposed Position

[] 

By default, this additional axis will be rendered right next to the corresponding primary axis as seen above. This might be undesirable and you would instead want it to be rendered at the opposite side of the primary axis. This is done by setting the **OpposedPosition** property to **true**. For more details, see [Opposed Axis]{.UGHyperlink}.

[] 

{border="0"}

[] 

Figure 245: ChartWebControl with a 2nd X-axis in Opposed Position

**[]** 

Stacked or SideBySide Position

[] 

By default, the secondary axes are rendered stacked over, or parallel, to the corresponding primary axis and sometimes rendered in a position opposite to the primary axis as shown in the above screenshots. This is because the **XAxisLayoutMode** and **YAxisLayoutMode** properties are set to **Stacking** by default.

However, you might want the secondary axis to be rendered in-line, side-by-side to the primary axis. You can do by setting the **XAxisLayoutMode** and **YAxisLayoutMode** properties to **SideBySide**.

Here is a code sample.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                    |
|                                                                                                                                                                                                   |
| **[]**                                                                                                                                          |
|                                                                                                                                                                                                   |
| [this][.ChartWebControl1.ChartArea.XAxesLayoutMode = [ChartAxesLayoutMode].SideBySide;] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                              |
|                                                                                                                                                                                                 |
| **[]**                                                                                                                                        |
|                                                                                                                                                                                                 |
| [Me][.ChartWebControl1.ChartArea.XAxesLayoutMode = [ChartAxesLayoutMode].SideBySide;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 246: ChartControl with SideBySide Layout of Multiple Axes

**[]** 

ChartAxesLayouts

[] 

You can now combine the stacking and side-by-side chart axes layouts when multiple Axes are used, as shown in the below image. Using this feature, it is possible to position the three Y axis, as one on right side and the second one on the same side and third one on the opposite side.

[] 

{border="0"}

**[]** 

Figure 247: Combining Stacking and SideBySide Layout

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                            |
|                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                  |
|                                                                                                                                                                                                                           |
| [//Created chart axes:]                                                                                                                                                 |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                                           |
| [ChartAxis][ axis = [this].ChartWebControl1.PrimaryYAxis;]                                                      |
|                                                                                                                                                                                                                           |
| [ChartAxis][ axis0 = [new] [ChartAxis]([ChartOrientation].Vertical);] |
|                                                                                                                                                                                                                           |
| [ChartAxis][ axis1 = [new] [ChartAxis]([ChartOrientation].Vertical);] |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [//Added chart axes into the chart:]                                                                                                                                    |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                                           |
| [ChartWebControl1.Axes.Add(axis0);]                                                                                                                                                   |
|                                                                                                                                                                                                                           |
| [ChartWebControl1.Axes.Add(axis1);]                                                                                                                                                   |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [//Created chart axis layout using ChartAxisLayout class:(New class)]                                                                                                   |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                                           |
| [ChartAxisLayout][ layout1 = [new] [ChartAxisLayout]();]                                   |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [//Added the axes to this layout including the primary axis:]                                                                                                           |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                                           |
| [layout1.Axes.Add(axis);]                                                                                                                                                             |
|                                                                                                                                                                                                                           |
| [layout1.Axes.Add(axis0);]                                                                                                                                                            |
|                                                                                                                                                                                                                           |
| [layout1.Axes.Add(axis1);]                                                                                                                                                            |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [//Added the layout into ChartArea.]                                                                                                                                    |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                                           |
| [ChartWebControl1.ChartArea.YLayouts.Add(layout1);]                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                              |
|                                                                                                                                                                                                 |
| **[]**                                                                                                                                        |
|                                                                                                                                                                                                 |
| [\'Created chart axes:]                                                                                                                       |
|                                                                                                                                                                                                 |
| []                                                                                                                                            |
|                                                                                                                                                                                                 |
| [Dim][ axis [As] ChartAxis = [Me].ChartWebControl1.PrimaryYAxis] |
|                                                                                                                                                                                                 |
| [Dim][ axis0 [As] [New] ChartAxis(ChartOrientation.Vertical)]    |
|                                                                                                                                                                                                 |
| [Dim][ axis1 [As] [New] ChartAxis(ChartOrientation.Vertical)]    |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
|                                                                                                                                                                                                 |
| [\'Added chart axes into the chart:]                                                                                                          |
|                                                                                                                                                                                                 |
| []                                                                                                                                            |
|                                                                                                                                                                                                 |
| [ChartWebControl1.Axes.Add(axis0)]                                                                                                                          |
|                                                                                                                                                                                                 |
| [ChartWebControl1.Axes.Add(axis1)]                                                                                                                          |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
|                                                                                                                                                                                                 |
| [\'Created chart axis layout using ChartAxisLayout class:(New class)]                                                                         |
|                                                                                                                                                                                                 |
| []                                                                                                                                            |
|                                                                                                                                                                                                 |
| [Dim][ layout1 [As] [New] ChartAxisLayout()]                     |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
|                                                                                                                                                                                                 |
| [\'Added the axes to this layout including the primary axis:]                                                                                 |
|                                                                                                                                                                                                 |
| []                                                                                                                                            |
|                                                                                                                                                                                                 |
| [layout1.Axes.Add(axis)]                                                                                                                                    |
|                                                                                                                                                                                                 |
| [layout1.Axes.Add(axis0)]                                                                                                                                   |
|                                                                                                                                                                                                 |
| [layout1.Axes.Add(axis1)]                                                                                                                                   |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
|                                                                                                                                                                                                 |
| [\'Added the layout into ChartArea.]                                                                                                          |
|                                                                                                                                                                                                 |
| []                                                                                                                                            |
|                                                                                                                                                                                                 |
| [ChartWebControl1.ChartArea.YLayouts.Add(layout1)]                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


{border="0"}Note: All the axes with the same orientation must be added to ChartAxisLayout (PrimaryAxis as well) as illustrated in the above code snippet.


[] 

A sample which demonstrates the above feature is available in the below sample installation path.

..\\\<Install Location\>\\Syncfusion\\EssentialStudio\\\<***Version Number***\>\\Web\\chart.web\\Samples\\3.5\\Chart Axes\\MultipleAxesLayout

[]{#p179} 

[]{#related-topics}

