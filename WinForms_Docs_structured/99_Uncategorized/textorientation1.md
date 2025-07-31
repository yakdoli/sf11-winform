---
title: textorientation1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\textorientation1.md
created_at: 2025-07-03
---






#### TextOrientation {#textorientation style="tab-stops: 0pt"}

 

It is used to align the text of the series within the data point region.

 


+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                |
|                                                                                                                                                                |
| Details                                                                                                                                                        |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| **Possible Values**                 | [·      ]**Center** - Aligns to the center of the point.                                    |
|                                     |                                                                                                                          |
|                                     | [·      ]**Down** - Aligns below the point.                                                 |
|                                     |                                                                                                                          |
|                                     | [·      ]**Left** - Aligns to the left position to the point.                               |
|                                     |                                                                                                                          |
|                                     | [·      ]**RegionCenter** - Aligns below the region that represents the points.             |
|                                     |                                                                                                                          |
|                                     | [·      ]**RegionDown** - Aligns below the region that represents the points.               |
|                                     |                                                                                                                          |
|                                     | [·      ]**RegionUp** - Aligns to the top of the region that represents the points.         |
|                                     |                                                                                                                          |
|                                     | [·      ]**Right** - Aligns to the right of the point.                                      |
|                                     |                                                                                                                          |
|                                     | [·      ]**Smart** - Aligns in a manner that is appropriate to the situation.               |
|                                     |                                                                                                                          |
|                                     | [·      ]**SymbolCenter** - Text is centered to the symbol that is associated to the point. |
|                                     |                                                                                                                          |
|                                     | [·      ]**Up** - Aligns to the top of the point.                                           |
|                                     |                                                                                                                          |
|                                     | [·      ]**UpLeft** - Aligns to the top left corner of the point.                           |
|                                     |                                                                                                                          |
|                                     | [·      ]**UpRight** - Aligns to the top right corner of the point.                         |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| **Default Value    **               | **Up**                                                                                                                   |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| **2D / 3D Limitations**             | No                                                                                                                       |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| **Applies to Chart Element**        | Any Series                                                                                                               |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| **Applies to Chart Types**          | All chart types                                                                                                          |
+-------------------------------------+--------------------------------------------------------------------------------------------------------------------------+


 

Here is some sample code.

 

Series Wide Setting

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                       |
| [// Text Orientation of chart series]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                       |
| [this][.chartControl1.Series\[1\].Style.TextOrientation = ][ChartTextOrientation][.RegionDown;] |
|                                                                                                                                                                                                                                                                                                       |
| [this][.chartControl1.Series\[0\].Style.TextOrientation = ][ChartTextOrientation][.Up;]         |
|                                                                                                                                                                                                                                                                                                       |
| [this][.chartControl1.Series\[0\].Style.TextColor=][Color][.Blue;]                              |
|                                                                                                                                                                                                                                                                                                       |
| [this][.chartControl1.Series\[1\].Style.TextColor=][Color][.Red;]                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                          |
| [\' Text Orientation of chart series]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                          |
| [Private Me][.chartControl1.Series(1).Style.TextOrientation = ][ChartTextOrientation][.RegionDown] |
|                                                                                                                                                                                                                                                                                                          |
| [Private Me][.chartControl1.Series(0).Style.TextOrientation = ][ChartTextOrientation][.Up]         |
|                                                                                                                                                                                                                                                                                                          |
| [Private Me][.chartControl1.Series(0).Style.TextColor=][Color][.Blue]                              |
|                                                                                                                                                                                                                                                                                                          |
| [Private Me][.chartControl1.Series(1).Style.TextColor=][Color][.Red]                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

 

Figure 222: Text Orientation set for the Chart Series

 

Specific Data Point Setting

**[]** 

Text orientation for specific data points can be set using **Series.Style\[i\].TextOrientation** property, where \"i\" represents the index of data points ranging from 0 to n.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                             |
| [this][.chartControl1.Series\[1\].Styles\[0\].TextOrientation = ][ChartTextOrientation][.RegionDown;] |
|                                                                                                                                                                                                                                                                                                             |
| [this][.chartControl1.Series\[0\].Styles\[0\].TextOrientation = ][ChartTextOrientation][.Up;]         |
|                                                                                                                                                                                                                                                                                                             |
| [this][.chartControl1.Series\[0\].Styles\[0\].TextColor=][Color][.Blue;]                              |
|                                                                                                                                                                                                                                                                                                             |
| [this][.chartControl1.Series\[1\].Styles\[0\].TextColor=][Color][.Red;]                               |
|                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                             |
| [this][.chartControl1.Series\[1\].Styles\[1\].TextOrientation = ][ChartTextOrientation][.Smart;]      |
|                                                                                                                                                                                                                                                                                                             |
| [this][.chartControl1.Series\[0\].Styles\[1\].TextOrientation = ][ChartTextOrientation][.UpRight;]    |
|                                                                                                                                                                                                                                                                                                             |
| [this][.chartControl1.Series\[0\].Styles\[1\].TextColor=][Color][.Green;]                             |
|                                                                                                                                                                                                                                                                                                             |
| [this][.chartControl1.Series\[1\].Styles\[1\].TextColor=][Color][.Yellow;]                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                              |
| [Private Me][.chartControl1.Series(1).Styles(0).TextOrientation = ][ChartTextOrientation][.RegionDown] |
|                                                                                                                                                                                                                                                                                                              |
| [Private Me][.chartControl1.Series(0).Styles(0).TextOrientation = ][ChartTextOrientation][.Up]         |
|                                                                                                                                                                                                                                                                                                              |
| [Private Me][.chartControl1.Series(0).Styles(0).TextColor=][Color][.Blue]                              |
|                                                                                                                                                                                                                                                                                                              |
| [Private Me][.chartControl1.Series(1).Styles(0).TextColor=][Color][.Red]                               |
|                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                              |
| [Private Me][.chartControl1.Series(1).Styles(1).TextOrientation = ][ChartTextOrientation][.Smart]      |
|                                                                                                                                                                                                                                                                                                              |
| [Private Me][.chartControl1.Series(0).Styles(1).TextOrientation = ][ChartTextOrientation][.UpRight]    |
|                                                                                                                                                                                                                                                                                                              |
| [Private Me][.chartControl1.Series(0).Styles(1).TextColor=][Color][.Green]                             |
|                                                                                                                                                                                                                                                                                                              |
| [Private Me][.chartControl1.Series(1).Styles(1).TextColor=][Color][.Yellow]                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

See Also

[[]]{.UGHyperlink}

[[Chart Types]]{.UGHyperlink}

 

[]{#p162} 

 

[]{#related-topics}

