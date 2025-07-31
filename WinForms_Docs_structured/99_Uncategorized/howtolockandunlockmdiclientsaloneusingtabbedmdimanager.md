---
title: howtolockandunlockmdiclientsaloneusingtabbedmdimanager.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtolockandunlockmdiclientsaloneusingtabbedmdimanager.md
created_at: 2025-07-03
---






#### How to lock and unlock MDIClients alone using TabbedMDIManager {#how-to-lock-and-unlock-mdiclients-alone-using-tabbedmdimanager style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

TabbedMDIManager has **LockMDIClientUpdate**() and **UnLockMDIClientUpdate**() methods to lock and unlock the MDIClients from updating.

[] 


  Method                    Description
  ------------------------- ------------------------------
  LockMDIClientUpdate()     Locks the MDIClients alone
  UnlockMDIClientUpdate()   Unlocks the MDIClients alone


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [private void ][unlockToolStripMenuItem_Click(][object][ sender, ][EventArgs][ e)] |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [   ][this][.tabbedMDIManager1.UnLockMDIClientUpdate();]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [private void ][lockToolStripMenuItem_Click(][object][ sender, ][EventArgs][ e)]   |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [   ][this][.tabbedMDIManager1.LockMDIClientUpdate();]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                            |
| [Private][ [Sub] unlockToolStripMenuItem_Click([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                            |
| [    [Me].tabbedMDIManager1.UnLockMDIClientUpdate()]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                            |
| [End][ [Sub]]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                            |
| [Private][ [Sub] lockToolStripMenuItem_Click([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)]   |
|                                                                                                                                                                                                                                                                                                                            |
| [    [Me].tabbedMDIManager1.LockMDIClientUpdate()]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                            |
| [End][ [Sub]]                                                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

