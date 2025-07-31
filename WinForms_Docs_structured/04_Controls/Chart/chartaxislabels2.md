---
title: chartaxislabels2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\chartaxislabels2.md
created_at: 2025-07-03
---






##### Chart Axis Labels {#chart-axis-labels style="tab-stops: 0pt"}

[] 

The Appearance dialog box enables you to customize the Labels of the Primary and the Secondary Axes.

###### 1.6.1.11.4.1        Customizing the Font Style of the Primary Axis {#customizing-the-font-style-of-the-primary-axis style="tab-stops: 0pt"}

 

OLAP Chart provides support to dynamically change the Font Family, Font Color, and Font Weight for the Labels of the Primary Axis.

 


  ----------------------------- --------------------------------------------------------------
  Property                      Description
  PrimaryAxis.LabelFontFamily   Specifies the font family for the label of the Primary Axis.
  PrimaryAxis.LabelForeground   Specifies the font color for the label of the Primary Axis.
  PrimaryAxis.LabelFontWeight   Specifies the font weight for the label of the Primary Axis.
  ----------------------------- --------------------------------------------------------------


 

The following code examples illustrate how to customize the font style of the Primary Axis:

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                                                                                  |
|                                                                                                                                                                             |
| [// Set the Font Family.]\                                                                                                                            |
| [this].olapchart1.PrimaryAxis.LabelFontFamily = [new] [FontFamily]([\"Arial\"]);\ |
|  \                                                                                                                                                                          |
| [// Set the Font Color.]\                                                                                                                             |
| [this].olapchart1.PrimaryAxis.LabelForeground = [Brushes].LightGray;\                                                          |
|  \                                                                                                                                                                          |
| [// Set the Font Weight.]\                                                                                                                            |
| [this].olapchart1.PrimaryAxis.LabelFontWeight = [FontWeights].Bold;                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[VB\]**                                                                                                                                                               |
|                                                                                                                                                                          |
| [\' Set the Font Family.]\                                                                                                                         |
| [Me].olapchart1.PrimaryAxis.LabelFontFamily = [New] [FontFamily]([\"Arial\"])\ |
|  \                                                                                                                                                                       |
| [\' Set the Font Color.]\                                                                                                                          |
| [Me].olapchart1.PrimaryAxis.LabelForeground = [Brushes].LightGray\                                                          |
|  \                                                                                                                                                                       |
| [\' Set the Font Weight.]\                                                                                                                         |
| [Me].olapchart1.PrimaryAxis.LabelFontWeight = [FontWeights].Bold                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

###### 1.6.1.11.4.2        Customizing the Font Style of the Secondary Axis {#customizing-the-font-style-of-the-secondary-axis style="tab-stops: 0pt"}

 

OLAP Chart provides support to dynamically change the Font Family, Font Color, and Font Weight for the Labels of the Secondary Axis.

 


  ----------------------------- ----------------------------------------------------------------
  Property                      Description
  PrimaryAxis.LabelFontFamily   Specifies the font family for the label of the Secondary Axis.
  PrimaryAxis.LabelForeground   Specifies the font color for the label of the Secondary Axis.
  PrimaryAxis.LabelFontWeight   Specifies the font weight for the label of the Secondary Axis.
  ----------------------------- ----------------------------------------------------------------


 

The following code examples illustrate how to customize the font style of the Secondary Axis:

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                                                                                    |
|                                                                                                                                                                               |
| [// Set the Font Family.]\                                                                                                                              |
| [this].olapchart1.SecondaryAxis.LabelFontFamily = [new] [FontFamily]([\"Arial\"]);\ |
|  \                                                                                                                                                                            |
| [// Set the Foreground Color.]\                                                                                                                         |
| [this].olapchart1.SecondaryAxis.LabelForeground = [Brushes].LightGray;\                                                          |
|  \                                                                                                                                                                            |
| [// Set the Font Weight.]\                                                                                                                              |
| [this].olapchart1.SecondaryAxis.LabelFontWeight = [FontWeights].Bold;                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[VB\]**                                                                                                                                                                 |
|                                                                                                                                                                            |
| [\' Set the Font Family.]\                                                                                                                           |
| [Me].olapchart1.SecondaryAxis.LabelFontFamily = [New] [FontFamily]([\"Arial\"])\ |
|  \                                                                                                                                                                         |
| [\' Set the Foreground Color.]\                                                                                                                      |
| [Me].olapchart1.SecondaryAxis.LabelForeground = [Brushes].LightGray\                                                          |
|  \                                                                                                                                                                         |
| [\' Set the Font Weight.]\                                                                                                                           |
| [Me].olapchart1.SecondaryAxis.LabelFontWeight = [FontWeights].Bold                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

 

Figure 67: Customizing the Chart Axis Labels[]

[] 

A sample, which demonstrates all the appearance properties, is available in the following installation location:

**..\\Syncfusion\\\<Version Number\>\\BI\\WPF\\OlapChart.WPF\\Samples\\Chart Appearance**

[] 

[]{#related-topics}

