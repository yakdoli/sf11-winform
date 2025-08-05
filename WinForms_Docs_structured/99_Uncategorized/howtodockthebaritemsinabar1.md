---
title: howtodockthebaritemsinabar1.md
original_path: WinForms_Docs/99_Uncategorized/howtodockthebaritemsinabar1.md
created_at: 2025-08-05
---






##### How to dock the bar items in a bar {#how-to-dock-the-bar-items-in-a-bar style="tab-stops: 0pt"}

[] 

We can dock the baritems in a bar using XPMenus CommandBarExt class as follows.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                      |
|                                                                                                                                                                                                     |
| []                                                                                                                                                              |
|                                                                                                                                                                                                     |
| [CommandBarExt cbe = [this].mainFrameBarManager1.GetBarControl([this].bar1) [as] CommandBarExt;] |
|                                                                                                                                                                                                     |
| [//Get the bar control that hold the baritems.]                                                                                                   |
|                                                                                                                                                                                                     |
| [cbe.BarControl.Dock = System.Windows.Forms.[DockStyle].Right;]                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                        |
| **[]**                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                        |
| [Dim][ cbe [As] CommandBarExt = [TryCast]([Me].mainFrameBarManager1.GetBarControl([Me].bar1), CommandBarExt)] |
|                                                                                                                                                                                                                                                                                        |
| [\'Get the bar control that hold the baritems. ]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                        |
| [cbe.BarControl.Dock = System.Windows.Forms.DockStyle.Right]                                                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

