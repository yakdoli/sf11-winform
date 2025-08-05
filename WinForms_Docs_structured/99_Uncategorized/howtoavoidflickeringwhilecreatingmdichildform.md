---
title: howtoavoidflickeringwhilecreatingmdichildform.md
original_path: WinForms_Docs/99_Uncategorized/howtoavoidflickeringwhilecreatingmdichildform.md
created_at: 2025-08-05
---






##### How to avoid flickering while creating MDI child form? {#how-to-avoid-flickering-while-creating-mdi-child-form style="tab-stops: 0pt"}

[] 

Flickering can be avoided by calling the below methods.

[] 

**LockHostFormUpdate and UnLockHostFormUpdate Methods** - The LockHostFormUpdate and UnLockHostFormUpdate methods are used to lock and unlock the host form\'s updates respectively. These methods helps in avoiding flickering while creating an MDI child form, these methods can be used in the following way.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                             |
|                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                            |
| [//To avoid flickering]                                                                                                                                                                  |
|                                                                                                                                                                                                                                            |
| [this][.dockingManager1.LockHostFormUpdate();]                                                                                                        |
|                                                                                                                                                                                                                                            |
| [this][.dockingManager1.DockControl(form, [this], Syncfusion.Windows.Forms.Tools.[DockingStyle].Right, 0);] |
|                                                                                                                                                                                                                                            |
| [this][.dockingManager1.SetAsMDIChild(form, [true]);]                                                                            |
|                                                                                                                                                                                                                                            |
| [this][.dockingManager1.SetControlSize(form, size);]                                                                                                  |
|                                                                                                                                                                                                                                            |
| [this][.dockingManager1.UnlockHostFormUpdate();]                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                    |
|                                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                              |
|                                                                                                                                                                                                                                       |
| [\'To avoid flickering]                                                                                                                                                             |
|                                                                                                                                                                                                                                       |
| [Me][.dockingManager1.LockHostFormUpdate()]                                                                                                      |
|                                                                                                                                                                                                                                       |
| [Me][.dockingManager1.DockControl(form, [Me], Syncfusion.Windows.Forms.Tools.[DockingStyle].Right, 0)] |
|                                                                                                                                                                                                                                       |
| [Me][.dockingManager1.SetAsMDIChild(form, [True])]                                                                          |
|                                                                                                                                                                                                                                       |
| [Me][.dockingManager1.SetControlSize(form, size)]                                                                                                |
|                                                                                                                                                                                                                                       |
| [Me][.dockingManager1.UnlockHostFormUpdate()]                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p142} 

[]{#related-topics}

