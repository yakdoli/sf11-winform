---
title: howtoaccessselectedrecords.md
original_path: WinForms_Docs/99_Uncategorized/howtoaccessselectedrecords.md
created_at: 2025-08-05
---






#### How to access selected records {#how-to-access-selected-records style="tab-stops: 0pt"}

[] 

The selected records can be accessed using the below code snippet.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                        |
|                                                                                                                                                                                                                       |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                                       |
| [//Accessing Selected records in a GridGroupingcontrol.      ]                                                                                                      |
|                                                                                                                                                                                                                       |
| [foreach][(SelectedRecord rec [in] [this].gridGroupingControl1.Table.SelectedRecords)] |
|                                                                                                                                                                                                                       |
| [System.Diagnostics.Trace.WriteLine(rec.Record.Info);]                                                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                      |
| [\'Accessing Selected records in a GridGroupingControl.]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                      |
| [For][ [Each] rec [As] SelectedRecord [In] [Me].gridGroupingControl1.Table.SelectedRecords] |
|                                                                                                                                                                                                                                                                      |
| [Console.WriteLine(rec.Record.Info)]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                      |
| [Next][ rec]                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p690} 

 

[]{#related-topics}

