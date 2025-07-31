---
title: howtosetstylepropertiesofanestedtable.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\howtosetstylepropertiesofanestedtable.md
created_at: 2025-07-03
---






#### How to set style properties of a nested table {#how-to-set-style-properties-of-a-nested-table style="tab-stops: 0pt"}

[] 

This can be done using the below code.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                  |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [// 1. Changing the backcolor of all the record field cells in the child table.]                                                                                              |
|                                                                                                                                                                                                                                 |
| [                        ]                                                                                                                                                                  |
|                                                                                                                                                                                                                                 |
| [// Get the child table descriptor for a particular relation]                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [GridTableDescriptor child_tabledescriptor = [this].gridGroupingControl1.TableDescriptor.Relations\[[\"MyChildTable\"]\].ChildTableDescriptor;] |
|                                                                                                                                                                                                                                 |
| [// Set the style properties   ]                                                                                                                                              |
|                                                                                                                                                                                                                                 |
| [child_tabledescriptor.Columns\[[\"childID\"]\].Appearance.AnyRecordFieldCell.BackColor = Color.Pink;]                                                               |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [// 2. Changing the cell property of all the record field cells in the child table.]                                                                                          |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [// Get the child table descriptor for a particular relation]                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [GridTableDescriptor child_tabledescriptor = [this].gridGroupingControl1.TableDescriptor.Relations\[[\"MyChildTable\"]\].ChildTableDescriptor;] |
|                                                                                                                                                                                                                                 |
| [// Set the style properties   ]                                                                                                                                              |
|                                                                                                                                                                                                                                 |
| [child_tableDescriptor.Columns\[[\"childID\"]\].Appearance.AnyRecordFieldCell.CellType=[\"ComboBox\"];]                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                       |
| [\' 1. Changing the backcolor of all the record field cells in the child table.]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                       |
| [\' Get the child table descriptor for a particular relation]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                       |
| [Dim][ child_tabledescriptor [As] GridTableDescriptor = [Me].gridGroupingControl1.TableDescriptor.Relations([\"ComSal\"]).ChildTableDescriptor] |
|                                                                                                                                                                                                                                                                                                       |
| [\' Set the style properties              ]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                       |
| [child_tabledescriptor.Columns([\"Des\"]).Appearance.AnyRecordFieldCell.BackColor = Color.Pink]                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                       |
| [\' 2. Changing the cell property of all the record field cells in the child table.]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                       |
| [\' Get the child table descriptor for a particular relation]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                       |
| [Dim][ child_tabledescriptor [As] GridTableDescriptor = [Me].gridGroupingControl1.TableDescriptor.Relations([\"ComSal\"]).ChildTableDescriptor] |
|                                                                                                                                                                                                                                                                                                       |
| [\' Set the style properties   ]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                       |
| [child_tabledescriptor.Columns([\"Des\"]).Appearance.AnyRecordFieldCell.CellType=[\"ComboBox\"]]                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p663} 

[]{#related-topics}

