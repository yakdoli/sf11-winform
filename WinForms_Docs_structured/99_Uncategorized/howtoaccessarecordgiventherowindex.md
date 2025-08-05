---
title: howtoaccessarecordgiventherowindex.md
original_path: WinForms_Docs/99_Uncategorized/howtoaccessarecordgiventherowindex.md
created_at: 2025-08-05
---






#### How to access a record given the row index {#how-to-access-a-record-given-the-row-index style="tab-stops: 0pt"}

[] 

This can be done using the following code snippet.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                               |
|                                                                                                                                              |
| []                                                                                         |
|                                                                                                                                              |
| [// Using the DisplayElements property of the grid, we can find the corresponding record.] |
|                                                                                                                                              |
| [Record r = gridGroupingControl1.Table.DisplayElements\[rowindex\].ParentRecord;]                        |
+----------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                      |
|                                                                                                                                                                                                     |
| []                                                                                                                                                |
|                                                                                                                                                                                                     |
| [\' Using the DisplayElements property of the grid, we can find the corresponding record.]                                                        |
|                                                                                                                                                                                                     |
| [Dim][ r [As] Record = gridGroupingControl1.Table.DisplayElements(rowindex).ParentRecord] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p696} 

 

[]{#related-topics}

