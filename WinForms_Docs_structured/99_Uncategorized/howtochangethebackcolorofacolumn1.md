---
title: howtochangethebackcolorofacolumn1.md
original_path: WinForms_Docs/99_Uncategorized/howtochangethebackcolorofacolumn1.md
created_at: 2025-08-05
---








  









### How to Change the Backcolor of a Column {#how-to-change-the-backcolor-of-a-column style="tab-stops: 0pt"}

[] 

Introduction

 

The GridDataBoundGrid maintains a collection of **GridBoundColumn** objects that will allow you to set **column** properties like **backcolor**, **textcolor**, **font**, etc. Either from code or at design-time, you can explicitly add GridBoundColumns to the this.gridDataBoundGrid1.GridBoundColumns property. If you do not explicitly add GridBoundColumns to this collection, then the grid will generate an internal set of columns that you can use, this.gridDataBoundGrid1.Binder.InternalColumns.

[] 

Example

[] 

To change the backcolor of a column named \"Price\", use the code given below.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                        |
| [// If you have added GridBoundColumns.\                                                                                                                                                                                                               |
| ][this][.gridDataBoundGrid1.GridBoundColumns\[\"Price\"\].StyleInfo.BackColor = Color.Red;]       |
|                                                                                                                                                                                                                                                        |
| [\                                                                                                                                                                                                                                                     |
| ][// If you haven\'t explicitly added GridBoundColumns.\                                                                                                                                             |
| ][this][.gridDataBoundGrid1.Binder.InternalColumns\[\"Price\"\].StyleInfo.BackColor = Color.Red;] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [\' If you have added GridBoundColumns.\                                                                                                                                                                                                          |
| ][Me][.gridDataBoundGrid1.GridBoundColumns(\"Price\").StyleInfo.BackColor = Color.Red]       |
|                                                                                                                                                                                                                                                   |
| [\                                                                                                                                                                                                                                                |
| ][\' If you haven\'t explicitly added GridBoundColumns.\                                                                                                                                        |
| ][Me][.gridDataBoundGrid1.Binder.InternalColumns(\"Price\").StyleInfo.BackColor = Color.Red] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p583} 

 

[]{#related-topics}

