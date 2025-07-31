---
title: imageasbackground.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\imageasbackground.md
created_at: 2025-07-03
---








  









### Image as Background {#image-as-background style="tab-stops: 0pt"}

The image can be displayed as chart background by passing its URL and setting the image in InteriorBackImage property.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                     |
|                                                                                                                                                                                                      |
| [System.Drawing.[Image] image = [new] [Bitmap](url);]                                       |
|                                                                                                                                                                                                      |
| [this][.olapChart1.ChartWebArea.InteriorBackImage = image;][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                           |
|                                                                                                                                                                                            |
| [Dim][ image [As] System.Drawing.Image = [New] Bitmap(url)] |
|                                                                                                                                                                                            |
| [Me.olapChart1.ChartWebArea.InteriorBackImage = image]                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

 

Figure 40: Image as background

 

Table 19: InteriorBackImageProperty

 


+-------------------------------------------+--------------------------------------------------------------------------+-------------------------------------+-------------------------------+---------------------------+
| Property                                  | Descriptions                                                             | Type                                | Data                          | Reference Link            |
|                                           |                                                                          |                                     |                               |                           |
|                                           |                                                                          |                                     | type                          |                           |
+-------------------------------------------+--------------------------------------------------------------------------+-------------------------------------+-------------------------------+---------------------------+
| InteriorBackImage[] | [The image can be set as chart area's background.] | [Server side] | [Image] | [-] |
+-------------------------------------------+--------------------------------------------------------------------------+-------------------------------------+-------------------------------+---------------------------+


 

Sample Link

A sample demo is available at the following location:

 

..\\Syncfusion\\EssentialStudio\\\<Version Number\>\\BI\\Web\\OlapChart.Web\\Samples\\3.5\\Chart Appearance\\Background Demo\\[]

[]{#related-topics}

