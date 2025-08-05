---
title: hostingwindowsformcontrolindockingmanager.md
original_path: WinForms_Docs/99_Uncategorized/hostingwindowsformcontrolindockingmanager.md
created_at: 2025-08-05
---






#### Hosting Windows Form control in DockingManager {#hosting-windows-form-control-in-dockingmanager style="tab-stops: 0pt"}

 

Hosting a Windows Form Host in DockingManager is an easy process for which you need to set **UseIntropCompaitableMode=true** in order to use Winform controls with in DockingManager. The following codes show how to use **webbrowser** control with in DockingManager.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<][syncfusion][:]**[DockingManager]**[ DockFill][=\"True\"][ UseInteropCompatibilityMode][=\"True\"\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [      ][\<][WebBrowser][ Name][=\"web1\"/\>][]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\</][syncfusion][:]**[DockingManager]**[\>][]                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                       |
|                                                                                                                                                                                                     |
| [//Navigating the webbrowser control defined in xaml to the given url.][] |
|                                                                                                                                                                                                     |
| [web1.Navigate([new] Uri([\"http://syncfusion.com\"]));]                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

{border="0"}

Figure 364: WebBrowser as child of DockingManager

[]{#related-topics}

