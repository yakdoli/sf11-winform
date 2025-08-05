---
title: chartborderandbackgroundstyle.md
original_path: WinForms_Docs/04_Controls/Chart/chartborderandbackgroundstyle.md
created_at: 2025-08-05
---






##### Chart Border and Background Style {#chart-border-and-background-style style="tab-stops: 0pt"}

[] 

The Chart Appearance dialog box of the OLAP Chart also provides options to set the Chart Border and the Background Style.

The following table lists the properties that are used to customize the Chart Border and the Background Style programmatically:

 


  ----------------- ---------------------------------------------------------------------
  Property          Description
  BorderThickness   Sets the border thickness for the OLAP Chart control.
  BorderBrush       Specifies the border color for the OLAP Chart control.
  Background        Specifies the background color for the OLAP Chart control.
  GridBackground    Specifies the interior background color for the OLAP Chart control.
  ----------------- ---------------------------------------------------------------------


 

The following code examples illustrate how to customize the Chart Border and the Background Style:

 

+-----------------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                                  |
|                                                                                                                             |
| [// Set the Chart Border Style.]                                                                      |
|                                                                                                                             |
| [this].olapchart1.BorderThickness = [new] [Thickness](2); |
|                                                                                                                             |
| [this].olapchart1.BorderBrush = [Brushes].Blue;                                |
|                                                                                                                             |
|                                                                                                                             |
|                                                                                                                             |
| [// Set the Chart Background Style.]                                                                  |
|                                                                                                                             |
| [this].olapchart1.Background = [Brushes].LightBlue;                            |
|                                                                                                                             |
| [this].olapchart1.GridBackground = [Brushes].LightGray;                        |
+-----------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------+
| **\[VB\]**                                                                                                                |
|                                                                                                                           |
| [\' Set the Chart Border Style.]\                                                                   |
| [Me].olapchart1.BorderThickness = [New] [Thickness](2)\ |
| [Me].olapchart1.BorderBrush = [Brushes].Blue\                                |
|  \                                                                                                                        |
| [\' Set the Chart Background Style.]\                                                               |
| [Me].olapchart1.Background = [Brushes].LightBlue\                            |
| [Me].olapchart1.GridBackground = [Brushes].LightGray                         |
+---------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

 

Figure 66: Customizing the Chart Border and the Background Style[]

A sample, which demonstrates all the appearance properties, is available in the following installation location:

**..\\Syncfusion\\\<Version Number\>\\BI\\WPF\\OlapChart.WPF\\Samples\\Chart Appearance**

[] 

[]{#related-topics}

