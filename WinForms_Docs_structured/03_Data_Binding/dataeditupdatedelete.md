---
title: dataeditupdatedelete.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\dataeditupdatedelete.md
created_at: 2025-07-03
---








  









## Data Edit / Update / Delete {#data-edit-update-delete style="tab-stops: 0pt"}

[] 

For disabling editing, you can set the **AllowEdit** property to **False**.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                             |
| [\<][TableDescriptor][ [AllowEdit][=\"false\"] [/\>]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                |
|                                                                                                                                                                               |
| []                                                                                                                          |
|                                                                                                                                                                               |
| [this][.GridGroupingControl1.TableDescriptor.AllowEdit = [false]; ] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                        |
|                                                                                                                                                                           |
| []                                                                                                                      |
|                                                                                                                                                                           |
| [Me][.GridGroupingControl1.TableDescriptor.AllowEdit = [False]] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Begin Editing

[] 

To start the editing, call the **BeginEdit** function. This would generate the appropriate table elements to enter the grid in the Edit mode.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                   |
|                                                                                                                                                                                                  |
| []                                                                                                                                             |
|                                                                                                                                                                                                  |
| [this][.CurrentTable.BeginEdit(); [// CurrentTable is the property described above.]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                              |
|                                                                                                                                                                                                 |
| [                         ]                                                                                                                   |
|                                                                                                                                                                                                 |
| [Me][.CurrentTable.BeginEdit() [\' CurrentTable is the property described above.; ]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Cancel Editing

[] 

To cancel the editing, call the **CancelEdit** function. This would revert the final changes done in the Grid and go back to the Read mode.

[] 

+-----------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                              |
|                                                                                                                             |
| []                                                                        |
|                                                                                                                             |
| [this][.CurrentTable.CancelEdit();   ] |
+-----------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                    |
|                                                                                                                       |
| []                                                                  |
|                                                                                                                       |
| [Me][.CurrentTable.CancelEdit()] |
+-----------------------------------------------------------------------------------------------------------------------+

[] 

Events related to Editing

[] 

Use the below given events to have the underlying datasource updated after validation / if you want to have custom query updates.

[] 

DataSourceControl related Events

[] 

[·      ]**DataSourceControlRowAdding** - occurs before adding a new record in the bound DataSourceControl. Good place to validate.

[·      ]**DataSourceControlRowAdded** - occurs after adding a new record in the bound DataSourceControl.

[·      ]**DataSourceControlUpdating** - occurs before updating a record in the bound DataSourceControl. Good place to validate.

[·      ]**DataSourceControlUpdated** - occurs after updating a record in the bound DataSourceControl.

[·      ]**DataSourceControlDeleting** - occurs before deleting a record in the bound DataSourceControl. Good place to validate.

[·      ]**DataSourceControlDeleted** - occurs after deleting a record in the bound DataSourceControl.

[] 

GridEngine related Events

[] 

[·      ]**CurrentRecordContextChange** - occurs before and after the status of the current record is changed.

 

[]{#p81} 

 

More:













