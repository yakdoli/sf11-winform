---
title: bubbletype.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\bubbletype.md
created_at: 2025-07-03
---






#### BubbleType {#bubbletype style="tab-stops: 0pt"}

**[]** 

**BubbleType -** Specifies whether to render the data point symbols as circle, square or as image.

[] 


+-------------------------------------+------------------------------------------+
|                                                                                |
|                                                                                |
| Details                                                                        |
+-------------------------------------+------------------------------------------+
| Possible Values                     | Circle - Symbol is rendered as a circle\ |
|                                     | Square - Symbol is rendered as a square  |
|                                     |                                          |
|                                     | Image - Symbol is rendered as an image   |
+-------------------------------------+------------------------------------------+
| Default Value                       | Circle                                   |
+-------------------------------------+------------------------------------------+
| 2D / 3D Limitations                 | No                                       |
+-------------------------------------+------------------------------------------+
| Applies to Chart Element            | All Series                               |
+-------------------------------------+------------------------------------------+
| Applies to Chart Types              | Bubble                                   |
+-------------------------------------+------------------------------------------+


**[]** 

Here is some sample code to specify an Image BubbleType.

[] 

Series wide setting

**[]** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                   |
| [this][.ChartWebControl1.Series\[0\].ConfigItems.BubbleItem.BubbleType = ChartBubbleType.Image;]                                                                             |
|                                                                                                                                                                                                                                                                   |
| [this][.ChartWebControl1.Series\[0\].Style.Images = [new] [ChartImageCollection]([this].imageList1.Images );] |
|                                                                                                                                                                                                                                                                   |
| [this][.ChartWebControl1.Series\[0\].Style.ImageIndex = 0;]                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                   |
|                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                             |
|                                                                                                                                                                                                                                      |
| [Me][.ChartWebControl1.Series\[0\].ConfigItems.BubbleItem.BubbleType = ChartBubbleType.Image]                                                   |
|                                                                                                                                                                                                                                      |
| [Me][.ChartWebControl1.Series\[0\].Style.Images = [New] ChartImageCollection([Me].imageList1.Images)] |
|                                                                                                                                                                                                                                      |
| [Me][.ChartWebControl1.Series\[0\].Style.ImageIndex = 0]                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Specific Data Point Setting

**[]** 

Specify image for specific data points.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                         |
| [this][.ChartWebControl1.Series\[0\].Styles\[0\].Images = [new] [ChartImageCollection]([this].imageList1.Images );] |
|                                                                                                                                                                                                                                                                         |
| [this][.ChartWebControl1.Series\[0\].Styles\[0\].ImageIndex = 0;]                                                                                                                  |
|                                                                                                                                                                                                                                                                         |
| [this][.ChartWebControl1.Series\[0\].Styles\[1\].Images = [new] [ChartImageCollection]([this].imageList1.Images );] |
|                                                                                                                                                                                                                                                                         |
| [this][.ChartWebControl1.Series\[0\].Styles\[1\].ImageIndex = 1;]                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                       |
|                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                          |
| [Me][.ChartWebControl1.Series\[0\].Styles(0).Images = [New] ChartImageCollection([Me].imageList1.Images)] |
|                                                                                                                                                                                                                                          |
| [Me][.ChartWebControl1.Series\[0\].Styles\[0).ImageIndex = 0]                                                                                       |
|                                                                                                                                                                                                                                          |
| [Me][.ChartWebControl1.Series\[0\].Styles(1).Images = [New] ChartImageCollection([Me].imageList1.Images)] |
|                                                                                                                                                                                                                                          |
| [Me][.ChartWebControl1.Series\[0\].Styles(1).ImageIndex = 1]                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

**[]** 

Figure 97: Image BubbleType Chart Series

**[]** 

See Also

[] 

[]{.UGHyperlink}

[]{#p82} 

[]{#related-topics}

