---
title: whataretheeventsfiredwhenthegroupisexpandedexpanding.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\whataretheeventsfiredwhenthegroupisexpandedexpanding.md
created_at: 2025-07-03
---






#### What are the events fired when the group is expanded / expanding? {#what-are-the-events-fired-when-the-group-is-expanded-expanding style="tab-stops: 0pt"}

[] 

Following are the events fired when the group is expanding or expanded.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                              |
| [//Shows the GroupExpanding event.]                                                                                                                                                        |
|                                                                                                                                                                                                                                              |
| [private][ [void] gridGroupingControl1_GroupExpanding([object] sender, Syncfusion.Grouping.GroupEventArgs e)] |
|                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                              |
| [// Shows all the records in the group which is being Expanded.]                                                                                                                           |
|                                                                                                                                                                                                                                              |
| [foreach][(Record r [in] e.Group.Records)]                                                                                         |
|                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                              |
| [Console.WriteLine([\"Expanding event \"]+r.Info);]                                                                                                                               |
|                                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                              |
| [//Shows the GroupExpanded event.]                                                                                                                                                         |
|                                                                                                                                                                                                                                              |
| [private][ [void] gridGroupingControl1_GroupExpanded([object] sender, Syncfusion.Grouping.GroupEventArgs e)]  |
|                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                              |
| [// Shows all the records in the group which has expanded.]                                                                                                                                |
|                                                                                                                                                                                                                                              |
| [foreach][(Record r [in] e.Group.Records)]                                                                                         |
|                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                              |
| [Console.WriteLine([\"Expanded event \"]+r.Info);]                                                                                                                                |
|                                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                              |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                                              |
| [//Shows the GroupExpanding event.]                                                                                                                                                        |
|                                                                                                                                                                                                                                              |
| [private][ [void] gridGroupingControl1_GroupExpanding([object] sender, Syncfusion.Grouping.GroupEventArgs e)] |
|                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                              |
| [    [// Shows all the records in the group which is being Expanded.]]                                                                                                             |
|                                                                                                                                                                                                                                              |
| [    [foreach](Record r [in] e.Group.Records)]                                                                                                                 |
|                                                                                                                                                                                                                                              |
| [    {]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                              |
| [        Console.WriteLine([\"Expanding event \"]+r.Info);]                                                                                                                       |
|                                                                                                                                                                                                                                              |
| [    }]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                              |
| [ [//Shows the GroupExpanded event.]]                                                                                                                                              |
|                                                                                                                                                                                                                                              |
| [private][ [void] gridGroupingControl1_GroupExpanded([object] sender, Syncfusion.Grouping.GroupEventArgs e)]  |
|                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                              |
| [    [// Shows all the records in the group which has expanded.]]                                                                                                                  |
|                                                                                                                                                                                                                                              |
| [    [foreach](Record r [in] e.Group.Records)]                                                                                                                 |
|                                                                                                                                                                                                                                              |
| [    {]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                              |
| [        Console.WriteLine([\"Expanded event \"]+r.Info);]                                                                                                                        |
|                                                                                                                                                                                                                                              |
| [    }]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

