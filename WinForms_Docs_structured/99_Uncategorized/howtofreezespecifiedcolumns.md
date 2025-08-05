---
title: howtofreezespecifiedcolumns.md
original_path: WinForms_Docs/99_Uncategorized/howtofreezespecifiedcolumns.md
created_at: 2025-08-05
---






#### How to freeze specified columns {#how-to-freeze-specified-columns style="tab-stops: 0pt"}

[] 

You can freeze Specified columns by making use of the below given code.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                         |
|                                                                                                                                                        |
| []                                                                                                 |
|                                                                                                                                                        |
| [//Add a specified column index  to freeze]                                                          |
|                                                                                                                                                        |
| [this][. gridGroupingControl1.TableModel.Cols.FreezeRange(1, 1);] |
|                                                                                                                                                        |
| []                                                                                                                 |
|                                                                                                                                                        |
| [//Add a range of columns to freeze.]                                                                |
|                                                                                                                                                        |
| [this][. gridGroupingControl1.TableModel.Cols.FreezeRange(1, 3);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                      |
|                                                                                                                                                     |
| []                                                                                              |
|                                                                                                                                                     |
| [\'Add a specified column index  to freeze]                                                       |
|                                                                                                                                                     |
| [Me][. gridGroupingControl1.TableModel.Cols.FreezeRange(1, 1)] |
|                                                                                                                                                     |
| []                                                                                                              |
|                                                                                                                                                     |
| [\'Add a range of columns to freeze.]                                                             |
|                                                                                                                                                     |
| [Me][. gridGroupingControl1.TableModel.Cols.FreezeRange(1, 3)] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p680} 

 

[]{#related-topics}

