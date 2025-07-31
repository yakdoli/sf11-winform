---
title: columnappearance1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\columnappearance1.md
created_at: 2025-07-03
---






##### Column Appearance {#column-appearance style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

The appearance of different columns can be customized through Column Styles settings.

 

**MultiColumnTreeView.ColumnHeaderBackground** property sets the background column headers for the control. These settings are overridden by above ColumnStyles settings.

[] 

{border="0"}

***[]*** 

Figure 1192: ColumnsHeaderBackground property in the Properties Grid

[] 

{border="0"}

[] 

Figure 1193: Gradient colors set for Header Background

***[]*** 

[] 

 

Adding HighlightBorderColor property

 

Essential tool is now enhanced with HighlightBorderColor property to set the highlight color of the column header in MultiColumnTreeView.

 

The following code illustrates how to set HighlightBorderColor property.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                              |
|                                                                                                                                                               |
| [this.treeColumnAdv1.HighlightBorderColor = Color.Brown;][] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                            |
|                                                                                                                                                             |
| [Me.treeColumnAdv1.HighlightBorderColor = Color.Brown;][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

{border="0"}

Figure 1194: Column Header Highlight Border Color changed

[] 

 

 

 

 

[]{#related-topics}

