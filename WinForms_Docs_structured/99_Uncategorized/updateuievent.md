---
title: updateuievent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\updateuievent.md
created_at: 2025-07-03
---






##### UpdateUI Event {#updateui-event style="tab-stops: 0pt"}

[] 

UpdateUI event is handled when the mouse moves over the bar item or before it gets shown in a dropdown.

[] 


{border="0"} Note:[ ]This event will be handled only when BarManager.UpdateUIMFCStyle property or BarItem.UpdateUIOnAppIdle is enabled. These properties decides whether to handle this event or not.


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                           |
|                                                                                                                                                                                                          |
| **[]**                                                                                                                                                 |
|                                                                                                                                                                                                          |
| [//Sets the dropdown border color before it is pulled down]                                                                                            |
|                                                                                                                                                                                                          |
| [private][ [void] barItem1_UpdateUI([object] sender, System.EventArgs e)] |
|                                                                                                                                                                                                          |
| [{]                                                                                                                                                                  |
|                                                                                                                                                                                                          |
| [MenuColors][.DropDownBorderColor = [Color].Red;]                                              |
|                                                                                                                                                                                                          |
| [}]                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                       |
| [\'Sets the dropdown border color before it is pulled down]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                       |
| [Private][ [Sub] barItem1_UpdateUI([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)] |
|                                                                                                                                                                                                                                                                                                                       |
| [MenuColors][.DropDownBorderColor = [Color].Red]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                       |
| [End][ [Sub]]                                                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 850: DropDownBorderColor set by handling UpdateUI Event

**[]** 

See Also

**[]** 

UpdateUIMFCStyle and UpdateUIOnAppIdle properties in[ ][UI Command Update Patterns]{.UGHyperlink}[ ]topic.[]

[]{#related-topics}

