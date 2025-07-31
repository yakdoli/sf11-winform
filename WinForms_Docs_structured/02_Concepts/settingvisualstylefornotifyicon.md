---
title: settingvisualstylefornotifyicon.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\settingvisualstylefornotifyicon.md
created_at: 2025-07-03
---






#### Setting VisualStyle for NotifyIcon {#setting-visualstyle-for-notifyicon style="tab-stops: 0pt"}

NotifyIcon supports different visual styles to enhance its look and feel. The visual style for the NotifyIcon is set by using the **VisualStyle** property.

[] 


+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                                                                      |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| VisualStyle                       | Sets the visual style for the NotifyIcon control. The options provided are as follows.                                                                           |
|                                   |                                                                                                                                                                  |
|                                   | []                                                                             |
|                                   |                                                                                                                                                                  |
|                                   | [·      ]Blend                                                                                                                      |
|                                   |                                                                                                                                                                  |
|                                   | [·      ]Office2003                                                                                                                 |
|                                   |                                                                                                                                                                  |
|                                   | [·      ]Office2007Blue                                                                                                             |
|                                   |                                                                                                                                                                  |
|                                   | [·      ]Office2007Black                                                                                                            |
|                                   |                                                                                                                                                                  |
|                                   | [·      ]Office2007Silver                                                                                                           |
|                                   |                                                                                                                                                                  |
|                                   | [·      ]ShinyBlue                                                                                                                  |
|                                   |                                                                                                                                                                  |
|                                   | [·      ]ShinyRed                                                                                                                   |
|                                   |                                                                                                                                                                  |
|                                   | [·      ]SyncOrange                                                                                                                 |
|                                   |                                                                                                                                                                  |
|                                   | [·      ]VS2010[] |
|                                   |                                                                                                                                                                  |
|                                   | [·      ]Metro[]  |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

The below code can be used to set various visual style.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                             |
|                                                                                                                                            |
| []                                                                        |
|                                                                                                                                            |
| [//For Office2007Blue]                                                   |
|                                                                                                                                            |
| [SkinStorage.VisualStyle(notifyIcon, [\"Office2007Blue\"]);]   |
|                                                                                                                                            |
| []                                                                                     |
|                                                                                                                                            |
| [//For Blend]                                                            |
|                                                                                                                                            |
| [SkinStorage.VisualStyle(notifyIcon, Blend[\");]]              |
|                                                                                                                                            |
| []                                                                     |
|                                                                                                                                            |
| [//For Office2007Silver]                                                 |
|                                                                                                                                            |
| [SkinStorage.VisualStyle(notifyIcon, [\"Office2007Silver\"]);] |
+--------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

{border="0"}

***[]*** 

Figure 756: NotifyIcon with \"Office2007Blue\" Visual Style

***[]*** 

***[]*** 

{border="0"}

***[]*** 

Figure 757: NotifyIcon with \"Blend\" Visual Style

***[]*** 

***[]*** 

{border="0"}

 

Figure 758: NotifyIcon with \"Office2007Silver\" Visual Style

{border="0"}

 

Figure 759: NotifyIcon with \"Metro\" Visual Style

 

[]{#p416} 

[]{#related-topics}

