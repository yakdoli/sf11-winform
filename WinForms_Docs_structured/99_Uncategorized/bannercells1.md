---
title: bannercells1.md
original_path: WinForms_Docs/99_Uncategorized/bannercells1.md
created_at: 2025-08-05
---






#### Banner Cells {#banner-cells style="tab-stops: 0pt"}

[] 

Banner cells are multiple cells spanning a single background image. An image to be displayed in the cell can be loaded on disk, by changing the **BackgroundImage** property for a cell in the **Property Grid** and applying a Banner for the cell area, displaying the image. For a cell background color, **Gradient** style can be set. Custom cell backgrounds can be drawn by handling the **DrawCellBackground** event. The Banner cells can also be defined through a recurring pattern, by handling **QueryBanneredRange** event.

 

The following screen shot shows an example of how multiple cells span a single background image to form banner cells.

[] 

{border="0"}

[] 

*[Figure ][187][: Banner Cells]*

[] 

Displaying Image using Banner Cells

[] 

The following code examples illustrate how to display images by using banner cells:

[] 

1.   Using C#

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                       |
|                                                                                                                                                      |
| []                                                                                                 |
|                                                                                                                                                      |
| [GridStyleInfo][ style;]                                     |
|                                                                                                                                                      |
| [style = grid\[4, 3\];]                                                                                          |
|                                                                                                                                                      |
| [grid.BanneredRanges.Add([GridRangeInfo].FromTlhw(4, 3, 8, 3));]                         |
|                                                                                                                                                      |
| [style.BackgroundImage = GetImage([@\"common\\Images\\Grid\\BannerCells\\back1.jpg\"]);] |
|                                                                                                                                                      |
| [style.Text = [\"back1.jpg\"];]                                                          |
|                                                                                                                                                      |
| [style.TextColor = [Color].Red;]                                                         |
|                                                                                                                                                      |
| [style.BackgroundImageMode = [GridBackgroundImageMode].StretchImage;]                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                 |
|                                                                                                                                                    |
| **[]**                                                                                           |
|                                                                                                                                                    |
| [Dim][ style [As] GridStyleInfo]         |
|                                                                                                                                                    |
| [style = grid(4, 3)]                                                                                           |
|                                                                                                                                                    |
| [grid.BanneredRanges.Add(GridRangeInfo.FromTlhw(4, 3, 8, 3))]                                                  |
|                                                                                                                                                    |
| [style.BackgroundImage = GetImage([\"common\\Images\\Grid\\BannerCells\\back1.jpg\"])] |
|                                                                                                                                                    |
| [style.Text = [\"back1.jpg\"]]                                                         |
|                                                                                                                                                    |
| [style.TextColor = Color.Red]                                                                                  |
|                                                                                                                                                    |
| [style.BackgroundImageMode = GridBackgroundImageMode.StretchImage]                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p344} 

 

[]{#related-topics}

