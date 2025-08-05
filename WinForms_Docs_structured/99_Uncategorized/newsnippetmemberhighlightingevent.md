---
title: newsnippetmemberhighlightingevent.md
original_path: WinForms_Docs/99_Uncategorized/newsnippetmemberhighlightingevent.md
created_at: 2025-08-05
---






#### NewSnippetMemberHighlighting Event {#newsnippetmemberhighlighting-event style="tab-stops: 0pt"}

 

This event is raised when a new code snippet member is highlighted.

 

The event handler receives an argument of type **NewSnippetMemberHighlightingEventArgs**. The following NewSnippetMemberHighlightingEventArgs members provide information, specific to this event.

 


  ------------------ -----------------------------------------------
  Member             Description
  Cancel             Indicates whether action has to be cancelled.
  CodeSnippet        Code snippet that is currently activated.
  NewSnippetMember   Snippet member that has to be highlighted.
  OldSnippetMember   Previously highlighted snippet member.
  ------------------ -----------------------------------------------


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                            |
| [private][ [void] editControl1_NewSnippetMemberHighlighting([object] sender, Syncfusion.Windows.Forms.Edit.[NewSnippetMemberHighlightingEventArgs] e)] |
|                                                                                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                            |
| [// The below line will be displayed in the output window at runtime.]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                            |
| [Console][.WriteLine([\" NewSnippetMemberHighlighting event is raised \"]);]                                                                                                                   |
|                                                                                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Private][ [Sub] editControl1_NewSnippetMemberHighlighting([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Windows.Forms.Edit.NewSnippetMemberHighlightingEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\' The below line will be displayed in the output window at runtime.]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Console.WriteLine([\" NewSnippetMemberHighlighting event is raised \"])]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                  |
| [End][ [Sub]]                                                                                                                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p117} 

[]{#related-topics}

