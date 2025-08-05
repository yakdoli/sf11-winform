---
title: eventsofbaritem.md
original_path: WinForms_Docs/99_Uncategorized/eventsofbaritem.md
created_at: 2025-08-05
---






#### Events of BarItem {#events-of-baritem style="tab-stops: 0pt"}

[] 

This section discusses the events of bar item.

[] 


  ---------------- -----------------------------------------------------------------------------------------------------
  BarItem Events   Description
  Click            It is handled when the bar item is clicked by the user.
  DoubleClick      It is handled when the bar item is double clicked by the user.
  Selected         It is handled when the user selects a bar item during menu navigation using mouse or keyboard.
  UnSelected       It is handled when the bar item has been unselected during menu navigation using mouse or keyboard.
  ---------------- -----------------------------------------------------------------------------------------------------


**[]** 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                             |
|                                                                                                                                                                                                            |
| **[]**                                                                                                                                                   |
|                                                                                                                                                                                                            |
| [//Enable themes when a BarItem is clicked]                                                                                                              |
|                                                                                                                                                                                                            |
| [private][ [void] barItem_Click([object] sender, System.EventArgs e)]       |
|                                                                                                                                                                                                            |
| [{]                                                                                                                                                                    |
|                                                                                                                                                                                                            |
| [this][.barManager1.ThemesEnabled = [true];]                                                     |
|                                                                                                                                                                                                            |
| [}]                                                                                                                                                                    |
|                                                                                                                                                                                                            |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                            |
| [//Disable themes when a BarItem is double clicked]                                                                                                      |
|                                                                                                                                                                                                            |
| [private][ [void] barItem_Click([object] sender, System.EventArgs e)]       |
|                                                                                                                                                                                                            |
| [{]                                                                                                                                                                    |
|                                                                                                                                                                                                            |
| [this][.barManager1.ThemesEnabled = [true];]                                                     |
|                                                                                                                                                                                                            |
| [}]                                                                                                                                                                    |
|                                                                                                                                                                                                            |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                            |
| [//Displays the text of selected BarItem in the status bar]                                                                                              |
|                                                                                                                                                                                                            |
| [private][ [void] barItem_Selected([object] sender, System.EventArgs e)]    |
|                                                                                                                                                                                                            |
| [{]                                                                                                                                                                    |
|                                                                                                                                                                                                            |
| [BarItem item = sender [as] BarItem;]                                                                                                             |
|                                                                                                                                                                                                            |
| [this][.staticBarItem1.Text = item.Text;]                                                                             |
|                                                                                                                                                                                                            |
| [}]                                                                                                                                                                    |
|                                                                                                                                                                                                            |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                            |
| [private][ [void] barItem1_Unselected([object] sender, System.EventArgs e)] |
|                                                                                                                                                                                                            |
| [{]                                                                                                                                                                    |
|                                                                                                                                                                                                            |
| [ParentBarItem barItem = sender [as] BarItem;]                                                                                                    |
|                                                                                                                                                                                                            |
| [Console.WriteLine(barItem.Text + \" Unselected.\");]                                                                                                                  |
|                                                                                                                                                                                                            |
| [}]                                                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                         |
| [\'Enable themes when a BarItem is clicked]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                         |
| [Private][ [Sub] barItem_Click([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)]       |
|                                                                                                                                                                                                                                                                                                                         |
| [Me][.barManager1.ThemesEnabled = [true]]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                         |
| [End][ [Sub]]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                         |
| [\'Disable themes when a BarItem is double clicked]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                         |
| [Private][ [Sub] barItem_Click([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)]       |
|                                                                                                                                                                                                                                                                                                                         |
| [Me][.barManager1.ThemesEnabled = [true]]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                         |
| [End][ [Sub]]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                         |
| [\'Displays the text of selected BarItem in the status bar]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                         |
| [Private][ [Sub] barItem_Selected([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)]    |
|                                                                                                                                                                                                                                                                                                                         |
| [    [Dim] item [As] BarItem = [CType](IIf([TypeOf] sender [Is] BarItem, sender, [Nothing]), BarItem)]                                                |
|                                                                                                                                                                                                                                                                                                                         |
| [    [Me].staticBarItem1.Text = item.Text]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                         |
| [End][ [Sub]]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                         |
| [Private][ [Sub] barItem1_Unselected([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)] |
|                                                                                                                                                                                                                                                                                                                         |
| [    [Dim] barItem [As] ParentBarItem = [CType](IIf([TypeOf] sender [Is] BarItem, sender, [Nothing]), BarItem)]                                       |
|                                                                                                                                                                                                                                                                                                                         |
| [    Console.WriteLine(barItem.Text & [\" Unselected.\"])]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                         |
| [End][ [Sub]]                                                                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

More:





