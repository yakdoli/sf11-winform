---
title: howtoselectarecordprogrammatically.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoselectarecordprogrammatically.md
created_at: 2025-07-03
---






#### How to select a record programmatically {#how-to-select-a-record-programmatically style="tab-stops: 0pt"}

[] 

The following code illustrates how to select a record programmatically.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                     |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                               |
|                                                                                                                                                                                                                    |
| [// select the 3 rd record]                                                                                                                                      |
|                                                                                                                                                                                                                    |
| [this][.gridGroupingControl1.Table.SelectedRecords.Add([this].gridGroupingControl1.Table.Records\[3\]);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                              |
|                                                                                                                                                                                                             |
| []                                                                                                                                                        |
|                                                                                                                                                                                                             |
| [\'select the 3 rd record]                                                                                                                                |
|                                                                                                                                                                                                             |
| [Me][.gridGroupingControl1.Table.SelectedRecords.Add([Me].gridGroupingControl1.Table.Records(3))] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p691} 

 

[]{#related-topics}

