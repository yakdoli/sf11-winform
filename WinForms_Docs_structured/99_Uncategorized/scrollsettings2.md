---
title: scrollsettings2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\scrollsettings2.md
created_at: 2025-07-03
---






##### Scroll Settings {#scroll-settings style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

**[]** 

XPTaskPane Enables vertical scrolling for the pages using **VerticalScroll** property. On mouse hovering over the scroll bar, the taskpage automatically moves and show the hidden contents. Scrolling speed can be fixed using ScrollSpeed property.

[]{#p1082}[] 


  --------------------- ----------------------------------------------------------------------------------------
  XPTaskPane Property   Description
  ScrollSpeed           Specifies the scrolling speed. Default value is 10.
  VerticalScroll        Enables scroll buttons that occupy vertical space instead of default horizontal space.
  --------------------- ----------------------------------------------------------------------------------------


**[]** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                |
|                                                                                                                                                                                               |
| []                                                                                                                                                                    |
|                                                                                                                                                                                               |
| [this][.xpTaskPane1.[ScrollSpeed= 20;]]                                            |
|                                                                                                                                                                                               |
| [this][.xpTaskPane1.VerticalScroll = [true];][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1083}[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                      |
|                                                                                                                                                                                                         |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                         |
| [Me][.xpTaskPane1.[ScrollSpeed = 20]]                                                        |
|                                                                                                                                                                                                         |
| [Me][.xpTaskPane1.VerticalScroll = [True]][] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1264: Vertical Scroll Bars Displayed

 

[]{#related-topics}

