---
title: showcontextmenuevent.md
original_path: WinForms_Docs/99_Uncategorized/showcontextmenuevent.md
created_at: 2025-08-05
---






##### ShowContextMenu Event {#showcontextmenu-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

It occurs on right-clicking the mouse button over the GroupBar control. It is handled when the mouse is right-clicked over the GroupBar control at runtime.

 

The event handler receives an argument of type **EventArgs**.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                   |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [private][ [void] groupBar1_ShowContextMenu([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [  // You can see the below line in the output window during run-time.]                                                                                                      |
|                                                                                                                                                                                                                                  |
| [Console][.Write([\" ShowContextMenu Event is raised \"]);]                                                          |
|                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                        |
| [Private][ [Sub] groupBar1_ShowContextMenu([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                        |
| [  // You can see the below line in the output window during run-time.]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                        |
| [Console.Write([\" ShowContextMenu Event is raised \"])]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                        |
| [End][ [Sub]]                                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#p623} 

 

[]{#related-topics}

