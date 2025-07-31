---
title: howtoaccesssortedorfilteredrecords.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoaccesssortedorfilteredrecords.md
created_at: 2025-07-03
---






#### How to access sorted or filtered records {#how-to-access-sorted-or-filtered-records style="tab-stops: 0pt"}

[] 

This can be done using the following code snippet.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                               |
|                                                                                                                                                                                                              |
| []                                                                                                                                                         |
|                                                                                                                                                                                                              |
| [// looping through the filtered records.]                                                                                                                 |
|                                                                                                                                                                                                              |
| [foreach][(Record fr [in] [this].gridGroupingControl1.Table.FilteredRecords)] |
|                                                                                                                                                                                                              |
| [{]                                                                                                                                                                      |
|                                                                                                                                                                                                              |
| [      Console.WriteLine(fr.Info);]                                                                                                                                      |
|                                                                                                                                                                                                              |
| [}]                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                             |
| [\' looping through the filtered records.]                                                                                                                                                                |
|                                                                                                                                                                                                                                                             |
| [For][ [Each] fr [As] Record [In] [Me].gridGroupingControl1.Table.FilteredRecords] |
|                                                                                                                                                                                                                                                             |
| [    Console.WriteLine(fr.Info)]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                             |
| [Next][ fr]                                                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p697} 

 

[]{#related-topics}

