---
title: settingvisualstyleforchecklistbox.md
original_path: WinForms_Docs/02_Concepts/settingvisualstyleforchecklistbox.md
created_at: 2025-08-05
---






#### Setting VisualStyle for CheckListBox {#setting-visualstyle-for-checklistbox style="tab-stops: 0pt"}

The appearance of the CheckListBox control is customized by applying a suitable style using the **VisualStyle** property.

 


+-----------------------------------+------------------------------------------------------------------------------------------+
| Property                          | Description                                                                              |
+-----------------------------------+------------------------------------------------------------------------------------------+
| VisualStyle                       | Sets the visual style for the CheckListBox control. The options provided are as follows. |
|                                   |                                                                                          |
|                                   | [·      ]Blend                                              |
|                                   |                                                                                          |
|                                   | [·      ]Office2003                                         |
|                                   |                                                                                          |
|                                   | [·      ]Office2007Blue                                     |
|                                   |                                                                                          |
|                                   | [·      ]Office2007Black                                    |
|                                   |                                                                                          |
|                                   | [·      ]Office2007Silver                                   |
|                                   |                                                                                          |
|                                   | [·      ]ShinyBlue                                          |
|                                   |                                                                                          |
|                                   | [·      ]ShinyRed                                           |
|                                   |                                                                                          |
|                                   | [·      ]SyncOrange                                         |
|                                   |                                                                                          |
|                                   | [·      ]VS2010                                             |
|                                   |                                                                                          |
|                                   | [·      ]Metro                                              |
+-----------------------------------+------------------------------------------------------------------------------------------+


 

For setting ***Blend*** style, refer the below code snippet.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\<!\-- Adding CheckListBox with Visual Style as Blend \--\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\<][syncfusion][:][CheckListBox][ Name][=\"checkListBox\"][ syncfusion][:][SkinStorage.VisualStyle][=\"Blend\"\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [    ][\<!\-- Adding CheckListBox items \--\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [    ][\<][syncfusion][:][CheckListBoxItem][ Content][=\"Mexico\"/\>]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [    ][\<][syncfusion][:][CheckListBoxItem][ Content][=\"Canada\" /\>]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [    ][\<][syncfusion][:][CheckListBoxItem][ Content][=\"Bermuda\" /\>]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [    ][\<][syncfusion][:][CheckListBoxItem][ Content][=\"Belize\" /\>]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [    ][\<][syncfusion][:][CheckListBoxItem][ Content][=\"Panama\" /\>]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\</][syncfusion][:][CheckListBox][\>]                                                                                                                                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                              |
|                                                                                                                                                                             |
| []                                                                                                                        |
|                                                                                                                                                                             |
| [// Setting the visual style as Blend.]                                                                                   |
|                                                                                                                                                                             |
| [SkinStorage][.SetVisualStyle(checkListBox, [\"Blend\"]); ] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 123: CheckListBox with \"Blend\" Visual Style

 

{border="0"}

Figure 124: CheckListBox with \"Default\" Visual Style

[] 

{border="0"}

Figure 125: CheckListBox with \"Office2007Black\" Visual Style

[] 

{border="0"}

Figure 126: CheckListBox with \"Office2003\" Visual Style

 

{border="0"}

Figure 127: CheckListBox with \"Metro\" Visual Style

 

[]{#related-topics}

