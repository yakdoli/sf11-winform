---
title: codesnippetdeactivatingevent.md
original_path: WinForms_Docs/99_Uncategorized/codesnippetdeactivatingevent.md
created_at: 2025-08-05
---






#### CodeSnippetDeactivating Event {#codesnippetdeactivating-event style="tab-stops: 0pt"}

 

This event occurs when the code snippet is to be deactivated.

 

The event handler receives an argument of type **CodeSnippetsEventArgs**. The following CodeSnippetsEventArgs member provides information, specific to this event.

 


  ------------- -------------------------------------------
  Member        Description
  CodeSnippet   Code snippet that is currently activated.
  ------------- -------------------------------------------


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                       |
| [private][ [void] editControl1_CodeSnippetDeactivating([object] sender, Syncfusion.Windows.Forms.Edit.[CodeSnippetsEventArgs] e)] |
|                                                                                                                                                                                                                                                                                       |
| [{]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                       |
| [// The below line will be displayed in the output window at runtime.]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                       |
| [Console][.WriteLine([\" CodeSnippetDeactivating event is raised \"]);]                                                                                                   |
|                                                                                                                                                                                                                                                                                       |
| [}]                                                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [Private][ [Sub] editControl1_CodeSnippetDeactivating([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Windows.Forms.Edit.CodeSnippetsEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [\' The below line will be displayed in the output window at runtime.]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [Console.WriteLine([\" CodeSnippetDeactivating event is raised \"])]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [End][ [Sub]]                                                                                                                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p115} 

[]{#related-topics}

