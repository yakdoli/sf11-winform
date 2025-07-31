---
title: howtodisplaythesplashpanelalongwiththemousepointer.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtodisplaythesplashpanelalongwiththemousepointer.md
created_at: 2025-07-03
---






##### How to display the SplashPanel along with the mouse pointer {#how-to-display-the-splashpanel-along-with-the-mouse-pointer style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

 

Set the [[DesktopAlignment]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Alignment_Settings_1)[ ]{.UGHyperlink}property of the SplashPanel to ***Custom***, and call the **ShowSplash** method, by passing the pointer position as the parameter as follows.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                  |
|                                                                                                                                                                                 |
| []                                                                                                                                          |
|                                                                                                                                                                                 |
| [Point][ pt = [Point].Empty;]                                   |
|                                                                                                                                                                                 |
| [if][( SplashPanel1.DesktopAlignment == [SplashAlignment].Custom)] |
|                                                                                                                                                                                 |
| [pt = [Control].MousePosition;]                                                                                     |
|                                                                                                                                                                                 |
| [SplashPanel1 .ShowSplash(pt, [this], [true]);]                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                             |
|                                                                                                                                                                                |
| []                                                                                                                            |
|                                                                                                                                                                                |
| [Private][ pt [As] Point = Point.Empty]                              |
|                                                                                                                                                                                |
| [If][ SplashPanel1.DesktopAlignment = SplashAlignment.Custom [Then]] |
|                                                                                                                                                                                |
| [pt = Control.MousePosition]                                                                                                               |
|                                                                                                                                                                                |
| [SplashPanel1.ShowSplash(pt, [Me], [True])]                                                      |
|                                                                                                                                                                                |
| [End][ [If]]                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

