---
title: howtoincludeaniconinthecolumnheader.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoincludeaniconinthecolumnheader.md
created_at: 2025-07-03
---








  









### How to Include an Icon in the Column Header {#how-to-include-an-icon-in-the-column-header style="tab-stops: 0pt"}

[] 

Introduction

[] 

[The GridControl will allow you to place images in cells by specifying a style.ImageIndex and style.ImageList value for the cell provided the style.CellType is either \"Static\" or \"Text Box\". So, to make your header cell hold an icon, make it \"Static\" and set the following properties.]

[] 

Example

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                         |
| [// GridControl]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                         |
| [this][.gridControl1\[0,3\].CellType = \"Static\";\                                                                                                                                                                                                                    |
| ][this][.gridControl1\[0,3\].CellAppearance = GridCellAppearance.Raised;\                                                                                                                                            |
| ][this][.gridControl1\[0,3\].ImageList = ][this][.imageList1; ] |
|                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                         |
| [// Some imagelist defined already.]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                         |
| [// Some index in the imagelist.\                                                                                                                                                                                                                                                                                       |
| ][this][.gridControl1\[0,3\].ImageIndex = 1; ]                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                            |
|                                                                                                                                                                                               |
| []                                                                                                                                          |
|                                                                                                                                                                                               |
| [\' GridControl\                                                                                                                                                                              |
| ][Me][.gridControl1(0,3).CellType = \"Static\"\                                            |
| ][Me][.gridControl1(0,3).CellAppearance = GridCellAppearance.Raised\                       |
| ][Me][.gridControl1(0,3).ImageList = imageList\                                            |
| ][Me][.gridControl1(0,3).ImageIndex = 1] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p559} 

 

[]{#related-topics}

