---
title: collapsedstatechangedevent.md
original_path: WinForms_Docs/99_Uncategorized/collapsedstatechangedevent.md
created_at: 2025-08-05
---






##### CollapsedStateChanged Event {#collapsedstatechanged-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This event occurs after the XPTaskBar Box has been collapsed or expanded.

 

The event handler receives an argument of the type **EventArgs**.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                      |
| [private][ [void] taskMenuBox1_CollapsedStateChanged([object] sender, System.[EventArgs] e)]                                     |
|                                                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| [XPTaskBarBox box = sender [as] XPTaskBarBox;]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                      |
| [ListViewItem listViewItem = [new] ListViewItem([new] [String]\[\]{[\"CollapsedStateChanged\"], [\"XPTaskBarBox: \"] + box.Text});] |
|                                                                                                                                                                                                                                                                                      |
| [this][.listView1.Items.Add(listViewItem);]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                      |
| [Private][ [Sub] taskMenuBox1_CollapsedStateChanged([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)]               |
|                                                                                                                                                                                                                                                                                                                                                      |
| [Dim][ box [As] XPTaskBarBox = [TryCast](sender, XPTaskBarBox)]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                      |
| [Dim][ listViewItem [As] [New] ListViewItem([New] [String]() {[\"CollapsedStateChanged\"], [\"XPTaskBarBox: \"] + box.Text})] |
|                                                                                                                                                                                                                                                                                                                                                      |
| [Me][.listView1.Items.Add(listViewItem)]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                      |
| [End][ [Sub]]                                                                                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#p688} 

 

[]{#related-topics}

