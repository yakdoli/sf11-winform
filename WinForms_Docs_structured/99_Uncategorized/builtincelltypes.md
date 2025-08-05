---
title: builtincelltypes.md
original_path: WinForms_Docs/99_Uncategorized/builtincelltypes.md
created_at: 2025-08-05
---






#### Built-In Celltypes {#built-in-celltypes style="tab-stops: 0pt"}

**[]** 

Grid CellTypes

Essential Grid allows the inclusion of special controls in Grid cells. The attribute of a grid cell is referred to as its CellType. The editor elements (all cell types) are created only on demand. Here "on demand" stands for the loading of cells, which depends upon the CellType. The CellTypes for which optimization is enabled will load the CellType as TextBox (default CellType) in the Grid portions that are visible in the screen and loads the editor elements only on cell click. The CellTypes for which optimization is not enabled will directly load the UIElement on the Grid for the visible portion in the screen. Figure 1 explains the loading of grid cells pictorially.

[] 

The following diagram explains the loading of the cell's UIElement in the Grid.

[] 

{border="0"}

Figure 22: Loading of Grid cells for which the CellTypes has SupportsRenderOptimization set to true

[] 

When SupporsRenderOptimization is set to true, the grid loads with improved performance. You can use customization of GridControl with different CellTypes. [Adding CellTypes to an Application]{.UGHyperlink} topic explains more about each CellType.

[] 

 

 

Use Case Scenarios

Each cell type has some unique features that can be implemented according to the user's need. With respect to the data used in the cell, the CellType can be assigned.

 

More:







