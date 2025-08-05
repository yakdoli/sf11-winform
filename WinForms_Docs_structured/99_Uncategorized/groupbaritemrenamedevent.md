---
title: groupbaritemrenamedevent.md
original_path: WinForms_Docs/99_Uncategorized/groupbaritemrenamedevent.md
created_at: 2025-08-05
---






##### GroupBarItemRenamed Event {#groupbaritemrenamed-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This event is handled after a GroupBar Item is renamed by an inplace edit operation. It is handled when a GroupBar Item is renamed at runtime.

 

The event handler of this event receives an argument of type **GroupItemRenamedEventArgs**.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [// The GroupBarItemRenamed event occurs when a GroupBar Item is renamed by an inplace edit operation.]                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [private][ [void] grpbr_GroupBarItemRenamed([object] obj, [GroupItemRenamedEventArgs] arg)]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [{]                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [listViewItem1 = [new] System.Windows.Forms.[ListViewItem]([new] [string]\[\] {[\"GroupBarItemRenamed\"], [\"Item Renamed: \"] +arg.Index + [\" NewLabel: \"] + arg.NewLabel + [\" OldLabel: \"] + arg.OldLabel});] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [this][.listView1.Items.Add(listViewItem1);]                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [// The GroupBarItemRenamed event occurs when a GroupBar Item is renamed by an inplace edit operation.]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Private][ [Sub] grpbr_GroupBarItemRenamed([ByVal] obj [As] [Object], [ByVal] arg [As] GroupItemRenamedEventArgs)]                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [listViewItem1 = [New] System.Windows.Forms.ListViewItem([New] [String]() {[\"GroupBarItemRenamed\"], [\"Item Renamed: \"] + arg.Index + [\" NewLabel: \"] + arg.NewLabel + [\" OldLabel: \"] + arg.OldLabel})] |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Me][.listView1.Items.Add(listViewItem1)]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [End][ [Sub]]                                                                                                                                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#p620} 

 

[]{#related-topics}

