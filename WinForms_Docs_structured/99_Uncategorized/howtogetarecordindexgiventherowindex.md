---
title: howtogetarecordindexgiventherowindex.md
original_path: WinForms_Docs/99_Uncategorized/howtogetarecordindexgiventherowindex.md
created_at: 2025-08-05
---






#### How to get a record index given the rowindex {#how-to-get-a-record-index-given-the-rowindex style="tab-stops: 0pt"}

[] 

This can be done using the following code snippet.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                              |
|                                                                                                                                             |
| []                                                                                        |
|                                                                                                                                             |
| [// Record index is being calculated.]                                                    |
|                                                                                                                                             |
| [Table table = e.TableCellIdentity.Table;]                                                              |
|                                                                                                                                             |
| [Element el = table.DisplayElements\[RowIndex\];]                                                       |
|                                                                                                                                             |
| [Record r = el.ParentRecord;]                                                                           |
|                                                                                                                                             |
| [int][ RecordIndex= table.UnsortedRecords.IndexOf(r);] |
+---------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                       |
|                                                                                                                                                                                                      |
| []                                                                                                                                                 |
|                                                                                                                                                                                                      |
| [\' Record index is being calculated.]                                                                                                             |
|                                                                                                                                                                                                      |
| [Dim][ table [As] Table = e.TableCellIdentity.Table]                                       |
|                                                                                                                                                                                                      |
| [Dim][ el [As] Element = table.DisplayElements(RowIndex)]                                  |
|                                                                                                                                                                                                      |
| [Dim][ r [As] Record = el.ParentRecord]                                                    |
|                                                                                                                                                                                                      |
| [Dim][ RecordIndex [As] [Integer] = table.UnsortedRecords.IndexOf(r)] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p699} 

 

[]{#related-topics}

