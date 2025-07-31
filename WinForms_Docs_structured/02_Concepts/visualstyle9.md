---
title: visualstyle9.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\visualstyle9.md
created_at: 2025-07-03
---






#### Visual Style {#visual-style style="tab-stops: 0pt"}

 

You can enhance the appearance of the FontListComboBox by using different visual styles that are available for the control. The visual style for the FontListComboBox is set by using the **VisualStyle** property.

 


+-----------------------------------+----------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                  |
+-----------------------------------+----------------------------------------------------------------------------------------------+
| VisualStyle                       | Sets the visual style for the FontListComboBox control. The options provided are as follows. |
|                                   |                                                                                              |
|                                   | []         |
|                                   |                                                                                              |
|                                   | [·      ]Blend                                                  |
|                                   |                                                                                              |
|                                   | [·      ]Office2003                                             |
|                                   |                                                                                              |
|                                   | [·      ]Office2007Blue                                         |
|                                   |                                                                                              |
|                                   | [·      ]Office2007Black                                        |
|                                   |                                                                                              |
|                                   | [·      ]Office2007Silver                                       |
|                                   |                                                                                              |
|                                   | [·      ]ShinyBlue                                              |
|                                   |                                                                                              |
|                                   | [·      ]ShinyRed                                               |
|                                   |                                                                                              |
|                                   | [·      ]SyncOrange                                             |
|                                   |                                                                                              |
|                                   | [·      ]VS2010                                                 |
|                                   |                                                                                              |
|                                   | [·      ]Metro                                                  |
|                                   |                                                                                              |
|                                   |                                                                                              |
+-----------------------------------+----------------------------------------------------------------------------------------------+


 

To set the visual style for the FontListComboBox, use the following code snippet.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                             |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                       |
|                                                                                                                                                                                                                            |
| [//for Default Style]                                                                                                                                    |
|                                                                                                                                                                                                                            |
| [SkinStorage][.SetVisualStyle(fontListComboBox1, [\"Default\"]);]          |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                                            |
| [//for Blend Style]                                                                                                                                      |
|                                                                                                                                                                                                                            |
| [SkinStorage][.SetVisualStyle(fontListComboBox1, [\"Blend\"]);]            |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                                            |
| [//for Office2007Silver]                                                                                                                                 |
|                                                                                                                                                                                                                            |
| [SkinStorage][.SetVisualStyle(fontListComboBox1, [\"Office2007Silver\"]);] |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                                            |
| [//for Office2007Blue]                                                                                                                                   |
|                                                                                                                                                                                                                            |
| [SkinStorage][.SetVisualStyle(fontListComboBox1, [\"Office2007Blue\"]);]   |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                                            |
| [//for Office2007Black]                                                                                                                                  |
|                                                                                                                                                                                                                            |
| [SkinStorage][.SetVisualStyle(fontListComboBox1, [\"Office2007Black\"]);]  |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                                            |
| [//for Office2003]                                                                                                                                       |
|                                                                                                                                                                                                                            |
| [SkinStorage][.SetVisualStyle(fontListComboBox1, [\"Office2003\"]);]       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 492: FontListComboBox with \"Blend\" Visual Style

 

{border="0"}

Figure 493: FontListComboBox with \"Office2007Black\" Visual Style

 

[]{#p281} 

[]{#related-topics}

