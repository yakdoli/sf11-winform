---
title: itemselection.md
original_path: WinForms_Docs/99_Uncategorized/itemselection.md
created_at: 2025-08-05
---






#### Item Selection {#item-selection style="tab-stops: 0pt"}

When the **IsCheckOnFirstClick** property is set to ***True***, user will be able to select an item, on the first mouse-click. The default value is ***True***.

 

Here is the code for setting this property.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<!\-- Adding CheckListBox \--\>]                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][syncfusion][:][CheckListBox][ Name][=\"checkListBox\"][ IsCheckOnFirstClick][=\"True\"\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [    ][\<!\-- Adding CheckListBox items \--\>]                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [    ][\<][syncfusion][:][CheckListBoxItem][ Content][=\"Mexico\"/\>]                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [    ][\<][syncfusion][:][CheckListBoxItem][ Content][=\"Canada\" /\>]                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [    ][\<][syncfusion][:][CheckListBoxItem][ Content][=\"Bermuda\" /\>]                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [    ][\<][syncfusion][:][CheckListBoxItem][ Content][=\"Belize\" /\>]                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [    ][\<][syncfusion][:][CheckListBoxItem][ Content][=\"Panama\" /\>]                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\</][syncfusion][:][CheckListBox][\>]                                                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                          |
|                                                                                                         |
| []                                                    |
|                                                                                                         |
| [// Enable the IsCheckOnFirstClick property.]         |
|                                                                                                         |
| [checkListBox.IsCheckOnFirstClick = [true];  ] |
+---------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 120: IsCheckOnFirstClick = \"True\"

 

[]{#related-topics}

