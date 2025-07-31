---
title: howtosetthebackgroundcolorforagrid.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\howtosetthebackgroundcolorforagrid.md
created_at: 2025-07-03
---








  









### How to Set the Background Color for a Grid {#how-to-set-the-background-color-for-a-grid style="tab-stops: 0pt"}

[] 

Introduction

[] 

To set the [backcolor] for the area of the grid populated by cells, you must set the **grid.BackColor** property to the color. The grid display may also have regions where there are no cells. These regions will be the grid\'s client area where there are no cells or scrollbars.

[] 

Example

[] 

+-----------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                      |
|                                                                                                     |
| []                                                |
|                                                                                                     |
| [// Blue]                                         |
|                                                                                                     |
| [grid.BackColor = Color.Blue;]                    |
|                                                                                                     |
| []                                                |
|                                                                                                     |
| [// Orange]                                       |
|                                                                                                     |
| [grid.Properties.BackgroundColor = Color.Orange;] |
+-----------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                 |
|                                                                                                    |
| []                                               |
|                                                                                                    |
| [\' Blue]                                        |
|                                                                                                    |
| [grid.BackColor = Color.Blue]                    |
|                                                                                                    |
| []                                               |
|                                                                                                    |
| [\' Orange]                                      |
|                                                                                                    |
| [grid.Properties.BackgroundColor = Color.Orange] |
+----------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

*[Figure ][500][: BackColor set to \"Blue\" and Properties.BackgroundColor set to \"Orange\"]*

 

[]{#p637} 

 

[]{#related-topics}

