---
title: whataretheeventsfiredwhentherecordvaluesarechanged.md
original_path: WinForms_Docs/99_Uncategorized/whataretheeventsfiredwhentherecordvaluesarechanged.md
created_at: 2025-08-05
---






#### What are the events fired when the record values are changed? {#what-are-the-events-fired-when-the-record-values-are-changed style="tab-stops: 0pt"}

[] 

When the record values are changed, the following events are fired.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                |
| [// The RecordValueChanged event gets fired after the record\'s value is changed.]                                                                                                                           |
|                                                                                                                                                                                                                                                                |
| [private][ [void] gridGroupingControl1_RecordValueChanged([object] sender,Syncfusion.Grouping.RecordValueChangedEventArgs e)]   |
|                                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                |
| [      Console.WriteLine([\"Changed \"]+e.Record.Info);]                                                                                                                                            |
|                                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                |
| [// The RecordValueChanging event gets fired while the record\'s value is changing.]                                                                                                                         |
|                                                                                                                                                                                                                                                                |
| [private][ [void] gridGroupingControl1_RecordValueChanging([object] sender,Syncfusion.Grouping.RecordValueChangingEventArgs e)] |
|                                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                |
| [      Console.WriteLine([\"Changing \"]+e.Record.Info);]                                                                                                                                           |
|                                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\' The RecordValueChanged event gets fired after the record\'s value is changed.]                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Private][ [Sub] gridGroupingControl1_RecordValueChanged([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Grouping.RecordValueChangedEventArgs) [Handles] gridGroupingControl1.RecordValueChanged]    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [    Console.WriteLine([\"Changed \"] + e.Record.Info)]                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\' The RecordValueChanging event gets fired while the record\'s value is changing.]                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Private][ [Sub] gridGroupingControl1_RecordValueChanging([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Grouping.RecordValueChangingEventArgs) [Handles] gridGroupingControl1.RecordValueChanging] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [    Console.WriteLine([\"Changing \"] + e.Record.Info)]                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p704} 

 

[]{#related-topics}

