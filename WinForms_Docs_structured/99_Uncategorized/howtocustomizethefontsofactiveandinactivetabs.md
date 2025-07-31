---
title: howtocustomizethefontsofactiveandinactivetabs.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtocustomizethefontsofactiveandinactivetabs.md
created_at: 2025-07-03
---






#### How to customize the fonts of Active and Inactive tabs {#how-to-customize-the-fonts-of-active-and-inactive-tabs style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

 

Using the TabControlAdded event, the fonts of active and inactive tabs can be customized.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                        |
| [// Handle the TabbedMDIManager\'s TabControlAdded event to get hold of ]                                                                                                                            |
|                                                                                                                                                                                                                                                        |
| [// the TabControlAdv associated with it.]                                                                                                                                                           |
|                                                                                                                                                                                                                                                        |
| [this][.tabbedMdiManager.TabControlAdded += [new] TabbedMDITabControlEventHandler(TabbedMDITabControl_Added);]                               |
|                                                                                                                                                                                                                                                        |
| [private][ [void] TabbedMDITabControl_Added([object] sender, [TabbedMDITabControlEventArgs] args)] |
|                                                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                        |
| [args.TabControl.ActiveTabFont = [new] [Font] ([\"Comic Sans MS\"], 11);      ]                                                                   |
|                                                                                                                                                                                                                                                        |
| [args.TabControl.Font = [new] [Font] ([\"Garamond\"], 12);              ]                                                                         |
|                                                                                                                                                                                                                                                        |
| [}]                                                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                              |
| [\' Handle the TabbedMDIManager\'s TabControlAdded event to get hold of ]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                              |
| [\' the TabControlAdv associated with it.]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                              |
| [Me][.tabbedMdiManager.TabControlAdded += [New] TabbedMDITabControlEventHandler(TabbedMDITabControl_Added)]                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                              |
| [Private][ [Sub] TabbedMDITabControl_Added([ByVal] sender [As] [Object], [ByVal] args [As] TabbedMDITabControlEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                              |
| [args.TabControl.ActiveTabFont = [New] Font([\"Comic Sans MS\"], 11)]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                              |
| [args.TabControl.Font = [New] Font([\"Garamond\"], 12)]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                              |
| [End][ [Sub]]                                                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

[]{#p936} 

[]{#related-topics}

