---
title: radiobuttonadvevents.md
original_path: WinForms_Docs/99_Uncategorized/radiobuttonadvevents.md
created_at: 2025-08-05
---






##### RadioButtonAdv Events      {#radiobuttonadv-events style="tab-stops: 0pt"}

[] 

The list of events and a detailed explanation about each of them is given in the following sections.

[] 


  ----------------------- -------------------------------------------------------------------------------------------
  RadioButtonAdv Events   Description
  CheckChanged            This event is fired when the Checked property of the RadioButtonAdv changes.
  GroupCheckChanged       This event is fired when the Checked property of the RadioButtonAdv in the group changes.
  ----------------------- -------------------------------------------------------------------------------------------


###### []{#p803}3.3.11.2.4.1        CheckChanged Event {#checkchanged-event style="tab-stops: 0pt"}

[] 

This event is fired when the **Checked** property of the RadioButtonAdv changes.

 

The event handler receives an argument of type **EventArgs** containing data related to this event.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                                        |
| [private][ [void] radioButtonAdv1_CheckChanged([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                        |
| [Console][.WriteLine([\" CheckChanged event is raised\"]);]                                                            |
|                                                                                                                                                                                                                                        |
| [}]                                                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                           |
| [Private][ [Sub] radioButtonAdv1_CheckChanged([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                           |
| [Console.WriteLine([\" CheckChanged event is raised\"])]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                           |
| [End][ [Sub]]                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

###### []{#p804}3.3.11.2.4.2        GroupCheckChanged Event {#groupcheckchanged-event style="tab-stops: 0pt"}

[] 

This event is fired when the Checked property of the RadioButtonAdv in the group changes.

 

The event handler receives an argument of type EventArgs containing data related to this event.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                              |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [private][ [void] radioButtonAdv1_GroupCheckChanged([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| [Console][.WriteLine([\" GroupCheckChanged event is raised\"]);]                                                            |
|                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                |
| [Private][ [Sub] radioButtonAdv1_GroupCheckChanged([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                |
| [Console.WriteLine([\" GroupCheckChanged event is raised\"])]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                |
| [End][ [Sub]]                                                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p805}[]{#_Layout_Managers_Package} 

 

[]{#related-topics}

