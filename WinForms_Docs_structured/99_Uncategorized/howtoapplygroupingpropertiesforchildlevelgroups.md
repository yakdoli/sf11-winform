---
title: howtoapplygroupingpropertiesforchildlevelgroups.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoapplygroupingpropertiesforchildlevelgroups.md
created_at: 2025-07-03
---






#### How to apply grouping properties for ChildLevelGroups {#how-to-apply-grouping-properties-for-childlevelgroups style="tab-stops: 0pt"}

[] 

Grouping properties for ChildLevelGroups can be applied using the below code snippet.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                   |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                             |
|                                                                                                                                                                                                                  |
| [//Hiding the caption text of the group.]                                                                                                                      |
|                                                                                                                                                                                                                  |
| [this][.gridGroupingControl1.TableDescriptor.ChildGroupOptions.ShowCaption=[false];]                   |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                  |
| [//Hiding the plus / minus sign from the group.]                                                                                                               |
|                                                                                                                                                                                                                  |
| [this][.gridGroupingControl1.TableDescriptor.ChildGroupOptions.ShowCaptionPlusMinus=[false];]          |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                  |
| [// Adding the Filter Bar to the Child level groups.]                                                                                                          |
|                                                                                                                                                                                                                  |
| [this][.gridGroupingControl1.TableDescriptor.ChildGroupOptions.ShowFilterBar=[true];]                  |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                  |
| [// Hiding the AddNewRecord field before details row.]                                                                                                         |
|                                                                                                                                                                                                                  |
| [this][.gridGroupingControl1.TableDescriptor.ChildGroupOptions.ShowAddNewRecordBeforeDetails=[false];] |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                  |
| [//Showing the footer of the group.]                                                                                                                           |
|                                                                                                                                                                                                                  |
| [this][.gridGroupingControl1.TableDescriptor.ChildGroupOptions.ShowGroupFooter=[true];]                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                |
|                                                                                                                                                                                                               |
| []                                                                                                                                                          |
|                                                                                                                                                                                                               |
| [\' Hiding the caption text of the group.]                                                                                                                  |
|                                                                                                                                                                                                               |
| [Me][.gridGroupingControl1.TableDescriptor.ChildGroupOptions.ShowCaption=[False]]                   |
|                                                                                                                                                                                                               |
| []                                                                                                                                                           |
|                                                                                                                                                                                                               |
| [\' Hiding the plus / minus symbols present in the group.]                                                                                                  |
|                                                                                                                                                                                                               |
| [Me][.gridGroupingControl1.TableDescriptor.ChildGroupOptions.ShowCaptionPlusMinus=[False]]          |
|                                                                                                                                                                                                               |
| []                                                                                                                                                           |
|                                                                                                                                                                                                               |
| [\' Showing the FilterBar.]                                                                                                                                 |
|                                                                                                                                                                                                               |
| [Me][.gridGroupingControl1.TableDescriptor.ChildGroupOptions.ShowFilterBar=[True]]                  |
|                                                                                                                                                                                                               |
| []                                                                                                                                                           |
|                                                                                                                                                                                                               |
| [\' Hiding the AddNewRecord before details.]                                                                                                                |
|                                                                                                                                                                                                               |
| [Me][.gridGroupingControl1.TableDescriptor.ChildGroupOptions.ShowAddNewRecordBeforeDetails=[False]] |
|                                                                                                                                                                                                               |
| []                                                                                                                                                           |
|                                                                                                                                                                                                               |
| [\' Showing the group footer.]                                                                                                                              |
|                                                                                                                                                                                                               |
| [Me][.gridGroupingControl1.TableDescriptor.ChildGroupOptions.ShowGroupFooter=[True]]                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p714} 

 

[]{#related-topics}

