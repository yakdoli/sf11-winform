---
title: displayorder.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\displayorder.md
created_at: 2025-07-03
---








  









### Display Order {#display-order style="tab-stops: 0pt"}

[] 

**VisibleColumnsCollection** is the collection of columns that are displayed in the GridGroupingControl. You can customize the columns by making changes in the VisibleColumnsCollection.

The display order the of the columns can be controlled by making use of the **Move** method from the VisibleColumnsCollection.

The following code example illustrates this.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                |
|                                                                                                                                                               |
| []                                                                                                          |
|                                                                                                                                                               |
| [// Interchange the position of 2nd and the 3rd column]                                                     |
|                                                                                                                                                               |
| [this][.GridGroupingControl1.TableDescriptor.VisibleColumns.Move(1, 2);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                         |
|                                                                                                                                                            |
| []                                                                                                        |
|                                                                                                                                                            |
| [\' Interchange the position of 2nd and the 3rd column]                                                  |
|                                                                                                                                                            |
| [Me][.GridGroupingControl1.TableDescriptor.VisibleColumns.Move(1, 2)] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 51

[]{#p40} 

[]{#related-topics}

