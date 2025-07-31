---
title: codesnippetactivatingevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\codesnippetactivatingevent.md
created_at: 2025-07-03
---






#### CodeSnippetActivating Event {#codesnippetactivating-event style="tab-stops: 0pt"}

 

This event occurs when the code snippet is to be activated.

 

The event handler receives an argument of type **CancellableCodeSnippetsEventArgs**. The following CancellableCodeSnippetsEventArgs members provide information, specific to this event.

 


  ------------- -----------------------------------------------
  Member        Description
  Cancel        Indicates whether action has to be cancelled.
  CodeSnippet   Code snippet that is currently activated.
  ------------- -----------------------------------------------


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                |
| [private][ [void] editControl1_CodeSnippetActivating([object] sender, Syncfusion.Windows.Forms.Edit.[CancellableCodeSnippetsEventArgs] e)] |
|                                                                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                |
| [  [// The below line will be displayed in the output window at runtime.]]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                |
| [Console][.WriteLine([\" CodeSnippetActivating event is raised \"]);]                                                                                                              |
|                                                                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [Private][ [Sub] editControl1_CodeSnippetActivating([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Windows.Forms.Edit.CancellableCodeSnippetsEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [\' The below line will be displayed in the output window at runtime.]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [Console.WriteLine([\" CodeSnippetActivating event is raised \"])]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [End][ [Sub]]                                                                                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p114} 

[]{#related-topics}

