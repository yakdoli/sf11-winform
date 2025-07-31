---
title: settingvisualstyles.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\settingvisualstyles.md
created_at: 2025-07-03
---






#### Setting Visual Styles {#setting-visual-styles style="tab-stops: 0pt"}

[] 

The appearance of the TabControlExt control is customized by using the **VisualStyle** property. This is an attached property which gets or sets the visual style for the control.

[] 


+-----------------------------------+-------------------------------------------------------------------------------------------+
| Property                          | Description                                                                               |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| VisualStyle                       | Sets the visual style for the TabControlExt control. The options provided are as follows. |
|                                   |                                                                                           |
|                                   | []      |
|                                   |                                                                                           |
|                                   | [·      ]Blend                                               |
|                                   |                                                                                           |
|                                   | [·      ]Office2003                                          |
|                                   |                                                                                           |
|                                   | [·      ]Office2007Blue                                      |
|                                   |                                                                                           |
|                                   | [·      ]Office2007Black                                     |
|                                   |                                                                                           |
|                                   | [·      ]Office2007Silver                                    |
|                                   |                                                                                           |
|                                   | [·      ]ShinyBlue                                           |
|                                   |                                                                                           |
|                                   | [·      ]ShinyRed                                            |
|                                   |                                                                                           |
|                                   | [·      ]SyncOrange                                          |
|                                   |                                                                                           |
|                                   | [·      ]VS2010                                              |
|                                   |                                                                                           |
|                                   | [·      ]Metro                                               |
|                                   |                                                                                           |
|                                   |                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------+


[] 

The following code example illustrates how to set the visual style for the TabControlExt.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<!\-- Adding TabControlExt \--\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][syncfusion][:][TabControlExt][ Name][=\"tabControlExt\"][ [syncfusion][:][SkinStorage.VisualStyle][=\"Office2007Blue\"\>]]                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [    ][\<!\-- Adding TabItemExt \--\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [    ][\<][syncfusion][:][TabItemExt][ Name][=\"tabItemExt1\"][ Header][=\"TabItemExt1\"/\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [    ][\<!\-- Adding TabItemExt \--\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [    ][\<][syncfusion][:][TabItemExt][ Name][=\"tabItemExt2\"][ Header][=\"TabItemExt2\"/\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\</][syncfusion][:][TabControlExt][\>]                                                                                                                                                                                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                  |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [// Setting the visual style]                                                                                                                                 |
|                                                                                                                                                                                                                                 |
| [// Creating instance of the TabControlExt control]                                                                                                           |
|                                                                                                                                                                                                                                 |
| [TabControlExt][ tabControlExt = [new] [TabControlExt]();] |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [// Creating the instance of StackPanel.]                                                                                                                     |
|                                                                                                                                                                                                                                 |
| [StackPanel][ stackPanel = [new] [StackPanel]();]          |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [// Creating instance of the TabItemExt]                                                                                                                      |
|                                                                                                                                                                                                                                 |
| [TabItemExt][ tabItemExt1 = [new] [TabItemExt]();]         |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [// Setting header of the TabItemExt]                                                                                                                         |
|                                                                                                                                                                                                                                 |
| [tabItemExt1.Header = [\"TabItemExt1\"];]                                                                                                           |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [// Adding TabItemExt to TabControlExt.]                                                                                                                      |
|                                                                                                                                                                                                                                 |
| [tabControlExt.Items.Add(tabItemExt1);]                                                                                                                                     |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [// Creating instance of the TabItemExt2]                                                                                                                     |
|                                                                                                                                                                                                                                 |
| [TabItemExt][ tabItemExt2 = [new] [TabItemExt]();]         |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [// Setting header of the TabItemExt]                                                                                                                         |
|                                                                                                                                                                                                                                 |
| [tabItemExt2.Header = [\"TabItemExt2\"];]                                                                                                           |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [// Adding TabItemExt to TabControlExt]                                                                                                                       |
|                                                                                                                                                                                                                                 |
| [tabControlExt.Items.Add(tabItemExt2);]                                                                                                                                     |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [// Adding control to the StackPanel]                                                                                                                         |
|                                                                                                                                                                                                                                 |
| [stackPanel.Children.Add(tabControlExt); ]                                                                                                                                  |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [// Setting the visual style as Office2007Blue]                                                                                                               |
|                                                                                                                                                                                                                                 |
| [SkinStorage][.SetVisualStyle(tabControlExt, [\"Office2007Blue\"]);]            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

***[]*** 

*[Figure ][1010][: TabControlExt with \"Office2007Blue\" Visual Style]*

***[]*** 

***[]*** 

{border="0"}

***[]*** 

*[Figure ][1011][: TabControlExt with \"Office2007Black\" Visual Style]*

*[]* 

*[]* 

{border="0"}

*[]* 

*[Figure ][1012][: TabControlExt with \"Blend\" Visual Style[]{#p536}]*

*[]* 

[]{#related-topics}

