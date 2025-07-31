---
title: howtogetbacktothegradientappearanceofthechartseries.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\howtogetbacktothegradientappearanceofthechartseries.md
created_at: 2025-07-03
---








  









## How to get back to the gradient appearance of the Chart Series? {#how-to-get-back-to-the-gradient-appearance-of-the-chart-series style="tab-stops: 0pt"}

[] 

The default appearance of the chart series is as shown in the image below.

[] 

{border="0"}

**[]** 

Figure 324: Chart with Flat Look and Feel

[] 

To get the gradient appearance, we need to set the **ChartControl.Model.ColorModel.AllowGradient** to **true**. By default this is set to **false**.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                               |
|                                                                                                                                                                              |
| **[]**                                                                                                                     |
|                                                                                                                                                                              |
| [//Sets the Gradient look and feel.]                                                                                       |
|                                                                                                                                                                              |
| [this][.ChartWebControl1.Model.ColorModel.AllowGradient = [true];] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                        |
|                                                                                                                                                                           |
| **[]**                                                                                                                  |
|                                                                                                                                                                           |
| [\'Sets the Gradient look and feel.]                                                                                    |
|                                                                                                                                                                           |
| [Me][.ChartWebControl1.Model.ColorModel.AllowGradient = [True]] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

**[]** 

Figure 325Chart with Gradient Look and Feel

**[]** 


 

{border="0"}Note: We can also use ChartControl.AllowGradientPalette property to enable or disable gradient effect for chart series. By default it set to false.


[]{#p281} 

[]{#related-topics}

