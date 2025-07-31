---
title: howtosetthewidthofacolumn1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtosetthewidthofacolumn1.md
created_at: 2025-07-03
---








  









### How to Set the Width of a Column {#how-to-set-the-width-of-a-column style="tab-stops: 0pt"}

[] 

Introduction

[] 

In order to change the width of the columns in the **GridDataBoundGrid**, you must do the following.

[] 

[·      ]Set the property **grid.AllowResizeToFit** to False. This can be done once in the forms constructor or Form.Load event. It  will turn off the grids default sizing behavior so that your explicit sizing will work. Otherwise, the default sizing will take precedence. The default sizing uses the width of the header text to size the columns.

 

[·      ]Then, explicitly set the width of the particular columns by using the **Model.ColWidths** collection.

[] 

Example

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                    |
| [// Set size of column 3 to 250.\                                                                                                                                                                                                                                                                                  |
| ][this][.gridDataBoundGrid1.AllowResizeToFit = ][false][;] |
|                                                                                                                                                                                                                                                                                                                    |
| [this][.gridDataBoundGrid1.Model.ColWidths\[3\] = 250; ]                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                             |
| [\' Set size of column 3 to 250.\                                                                                                                                                                                                                           |
| ][Me][.GridDataBoundGrid1.AllowResizeToFit = ][False] |
|                                                                                                                                                                                                                                                             |
| [Me][.GridDataBoundGrid1.Model.ColWidths(3) = 250 ]                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p599} 

 

[]{#related-topics}

