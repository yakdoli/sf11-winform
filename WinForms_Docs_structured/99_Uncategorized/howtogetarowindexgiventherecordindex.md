---
title: howtogetarowindexgiventherecordindex.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtogetarowindexgiventherecordindex.md
created_at: 2025-07-03
---






#### How to get a rowindex given the record index {#how-to-get-a-rowindex-given-the-record-index style="tab-stops: 0pt"}

[] 

This can be done using the following code snippet.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                      |
|                                                                                                                                                                     |
| []                                                                                                                |
|                                                                                                                                                                     |
| [int][ position = gridGroupingControl1.Table.DisplayElements.IndexOf(record);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                              |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                                             |
| [Dim][ position [As] [Integer] = gridGroupingControl1.Table.DisplayElements.IndexOf(record)] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p700} 

 

[]{#related-topics}

