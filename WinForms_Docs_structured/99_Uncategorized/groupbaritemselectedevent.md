---
title: groupbaritemselectedevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\groupbaritemselectedevent.md
created_at: 2025-07-03
---






##### GroupBarItemSelected Event {#groupbaritemselected-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

It occurs when a GroupBar Item of the GroupBar control is selected. Accessing the **GroupBar.SelectedItem** property from within the GroupBarItemSelected event handler will allow you to determine the item that was clicked. Based on this appropriate command, handling routines can be invoked.

 

The event handler of this event receives an argument of type **EventArgs**.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [// Provide a handler for the GroupBar.GroupBarItemSelected event.]                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [this][.groupBar1.GroupBarItemSelected += ][new][ System.EventHandler(][this][.groupBar1_GroupBarItemSelected); ]                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [// GroupBar.GroupBarItemSelected event handler.]                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [// The GroupBar.SelectedItem property fetches the index of the selected item, while][ ][the item is obtained by referencing the selected index within the][ ][GroupBar.GroupBarItems collection.]                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [private void ][groupBar1_GroupBarItemSelected(][object][ sender, System.EventArgs e)]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Trace.WriteLine(][String][.Concat(\"Selected Item = \", ][this][.groupBar1.GroupBarItems\[][this][.groupBar1.SelectedItem\].Text)); ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                    |
| [\' Provide a handler for the GroupBar.GroupBarItemSelected event.]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                    |
| [Private][ [Me].groupBar1.GroupBarItemSelected += [New] System.EventHandler([Me].groupBar1_GroupBarItemSelected)]                                                              |
|                                                                                                                                                                                                                                                                                                                                    |
| [\' GroupBar.GroupBarItemSelected event handler.]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                    |
| [\' The GroupBar.SelectedItem property fetches the index of the selected item, while the item is obtained by referencing the selected index within the GroupBar.GroupBarItems collection.]                                                                                       |
|                                                                                                                                                                                                                                                                                                                                    |
| [Private][ [Sub] groupBar1_GroupBarItemSelected([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                    |
| [Trace.WriteLine([String].Concat([\"Selected Item = \"], [Me].groupBar1.GroupBarItems([Me].groupBar1.SelectedItem).Text))]                                                                               |
|                                                                                                                                                                                                                                                                                                                                    |
| [End][ [Sub]]                                                                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#p622} 

 

[]{#related-topics}

