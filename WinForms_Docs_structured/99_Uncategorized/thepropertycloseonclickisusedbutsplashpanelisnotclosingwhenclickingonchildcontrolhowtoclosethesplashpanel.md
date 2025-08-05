---
title: thepropertycloseonclickisusedbutsplashpanelisnotclosingwhenclickingonchildcontrolhowtoclosethesplashpanel.md
original_path: WinForms_Docs/99_Uncategorized/thepropertycloseonclickisusedbutsplashpanelisnotclosingwhenclickingonchildcontrolhowtoclosethesplashpanel.md
created_at: 2025-08-05
---






##### The property CloseOnClick is used but SplashPanel is not closing when clicking on child control. How to close the splash panel {#the-property-closeonclick-is-used-but-splashpanel-is-not-closing-when-clicking-on-child-control.-how-to-close-the-splash-panel style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

 

When **CloseOnClick** property is set to ***true***, the Splash Panel closes when clicked. But this is not applicable for the child controls inside the Splash Panel. To enable this feature, you need to call the HideSplash method inside the click event of the particular control.

 

For example, if you want to close SplashPanel when clicking its child control say, Label1, handle its click event as follows.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                         |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [private][ [void] label1_Click([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                |
|                                                                                                                                                                                                                        |
| [    [this].splashPanel1.HideSplash();]                                                                                                                       |
|                                                                                                                                                                                                                        |
| [}]                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                           |
| [Private][ [Sub] label1_Click([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                           |
| [    [Me].splashPanel1.HideSplash()]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                           |
| [End][ [Sub]]                                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

