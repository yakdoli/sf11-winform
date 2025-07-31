---
title: howtodisablekeyboardshortcutsfortheeditcontrol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtodisablekeyboardshortcutsfortheeditcontrol.md
created_at: 2025-07-03
---








  









## How To Disable Keyboard Shortcuts For the Edit Control {#how-to-disable-keyboard-shortcuts-for-the-edit-control style="tab-stops: 0pt"}

[] 

To disable keyboard shortcuts, first you must remove them from the context menu. Here is an example for removing the F5 shortcut.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                           |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                                          |
| [private][ [void] Form1_Load([object] sender, System.[EventArgs] e)] |
|                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                                  |
|                                                                                                                                                                                                                          |
| [ContextMenu][ cm = [this].editControl1.ContextMenu;]                                                          |
|                                                                                                                                                                                                                          |
| [foreach][([MenuItem] mi [in] cm.MenuItems)]                                              |
|                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                                  |
|                                                                                                                                                                                                                          |
| [this][.RemoveShortcutInEditControl(mi);]                                                                                           |
|                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                                  |
|                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                                  |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                          |
| [private][ [void] RemoveShortcutInEditControl([MenuItem] miParent)]                       |
|                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                                  |
|                                                                                                                                                                                                                          |
| [// Remove F5 shortcut.]                                                                                                                                               |
|                                                                                                                                                                                                                          |
| [if][(miParent.Shortcut == [Shortcut].F5)]                                                                     |
|                                                                                                                                                                                                                          |
| [miParent.Shortcut = [Shortcut].None;]                                                                                                                          |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                          |
| [// Parse through the children recursively.]                                                                                                                           |
|                                                                                                                                                                                                                          |
| [foreach][([MenuItem] mi [in] miParent.MenuItems)]                                        |
|                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                                  |
|                                                                                                                                                                                                                          |
| [this][.RemoveShortcutInEditControl(mi);]                                                                                           |
|                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                                  |
|                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                |
| [Private][ [Sub] Form1_Load([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)] |
|                                                                                                                                                                                                                                                                                                                |
| [Dim][ cm [As] ContextMenu = [Me].editControl1.ContextMenu]                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                |
| [Dim][ mi [As] MenuItem]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                |
| [For][ [Each] mi [In] cm.MenuItems]                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                |
| [Me][.RemoveShortcutInEditControl(mi)]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                |
| [Next]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                |
| [End][ [Sub]]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                |
| [Private][ [Sub] RemoveShortcutInEditControl([ByVal] miParent [As] MenuItem)]                                                                              |
|                                                                                                                                                                                                                                                                                                                |
| [\' Remove F5 shortcut.]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                |
| [If][ miParent.Shortcut = Shortcut.F5 [Then]]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                |
| [miParent.Shortcut = Shortcut.None]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                |
| [End][ [If]]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                |
| [\' Parse through the children recursively.]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                |
| [Dim][ mi [As] MenuItem]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                |
| [For][ [Each] mi [In] miParent.MenuItems]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                |
| [Me][.RemoveShortcutInEditControl(mi)]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                |
| [Next]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                |
| [End][ [Sub]]                                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p188} 

[]{#related-topics}

