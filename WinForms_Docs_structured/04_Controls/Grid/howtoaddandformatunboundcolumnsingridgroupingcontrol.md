---
title: howtoaddandformatunboundcolumnsingridgroupingcontrol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\howtoaddandformatunboundcolumnsingridgroupingcontrol.md
created_at: 2025-07-03
---






#### How to add and format unbound columns in GridGrouping control {#how-to-add-and-format-unbound-columns-in-gridgrouping-control style="tab-stops: 0pt"}

[] 

The unbound columns can be added and formatted using the below code.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                           |
| [// Adding unbound column in the GridGroupingControl.]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                           |
| [this][.gridGroupingControl1.TableDescriptor.UnboundFields.Add([\"UnboundColumn1\"]);]                                                                        |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [//Formatting the Unbound column]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                           |
| [this][.gridGroupingControl1.TableDescriptor.Columns\[[\"UnboundColumn1\"]\].Appearance.AnyRecordFieldCell.CellType = [\"CheckBox\"];] |
|                                                                                                                                                                                                                                                                           |
| [this][.gridGroupingControl1.TableDescriptor.Columns\[[\"UnboundColumn1\"]\].Appearance.AnyRecordFieldCell.BackColor = Color.LightSteelBlue;]                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                      |
| [\'Adding an Unbound column in a  GridGroupingControl]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                      |
| [Me][.gridGroupingControl1.TableDescriptor.UnboundFields.Add([\"UnboundColumn1\"])]                                                                      |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                      |
| [\'Formatting an Unbound column in a GridGroupingControl]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                      |
| [Me][.gridGroupingControl1.TableDescriptor.Columns([\"UnboundColumn1\"]).Appearance.AnyRecordFieldCell.CellType = [\"CheckBox\"]] |
|                                                                                                                                                                                                                                                                      |
| [Me][.gridGroupingControl1.TableDescriptor.Columns([\"UnboundColumn1\"]).Appearance.AnyRecordFieldCell.BackColor = Color.LightSteelBlue]                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p645} 

 

[]{#related-topics}

