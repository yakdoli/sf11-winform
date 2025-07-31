---
title: scrollsettingsinscrollersframe1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\scrollsettingsinscrollersframe1.md
created_at: 2025-07-03
---






##### Scroll Settings in ScrollersFrame {#scroll-settings-in-scrollersframe style="tab-stops: 0pt"}

[] 

The horizontal and vertical scrollers has **Value** property, which represents the current position of the scrollbox on the scroll bar control at runtime. This value can be changed using the HorizontalSmallChange and VerticalSmallChange properties.

[] 


  ----------------------- --------------------------------------------------------------------------------------------------------------------------------------------------
  Property                Description
  HorizontalSmallChange   Gets / sets a value to be added or subtracted from the Value Property, when horizontal scroll box is moved a small distance. Default value is 1.
  VerticallSmallChange    Gets / sets a value to be added or subtracted from the Value Property, when vertical scroll box is moved a small distance. Default value is 1.
  ----------------------- --------------------------------------------------------------------------------------------------------------------------------------------------


[]{#p1179}[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                        |
|                                                                                                                                                                                                                       |
| []                                                                                                                                                                   |
|                                                                                                                                                                                                                       |
| [this][.scrollersFrame2.][VerticallSmallChange = 25;]                                        |
|                                                                                                                                                                                                                       |
| [this][.scrollersFrame2.[HorizontalSmallChange = 25;]][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [Me][.scrollersFrame2.][VerticallSmallChange = 25]                                                                 |
|                                                                                                                                                                                                                                             |
| [Me][.scrollersFrame2.[HorizontalSmallChange ]][ = 25][] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

