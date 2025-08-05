---
title: whataretheeventsfiredwhentherecordsareexpandedexpanding.md
original_path: WinForms_Docs/99_Uncategorized/whataretheeventsfiredwhentherecordsareexpandedexpanding.md
created_at: 2025-08-05
---






#### What are the events fired when the records are expanded / expanding? {#what-are-the-events-fired-when-the-records-are-expanded-expanding style="tab-stops: 0pt"}

[] 

When the records are expanding or expanded, the following events are fired.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                |
| [// The RecordExpanded event gets fired after the record is expanded]                                                                                                                        |
|                                                                                                                                                                                                                                                |
| [private][ [void] gridGroupingControl1_RecordExpanded([object] sender, Syncfusion.Grouping.RecordEventArgs e)]  |
|                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                |
| [      Console.WriteLine([\"Expanded\"]+ e.Record.Info);]                                                                                                                           |
|                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                |
| [// The RecordExpanding event gets fired when the record is expanding]                                                                                                                       |
|                                                                                                                                                                                                                                                |
| [private][ [void] gridGroupingControl1_RecordExpanding([object] sender, Syncfusion.Grouping.RecordEventArgs e)] |
|                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                |
| [      Console.WriteLine([\"Expanding\"]+ e.Record.Info);]                                                                                                                          |
|                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\' The RecordExpanded event gets fired after the record is expanded]                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Private][ [Sub] gridGroupingControl1_RecordExpanded([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Grouping.RecordEventArgs) [Handles] gridGroupingControl1.RecordExpanded]   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [    Console.WriteLine([\"Expanded\"] + e.Record.Info)]                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\' The RecordExpanding event gets fired when the record is expanding]                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Private][ [Sub] gridGroupingControl1_RecordExpanding([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Grouping.RecordEventArgs) [Handles] gridGroupingControl1.RecordExpanding] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [    Console.WriteLine([\"Expanding\"] + e.Record.Info)]                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: This applies only when nested tables are used.


 

[]{#p703} 

 

[]{#related-topics}

