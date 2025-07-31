---
title: previewkeydownevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\previewkeydownevent.md
created_at: 2025-07-03
---






#### PreviewKeyDown Event {#previewkeydown-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This event occurs before the KeyDown event when a key is pressed, while focus is on the TabControlAdv.

 

**Event Data**

 

This Event Handler receives an argument of type **EditEventArgs** containing data related to this event. The following EditEventArgs properties provide information specific to this event.

[] 


  ------------ ------------------------------------------------------------------------------------------------------------------
  Members      Description
  Alt          Gets a value indicating whether ALT key was pressed.
  Control      Gets a value indicating whether CTRL key was pressed.
  IsInputKey   Gets / sets a value indicating whether a key is a regular input key.
  KeyCode      Gets the keyboard code for a System.Windows.Forms.Controls.KeyUp / System.Windows.Forms.Controls.KeyDown event.
  KeyData      Gets the key data code for a System.Windows.Forms.Controls.KeyUp / System.Windows.Forms.Controls.KeyDown event.
  KeyValue     Gets the keyboard value for a System.Windows.Forms.Controls.KeyUp / System.Windows.Forms.Controls.KeyDown event.
  Modifiers    Gets the modifiers flag for a System.Windows.Forms.Controls.KeyUp / System.Windows.Forms.Controls.KeyDown event.
  Shift        Gets a value indicating whether SHIFT key was pressed.
  ------------ ------------------------------------------------------------------------------------------------------------------


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [private][ [void] tabControlAdv1_PreviewKeyDown([object] sender, System.Windows.Forms.[PreviewKeyDownEventArgs] e)]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [//Below line will be displayed in the output window at run-time, when this event is fired.]                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Console][.Write([\"PreviewKeyDown event is raised\"]);]                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [//The below code prints the KeyCode, KeyValue, KeyData and Modifiers in the output window at run-time.]                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Console][.Write([\"Key code :\"] + e.KeyCode.ToString() + [\"\\n\"] + [\"Key Value :\"] + e.KeyValue.ToString() + [\"\\n\"] + [\"Key Data:\"] + e.KeyData.ToString() + [\"\\n\"] + [\"Modifiers:\"] + e.Modifiers.ToString());] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [}]                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Private][ [Sub] tabControlAdv1_PreviewKeyDown([ByVal] sender [As] [Object], [ByVal] e [As] System.Windows.Forms.[PreviewKeyDownEventArgs])]                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [//Below line will be displayed in the output window at run-time, when this event is fired.]                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Console.Write([\"PreviewKeyDown event is raised\"])]                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\'The below code prints the Keycode, KeyValue, KeyData and Modifiers in the output window at run-time.]                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Console][.Write([\"Key code :\"] + e.KeyCode.ToString() + [\"\\n\"] + [\"Key Value :\"] + e.KeyValue.ToString() + [\"\\n\"] + [\"Key Data:\"] + e.KeyData.ToString() + [\"\\n\"] + [\"Modifiers:\"] + e.Modifiers.ToString())] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

