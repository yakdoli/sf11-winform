---
title: chartstyleandlegends.md
original_path: WinForms_Docs/04_Controls/Chart/chartstyleandlegends.md
created_at: 2025-08-05
---






##### Chart Style and Legends   {#chart-style-and-legends style="tab-stops: 0pt"}

[] 

The Chart Appearance dialog box of the OLAP Chart provides options to set the Chart Type, Chart Color, Chart Legend Position, and Chart Legend and Legend Check Box Visibility.

The following table lists the properties and methods that are used to customize the Chart Style and Legends programmatically:

 


+-----------------------------------+---------------------------------------------------------+
| Property                          | Description                                             |
+-----------------------------------+---------------------------------------------------------+
| ChartType                         | Sets the chart type for the OLAP Chart control.         |
+-----------------------------------+---------------------------------------------------------+
| ColorModel.Palette                | Specifies the chart color for the OLAP Chart control.   |
+-----------------------------------+---------------------------------------------------------+
| Legend.Visibility                 | Specifies the visibility of the Chart Legend.           |
|                                   |                                                         |
|                                   | The options included are as follows:                    |
|                                   |                                                         |
|                                   | [·      ]Visible           |
|                                   |                                                         |
|                                   | [·      ]Collapsed         |
+-----------------------------------+---------------------------------------------------------+
| Legend.CheckBoxVisibility         | Specifies the visibility of the Chart Legend Check Box. |
|                                   |                                                         |
|                                   |                                                         |
|                                   |                                                         |
|                                   | The options included are as follows:                    |
|                                   |                                                         |
|                                   | [·      ]Visible           |
|                                   |                                                         |
|                                   | [·      ]Collapsed         |
+-----------------------------------+---------------------------------------------------------+


 


+-----------------------------------+------------------------------------------------+
| Method                            | Description                                    |
+-----------------------------------+------------------------------------------------+
| ChartDockPanel.SetDock            | Specifies the position of the Chart Legend.    |
|                                   |                                                |
|                                   |                                                |
|                                   |                                                |
|                                   | The options included are as follows:           |
|                                   |                                                |
|                                   | [·      ]Right    |
|                                   |                                                |
|                                   | [·      ]Left     |
|                                   |                                                |
|                                   | [·      ]Top      |
|                                   |                                                |
|                                   | [·      ]Bottom   |
|                                   |                                                |
|                                   | [·      ]Floating |
+-----------------------------------+------------------------------------------------+


 

The following code examples illustrate how to customize the Chart Style and Legends:

+------------------------------------------------------------------------------------------------------------------------------------------------+
| \[**C#\]**                                                                                                                                     |
|                                                                                                                                                |
| []                                                                                                                       |
|                                                                                                                                                |
| [// Set the Chart Type.]\                                                                                                |
| [this].olapchart1.ChartType = [ChartTypes].Column;\                                               |
|  \                                                                                                                                             |
| [// Set the Chart Color.]\                                                                                               |
| [this].olapchart1.ColorModel.Palette = [ChartColorPalette].Colorful;\                             |
|  \                                                                                                                                             |
| [// Set the Chart Legend and Legend Check Box Visibility.]\                                                              |
| [this].olapchart1.Legend.Visibility = [Visibility].Visible;\                                      |
| [this].olapchart1.Legend.Visibility = [Visibility].Collapsed;\                                    |
| [this].olapchart1.Legend.CheckBoxVisibility = [Visibility].Visible;\                              |
| [this].olapchart1.Legend.CheckBoxVisibility = [Visibility].Collapsed;\                            |
|  \                                                                                                                                             |
| [// Set the Chart Legend Position.]\                                                                                     |
| [ChartDockPanel].SetDock([this].olapchart1.Legend, [ChartDock].Right);\   |
| [ChartDockPanel].SetDock([this].olapchart1.Legend, [ChartDock].Left);\    |
| [ChartDockPanel].SetDock([this].olapchart1.Legend, [ChartDock].Top);\     |
| [ChartDockPanel].SetDock([this].olapchart1.Legend, [ChartDock].Bottom);\  |
| [ChartDockPanel].SetDock([this].olapchart1.Legend, [ChartDock].Floating); |
+------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------+
| **\[VB\]**                                                                                                                                  |
|                                                                                                                                             |
| []                                                                                                                    |
|                                                                                                                                             |
| [\' Set the Chart Type.]\                                                                                             |
| [Me].olapchart1.ChartType = [ChartTypes].Column\                                               |
|  \                                                                                                                                          |
| [\' Set the Chart Series Color.]\                                                                                     |
| [Me].olapchart1.ColorModel.Palette = [ChartColorPalette].Colorful\                             |
|  \                                                                                                                                          |
| [\' Set the Chart Legend and Legend Check Box Visibility.]\                                                           |
| [Me].olapchart1.Legend.Visibility = Visibility.Visible\                                                                |
| [Me].olapchart1.Legend.Visibility = Visibility.Collapsed\                                                              |
| [Me].olapchart1.Legend.CheckBoxVisibility = Visibility.Visible\                                                        |
| [Me].olapchart1.Legend.CheckBoxVisibility = Visibility.Collapsed\                                                      |
|  \                                                                                                                                          |
| [\' Set the Chart Legend Position.]\                                                                                  |
| [ChartDockPanel].SetDock([Me].olapchart1.Legend, [ChartDock].Right)\   |
| [ChartDockPanel].SetDock([Me].olapchart1.Legend, [ChartDock].Left)\    |
| [ChartDockPanel].SetDock([Me].olapchart1.Legend, [ChartDock].Top)\     |
| [ChartDockPanel].SetDock([Me].olapchart1.Legend, [ChartDock].Bottom)\  |
| [ChartDockPanel].SetDock([Me].olapchart1.Legend, [ChartDock].Floating) |
+---------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 65: Customizing the Chart Style and Legends[]

A sample, which demonstrates all the appearance properties, is available in the following installation location:

**..\\Syncfusion\\\<Version Number\>\\BI\\WPF\\OlapChart.WPF\\Samples\\Chart Appearance**

[] 

[]{#related-topics}

