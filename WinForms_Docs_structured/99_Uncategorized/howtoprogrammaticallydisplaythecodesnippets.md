---
title: howtoprogrammaticallydisplaythecodesnippets.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoprogrammaticallydisplaythecodesnippets.md
created_at: 2025-07-03
---








  









## How To Programmatically Display the Code Snippets {#how-to-programmatically-display-the-code-snippets style="tab-stops: 0pt"}

[] 

You can display the code snippets programmatically by using the **StreamEditControl** class of Edit Control. The following code snippet illustrates this.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                      |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                |
|                                                                                                                                                                                                                                     |
| [private][ [void] editControl1_ReadOnlyChanged([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                     |
| [edit = ([StreamEditControl])sender;]                                                                                                                                      |
|                                                                                                                                                                                                                                     |
| [}]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [private][ [void] menuItem15_Click([object] sender, [EventArgs] e)]             |
|                                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                     |
| [edit.ShowCodeSnippets();]                                                                                                                                                                      |
|                                                                                                                                                                                                                                     |
| [}]                                                                                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                              |
| [Private][ [Sub] editControl1_ReadOnlyChanged([ByVal] sender [As] System.Object, [ByVal] e [As] System.EventArgs) [Handles] editControl1.ReadOnlyChanged] |
|                                                                                                                                                                                                                                                                                                                                                                              |
| [edit = [CType](sender, StreamEditControl)]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                              |
| [End][ [Sub]]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                              |
| [Private][ [Sub] MenuItem9_Click([ByVal] sender [As] System.Object, [ByVal] e [As] System.EventArgs) [Handles] MenuItem9.Click]                           |
|                                                                                                                                                                                                                                                                                                                                                                              |
| [edit.ShowCodeSnippets()]                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                              |
| [End][ [Sub]]                                                                                                                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p198} 

[]{#related-topics}

