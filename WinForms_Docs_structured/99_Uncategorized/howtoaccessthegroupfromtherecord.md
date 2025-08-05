---
title: howtoaccessthegroupfromtherecord.md
original_path: WinForms_Docs/99_Uncategorized/howtoaccessthegroupfromtherecord.md
created_at: 2025-08-05
---






#### How to access the group from the Record {#how-to-access-the-group-from-the-record style="tab-stops: 0pt"}

[] 

To access the group from the record, use the following code snippet.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                    |
|                                                                                                                                                                                   |
| []                                                                                                                              |
|                                                                                                                                                                                   |
| [// For all the display elements in the Table]                                                                                  |
|                                                                                                                                                                                   |
| [foreach][(Element el [in] gridGroupingControl1.Table.DisplayElements)] |
|                                                                                                                                                                                   |
| [{     ]                                                                                                                                      |
|                                                                                                                                                                                   |
| [      [// DisplayElementKind.Record or DisplayElementKind.Summary]]                                                    |
|                                                                                                                                                                                   |
| [      [if](el.Kind==DisplayElementKind.Record \|\| DisplayElementKind.Summary)]                                         |
|                                                                                                                                                                                   |
| [      {]                                                                                                                                     |
|                                                                                                                                                                                   |
| [            Group g = el.ParentGroup;]                                                                                                       |
|                                                                                                                                                                                   |
| [            System.Diagnostics.Trace.WriteLine(g.Info);]                                                                                     |
|                                                                                                                                                                                   |
| [      }]                                                                                                                                     |
|                                                                                                                                                                                   |
| [}]                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                     |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                                    |
| [\' For all the display elements in the Table]                                                                                                                                   |
|                                                                                                                                                                                                                                    |
| [For][ [Each] el [As] Element [In] gridGroupingControl1.Table.DisplayElements] |
|                                                                                                                                                                                                                                    |
| [\' DisplayElementKind.Record or DisplayElementKind.Summary]                                                                                                                     |
|                                                                                                                                                                                                                                    |
| [    [If] el.Kind=DisplayElementKind.Record [OrElse] el.Kind=DisplayElementKind.Summary [Then]]                                 |
|                                                                                                                                                                                                                                    |
| [    Dim][ g [As] Group = el.ParentGroup]                                                                                |
|                                                                                                                                                                                                                                    |
| [         System.Diagnostics.Trace.WriteLine(g.Info)]                                                                                                                                          |
|                                                                                                                                                                                                                                    |
| [     [End] [If]]                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [Next][ el]                                                                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p712} 

 

[]{#related-topics}

