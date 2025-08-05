---
title: savestreamwithdatalossevent.md
original_path: WinForms_Docs/03_Data_Binding/savestreamwithdatalossevent.md
created_at: 2025-08-05
---






#### SaveStreamWithDataLoss Event {#savestreamwithdataloss-event style="tab-stops: 0pt"}

 

This event is raised when user tries to save streams with data loss.

 

The event handler receives an argument of type **SaveWithDataLosingEventArgs**. The following SaveWithDataLosingEventArgs members provide information, specific to this event.

 


  -------------- --------------------------------------------------------------------------
  Member         Description
  SaveWithLoss   Gets / sets value that indicates whether data has to be saved with loss.
  UserHandling   Gets / sets value that indicates whether user handled the event.
  -------------- --------------------------------------------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                            |
| [private][ [void] editControl1_SaveStreamWithDataLoss([object] sender, Syncfusion.Windows.Forms.Edit.[SaveWithDataLosingEventArgs] e)] |
|                                                                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                            |
| [e.SaveWithLoss = [true];]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                            |
| [e.UserHandling = [true];]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [Private][ [Sub] editControl1_SaveStreamWithDataLoss([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Windows.Forms.Edit.SaveWithDataLosingEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [e.SaveWithLoss = [True]]                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [e.UserHandling = [True]]                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [End][ [Sub]]                                                                                                                                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p166}[] 

[]{#related-topics}

