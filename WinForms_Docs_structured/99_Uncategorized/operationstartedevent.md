---
title: operationstartedevent.md
original_path: WinForms_Docs/99_Uncategorized/operationstartedevent.md
created_at: 2025-08-05
---






#### OperationStarted Event {#operationstarted-event style="tab-stops: 0pt"}

 

This event occurs when an operation starts.

 

The event handler receives an argument of type **ILongOperation**. The following ILongOperation members provide information, specific to this event.

[] 


  ------------- ---------------------------------------------------------
  Member        Description
  ID            Gets ID of the operation.
  IsRunning     Gets value indicating whether operation is running now.
  Name          Gets name of the operation.
  RunningTime   Gets time of the operation activity.
  ------------- ---------------------------------------------------------


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                      |
| [private][ [void] editControl1_OperationStarted(Syncfusion.Windows.Forms.Edit.Interfaces.[ILongOperation] operation)] |
|                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                      |
| [Console][.WriteLine([\" OperationStarted event is raised \"]);]                                                                         |
|                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                     |
| [Private][ [Sub] editControl1_OperationStarted([ByVal] operation [As] Syncfusion.Windows.Forms.Edit.Interfaces.ILongOperation)] |
|                                                                                                                                                                                                                                                                                     |
| [Console.WriteLine([\" OperationStarted event is raised \"])]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                     |
| [End][ [Sub]]                                                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p148} 

[]{#related-topics}

