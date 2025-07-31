---
title: howtocustomizethelayoutofmultiplegaugecontrols.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Gauge\howtocustomizethelayoutofmultiplegaugecontrols.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






    


### How to customize the layout of multiple gauge controls? {#how-to-customize-the-layout-of-multiple-gauge-controls style="tab-stops: 0pt"}

The *OLAP Gauge* control provides support to display *multiplegauges* in a structured layout. You can customize the layout by using the *ColumnsCount* and *RowsCount* properties. These properties are used to specify the number of columns and rows for displaying controls.

 

+-----------------------------------------------------------------------+
| **\[C#\]**                                                            |
|                                                                       |
|                                                                       |
|                                                                       |
| [this].olapGauge.ColumnsCount = 2;               |
|                                                                       |
| [this].olapGauge.RowsCount = 2;                  |
+-----------------------------------------------------------------------+

 

+-----------------------------------------------------------------------+
| **\[VB\]**                                                            |
|                                                                       |
|                                                                       |
|                                                                       |
| [Me].olapGauge.ColumnsCount = 2                  |
|                                                                       |
| [Me].olapGauge.RowsCount = 2                     |
+-----------------------------------------------------------------------+

 

{border="0"}

Figure 11: Multiple OLAP Gauge

Sample Location

**[]**  

A sample demo is available at the following location:

**..\\Syncfusion\\EssentialStudio\\\<Version Number\>\\BI\\WPF\\OLAPGauge.WPF\\Samples\\Product ShowCase\\Product Showcase Demo\\**

[]{#related-topics}

