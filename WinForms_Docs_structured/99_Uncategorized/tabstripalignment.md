---
title: tabstripalignment.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\tabstripalignment.md
created_at: 2025-07-03
---






#### Tab Strip Alignment {#tab-strip-alignment style="tab-stops: 0pt"}

[] 

TabStrip of the TabControlExt can be aligned to all four sides of the TabControlExt by using the TabStripPlacement property. This dependency property is used to dock the Tab Header, relative to the content of the TabControlExt. It returns the docking state of the TabItem.

 

The following TabStrip placement options are supported by the TabControlExt.

[] 

[·      ]**Top**-positions the TabStrip at the top of the TabControlExt control

[·      ]**Bottom**-positions the TabStrip at the bottom of the TabControlExt control

[·      ]**Left**-positions the TabStrip to the left of the TabControlExt control

[·      ]**Right**-positions the TabStrip to the right of the TabControlExt control

[] 

To place the TabStrip to the \"Left\" of the TabControlExt, use the below code.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\<!\-- Adding TabControlExt with TabStripPlacement is left \--\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\<][syncfusion][:][TabControlExt][ Margin][=\"20\"][ Name][=\"tabControlExt\"][ TabStripPlacement][=\"Left\"\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [    ][\<!\-- Adding TabItemExt \--\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [    ][\<][syncfusion][:][TabItemExt][ Name][=\"tabItemExt1\"][ Header][=\"TabItemExt1\"/\>]                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [    ][\<!\-- Adding TabItemExt \--\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [    ][\<][syncfusion][:][TabItemExt][ Name][=\"tabItemExt2\"][ Header][=\"TabItemExt2\"/\>]                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\</][syncfusion][:][TabControlExt][\>]                                                                                                                                                                                                                                                                                                                                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                  |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [// Creating instance of the TabControlExt control]                                                                                                           |
|                                                                                                                                                                                                                                 |
| [TabControlExt][ tabControlExt = [new] [TabControlExt]();] |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [//Creating the instance of StackPanel]                                                                                                                       |
|                                                                                                                                                                                                                                 |
| [StackPanel][ stackPanel = [new] [StackPanel]();]          |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [//Creating instance of the TabItemExt ]                                                                                                                      |
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
| [//Adding TabItemExt to TabControlExt]                                                                                                                        |
|                                                                                                                                                                                                                                 |
| [tabControlExt.Items.Add(tabItemExt1);]                                                                                                                                     |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [//Creating instance of the TabItemExt2 ]                                                                                                                     |
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
| [//Adding TabItemExt to TabControlExt]                                                                                                                        |
|                                                                                                                                                                                                                                 |
| [tabControlExt.Items.Add(tabItemExt2);]                                                                                                                                     |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [//Setting TabStripPlacement property as Left]                                                                                                                |
|                                                                                                                                                                                                                                 |
| [tabControlExt.TabStripPlacement = [Dock].Left;]                                                                                                    |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [//Adding control to the StackPanel]                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [stackPanel.Children.Add(tabControlExt); ]                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

*[]* 

Figure 1001: TabStripPlacement = \"Left\"

 

[]{#p526} 

More:





