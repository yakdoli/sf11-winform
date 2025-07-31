---
title: classhierarchy1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\classhierarchy1.md
created_at: 2025-07-03
---








  









## Class Hierarchy {#class-hierarchy style="tab-stops: 0pt"}

[]{#p14}The following hierarchy diagram depicts the relationship between different Grid control classes.

[] 

{border="0"}

Figure 14: Class Hierarchy

Let us see some introduction to all these classes.

[·      ]GridControlBase serves as the parent class for the other grids and derives from VirtualizingCellsControl. The VirtualizingCellsControl is an abstract class and can be used as a base class for any control that tends to display cells within scrollable rows and columns with built-in virtualization of visual elements inside the cells.

 

[·      ]GridControl, derived from GridControlBase, is a powerful cell-oriented control. It supports virtual mode, 20+ cell types, rich style support, etc.

 

[·      ]GridDataControl is a binding grid that offers excellent features like grouping, sorting, filtering and summaries. It can also display relational data in a nested grid structure. NestedGridControl is used in conjunction with GridDataControl and is used to display the child tables in nested relation.

 

[·      ]GridTreeControl, which is derived from GridControl, is a multi-column tree control. It is especially used to display hierarchical data in a tree-like structure. It offers unique features such as multi-column sorting, level styling, custom glyphs, and more.

[]{#related-topics}

