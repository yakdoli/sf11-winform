---
title: settingtheexteriorappearanceofchart.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\settingtheexteriorappearanceofchart.md
created_at: 2025-07-03
---








  









### Setting the Exterior Appearance of Chart {#setting-the-exterior-appearance-of-chart style="tab-stops: 0pt"}

 

The BackInterior property sets the appearance as well as gradient style of the exterior portion of the chart.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                              |
| [this][.olapChart1.BackInterior = [new] Syncfusion.Drawing.[BrushInfo](Syncfusion.Drawing.[GradientStyle].Vertical, System.Drawing.[Color].White, System.Drawing.[Color].FromArgb(85, 142, 213));] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                       |
| [Me][.olapChart1.BackInterior = [New] Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.Vertical, System.Drawing.Color.White, System.Drawing.Color.FromArgb(85, 142, 213))][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

 

Figure 39: Exterior Style

 

Table 18: BackInterior Property

 


+--------------+---------------------------------------------------+-------------+-------------+----------------+
| Property     | Descriptions                                      | Type        | Data        | Reference Link |
|              |                                                   |             |             |                |
|              |                                                   |             | type        |                |
+--------------+---------------------------------------------------+-------------+-------------+----------------+
| BackInterior | Specifies the exterior style of the chart region. | Server side | BrushInfo   | \-             |
+--------------+---------------------------------------------------+-------------+-------------+----------------+


 

Sample Link

A sample demo is available at the following location:

 

..\\Syncfusion\\EssentialStudio\\\<Version Number\>\\BI\\Web\\OlapChart.Web\\Samples\\3.5\\Chart Appearance\\Background Demo\\[]

[]{#related-topics}

