---
title: operationstoppedevent.md
original_path: WinForms_Docs/99_Uncategorized/operationstoppedevent.md
created_at: 2025-08-05
---






#### OperationStopped Event {#operationstopped-event style="tab-stops: 0pt"}

 

This event occurs when an operation ends.

 

The event handler receives an argument of type **ILongOperation**. The following ILongOperation members provide information, specific to this event.

 


  ------------------- ---------------------------------------------------------
  Member              Description
  ID                  Gets ID of the operation.
  IsRunning           Gets value indicating whether operation is running now.
  Name                Gets name of the operation.
  RunningTime         Gets time of the operation activity.
  ------------------- ---------------------------------------------------------


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                      |
| [private][ [void] editControl1_OperationStopped(Syncfusion.Windows.Forms.Edit.Interfaces.[ILongOperation] operation)] |
|                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                      |
| [Console][.WriteLine([\" OperationStopped event is raised \"]);]                                                                         |
|                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                     |
| [Private][ [Sub] editControl1_OperationStopped([ByVal] operation [As] Syncfusion.Windows.Forms.Edit.Interfaces.ILongOperation)] |
|                                                                                                                                                                                                                                                                                     |
| [Console.WriteLine([\" OperationStopped event is raised \"])]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                     |
| [End][ [Sub]]                                                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p149} 

 

[]{#related-topics}

