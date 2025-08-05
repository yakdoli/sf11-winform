---
title: alignmentsettings2.md
original_path: WinForms_Docs/99_Uncategorized/alignmentsettings2.md
created_at: 2025-08-05
---






##### Alignment Settings {#alignment-settings style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This section discusses the alignment settings available in SplashControl.

 

SplashControl provides options to customize the alignment of the splash image in the desktop. The property that is related to this feature is given below.

[] 


+-----------------------------------+-----------------------------------------------------------------------------------------+
| SplashControl Property            | Description                                                                             |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| DesktopAlignment                  | Specifies the desktop alignment of the splash image. It includes the following options. |
|                                   |                                                                                         |
|                                   |                                                                                         |
|                                   |                                                                                         |
|                                   | [·      ]SystemTray,                                       |
|                                   |                                                                                         |
|                                   | [·      ]Center,                                           |
|                                   |                                                                                         |
|                                   | [·      ]LeftTop,                                          |
|                                   |                                                                                         |
|                                   | [·      ]LeftBottom,                                       |
|                                   |                                                                                         |
|                                   | [·      ]RightTop,                                         |
|                                   |                                                                                         |
|                                   | [·      ]RightBottom and                                   |
|                                   |                                                                                         |
|                                   | [·      ]Custom.                                           |
+-----------------------------------+-----------------------------------------------------------------------------------------+


[] 

This can be done through code using the code snippet below.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                    |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                              |
|                                                                                                                                                                                                                   |
| [this][.splashControl1.DesktopAlignment = Syncfusion.Windows.Forms.Tools.[SplashAlignment].SystemTray;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                      |
|                                                                                                                                                                                         |
| []                                                                                                                                    |
|                                                                                                                                                                                         |
| [Me][.SplashControl1.DesktopAlignment = Syncfusion.Windows.Forms.Tools.SplashAlignment.SystemTray] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 987: Desktop Alignment Options

 

 

 

 

[]{#related-topics}

