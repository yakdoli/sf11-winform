---
title: slider2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\slider2.md
created_at: 2025-07-03
---






##### Slider {#slider style="tab-stops: 0pt"}

[] 

You can use slider cells in grid cells. You can also share a single Slider control among multiple cells. To set the slider properties for a cell, make use of the **SliderStyleProperties** object.

 

The following code example illustrates how to set the cell type to Slider.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                            |
|                                                                                                                                                                                                           |
| []                                                                                                                                                      |
|                                                                                                                                                                                                           |
| [// Set up a Slider control.]                                                                                                                           |
|                                                                                                                                                                                                           |
| [GridStyleInfo][ style = gridControl1\[row, 3\];]                                                                 |
|                                                                                                                                                                                                           |
| [SliderStyleProperties][ sp = [new] [SliderStyleProperties](style);] |
|                                                                                                                                                                                                           |
| [style.CellType = [\"Slider\"];]                                                                                                              |
|                                                                                                                                                                                                           |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                           |
| [// Set Slider Properties.]                                                                                                                             |
|                                                                                                                                                                                                           |
| [sp.Maximum = 40;]                                                                                                                                                    |
|                                                                                                                                                                                                           |
| [sp.Minimum = 0;]                                                                                                                                                     |
|                                                                                                                                                                                                           |
| [sp.TickFrequency = 8;]                                                                                                                                               |
|                                                                                                                                                                                                           |
| [sp.LargeChange = 16;]                                                                                                                                                |
|                                                                                                                                                                                                           |
| [sp.SmallChange = 4;]                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                        |
|                                                                                                                                                                                                           |
| []                                                                                                                                                      |
|                                                                                                                                                                                                           |
| [\' Set up a Slider control.]                                                                                                                           |
|                                                                                                                                                                                                           |
| [Dim][ style [As] GridStyleInfo = gridControl1(row, 3)]                                         |
|                                                                                                                                                                                                           |
| [Dim][ sp [As] SliderStyleProperties = [New] SliderStyleProperties(style)] |
|                                                                                                                                                                                                           |
| [style.CellType = [\"Slider\"]]                                                                                                               |
|                                                                                                                                                                                                           |
| []                                                                                                                                                    |
|                                                                                                                                                                                                           |
| [\' Set Slider Properties.]                                                                                                                             |
|                                                                                                                                                                                                           |
| [sp.Maximum = 40]                                                                                                                                                     |
|                                                                                                                                                                                                           |
| [sp.Minimum = 0]                                                                                                                                                      |
|                                                                                                                                                                                                           |
| [sp.TickFrequency = 8]                                                                                                                                                |
|                                                                                                                                                                                                           |
| [sp.LargeChange = 16]                                                                                                                                                 |
|                                                                                                                                                                                                           |
| [sp.SmallChange = 4]                                                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

*[Figure ][89][: Slider Cells]*

 

[]{#p65} 

 

[]{#related-topics}

