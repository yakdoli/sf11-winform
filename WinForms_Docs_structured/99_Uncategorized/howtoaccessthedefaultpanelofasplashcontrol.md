---
title: howtoaccessthedefaultpanelofasplashcontrol.md
original_path: WinForms_Docs/99_Uncategorized/howtoaccessthedefaultpanelofasplashcontrol.md
created_at: 2025-08-05
---






##### How to access the default panel of a SplashControl {#how-to-access-the-default-panel-of-a-splashcontrol style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

The default panel of a SplashControl can be accessed through the **SplashControlPanel** property.

 

The example given below illustrates how the background color of a SplashControl\'s internal panel can be changed.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [this][.splashControl1.SplashControlPanel.BackgroundColor = [new] Syncfusion.Drawing.[BrushInfo](Syncfusion.Drawing.[GradientStyle].Vertical, System.Drawing.[Color].RosyBrown, System.Drawing.[SystemColors].ControlLight);] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                              |
| [Me][.splashControl1.SplashControlPanel.BackgroundColor = [New] Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.Vertical, System.Drawing.Color.RosyBrown, System.Drawing.SystemColors.ControlLight)] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

