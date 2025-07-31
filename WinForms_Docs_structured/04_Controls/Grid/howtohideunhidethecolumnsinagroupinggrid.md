---
title: howtohideunhidethecolumnsinagroupinggrid.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\howtohideunhidethecolumnsinagroupinggrid.md
created_at: 2025-07-03
---






#### How to Hide / Unhide the Columns in a Grouping Grid {#how-to-hide-unhide-the-columns-in-a-grouping-grid style="tab-stops: 0pt"}

[] 

The TableDescriptor object has a **VisibleColumns** collection that you can use to control which columns are visible. You can hide / unhide columns using the following code.

[] 

Example

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                      |
|                                                                                                                                                                     |
| []                                                                                                                |
|                                                                                                                                                                     |
| [//Hide]                                                                                                          |
|                                                                                                                                                                     |
| [this][.gridGroupingControl1.TableDescriptor.VisibleColumns.Remove(\"Col1\");] |
|                                                                                                                                                                     |
| []                                                                                                                              |
|                                                                                                                                                                     |
| [//Unhide]                                                                                                        |
|                                                                                                                                                                     |
| [this][.gridGroupingControl1.TableDescriptor.VisibleColumns.Add(\"Col1\");]    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                   |
|                                                                                                                                                                  |
| []                                                                                                             |
|                                                                                                                                                                  |
| [\'Hide]                                                                                                       |
|                                                                                                                                                                  |
| [Me][.gridGroupingControl1.TableDescriptor.VisibleColumns.Remove(\"Col1\")] |
|                                                                                                                                                                  |
| []                                                                                                                           |
|                                                                                                                                                                  |
| [\'Unhide]                                                                                                     |
|                                                                                                                                                                  |
| [Me][.gridGroupingControl1.TableDescriptor.VisibleColumns.Add(\"Col1\")]    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p652} 

 

[]{#related-topics}

