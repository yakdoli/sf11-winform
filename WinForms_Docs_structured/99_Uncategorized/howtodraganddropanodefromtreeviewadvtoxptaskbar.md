---
title: howtodraganddropanodefromtreeviewadvtoxptaskbar.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtodraganddropanodefromtreeviewadvtoxptaskbar.md
created_at: 2025-07-03
---






##### How to drag and drop a node from TreeViewAdv to XPTaskBar? {#how-to-drag-and-drop-a-node-from-treeviewadv-to-xptaskbar style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This can be achieved by handling the **ItemDrag** event of TreeViewAdv and **DragDrop** event of the XPTaskBar.

 

The following code snippet illustrates this.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                              |
| [private][ [void] treeViewAdv1_ItemDrag([object] sender, System.Windows.Forms.[ItemDragEventArgs] e)] |
|                                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [    [TreeViewAdv] treeViewAdv = ([TreeViewAdv])sender;]                                                                                                                 |
|                                                                                                                                                                                                                                                              |
| [    [TreeNodeAdv]\[\] nodes = ([TreeNodeAdv]\[\])e.Item;]                                                                                                               |
|                                                                                                                                                                                                                                                              |
| [    [TreeNodeAdv] node = nodes\[0\];]                                                                                                                                                           |
|                                                                                                                                                                                                                                                              |
| [    [this].treeViewAdv1.DoDragDrop(node.Text, [DragDropEffects].All);]                                                                                                     |
|                                                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [private][ [void] xPTaskBar1_DragOver([object] sender, System.Windows.Forms.[DragEventArgs] e)]       |
|                                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                              |
| [    e.Effect = [DragDropEffects].All;]                                                                                                                                                          |
|                                                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [private][ [void] xPTaskBar1_DragDrop([object] sender, System.Windows.Forms.[DragEventArgs] e)]       |
|                                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                              |
| [    [if] (e.Data.GetDataPresent([DataFormats].StringFormat))]                                                                                                              |
|                                                                                                                                                                                                                                                              |
| [    {]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                              |
| [        [string] str = System.[Convert].ToString(e.Data.GetData([DataFormats].StringFormat));]                                                     |
|                                                                                                                                                                                                                                                              |
| [        [Point] pt = xpTaskBarBox3.PointToClient([new] [Point](e.X, e.Y));]                                                                        |
|                                                                                                                                                                                                                                                              |
| [        Syncfusion.Windows.Forms.Tools.[XPTaskBarItem] taskItem = xpTaskBarBox3.HitTest(pt);]                                                                                                   |
|                                                                                                                                                                                                                                                              |
| [        taskItem.Text = str;]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                              |
| [    }]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                              |
| [} ]                                                                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#p700} 

[]{#related-topics}

