---
title: getsetdockedelementtabbedhostsize.md
original_path: WinForms_Docs/99_Uncategorized/getsetdockedelementtabbedhostsize.md
created_at: 2025-08-05
---






#### Get/Set DockedElementTabbed host size {#getset-dockedelementtabbed-host-size style="tab-stops: 0pt"}

**Get/Set HostSize()** method has direct control over the size of the **DockedElementTabbedHost**,  which  acts as a container for the dockingchild in both Dock and Float state. The container for Dock and Float state, which belongs to the given element, can be obtained as follows.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                              |
|                                                                                                                                                                                                                                               |
| [//To get DockedElementTabbedHost Container for Dock State.]                                                                                                                                |
|                                                                                                                                                                                                                                               |
| [DockedElementTabbedHost][ dockHost = **[DockingManager]**.ResolveHost(element, [DockState].Dock);]   |
|                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                               |
| [//To get DockedElementTabbedHost Container for float State.]                                                                                                                               |
|                                                                                                                                                                                                                                               |
| [DockedElementTabbedHost][ floathost = **[DockingManager]**.ResolveHost(element, [DockState].Float);] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Now you can set the size of the host as follows:

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                   |
| [//To get DockedElementTabbedHost Container for Dock State.][]                                                                                                                              |
|                                                                                                                                                                                                                                                                                   |
| [DockedElementTabbedHost][ dockHost = **[DockingManager]**.ResolveHost(element, [DockState].Dock);][] |
|                                                                                                                                                                                                                                                                                   |
| [//To set HostSize.]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| **[DockingManager]**[.SetHostSize(dockHost, [new] [Size](50, 100));]                                                                         |
|                                                                                                                                                                                                                                                                                   |
| [            ]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                   |
| [//To get HostSize.]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| [Size][ hostsize = **[DockingManager]**.GetHostSize(dockHost);[]]                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

