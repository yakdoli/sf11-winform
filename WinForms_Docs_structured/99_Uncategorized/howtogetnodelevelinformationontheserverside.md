---
title: howtogetnodelevelinformationontheserverside.md
original_path: WinForms_Docs/99_Uncategorized/howtogetnodelevelinformationontheserverside.md
created_at: 2025-08-05
---






##### How to get node level information on the server-side? {#how-to-get-node-level-information-on-the-server-side style="tab-stops: 0pt"}

[] 

In server side, you can use following code snippet to get node level information.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                     |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                  |
|                                                                                                                                                                                                                      |
| [private][ [int] GetNodeLevel( [TreeViewNode] node )] |
|                                                                                                                                                                                                                      |
| [{]                                                                                                                                                              |
|                                                                                                                                                                                                                      |
| [       [int] nLevel = 0;]                                                                                                                  |
|                                                                                                                                                                                                                      |
| [       [while]( [null] != node.ParentItem )]                                                                          |
|                                                                                                                                                                                                                      |
| [       {]                                                                                                                                                       |
|                                                                                                                                                                                                                      |
| [              node = node.ParentItem;]                                                                                                                          |
|                                                                                                                                                                                                                      |
| [              nLevel++;]                                                                                                                                        |
|                                                                                                                                                                                                                      |
| [       }]                                                                                                                                                       |
|                                                                                                                                                                                                                      |
| [       [return] nLevel;]                                                                                                                   |
|                                                                                                                                                                                                                      |
| [}]                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

