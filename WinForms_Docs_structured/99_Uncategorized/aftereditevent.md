---
title: aftereditevent.md
original_path: WinForms_Docs/99_Uncategorized/aftereditevent.md
created_at: 2025-08-05
---






#### AfterEdit Event {#afteredit-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This event occurs after text editing is complete. It is fired even if no changes are made.

[] 

Event Data

 

The Edit Event Handler receives an argument of type EditEventArgs containing data related to this event. The following EditEventArgs property provides information specific to this event.

[] 


  ---------- -----------------------
  Member     Description
  EditText   Gets the edited text.
  ---------- -----------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                    |
| [private][ [void] tabControlAdv1_AfterEdit([object] sender, Syncfusion.Windows.Forms.Tools.[EditEventArgs] e)] |
|                                                                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                    |
| [//Below line will be displayed in the output window at run-time, when this event is fired.]                                                                                                                     |
|                                                                                                                                                                                                                                                                    |
| [Console][.Write([\" AfterEdit event is triggered\"]);]                                                                                                |
|                                                                                                                                                                                                                                                                    |
| [//Gets the edited text in the output window.]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                    |
| [Console][.Write([\"Edit text :\"] + e.EditText.ToString());                ]                                                                          |
|                                                                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [Private][ [Sub] tabControlAdv1_AfterEditEvent([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Windows.Forms.Tools.[EditEventArgs])] |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [\'Below line will be displayed in the output window at run-time, when this event is fired.]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [Console][.Write([\" AfterEdit event is triggered\"])]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [\'Gets the edited text in the output window.]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [Console][.Write([\"Edit text :\"] + e.EditText.ToString())]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [End][ [Sub]]                                                                                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

