---
title: customcelltypes2.md
original_path: WinForms_Docs/99_Uncategorized/customcelltypes2.md
created_at: 2025-08-05
---






#### Custom Cell Types {#custom-cell-types style="tab-stops: 0pt"}

 

Essential Grid allows you to create custom derived controls to use additional cell types. This requires a cellmodel class and a cellrenderer class. The cellmodel class creates the actual cell control while the cellrenderer class handles the UI requirements of the cell control. The custom cell type can be created by  registering the cellmodel to the corresponding grid by naming this cell type. It can be enabled by assigning its name to the style.CellType property.

In general, the built-in cell types are also constructed only in this way. Every such cell type has its own cell model and renderer classes in the code base. These cell model and renderer classes originate from GridCellModelBase and GridCellRendererBase classes. These two classes define the basic functionality for a cell type.

Examples of custom cell types are discussed in later sections.

 

 

More:











