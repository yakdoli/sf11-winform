---
title: howtoaccessthecurrentrecord.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoaccessthecurrentrecord.md
created_at: 2025-07-03
---






#### How to access the current record {#how-to-access-the-current-record style="tab-stops: 0pt"}

[] 

To access the current record, use the following code.

**[]** 

+--------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                           |
|                                                                                                                          |
| []                                                                     |
|                                                                                                                          |
| [Record rec = [this].gridGroupingControl1.Table.CurrentRecord;] |
|                                                                                                                          |
| [Trace.WriteLine(rec.ToString());]                                                   |
+--------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                     |
|                                                                                                                                                                                                        |
| []                                                                                                                                                   |
|                                                                                                                                                                                                        |
| [Dim][ rec [As] Record = [Me].gridGroupingControl1.Table.CurrentRecord] |
|                                                                                                                                                                                                        |
| [Trace.WriteLine(rec.ToString())]                                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p644} 

 

[]{#related-topics}

