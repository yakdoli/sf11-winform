---
title: hostformsettings.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\hostformsettings.md
created_at: 2025-07-03
---






##### Host Form Settings {#host-form-settings style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

The host form of a SplashControl application can be hidden or shown, when the splash image is displayed. The properties given below illustrate this.

[] 


+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| SplashControl Property            | Description                                                                                                                   |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| HostForm                          | Gets / sets the host form of the SplashControl.                                                                               |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| HideHostForm                      | Specifies if the host form should be hidden when the splash screen is displayed.                                              |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| HostFormWindowState               | Specifies whether the host form should be displayed as normal or minimized or maximized, when the splash screen is displayed. |
|                                   |                                                                                                                               |
|                                   |                                                                                                                               |
|                                   |                                                                                                                               |
|                                   | The HideHostForm property should be set to \'True\'.                                                                          |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------+


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                         |
|                                                                                                                                                                                                        |
| []                                                                                                                                                   |
|                                                                                                                                                                                                        |
| [this][.splashControl2.HostForm = [this];]                                                   |
|                                                                                                                                                                                                        |
| [this][.splashControl1.HideHostForm = [true];]                                               |
|                                                                                                                                                                                                        |
| [this][.splashControl1.HostFormWindowState = System.Windows.Forms.[FormWindowState].Normal;] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                           |
|                                                                                                                                                                              |
| []                                                                                                                         |
|                                                                                                                                                                              |
| [Me][.splashControl2.HostForm = [Me]]                              |
|                                                                                                                                                                              |
| [Me][.SplashControl1.HideHostForm = [True]]                        |
|                                                                                                                                                                              |
| [Me][.SplashControl1.HostFormWindowState = System.Windows.Forms.FormWindowState.Normal] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

