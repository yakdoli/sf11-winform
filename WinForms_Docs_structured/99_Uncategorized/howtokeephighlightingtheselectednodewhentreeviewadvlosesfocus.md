---
title: howtokeephighlightingtheselectednodewhentreeviewadvlosesfocus.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtokeephighlightingtheselectednodewhentreeviewadvlosesfocus.md
created_at: 2025-07-03
---






#### How to keep highlighting the selected node when TreeViewAdv loses focus {#how-to-keep-highlighting-the-selected-node-when-treeviewadv-loses-focus style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

We can set **HideSelection** property to ***false***, to ensure that the node remains selected even when the TreeViewAdv control does not have focus.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [this][.treeViewAdv1.HideSelection = [false];][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                       |
|                                                                                                                                                                                                          |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                          |
| [Me][.treeViewAdv1.HideSelection = [False]][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

