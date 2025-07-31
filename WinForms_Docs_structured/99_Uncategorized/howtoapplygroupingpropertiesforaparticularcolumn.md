---
title: howtoapplygroupingpropertiesforaparticularcolumn.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoapplygroupingpropertiesforaparticularcolumn.md
created_at: 2025-07-03
---






#### How to apply grouping properties for a particular column {#how-to-apply-grouping-properties-for-a-particular-column style="tab-stops: 0pt"}

[] 

Grouping properties for a particular column can be applied using the below code snippet.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                      |
| [// Setting the color of any group cell in column \'Col1\'.]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                      |
| [this][.gridGroupingControl1.TableDescriptor.Columns\[[\"Col1\"]\].GroupByAppearance.AnyGroupCell.BackColor=Color.LightBlue;]                            |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [// Setting the FilterBar cell appearance to be raised.]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                      |
| [this][.gridGroupingControl1.TableDescriptor.Columns\[[\"Col1\"]\].GroupByAppearance.FilterBarCell.CellAppearance=GridCellAppearance.Raised;]            |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                      |
| [// Setting the cell type of any record cell.]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                      |
| [this][.gridGroupingControl1.TableDescriptor.Columns\[[\"Col1\"]\].GroupByAppearance.AnyRecordFieldCell.CellType=[\"ComboBox\"];] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                 |
| [\' Shows how to apply grouping properties for particular column.]                                                                                                                                            |
|                                                                                                                                                                                                                                                                 |
| [\' Setting the color of any record cell in column \'Col1\'.]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                 |
| [Me][.gridGroupingControl1.TableDescriptor.Columns([\"Col1\"]).GroupByAppearance.AnyRecordFieldCell.BackColor=Color.LightBlue]                      |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                 |
| [\' Setting the FilterBar cell appearance to be raised.]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                 |
| [Me][.gridGroupingControl1.TableDescriptor.Columns([\"Col1\"]).GroupByAppearance.FilterBarCell.CellAppearance=GridCellAppearance.Raised]            |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                 |
| [\' Setting the cell type of any record cell.]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                 |
| [Me][.gridGroupingControl1.TableDescriptor.Columns([\"Col1\"]).GroupByAppearance.AnyRecordFieldCell.CellType=[\"ComboBox\"]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p713} 

 

[]{#related-topics}

