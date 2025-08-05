---
title: eventsofparentbaritem.md
original_path: WinForms_Docs/99_Uncategorized/eventsofparentbaritem.md
created_at: 2025-08-05
---






#### Events of ParentBarItem {#events-of-parentbaritem style="tab-stops: 0pt"}

[] 

ParentBarItem includes events of BarItem and also contains events discussed in this section.

[] 


+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| BarItem Events                              | Description                                                                                                                                                                                                                                  |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [BeforePopup]{.UGHyperlink}[]{.UGHyperlink} | This event is handled before the sub menu gets shown.                                                                                                                                                                                        |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Popup                                       | It is handled before the sub menu item\'s list of menu items is displayed.                                                                                                                                                                   |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PopupClosed                                 | It is handled just after the menu item has closed.                                                                                                                                                                                           |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PopupClosing                                | It is handled just before the dropdown gets closed. The event handler receives an argument of type CancelEventArgs containing data related to this event. The event property associated with the PopupClosing Event parameter is as follows. |
|                                             |                                                                                                                                                                                                                                              |
|                                             |                                                                                                                                                                                                                                              |
|                                             |                                                                                                                                                                                                                                              |
|                                             | Cancel - Gets/Sets a value indicating whether the event should be canceled.                                                                                                                                                                  |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Selected                                    | It is handled when the user selects a BarItem during menu navigation using mouse or keyboard.                                                                                                                                                |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


**[]** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                    |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                              |
|                                                                                                                                                                                                                   |
| [//Popup event handled before the popup is displayed]                                                                                                           |
|                                                                                                                                                                                                                   |
| [private][ [void] parentBarItem1_Popup([object] sender, System.EventArgs e)]       |
|                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                           |
|                                                                                                                                                                                                                   |
| [if][(sender [is] ParentBarItem)]                                                                       |
|                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                           |
|                                                                                                                                                                                                                   |
| [ParentBarItem barItem = sender [as] ParentBarItem;]                                                                                                     |
|                                                                                                                                                                                                                   |
| [Console.WriteLine(barItem.Text + \" Popup.\");]                                                                                                                              |
|                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                           |
|                                                                                                                                                                                                                   |
| [else]                                                                                                                                                           |
|                                                                                                                                                                                                                   |
| [Console.WriteLine(\"Unknown Item Popup.\");]                                                                                                                                 |
|                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                           |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                   |
| [//Popup event handled after the popup is closed.]                                                                                                              |
|                                                                                                                                                                                                                   |
| [private][ [void] parentBarItem1_PopupClosed([object] sender, System.EventArgs e)] |
|                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                           |
|                                                                                                                                                                                                                   |
| [if][(sender [is] ParentBarItem)]                                                                       |
|                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                           |
|                                                                                                                                                                                                                   |
| [ParentBarItem barItem = sender [as] ParentBarItem;]                                                                                                     |
|                                                                                                                                                                                                                   |
| [Console.WriteLine(barItem.Text + \" PopupClosed.\");]                                                                                                                        |
|                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                           |
|                                                                                                                                                                                                                   |
| [else]                                                                                                                                                           |
|                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                           |
|                                                                                                                                                                                                                   |
| [Console.WriteLine(\"Unknown Item PopupClosed.\");]                                                                                                                           |
|                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                           |
|                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                           |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                   |
| [//Displays Message when a menu item is selected]                                                                                                               |
|                                                                                                                                                                                                                   |
| [private][ [void] parentBarItem_Selected([object] sender, System.EventArgs e)]     |
|                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                           |
|                                                                                                                                                                                                                   |
| [if][(sender [is] ParentBarItem)]                                                                       |
|                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                           |
|                                                                                                                                                                                                                   |
| [ParentBarItem barItem = sender [as] ParentBarItem;]                                                                                                     |
|                                                                                                                                                                                                                   |
| [Console.WriteLine(barItem.Text + \" Selected.\");]                                                                                                                           |
|                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                           |
|                                                                                                                                                                                                                   |
| [else]                                                                                                                                                           |
|                                                                                                                                                                                                                   |
| [Console.WriteLine(\"Unknown Item Selected.\");]                                                                                                                              |
|                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                |
| [\'Popup - event handled before the popup is displayed]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                |
| [Private][ [Sub] parentBarItem1_Popup([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)]       |
|                                                                                                                                                                                                                                                                                                                                |
| [    [If] [TypeOf] sender [Is] ParentBarItem [Then]]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                |
| [        [Dim] barItem [As] ParentBarItem = [CType](IIf([TypeOf] sender [Is] ParentBarItem, sender, [Nothing]), ParentBarItem)]                              |
|                                                                                                                                                                                                                                                                                                                                |
| [        Console.WriteLine(barItem.Text & [\" Popup.\"])]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                |
| [    [Else]]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                |
| [        Console.WriteLine([\"Unknown Item Popup.\"])]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                |
| [    [End] [If]]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                |
| [End][ [Sub]]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                |
| [\'Popup event handled after the popup is closed]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                |
| [Private][ [Sub] parentBarItem1_PopupClosed([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                |
| [    [If] [TypeOf] sender [Is] ParentBarItem [Then]]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                |
| [        [Dim] barItem [As] ParentBarItem = [CType](IIf([TypeOf] sender [Is] ParentBarItem, sender, [Nothing]), ParentBarItem)]                              |
|                                                                                                                                                                                                                                                                                                                                |
| [        Console.WriteLine(barItem.Text & [\" PopupClosed.\"])]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                |
| [    [Else]]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                |
| [        Console.WriteLine([\"Unknown Item PopupClosed.\"])]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                |
| [    [End] [If]]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                |
| [End][ [Sub]]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                |
| [\'Displays Message when a menu item is selected]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                |
| [Private][ [Sub] parentBarItem_Selected([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)]     |
|                                                                                                                                                                                                                                                                                                                                |
| [    [If] [TypeOf] sender [Is] ParentBarItem [Then]]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                |
| [        [Dim] barItem [As] ParentBarItem = [CType](If([TypeOf] sender [Is] ParentBarItem, sender, [Nothing]), ParentBarItem)]                               |
|                                                                                                                                                                                                                                                                                                                                |
| [        Console.WriteLine(barItem.Text & [\" Selected.\"])]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                |
| [    [Else]]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                |
| [        Console.WriteLine([\"Unknown Item Selected.\"])]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                |
| [    [End] [If]]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                |
| [End][ [Sub]]                                                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

