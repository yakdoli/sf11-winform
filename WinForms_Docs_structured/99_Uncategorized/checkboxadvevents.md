---
title: checkboxadvevents.md
original_path: WinForms_Docs/99_Uncategorized/checkboxadvevents.md
created_at: 2025-08-05
---






##### CheckBoxAdv Events {#checkboxadv-events style="tab-stops: 0pt"}

[] 

A detailed explanation about the **CheckStateChanged** event is given in the following section.

[] 


  -------------------- ------------------------------------------------------------
  CheckBoxAdv Events   Description
  CheckStateChanged    This event occurs when the CheckState property is changed.
  CheckedChanged       This event is raised when the Checked property is changed.
  -------------------- ------------------------------------------------------------


###### []{#p781}3.3.11.1.4.1        CheckStateChanged Event {#checkstatechanged-event style="tab-stops: 0pt"}

[] 

This event occurs when the **CheckState** property is changed.

 

The event handler receives an argument of type **EventArgs** containing data related to this event.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                           |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                     |
|                                                                                                                                                                                                                                          |
| [private][ [void] checkBoxAdv1_CheckStateChanged([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                          |
| [Console][.WriteLine([\" CheckStateChanged event is raised\"]);]                                                         |
|                                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                             |
| [Private][ [Sub] checkBoxAdv1_CheckStateChanged([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                             |
| [Console.WriteLine([\" CheckStateChanged event is raised\"])]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                             |
| [End][ [Sub]]                                                                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

###### 3.3.11.1.4.2        CheckedChanged Event {#checkedchanged-event style="tab-stops: 0pt"}

[]{#p782} 

This event is raised when the **Checked** property is changed. Checked property changes automatically, when the CheckedState property is changed.

 

The event handler receives an argument of type **CheckedChangedEventArgs** containing data related to this event. The member, **Source** of this argument, allows you to check the SourceType. Refer to the below code snippet.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                    |
| [private][ [void] checkBoxAdv1_CheckedChanged([object] sender, Syncfusion.Windows.Forms.Tools.[CheckedChangedEventArgs] e)] |
|                                                                                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                    |
| [    [if] (e.Source == [CheckedChangedEventArgs].SourceType.Mouse)]                                                                                                                               |
|                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                    |
| [        [Console].WriteLine([\"Using Mouse\"]);]                                                                                                                                              |
|                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                    |
| [    [else] [if] (e.Source == [CheckedChangedEventArgs].SourceType.Keyboard)]                                                                                                |
|                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                    |
| [        [Console].WriteLine([\"Using Keyboard\"]);]                                                                                                                                           |
|                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                    |
| [    [else] [if] (e.Source == [CheckedChangedEventArgs].SourceType.Programmatic)]                                                                                            |
|                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                    |
| [        [Console].WriteLine([\"Using Code\"]);]                                                                                                                                               |
|                                                                                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [Private][ [Sub] checkBoxAdv1_CheckedChanged([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Windows.Forms.Tools.CheckedChangedEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [    [If] e.Source = CheckedChangedEventArgs.SourceType.Mouse [Then]]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [        Console.WriteLine([\"Using Mouse\"])]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [    [ElseIf] e.Source = CheckedChangedEventArgs.SourceType.Keyboard [Then]]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [        Console.WriteLine([\"Using Keyboard\"])]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [    [ElseIf] e.Source = CheckedChangedEventArgs.SourceType.Programmatic [Then]]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [        Console.WriteLine([\"Using Code\"])]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [    [End] [If]]                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [End][ [Sub]]                                                                                                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

