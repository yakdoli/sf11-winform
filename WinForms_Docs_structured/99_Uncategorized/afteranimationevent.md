---
title: afteranimationevent.md
original_path: WinForms_Docs/99_Uncategorized/afteranimationevent.md
created_at: 2025-08-05
---






##### AfterAnimation Event {#afteranimation-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This event gets called after the XPTaskBar Box box expands or collapses.

 

The event handler receives an argument of the type **EventArgs**.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                |
| [private][ [void] taskMenuBox1_AfterAnimation([object] sender, System.[EventArgs] e)]                                      |
|                                                                                                                                                                                                                                                                                |
| [{  ]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                |
| [XPTaskBarBox box = sender [as] XPTaskBarBox;]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                |
| [ListViewItem listViewItem = [new] ListViewItem([new] [String]\[\]{[\"After Animation\"], [\"XPTaskBarBox: \"] + box.Text});] |
|                                                                                                                                                                                                                                                                                |
| [this][.listView1.Items.Add(listViewItem);]                                                                                                                                               |
|                                                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                |
| [Private][ [Sub] taskMenuBox1_AfterAnimation([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)]                |
|                                                                                                                                                                                                                                                                                                                                                |
| [Dim][ box [As] XPTaskBarBox = [TryCast](sender, XPTaskBarBox)]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                |
| [Dim][ listViewItem [As] [New] ListViewItem([New] [String]() {[\"After Animation\"], [\"XPTaskBarBox: \"] + box.Text})] |
|                                                                                                                                                                                                                                                                                                                                                |
| [Me][.listView1.Items.Add(listViewItem)]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                |
| [End][ [Sub]]                                                                                                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#p686} 

 

[]{#related-topics}

