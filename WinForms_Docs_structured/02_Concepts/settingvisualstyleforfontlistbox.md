---
title: settingvisualstyleforfontlistbox.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\settingvisualstyleforfontlistbox.md
created_at: 2025-07-03
---






#### Setting VisualStyle for FontListBox   {#setting-visualstyle-for-fontlistbox style="tab-stops: 0pt"}

 

Different visual styles are available for the FontListBox control to enhance its appearance. The visual style for the FontListBox is set by using the **VisualStyle** property.

 


+-----------------------------------+-----------------------------------------------------------------------------------------+
| Property                          | Description                                                                             |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| VisualStyle                       | Sets the visual style for the FontListBox control. The options provided are as follows. |
|                                   |                                                                                         |
|                                   | []    |
|                                   |                                                                                         |
|                                   | [·      ]Blend                                             |
|                                   |                                                                                         |
|                                   | [·      ]Office2003                                        |
|                                   |                                                                                         |
|                                   | [·      ]Office2007Blue                                    |
|                                   |                                                                                         |
|                                   | [·      ]Office2007Black                                   |
|                                   |                                                                                         |
|                                   | [·      ]Office2007Silver                                  |
|                                   |                                                                                         |
|                                   | [·      ]ShinyBlue                                         |
|                                   |                                                                                         |
|                                   | [·      ]ShinyRed                                          |
|                                   |                                                                                         |
|                                   | [·      ]SyncOrange                                        |
|                                   |                                                                                         |
|                                   | [·      ]VS2010                                            |
|                                   |                                                                                         |
|                                   | [·      ]Metro                                             |
|                                   |                                                                                         |
|                                   |                                                                                         |
+-----------------------------------+-----------------------------------------------------------------------------------------+


 

To the set the visual style for the FontListBox, use the following code snippets.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                       |
|                                                                                                                                                                                                                      |
| **[]**                                                                                                                                             |
|                                                                                                                                                                                                                      |
| [//for Default Style]                                                                                                                              |
|                                                                                                                                                                                                                      |
| [SkinStorage][.SetVisualStyle(fontListBox, [\"Default\"]);]          |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [//for Blend Style]                                                                                                                                |
|                                                                                                                                                                                                                      |
| [SkinStorage][.SetVisualStyle(fontListBox, [\"Blend\"]);]            |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [//for Office2007Silver]                                                                                                                           |
|                                                                                                                                                                                                                      |
| [SkinStorage][.SetVisualStyle(fontListBox, [\"Office2007Silver\"]);] |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [//for Office2007Blue]                                                                                                                             |
|                                                                                                                                                                                                                      |
| [SkinStorage][.SetVisualStyle(fontListBox, [\"Office2007Blue\"]);]   |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [//for Office2007Black]                                                                                                                            |
|                                                                                                                                                                                                                      |
| [SkinStorage][.SetVisualStyle(fontListBox, [\"Office2007Black\"]);]  |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [//for Office2003]                                                                                                                                 |
|                                                                                                                                                                                                                      |
| [SkinStorage][.SetVisualStyle(fontListBox, [\"Office2003\"]);]       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 483: FontListBox with \"Blend\" Visual Style

***[]*** 

{border="0"}

Figure 484: FontListBox with \"Office2007Silver\" Visual Style

 

[]{#p266} 

[]{#related-topics}

