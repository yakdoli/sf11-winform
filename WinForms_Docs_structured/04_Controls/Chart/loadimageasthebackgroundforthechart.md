---
title: loadimageasthebackgroundforthechart.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\loadimageasthebackgroundforthechart.md
created_at: 2025-07-03
---








  









## Load Image as the Background for the Chart? {#load-image-as-the-background-for-the-chart style="tab-stops: 0pt"}

 

The image can be displayed as chart background by passing its URL and setting the image in InteriorBackImage property.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                               |
|                                                                                                                                                                                                      |
| [System.Drawing.[Image] image = [new] [Bitmap](url);]                                       |
|                                                                                                                                                                                                      |
| [this][.olapChart1.ChartWebArea.InteriorBackImage = image;][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**[]                                                                                                     |
|                                                                                                                                                                                            |
| [Dim][ image [As] System.Drawing.Image = [New] Bitmap(url)] |
|                                                                                                                                                                                            |
| [Me.olapChart1.ChartWebArea.InteriorBackImage = image]                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

 

Figure 64: Image as background

[]{#related-topics}

