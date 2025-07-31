---
title: watermarksupport7.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\watermarksupport7.md
created_at: 2025-07-03
---








  









### Watermark Support {#watermark-support style="tab-stops: 0pt"}

 

Essential Chart supports watermark feature using which we can show text, image, or both as watermark inside the chart area.

 

Below are the WaterMark properties with descriptions.

 


  -------------------- ------------------------------------------------------------------------
  ChartAxis Property   Description
  Text                 Sets the watermark text.
  Image                Used to display image as the watermark.
  Opacity              Sets the opacity of the watermark.
  HorizontalAlign      Sets watermark horizontally in the chart area.
  VerticalAlign        Sets watermark vertically in the chart area.
  Zorder               Used to specify whether watermark should be shown on top of the chart.
  -------------------- ------------------------------------------------------------------------


 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                         |
| [this][.chartControl1.ChartArea.WaterMark.Text=\"Syncfusion Chart\";]                                                                |
|                                                                                                                                                                                                                                         |
| [this][.chartControl1.ChartArea.Watermark.Image = System.Drawing.Image.FromFile(\"Logo.bmp\"); ]                                     |
|                                                                                                                                                                                                                                         |
| [this][.chartControl1.ChartArea.Watermark.Opacity=60;]                                                                               |
|                                                                                                                                                                                                                                         |
| [this][.chartControl1.ChartArea.Watermark.HorizontalAlignment=ChartAlignment.Near\                                                                                                     |
| ][this][.chartControl1.ChartArea.Watermark.VerticalAlignment=ChartAlignment.Near;] |
|                                                                                                                                                                                                                                         |
| [this][.chartControl1.ChartArea.Watermark.ZOrder=ChartWaterMarkOrder.Behind;]                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                   |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                      |
| [Me][.chartControl1.ChartArea.WaterMark.Text=\"Syncfusion Chart\"]                                                                |
|                                                                                                                                                                                                                                      |
| [Me][.chartControl1.ChartArea.Watermark.Image = System.Drawing.Image.FromFile(\"Logo.bmp\")]                                      |
|                                                                                                                                                                                                                                      |
| [Me][.chartControl1.ChartArea.Watermark.Opacity=60]                                                                               |
|                                                                                                                                                                                                                                      |
| [Me][.chartControl1.ChartArea.Watermark.HorizontalAlignment=ChartAlignment.Near\                                                                                                    |
| ][Me][.chartControl1.ChartArea.Watermark.VerticalAlignment=ChartAlignment.Near] |
|                                                                                                                                                                                                                                      |
| [Me][.chartControl1.ChartArea.Watermark.ZOrder=ChartWaterMarkOrder.Behind;]                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 326: \"Image\" displayed as Watermark; Opacity = \"60\"; HorizontalAlignment = \"Near\"; VerticalAlignment = \"Near\"; ZOrder = \"Behind\"

[]{#p212} 

[]{#related-topics}

