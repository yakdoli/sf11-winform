---
title: nodeeditingevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\nodeeditingevent.md
created_at: 2025-07-03
---






##### Node Editing Event {#node-editing-event style="tab-stops: 0pt"}

[] 

The following events are handled when the tree node is in Edit Mode.

[] 

[·      ]**BeforeItemEdit**--Occurs when the **IsInEditMode** property changes. This event is handled before the TreeViewItemAdv enters the edit mode.

[·      ]**AfterItemEdit**--Occurs when the **IsInEditMode** property changes. This event is handled after the edit operations are completed.

[·      ]**EditKeyUp**--Occurs when a key is raised, when the item in edit mode. This event is handled when the item is in edit mode.

[·      ]**EditKeyDown**--Occurs when a key is raised, when the item is in edit mode. This event is handled when the item is in edit mode.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                              |
| [private][ [void] TreeViewItemAdv_EditKeyDown([object] sender, KeyEventArgs e)]               |
|                                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                              |
| [    Debug.WriteLine([\"Down: \"] + e.Key);]                                                                                                                                     |
|                                                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                              |
| [private][ [void] TreeViewItemAdv_EditKeyUp([object] sender, KeyEventArgs e)]                 |
|                                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                              |
| [    Debug.WriteLine([\"Up: \"] + e.Key);]                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                              |
| [private][ [void] TreeViewItemAdv_AfterItemEdit([object] sender, EditModeChangeEventArgs e)]  |
|                                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                              |
| [    Debug.WriteLine([\"AfterItemEdit: old( \"] + e.OldValue + [\"), new( \"] + e.NewValue + [\")\"]);]                          |
|                                                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                              |
| [private][ [void] TreeViewItemAdv_BeforeItemEdit([object] sender, EditModeChangeEventArgs e)] |
|                                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                              |
| [    Debug.WriteLine([\"BeforeItemEdit: old( \"] + e.OldValue + [\"), new( \"] + e.NewValue + [\")\"]);]                         |
|                                                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p596} 

 

 

[]{#related-topics}

