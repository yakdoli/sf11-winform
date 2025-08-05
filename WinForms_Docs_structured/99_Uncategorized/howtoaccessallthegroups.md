---
title: howtoaccessallthegroups.md
original_path: WinForms_Docs/99_Uncategorized/howtoaccessallthegroups.md
created_at: 2025-08-05
---






#### How to access all the groups {#how-to-access-all-the-groups style="tab-stops: 0pt"}

[] 

To access all the groups and the records categorized under it, use the following code.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                               |
|                                                                                                                                                                              |
| []                                                                                                                         |
|                                                                                                                                                                              |
| [this][.iterate([this].gridGroupingControl1.Table.TopLevelGroup);] |
|                                                                                                                                                                              |
| []                                                                                                                                       |
|                                                                                                                                                                              |
| [public][ [void] iterate(Group g)]                                 |
|                                                                                                                                                                              |
| [{]                                                                                                                                      |
|                                                                                                                                                                              |
| [      System.Diagnostics.Trace.WriteLine([\"GroupLevel = \"]+g.GroupLevel);]                                     |
|                                                                                                                                                                              |
| [      System.Diagnostics.Trace.WriteLine(g.Info);]                                                                                      |
|                                                                                                                                                                              |
| [      [foreach](Record r [in] g.Records)]                                                     |
|                                                                                                                                                                              |
| [      {]                                                                                                                                |
|                                                                                                                                                                              |
| [            System.Diagnostics.Trace.WriteLine(r.Info);]                                                                                |
|                                                                                                                                                                              |
| [      }]                                                                                                                                |
|                                                                                                                                                                              |
| [      [foreach](Group gr [in] g.Groups)]                                                      |
|                                                                                                                                                                              |
| [      {]                                                                                                                                |
|                                                                                                                                                                              |
| [            iterate(gr);]                                                                                                               |
|                                                                                                                                                                              |
| [      }]                                                                                                                                |
|                                                                                                                                                                              |
| [}]                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                     |
|                                                                                                                                                                                                    |
| []                                                                                                                                               |
|                                                                                                                                                                                                    |
| [Me][.iterate([Me].gridGroupingControl1.Table.TopLevelGroup)]                            |
|                                                                                                                                                                                                    |
| []                                                                                                                                                             |
|                                                                                                                                                                                                    |
| [Public][ [Sub] iterate([ByVal] g [As] Group)] |
|                                                                                                                                                                                                    |
| [    System.Diagnostics.Trace.WriteLine([\"GroupLevel = \"] + g.GroupLevel.toString())]                                                 |
|                                                                                                                                                                                                    |
| [    System.Diagnostics.Trace.WriteLine(g.Info)]                                                                                                               |
|                                                                                                                                                                                                    |
| [    [For] [Each] r [As] Record [In] g.Records]                            |
|                                                                                                                                                                                                    |
| [        System.Diagnostics.Trace.WriteLine(r.Info)]                                                                                                           |
|                                                                                                                                                                                                    |
| [    [Next] r]                                                                                                                            |
|                                                                                                                                                                                                    |
| [    [For] [Each] gr [As] Group [In] g.Groups]                             |
|                                                                                                                                                                                                    |
| [        iterate(gr)]                                                                                                                                          |
|                                                                                                                                                                                                    |
| [    [Next] gr]                                                                                                                           |
|                                                                                                                                                                                                    |
| [End][ [Sub]]                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p709} 

 

[]{#related-topics}

