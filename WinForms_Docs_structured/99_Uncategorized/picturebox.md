---
title: picturebox.md
original_path: WinForms_Docs/99_Uncategorized/picturebox.md
created_at: 2025-08-05
---






##### Picture Box {#picture-box style="tab-stops: 0pt"}

[] 

The Picture Box cell type can be embedded into a cell by calculating the size of the picture, and extending the width and height of the cell accordingly. The **PictureBoxStyleProperties** class provides the style where it holds the information of the picture that has to be added.

 

The following code examples illustrate how to set the cell type to PictureBox.

[] 

1.   Using C#

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                  |
|                                                                                                                                                                                                 |
| []                                                                                                                                            |
|                                                                                                                                                                                                 |
| [RegisterCellModel][.GridCellType(gridControl1, [CustomCellTypes].PictureBox);] |
|                                                                                                                                                                                                 |
| [PictureBoxStyleProperties][ sp;]                                                                       |
|                                                                                                                                                                                                 |
| [style = gridControl1\[2, 2\];]                                                                                                                             |
|                                                                                                                                                                                                 |
| [style.CellType = [CustomCellTypes].PictureBox.ToString();]                                                                         |
|                                                                                                                                                                                                 |
| [sp = [new] [PictureBoxStyleProperties](style);]                                                               |
|                                                                                                                                                                                                 |
| [sp.Image = GetImage([\"one.jpg\"]);]                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                  |
|                                                                                                                                                     |
| []                                                                                                |
|                                                                                                                                                     |
| [RegisterCellModel.GridCellType([Me].gridControl1, CustomCellTypes.PictureBox)]            |
|                                                                                                                                                     |
| [Dim][ sp [As] PictureBoxStyleProperties] |
|                                                                                                                                                     |
| [style = gridControl1(2, 2)]                                                                                    |
|                                                                                                                                                     |
| [style.CellType = CustomCellTypes.PictureBox.ToString()]                                                        |
|                                                                                                                                                     |
| [sp = [New] PictureBoxStyleProperties(style)]                                              |
|                                                                                                                                                     |
| [sp.Image = GetImage([\"one.jpg\"])]                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[{border="0"}][]

[] 

*[Figure ][112][: Picture Box Cell]*

 

[]{#p101} 

 

[]{#related-topics}

