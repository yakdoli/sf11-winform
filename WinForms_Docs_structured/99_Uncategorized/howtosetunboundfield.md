---
title: howtosetunboundfield.md
original_path: WinForms_Docs/99_Uncategorized/howtosetunboundfield.md
created_at: 2025-08-05
---








  









## How to set unbound fields in GridCoupingControl that uses VisibleColumns in the TableDescriptor {#how-to-set-unbound-fields-in-gridcoupingcontrol-that-uses-visiblecolumns-in-the-tabledescriptor style="tab-stops: 0pt"}

Visible Columns

[] 

*VisibleColumns* collection is used to customize the grid view. You have to define the column in *GridVisibleColumnDescriptor,* which you want to display in grid. To set the unbound column visible, add it to the *VisibleColumns*. To know more about the unbound column refer [[4.2.3 Unbound Column]{.UGHyperlink}](http://help.syncfusion.com/ug_91/User%20Interface/ASP.NET/grid/Documents/423unboundcolumn.htm).

[] 

The following code illustrates how to add unbound columns to the *VisibleColumns*:

**** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX}]**                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<%][\--VisibleColumns \--][%\>]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<][TableDescriptor][ [AllowEdit][=\"true\"] [AllowNew][=\"true\"\>]]                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<][VisibleColumns][\>]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<][syncfusion][:][GridVisibleColumnDescriptor][ [Name][=\"ID\"] [/\>]]   |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<][syncfusion][:][GridVisibleColumnDescriptor][ [Name][=\"Name\"] [/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<][syncfusion][:][GridVisibleColumnDescriptor][ [Name][=\"Dept\"] [/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [\</][VisibleColumns][\>]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [\</][TableDescriptor][\>]                                                                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**** 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                           |
| [//Adding Unbound columns]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                           |
| [this][.][GridGroupingControl1][.TableDescriptor.UnboundFields.Add([\"Unbound\"]);]  |
|                                                                                                                                                                                                                                                                           |
| [//Adding UnboundFields to VisibleColumns]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                           |
| [this][.][GridGroupingControl1][.TableDescriptor.VisibleColumns.Add([\"Unbound\"]);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                                              |
| [\'Adding Unbound columns][]                                                                                                                           |
|                                                                                                                                                                                                                                              |
| [Me][.][GridGroupingControl1][.TableDescriptor.UnboundFields.Add(\"Unbound\")]  |
|                                                                                                                                                                                                                                              |
| [\'Adding UnboundFields to VisibleColumns][]                                                                                                           |
|                                                                                                                                                                                                                                              |
| [Me][.][GridGroupingControl1][.TableDescriptor.VisibleColumns.Add(\"Unbound\")] |
|                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

