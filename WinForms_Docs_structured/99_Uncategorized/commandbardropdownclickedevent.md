---
title: commandbardropdownclickedevent.md
original_path: WinForms_Docs/99_Uncategorized/commandbardropdownclickedevent.md
created_at: 2025-08-05
---






##### CommandBarDropDownClicked Event {#commandbardropdownclicked-event style="tab-stops: 0pt"}

[]{#p33} 

This event is raised when the dropdown button of a CommandBar is clicked.

 

The event handler receives an argument of type **EventArgs**[ ]containing data related to this event.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                              |
| [// Add a PopupMenu control and assign it to the PopupMenu property of the CommandBar.]                                                                                                    |
|                                                                                                                                                                                                                                              |
| [this][.commandBar1.PopupMenu = [this].popupMenu1;]                                                                                |
|                                                                                                                                                                                                                                              |
| [// Add a ParentBarItem to the PopupMenu.]                                                                                                                                                 |
|                                                                                                                                                                                                                                              |
| [this][.popupMenu1.ParentBarItem = [this].parentBarItem1;]                                                                         |
|                                                                                                                                                                                                                                              |
| [// Add items to the ParentBarItem.]                                                                                                                                                       |
|                                                                                                                                                                                                                                              |
| [this][.parentBarItem1.Items.AddRange([new] Syncfusion.Windows.Forms.Tools.XPMenus.BarItem\[\] {]                                  |
|                                                                                                                                                                                                                                              |
| [this][.barItem1,]                                                                                                                                      |
|                                                                                                                                                                                                                                              |
| [this][.barItem2,]                                                                                                                                      |
|                                                                                                                                                                                                                                              |
| [this][.barItem3});]                                                                                                                                    |
|                                                                                                                                                                                                                                              |
| [this][.barItem1.Text = [\"Windows Forms Samples\"];]                                                                            |
|                                                                                                                                                                                                                                              |
| [this][.barItem2.Text = [\"ASP.NET Samples\"];]                                                                                  |
|                                                                                                                                                                                                                                              |
| [this][.barItem3.Text = [\"WPF Samples\"];]                                                                                      |
|                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                              |
| [// Handle the CommandBarDropDownClicked event.]                                                                                                                                           |
|                                                                                                                                                                                                                                              |
| [this][.commandBar1.CommandBarDropDownClicked+=[new]  [EventHandler](commandBar1_CommandBarDropDownClicked);] |
|                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                              |
| [private][ [void] commandBar1_CommandBarDropDownClicked([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                              |
| [// The below line will be displayed in the output window at runtime.]                                                                                                                     |
|                                                                                                                                                                                                                                              |
| [Console][.WriteLine([\" CommandBarDropDownClicked event is raised \"]);]                                                        |
|                                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                    |
| [\' Add a PopupMenu control and assign it to the PopupMenu property of the CommandBar. ]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                    |
| [Me][.commandBar1.PopupMenu = [Me].popupMenu1 ]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                    |
| [\' Add a ParentBarItem to the PopupMenu. ]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                    |
| [Me][.popupMenu1.ParentBarItem = [Me].parentBarItem1 ]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                    |
| [\' Add items to the ParentBarItem. ]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                    |
| [Me][.parentBarItem1.Items.AddRange([New] Syncfusion.Windows.Forms.Tools.XPMenus.BarItem() {[Me].barItem1, [Me].barItem2, [Me].barItem3}) ]               |
|                                                                                                                                                                                                                                                                                                                                    |
| [Me][.barItem1.Text = [\"Windows Forms Samples\"] ]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                    |
| [Me][.barItem2.Text = [\"ASP.NET Samples\"] ]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                    |
| [Me][.barItem3.Text = [\"WPF Samples\"] ]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                    |
| [\' Handle the CommandBarDropDownClicked event. ]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                    |
| [AddHandler][ [Me].commandBar1.CommandBarDropDownClicked, [AddressOf] commandBar1_CommandBarDropDownClicked ]                                                                                       |
|                                                                                                                                                                                                                                                                                                                                    |
| [Private][ [Sub] commandBar1_CommandBarDropDownClicked([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                    |
| [    [\' The below line will be displayed in the output window at runtime. ]]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                    |
| [    Console.WriteLine([\" CommandBarDropDownClicked event is raised \"])]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                    |
| [End][ [Sub]]                                                                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

