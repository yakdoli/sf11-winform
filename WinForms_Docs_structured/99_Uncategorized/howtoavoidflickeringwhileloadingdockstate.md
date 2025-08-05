---
title: howtoavoidflickeringwhileloadingdockstate.md
original_path: WinForms_Docs/99_Uncategorized/howtoavoidflickeringwhileloadingdockstate.md
created_at: 2025-08-05
---






##### How to avoid flickering while loading dock state? {#how-to-avoid-flickering-while-loading-dock-state style="tab-stops: 0pt"}

[] 

Flickering can be avoided by calling the below methods.

**[]** 

**LockDockPanelsUpdate and** **UnLockDockPanelsUpdate Methods -** The LockDockPanelsUpdate and UnLockDockPanelsUpdate methods are used to lock and unlock the panel\'s repainting respectively. For example to avoid flickering while loading a dock state, these methods can be used in the following way.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                        |
|                                                                                                                                       |
| **[]**                                                                              |
|                                                                                                                                       |
| [//Avoids flickering while loading dock state]                                      |
|                                                                                                                                       |
| [this][.dockingManager1.LockHostFormUpdate();]   |
|                                                                                                                                       |
| [this][.dockingManager1.LoadDockState();]        |
|                                                                                                                                       |
| [this][.dockingManager1.UnlockHostFormUpdate();] |
+---------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                 |
|                                                                                                                                    |
| **[]**                                                                           |
|                                                                                                                                    |
| [\'Avoids flickering while loading dock state]                                   |
|                                                                                                                                    |
| [Me][.dockingManager1.LockHostFormUpdate()]   |
|                                                                                                                                    |
| [Me][.dockingManager1.LoadDockState()]        |
|                                                                                                                                    |
| [Me][.dockingManager1.UnlockHostFormUpdate()] |
+------------------------------------------------------------------------------------------------------------------------------------+

[] 

See Also

[] 

[Persistence]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

