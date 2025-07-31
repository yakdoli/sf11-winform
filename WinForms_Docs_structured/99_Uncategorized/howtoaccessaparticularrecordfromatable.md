---
title: howtoaccessaparticularrecordfromatable.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoaccessaparticularrecordfromatable.md
created_at: 2025-07-03
---






#### How to access a particular record from a table {#how-to-access-a-particular-record-from-a-table style="tab-stops: 0pt"}

[] 

This can be done using the following code snippet.

[] 

+-------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                |
|                                                                                                                               |
| []                                                                          |
|                                                                                                                               |
| [// Using the record Index to access a particular record from a table.]     |
|                                                                                                                               |
| [Record r=[this].gridGroupingControl1.Table.Records\[RecordIndex\];] |
+-------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                              |
|                                                                                                                                                                                                             |
| []                                                                                                                                                        |
|                                                                                                                                                                                                             |
| [\'Using the record Index to access a particular record from a table.]                                                                                    |
|                                                                                                                                                                                                             |
| [Dim][ r [As] Record = [Me].gridGroupingControl1.Table.Records(RecordIndex)] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p695} 

 

[]{#related-topics}

