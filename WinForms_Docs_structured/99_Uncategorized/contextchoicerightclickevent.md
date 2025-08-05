---
title: contextchoicerightclickevent.md
original_path: WinForms_Docs/99_Uncategorized/contextchoicerightclickevent.md
created_at: 2025-08-05
---






#### ContextChoiceRightClick Event {#contextchoicerightclick-event style="tab-stops: 0pt"}

 

This event is raised when the context choice item is right-clicked.

 

The event handler receives an argument of type **ContextChoiceItemEventArgs**. The following CancellableCodeSnippetsEventArgs member provides information, specific to this event.

 


  -------- -------------------------------
  Member   Description
  Item     Underlying ContextChoiceItem.
  -------- -------------------------------


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                       |
| [private][ [void] editControl1_ContextChoiceRightClick(Syncfusion.Windows.Forms.Edit.Interfaces.[IContextChoiceController] sender, Syncfusion.Windows.Forms.Edit.[ContextChoiceItemEventArgs] e)] |
|                                                                                                                                                                                                                                                                                                                                                       |
| [{]                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                       |
| [e.Item.ForeColor = System.Drawing.[Color].Maroon;]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                       |
| [e.Item.BackColor = System.Drawing.[Color].MistyRose;]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                       |
| [MessageBox][.Show([\" ContextChoiceRightClick event is raised \"]);]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                       |
| [}]                                                                                                                                                                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Private][ [Sub] editControl1_ContextChoiceRightClick([ByVal] sender [As] Syncfusion.Windows.Forms.Edit.Interfaces.IContextChoiceController, [ByVal] e [As] Syncfusion.Windows.Forms.Edit.ContextChoiceItemEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [e.Item.ForeColor = System.Drawing.Color.Maroon]                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [e.Item.BackColor = System.Drawing.Color.MistyRose]                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [MessageBox.Show([\" ContextChoiceRightClick event is raised \"])]                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p129} 

[]{#related-topics}

