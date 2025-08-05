---
title: checkedlistboxmodes1.md
original_path: WinForms_Docs/99_Uncategorized/checkedlistboxmodes1.md
created_at: 2025-08-05
---






#### CheckedListBox Modes {#checkedlistbox-modes style="tab-stops: 0pt"}

The mode of the CheckedListBox can be changed by using the Mode property. This is an enumeration property that holds three modes namely, Normal, Checked and RadioGroup. By setting the value for the mode, the item present in the CheckedListBox will change. The default value for the property is checked. The Normal Mode will be like a List Box with ListBoxItems listed. In the Checked mode, a Checkbox will be visible in front of the content that allows users to select / check the item, and in the RadioGroup mode a Radio button will be present, which allows users to select / check the item.

 

Use Case Scenarios

This feature will be useful for users to view the CheckedListBoxItems that can be switched between the three modes Normal, Checked and RadioGroup Modes.

 

Adding CheckedListBox Mode to an Application

The following code example illustrates the addition of CheckedListBox Mode to the application through XAML.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][syncfusion][:][CheckedListBox ][Mode][=\"Checked\"][ HorizontalAlignment][=\"Center\"][ VerticalAlignment][=\"Center\"][ CheckOnClick][=\"True\"][ ][\>][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                    ][\<][syncfusion][:][CheckedListBoxItem][ [ Content][=\"Chart\"][ ImageMargin][=\"5,5,15,5\"] [ LeftImageSource][=\"images\\chart.png\"][ LeftImageWidth][=\"70\"] [ ImageVerticalAlignment][=\"Center\"\>\</][syncfusion][:][CheckedListBoxItem][\>]]                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                    ][\<][syncfusion][:][CheckedListBoxItem][ [ Content][=\"Gauge\"][ ImageMargin][=\"5,5,15,5\"][ LeftImageSource][=\"images\\gauge.png\"] [ LeftImageWidth][=\"70\"][ IsChecked][=\"True\"\>\</][syncfusion][:][CheckedListBoxItem][\>]]                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                    ][\<][syncfusion][:][CheckedListBoxItem][ [ Content][=\"ListBox\"][ ImageMargin][=\"5,5,15,5\"] [ LeftImageSource][=\"images\\List box.png\"][ LeftImageWidth][=\"70\"] [ \>\</][syncfusion][:][CheckedListBoxItem][\>]]                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\</][syncfusion][:][CheckedListBox][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [              ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

{border="0"}

Figure 45:  CheckedListBox with Checked Mode

 

{border="0"}

Figure 46: CheckedListBox with Normal Mode

 

 

{border="0"}

Figure 47: CheckedListBox with Radio Group Mode

 

 

Properties

Table 14: CheckedListBox Mode Properties Table

  ---------- -------------------------------------------------------------------- -------------------- --------------- -----------------
  Property   Description                                                          Type                 Data Type       Reference links
  Mode       Specifies the mode that is used to display the CheckedListBoxItems   DependencyProperty   Modes.Checked   
  ---------- -------------------------------------------------------------------- -------------------- --------------- -----------------

[] 

[]{#related-topics}

