---
title: backgroundimage.md
original_path: WinForms_Docs/99_Uncategorized/backgroundimage.md
created_at: 2025-08-05
---








  









### Background Image {#background-image style="tab-stops: 0pt"}

[] 

Chart Settings

[] 

Use the **ChartAreaBackImage** property to specify a custom image as the background of the chart.

[] 


  ---------------------------- -----------------------------------------------------------------------------
  ChartWebControl Properties   Description
  ChartAreaBackImage           Indicates the background image of the chart area. This specifies the image.
  ---------------------------- -----------------------------------------------------------------------------


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                    |
|                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                          |
|                                                                                                                                                                                                                   |
| [string][ url = Page.MapPath(Page.AppRelativeTemplateSourceDirectory) + [\"Images\\\\Winter.jpg\"];] |
|                                                                                                                                                                                                                   |
| [System.Drawing.[Image] image = [new] Bitmap(url);]                                                                              |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                   |
| [this][.ChartWebControl1.ChartAreaBackImage = image;]                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                           |
|                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                              |
| [Dim][ url [As] String = Page.MapPath(Page.AppRelativeTemplateSourceDirectory) & [\"Images\\Winter.jpg\"]] |
|                                                                                                                                                                                                                                              |
| [Dim][ image [As] System.Drawing.Image = New Bitmap(url)]                                                                          |
|                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                              |
| [Me][.ChartWebControl1.ChartAreaBackImage = image]                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

**[]** 

Figure 298: Background Image set for the Chart

**[]** 

Chart Interior Background Image

**[]** 

Chart Interior can be rendered with a custom background image using the **ChartInteriorBackImage** property.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                         |
|                                                                                                                                                        |
| **[]**                                                                                               |
|                                                                                                                                                        |
| [this][.ChartWebControl1.ChartInteriorBackImage = myCustomImage;] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                  |
|                                                                                                                                                     |
| **[]**                                                                                            |
|                                                                                                                                                     |
| [Me][.ChartWebControl1.ChartInteriorBackImage = myCustomImage] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

***[]*** 

Background Image set for the Chart Interior

**[]** 

A sample which demonstrates this feature is available in the below sample installation path.

\<Install location\>\\Syncfusion\\EssentialStudio\\***Version Number***\\Web\\chart.web\\Samples\\3.5\\Chart Appearance\\ChartBackGroundSample

[]{#p207} 

[]{#related-topics}

