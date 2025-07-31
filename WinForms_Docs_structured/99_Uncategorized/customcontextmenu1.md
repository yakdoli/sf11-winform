---
title: customcontextmenu1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\customcontextmenu1.md
created_at: 2025-07-03
---






##### Custom Context Menu {#custom-context-menu style="tab-stops: 0pt"}

[] 

It is possible to customize the statusbar context menu that displays in StatusStripEx, to look like Word2007. This can be done by setting **StatusString** property of NotificationItems like StatusStripButton, StatusStripLabel, so on.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                         |
|                                                                                                                                                                                                        |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                        |
| [this][.statusStripLabel1.Text = [\"Pages\"];]                                             |
|                                                                                                                                                                                                        |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                        |
| [this][.statusStripLabel1.StatusString = [\"1/1\"];][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1178}[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                 |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                               |
|                                                                                                                                                                                                                    |
| [Me][.statusStripLabel1.Text = [\"Pages\"]]                                                            |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                              |
|                                                                                                                                                                                                                    |
| [Me][.statusStripLabel1.StatusString = [\"1/1\"]][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

