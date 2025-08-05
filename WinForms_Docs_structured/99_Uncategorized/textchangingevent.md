---
title: textchangingevent.md
original_path: WinForms_Docs/99_Uncategorized/textchangingevent.md
created_at: 2025-08-05
---






#### TextChanging Event {#textchanging-event style="tab-stops: 0pt"}

 

This event is raised when the text is to be changed.

 

The event handler receives an argument of type **TextChangingEventArgs**. The following TextChangingEventArgs members provide information, specific to this event.

 


  ------------- -------------------------------------------------------------------------------------------
  Member        Description
  Cancel        Gets/sets the value indicating whether text change has been canceled.
  StartColumn   Gets/sets virtual column of Insert/Delete start.
  StartLine     Gets/sets virtual line of Insert/Delete start.
  Text          Gets/sets event\'s text.
  Type          Gets/sets type of the event (Changed/Insert/Delete). It includes the below given options.
  ------------- -------------------------------------------------------------------------------------------


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                            |
| [private][ [void] editControl1_TextChanging([object] sender, Syncfusion.Windows.Forms.Edit.[TextChangingEventArgs] e)] |
|                                                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                            |
| [e.Type = Syncfusion.Windows.Forms.Edit.Enums.[TextChange].Deleted;]                                                                                                                                              |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                            |
| [// The below statement can be seen in the output window at runtime when the text of the Edit Control is deleted.]                                                                                                       |
|                                                                                                                                                                                                                                                                            |
| [Console][.WriteLine([\" TextChanging event is raised \"]);]                                                                                                   |
|                                                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [Private][ [Sub] editControl1_TextChanging([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Windows.Forms.Edit.TextChangingEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [e.Type = Syncfusion.Windows.Forms.Edit.Enums.TextChange.Deleted]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [\' The below statement can be seen in the output window at runtime when the text of the Edit Control is deleted. ]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [Console.WriteLine([\" TextChanging event is raised \"])]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [End][ [Sub]]                                                                                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p174} 

[]{#related-topics}

