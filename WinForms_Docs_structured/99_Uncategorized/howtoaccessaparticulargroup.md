---
title: howtoaccessaparticulargroup.md
original_path: WinForms_Docs/99_Uncategorized/howtoaccessaparticulargroup.md
created_at: 2025-08-05
---






#### How to access a particular group {#how-to-access-a-particular-group style="tab-stops: 0pt"}

 

To access a particular group and the records categorized under it, use the following code.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                               |
| [///][Accessing a particular group and the categorized records under it]                                                   |
|                                                                                                                                                                                                                               |
| [this][.gridGroupingControl1.TableDescriptor.GroupedColumns.Add([\"Col1\"]);]                                     |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                               |
| [// Using category]                                                                                                                                                         |
|                                                                                                                                                                                                                               |
| [this][.iterate([this].gridGroupingControl1.Table.TopLevelGroup.Groups\[[\"row6 col1\"]\]);] |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                               |
| [//Or using index]                                                                                                                                                          |
|                                                                                                                                                                                                                               |
| [//this.iterate(this.gridGroupingControl1.Table.TopLevelGroup.Groups\[6\]);]                                                                                                |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                               |
| [public][ [void] iterate(Group g)]                                                                                  |
|                                                                                                                                                                                                                               |
| [{]                                                                                                                                                                                       |
|                                                                                                                                                                                                                               |
| [      System.Diagnostics.Trace.WriteLine([\"GroupLevel = \"]+g.GroupLevel);]                                                                                      |
|                                                                                                                                                                                                                               |
| [      System.Diagnostics.Trace.WriteLine(g.Info);]                                                                                                                                       |
|                                                                                                                                                                                                                               |
| [      [foreach](Record r [in] g.Records)]                                                                                                      |
|                                                                                                                                                                                                                               |
| [      {]                                                                                                                                                                                 |
|                                                                                                                                                                                                                               |
| [            System.Diagnostics.Trace.WriteLine(r.Info);]                                                                                                                                 |
|                                                                                                                                                                                                                               |
| [      }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                               |
| [      [foreach](Group gr [in] g.Groups)]                                                                                                       |
|                                                                                                                                                                                                                               |
| [      {]                                                                                                                                                                                 |
|                                                                                                                                                                                                                               |
| [            iterate(gr);]                                                                                                                                                                |
|                                                                                                                                                                                                                               |
| [      }]                                                                                                                                                                                 |
|                                                                                                                                                                                                                               |
| [}]                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                     |
|                                                                                                                                                                                                    |
| []                                                                                                                                               |
|                                                                                                                                                                                                    |
| [\'Accessing a particular group and the categorized records under it  ]                                                                          |
|                                                                                                                                                                                                    |
| [    [Me].gridGroupingControl1.TableDescriptor.GroupedColumns.Add([\"Col1\"])]                                     |
|                                                                                                                                                                                                    |
| [\' Using category]                                                                                                                              |
|                                                                                                                                                                                                    |
| [    [Me].iterate([Me].gridGroupingControl1.Table.TopLevelGroup.Groups([\"row6 col1\"]))]     |
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

 

[]{#p710} 

 

[]{#related-topics}

