---
title: howtozoominthespread1.md
original_path: WinForms_Docs/99_Uncategorized/howtozoominthespread1.md
created_at: 2025-08-05
---








  





## How to Zoom in the Spreadsheet Control {#how-to-zoom-in-the-spreadsheet-control style="TEXT-ALIGN: justify; tab-stops: 0pt"}

You can access all grid control-related properties by using the **ActiveSpreadsheetGrid** property in the **SpreadsheetControl.GridProperties** class. By using that you can also change the zoom level of the active spreadsheet grid. The **ZoomScale** property is used to change the zoom level of the grid control. By increasing the **ZoomScale** of the spreadsheet grid, you can see the close-up view of the cells. By decreasing the **ZoomScale**, you can view more of the cells in the grid.

 

The following code shows how to change the zoom scale of the active grid.

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                       |
|                                                                                                                                                                        |
| [this][.spreadsheetControl.GridProperties.ActiveSpreadsheetGrid.ZoomScale = 1.5;] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 48: Zoom In

 

{border="0"}

Figure 49: Zoom Out

 

[]{#related-topics}

