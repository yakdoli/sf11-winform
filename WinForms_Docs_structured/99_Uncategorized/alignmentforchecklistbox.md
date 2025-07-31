---
title: alignmentforchecklistbox.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\alignmentforchecklistbox.md
created_at: 2025-07-03
---






#### Alignment for CheckListBox {#alignment-for-checklistbox style="tab-stops: 0pt"}

The check box in the CheckListBox Item can be aligned to the left or right side of the control using the **CheckBoxAlignment** property. This dependency property sets the alignment of the check box of the items. Following are the alignment options.

[·      ]**Left**: Check box in the CheckListBox Item is aligned to the left

[·      ]**Right**: Check box in the CheckListBox Item is aligned to the right

 

To set the CheckBoxAlignment to ***Right***, use the following code.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\<!\-- Adding CheckListBox with CheckBoxAlignment \--\>]                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\<][syncfusion][:][CheckListBox][ Name][=\"checkListBox\"][ CheckBoxAlignment][=\"Right\"\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    ][\<!\-- Adding CheckListBox items \--\>]                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    ][\<][syncfusion][:][CheckListBoxItem][ Content][=\"Mexico\"/\>]                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    ][\<][syncfusion][:][CheckListBoxItem][ Content][=\"Canada\" /\>]                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    ][\<][syncfusion][:][CheckListBoxItem][ Content][=\"Bermuda\" /\>]                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    ][\<][syncfusion][:][CheckListBoxItem][ Content][=\"Belize\" /\>]                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    ][\<][syncfusion][:][CheckListBoxItem][ Content][=\"Panama\" /\>]                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\</][syncfusion][:][CheckListBox][\>]                                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                            |
|                                                                                                                           |
| []                                                                      |
|                                                                                                                           |
| [// Align the Check Box.]                                               |
|                                                                                                                           |
| [checkListBox.CheckBoxAlignment = [CheckBoxAlignment].Right;] |
+---------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 121: CheckBoxAlignment = \"Right\"

[]{#related-topics}

