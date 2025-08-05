---
title: usingthereadonlyattribute.md
original_path: WinForms_Docs/99_Uncategorized/usingthereadonlyattribute.md
created_at: 2025-08-05
---






#### Using the ReadOnly Attribute {#using-the-readonly-attribute style="tab-stops: 0pt"}

[] 

There are several ways by which, you can prevent the user from making a change to the contents of a grid cell. If you set a cell\'s **GridStyleInfo.CellType** to \"Static\", the user will not be able to type in the cell. Another way to accomplish this is to use the Read-only attribute. This can be done on a grid-wide or cell-by-cell basis.

 

A Static cell will not allow the edit cursor to become visible. With a Read-only text box cell, the edit cursor may be visible. But, a Static cell can be pasted over or cleared by hitting the Delete key. Read-only cells cannot be pasted over or cleared. If you want a cell that will not show an edit cursor and which, cannot be pasted over or cleared, you must set the **CellType** to \"Static\" and also set the Read-only property to True.

[] 

 

[]{#p291} 

 

More:









