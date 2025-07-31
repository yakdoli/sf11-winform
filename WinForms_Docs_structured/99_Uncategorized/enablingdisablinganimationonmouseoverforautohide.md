---
title: enablingdisablinganimationonmouseoverforautohide.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\enablingdisablinganimationonmouseoverforautohide.md
created_at: 2025-07-03
---






#### Enabling/Disabling Animation on mouse over for auto hide {#enablingdisabling-animation-on-mouse-over-for-auto-hide style="tab-stops: 0pt"}

By default, whenever you move your mouse over the **AutoHidden** tab, the autohide animation will start. You can disable this behavior by setting the **IsAutoHideAnimationOnMouseOver=true** so that when you move the mouse over the autohide tab it does not start the Autohide animation.  But it will make you click the autohide tab to start autohide animation.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][syncfusion][:]**[DockingManager]**[ Name][=\"**DockingManager**\"][ IsAnimationEnabledOnMouseOver][=\"True\" \>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [   ][\<][Grid][/\>]                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\</][syncfusion][:]**[DockingManager]**[\>]                                                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                  |
|                                                                                                                                                                                                                                |
| **[DockingManager]**[.IsAnimationEnabledOnMouseOver = [true];][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

