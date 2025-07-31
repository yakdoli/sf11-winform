---
title: codesnippettemplatetextchangingevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\codesnippettemplatetextchangingevent.md
created_at: 2025-07-03
---






#### CodeSnippetTemplateTextChanging Event {#codesnippettemplatetextchanging-event style="tab-stops: 0pt"}

 

This event is raised when the text of the code snippet template member is to be changed.

 

The event handler receives an argument of type **CodeSnippetTemplateTextChangingEventArgs**. The following CodeSnippetTemplateTextChangingEventArgs members provide information, specific to this event.

 


  -------------------- ------------------------------------------------
  Member               Description
  Cancel               Indicates whether action has to be canceled.
  CodeSnippet          Code snippet that is currently activated.
  NewText              New text.
  TemplateMemberName   Name of template member that is to be changed.
  -------------------- ------------------------------------------------


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                        |
| [// Change the text of all template members with defined name of currently activated code snippet.]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                        |
| [this][.editControl1.ChangeSnippetTemplateText([\" old member name\"], [\" new text\"]);]                                                                                           |
|                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                        |
| [// Handle the CodeSnippetTemplateTextChanging event.]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                        |
| [this][.editControl1.CodeSnippetTemplateTextChanging+=[new] Syncfusion.Windows.Forms.Edit.[CodeSnippetTemplateTextChangingEventHandler](editControl1_CodeSnippetTemplateTextChanging);] |
|                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                        |
| [private][ [void] editControl1_CodeSnippetTemplateTextChanging([object] sender, Syncfusion.Windows.Forms.Edit.[CodeSnippetTemplateTextChangingEventArgs] e)]       |
|                                                                                                                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                        |
| [// The below line will be displayed in the output window at runtime.]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                        |
| [Console][.WriteLine([\" CodeSnippetTemplateTextChanging event is raised \"]);]                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                        |
| [}]                                                                                                                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\' Change the text of all template members with defined name of currently activated code snippet.]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Me][.editControl1.ChangeSnippetTemplateText([\" old member name\"], [\" new text\"])]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\' Handle the CodeSnippetTemplateTextChanging event.]                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Me][.editControl1.CodeSnippetTemplateTextChanging+=[New] Syncfusion.Windows.Forms.Edit.CodeSnippetTemplateTextChangingEventHandler(editControl1_CodeSnippetTemplateTextChanging)]                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Private][ [Sub] editControl1_CodeSnippetTemplateTextChanging([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Windows.Forms.Edit.CodeSnippetTemplateTextChangingEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\' The below line will be displayed in the output window at runtime.]                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Console.WriteLine([\" CodeSnippetTemplateTextChanging event is raised \"])]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p116} 

[]{#related-topics}

