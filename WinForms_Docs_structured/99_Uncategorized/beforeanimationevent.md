---
title: beforeanimationevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\beforeanimationevent.md
created_at: 2025-07-03
---






##### BeforeAnimation Event {#beforeanimation-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This event gets called before the XPTaskBar Box expands or collapses.

 

The event handler receives an argument of the type **EventArgs**.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                 |
| [private][ [void] taskMenuBox1_BeforeAnimation([object] sender, System.[EventArgs] e)]                                      |
|                                                                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                 |
| [XPTaskBarBox box = sender [as] XPTaskBarBox;]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                 |
| [ListViewItem listViewItem = [new] ListViewItem([new] [String]\[\]{[\"Before Animation\"], [\"XPTaskBarBox: \"] + box.Text});] |
|                                                                                                                                                                                                                                                                                 |
| [this][.listView1.Items.Add(listViewItem);]                                                                                                                                                |
|                                                                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                 |
| [Private][ [Sub] taskMenuBox1_BeforeAnimation([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)]                |
|                                                                                                                                                                                                                                                                                                                                                 |
| [Dim][ box [As] XPTaskBarBox = [TryCast](sender, XPTaskBarBox)]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                 |
| [Dim][ listViewItem [As] [New] ListViewItem([New] [String]() {[\"Before Animation\"], [\"XPTaskBarBox: \"] + box.Text})] |
|                                                                                                                                                                                                                                                                                                                                                 |
| [Me][.listView1.Items.Add(listViewItem)]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                 |
| [End][ [Sub]]                                                                                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#p687} 

 

[]{#related-topics}

