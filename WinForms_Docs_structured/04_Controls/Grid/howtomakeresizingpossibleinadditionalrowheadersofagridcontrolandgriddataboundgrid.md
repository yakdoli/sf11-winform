---
title: howtomakeresizingpossibleinadditionalrowheadersofagridcontrolandgriddataboundgrid.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\howtomakeresizingpossibleinadditionalrowheadersofagridcontrolandgriddataboundgrid.md
created_at: 2025-07-03
---








  









### How to make resizing possible in additional row headers of a GridControl and GridDataBoundGrid {#how-to-make-resizing-possible-in-additional-row-headers-of-a-gridcontrol-and-griddataboundgrid style="tab-stops: 0pt"}

[] 

The resizing of additional row headers on the grid can be made possible by setting the ResizeColsBahaviour flag to Grid.GridResizeCellsBehavior.InsideGrid.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                               |
|                                                                                                                                                              |
| []                                                                                                         |
|                                                                                                                                                              |
| [grid.ResizeColsBehavior = (((Syncfusion.Windows.Forms.Grid.[GridResizeCellsBehavior].ResizeSingle] |
|                                                                                                                                                              |
| [\| Syncfusion.Windows.Forms.Grid.[GridResizeCellsBehavior].InsideGrid)]                            |
|                                                                                                                                                              |
| [\| Syncfusion.Windows.Forms.Grid.[GridResizeCellsBehavior].OutlineHeaders)]                        |
|                                                                                                                                                              |
| [\| Syncfusion.Windows.Forms.Grid.[GridResizeCellsBehavior].OutlineBounds);]                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                             |
|                                                                                                                                                                                                |
| []                                                                                                                                           |
|                                                                                                                                                                                                |
| [grid.ResizeColsBehavior = (((Syncfusion.Windows.Forms.Grid.GridResizeCellsBehavior.ResizeSingle]                                                          |
|                                                                                                                                                                                                |
| [\| Syncfusion.Windows.Forms.Grid.GridResizeCellsBehavior.InsideGrid)]                                                                                     |
|                                                                                                                                                                                                |
| [\| Syncfusion.Windows.Forms.Grid.GridResizeCellsBehavior.OutlineHeaders)]                                                                                 |
|                                                                                                                                                                                                |
| [Dim][ Syncfusion.Windows.Forms.Grid.GridResizeCellsBehavior.OutlineBounds) [As] \|] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p629} 

 

[]{#related-topics}

