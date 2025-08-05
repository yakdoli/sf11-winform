---
title: howtodockthecontrolbarstoanyedgeofthehostform.md
original_path: WinForms_Docs/99_Uncategorized/howtodockthecontrolbarstoanyedgeofthehostform.md
created_at: 2025-08-05
---






##### How to dock the ControlBars to any edge of the host form {#how-to-dock-the-controlbars-to-any-edge-of-the-host-form style="tab-stops: 0pt"}

[] 

It can be done using the DockState property of the control bar. The options are Right, Left, Top and Bottom.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                   |
|                                                                                                                                                  |
| []                                                                                                           |
|                                                                                                                                                  |
| [// Dock to the right edge of the host form]                                                   |
|                                                                                                                                                  |
| [this][.controlBar1.DockState = CommandBarDockState.Right;] |
+--------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                            |
|                                                                                                                                               |
| **[]**                                                                                      |
|                                                                                                                                               |
| [// Dock to the right edge of the host form]                                                |
|                                                                                                                                               |
| [Me][.controlBar1.DockState = CommandBarDockState.Right] |
+-----------------------------------------------------------------------------------------------------------------------------------------------+

[] 

See Also

[] 

[Detached ControlBars]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

