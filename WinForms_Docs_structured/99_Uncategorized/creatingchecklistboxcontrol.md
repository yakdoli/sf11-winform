---
title: creatingchecklistboxcontrol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\creatingchecklistboxcontrol.md
created_at: 2025-07-03
---








  









### Creating CheckListBox control {#creating-checklistbox-control style="tab-stops: 0pt"}

You can create a CheckListBox control either by using XAML code or C# code. To create a CheckListBox control, use the following code.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<!\-- Adding CheckListBox \--\>]                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<][syncfusion][:][CheckListBox][ Name][=\"checkListBox\"\>]                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [    ][\<!\-- Adding CheckListBox items \--\>]                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [    ][\<][syncfusion][:][CheckListBoxItem][ Content][=\"Mexico\"/\>]   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [    ][\<][syncfusion][:][CheckListBoxItem][ Content][=\"Canada\" /\>]  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [    ][\<][syncfusion][:][CheckListBoxItem][ Content][=\"Bermuda\" /\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [    ][\<][syncfusion][:][CheckListBoxItem][ Content][=\"Belize\" /\>]  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [    ][\<][syncfusion][:][CheckListBoxItem][ Content][=\"Panama\" /\>]  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\</][syncfusion][:][CheckListBox][\>]                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                            |
|                                                                                                                                                                                                           |
| []                                                                                                                                                      |
|                                                                                                                                                                                                           |
| [// Creating an instance of CheckListBox]                                                                                                               |
|                                                                                                                                                                                                           |
| [CheckListBox][ checkListBox = [new] [CheckListBox]();]              |
|                                                                                                                                                                                                           |
| []                                                                                                                                                      |
|                                                                                                                                                                                                           |
| [// Creating an instance of CheckListBoxItem]                                                                                                           |
|                                                                                                                                                                                                           |
| [CheckListBoxItem][ checkListBoxItem1 = [new] [CheckListBoxItem]();] |
|                                                                                                                                                                                                           |
| []                                                                                                                                                      |
|                                                                                                                                                                                                           |
| [// Adding content to CheckListBoxItem]                                                                                                                 |
|                                                                                                                                                                                                           |
| [checkListBoxItem1.Content = [\"Mexico\"];]                                                                                                   |
|                                                                                                                                                                                                           |
| []                                                                                                                                                      |
|                                                                                                                                                                                                           |
| [// Adding CheckListBoxItem to CheckListBox]                                                                                                            |
|                                                                                                                                                                                                           |
| [checkListBox.Items.Add(checkListBoxItem1);   ]                                                                                                                       |
|                                                                                                                                                                                                           |
| []                                                                                                                                                      |
|                                                                                                                                                                                                           |
| [// Creating an instance of CheckListBoxItem]                                                                                                           |
|                                                                                                                                                                                                           |
| [CheckListBoxItem][ checkListBoxItem2 = [new] [CheckListBoxItem]();] |
|                                                                                                                                                                                                           |
| []                                                                                                                                                      |
|                                                                                                                                                                                                           |
| [// Adding content to CheckListBoxItem]                                                                                                                 |
|                                                                                                                                                                                                           |
| [checkListBoxItem1.Content = [\"Bermuda\"];]                                                                                                  |
|                                                                                                                                                                                                           |
| []                                                                                                                                                      |
|                                                                                                                                                                                                           |
| [// Adding CheckListBoxItem to CheckListBox]                                                                                                            |
|                                                                                                                                                                                                           |
| [checkListBox.Items.Add(checkListBoxItem2); ]                                                                                                                         |
|                                                                                                                                                                                                           |
| []                                                                                                                                                      |
|                                                                                                                                                                                                           |
| [// \...\.....]                                                                                                                                         |
|                                                                                                                                                                                                           |
| [// \...\.....]                                                                                                                                         |
|                                                                                                                                                                                                           |
| [this][.Content = checkListBox;   ]                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 119: CheckListBox Control

 

[]{#related-topics}

