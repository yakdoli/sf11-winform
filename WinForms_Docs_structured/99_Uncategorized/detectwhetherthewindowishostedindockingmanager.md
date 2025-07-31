---
title: detectwhetherthewindowishostedindockingmanager.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\detectwhetherthewindowishostedindockingmanager.md
created_at: 2025-07-03
---






#### Detect whether the window is hosted in DockingManager {#detect-whether-the-window-is-hosted-in-dockingmanager style="tab-stops: 0pt"}

 

There two ways to detect whether a **FrameworkElement** is hosted **in DockingManager** or not. They are: 

1.   Getting **DockingManager** instance for a **FrameworkElement** and checking whether it is null or not.

2.   Detecting whether the **FrameworkElement** is present in the Children collection of DockingManager.

 

The two ways are shown below:

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                     |
|                                                                                                                                                                                                      |
| [//Getting **DockingManager** Instance.]                                                                                                           |
|                                                                                                                                                                                                      |
| **[DockingManager]**[ manager=**[DockingManager]**.Get**DockingManager**(element1);] |
|                                                                                                                                                                                                      |
| []                                                                                                                                                               |
|                                                                                                                                                                                                      |
| [//Checking whether element1 is in children collection.]                                                                                           |
|                                                                                                                                                                                                      |
| **[DockingManager]**[.Children.Contains(element1);[]]                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

