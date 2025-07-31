---
title: beforeeditevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\beforeeditevent.md
created_at: 2025-07-03
---






#### BeforeEdit Event {#beforeedit-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This event occurs when the text enters into Edit mode.

[] 

Event Data

 

This Event Handler receives an argument of type EditEventArgs containing data related to this event. The following EditEventArgs property provides information specific to this event.

[] 


  ---------- -----------------------
  Member     Description
  EditText   Gets the edited text.
  ---------- -----------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                          |
| [private][ [void] tabControlAdv1_BeforeEditEvent([object] sender, Syncfusion.Windows.Forms.Tools.[EditEventArgs] e)] |
|                                                                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                          |
| [//Below line will be displayed in the output window, when this event is fired.]                                                                                                                                       |
|                                                                                                                                                                                                                                                                          |
| [Console][.Write([\"BeforeEdit event is triggered\"]);]                                                                                                      |
|                                                                                                                                                                                                                                                                          |
| [//Gets the edited text in the output window.]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                          |
| [Console][.Write([\"Edit text :\"] + e.EditText.ToString());]                                                                                                |
|                                                                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                       |
| [Private][ [Sub] tabControlAdv1_BeforeEditEvent([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Windows.Forms.Tools.[EditEventArgs])] |
|                                                                                                                                                                                                                                                                                                                                                                                       |
| [\'Below line will be displayed in the output window, when this event is fired.]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                       |
| [Console][.Write([\"BeforeEdit event is triggered\"])]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                       |
| [\'Gets the edited text in the output window.]                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                       |
| [Console][.Write([\"Edit text :\"] + e.EditText.ToString())]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                       |
| [End][ [Sub]]                                                                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

