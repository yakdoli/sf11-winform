---
title: howtoapplygroupingpropertiesfortoplevelgroups.md
original_path: WinForms_Docs/99_Uncategorized/howtoapplygroupingpropertiesfortoplevelgroups.md
created_at: 2025-08-05
---






#### How to apply grouping properties for TopLevelGroups {#how-to-apply-grouping-properties-for-toplevelgroups style="tab-stops: 0pt"}

[] 

Grouping properties for TopLevelGroups can be applied using the below code snippet.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                      |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                |
|                                                                                                                                                                                                                     |
| [// Hiding the AddNewRecord field before details row.]                                                                                                            |
|                                                                                                                                                                                                                     |
| [this][.gridGroupingControl1.TableDescriptor.TopLevelGroupOptions.ShowAddNewRecordBeforeDetails=[false];] |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [// Hiding the Header cells.]                                                                                                                                     |
|                                                                                                                                                                                                                     |
| [this][.gridGroupingControl1.TableDescriptor.TopLevelGroupOptions.ShowColumnHeaders=[false];]             |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [// Adding the Filter Bar to the Child level groups.]                                                                                                             |
|                                                                                                                                                                                                                     |
| [this][.gridGroupingControl1.TableDescriptor.TopLevelGroupOptions.ShowFilterBar=[true];]                  |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [//Setting the caption.]                                                                                                                                          |
|                                                                                                                                                                                                                     |
| [this][.gridGroupingControl1.TableDescriptor.TopLevelGroupOptions.CaptionText=[\"Hai\"];]               |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                     |
| [//Shows the group footer.]                                                                                                                                       |
|                                                                                                                                                                                                                     |
| [this][.gridGroupingControl1.TableDescriptor.TopLevelGroupOptions.ShowGroupFooter=[true];]                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                   |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                             |
|                                                                                                                                                                                                                  |
| [\' Hiding the AddNewRecord before details.]                                                                                                                   |
|                                                                                                                                                                                                                  |
| [Me][.gridGroupingControl1.TableDescriptor.TopLevelGroupOptions.ShowAddNewRecordBeforeDetails=[False]] |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                              |
|                                                                                                                                                                                                                  |
| [\' Hiding the column headers.]                                                                                                                                |
|                                                                                                                                                                                                                  |
| [   [Me].gridGroupingControl1.TableDescriptor.TopLevelGroupOptions.ShowColumnHeaders=[False]]                                      |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                              |
|                                                                                                                                                                                                                  |
| [\' Adding the Filter Bar to the Top level groups.]                                                                                                            |
|                                                                                                                                                                                                                  |
| [   [Me].gridGroupingControl1.TableDescriptor.TopLevelGroupOptions.ShowFilterBar=[True]]                                           |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                              |
|                                                                                                                                                                                                                  |
| [\'Setting the caption.]                                                                                                                                       |
|                                                                                                                                                                                                                  |
| [Me][.gridGroupingControl1.TableDescriptor.TopLevelGroupOptions.CaptionText=[\"Hai\"]]               |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                  |
| [\'Shows the group footer.]                                                                                                                                    |
|                                                                                                                                                                                                                  |
| [Me][.gridGroupingControl1.TableDescriptor.TopLevelGroupOptions.ShowGroupFooter=[True]]                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p715} 

 

[]{#related-topics}

