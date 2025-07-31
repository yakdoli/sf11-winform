---
title: howtoaccessthegroupfromthedisplayelements.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoaccessthegroupfromthedisplayelements.md
created_at: 2025-07-03
---






#### How to access the group from the DisplayElements {#how-to-access-the-group-from-the-displayelements style="tab-stops: 0pt"}

[] 

To access the group from the DisplayElements, use the following code snippet.

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

 

[]{#p711} 

 

[]{#related-topics}

