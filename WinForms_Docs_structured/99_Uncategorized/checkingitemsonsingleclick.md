---
title: checkingitemsonsingleclick.md
original_path: WinForms_Docs/99_Uncategorized/checkingitemsonsingleclick.md
created_at: 2025-08-05
---






##### Checking Items on Single Click {#checking-items-on-single-click style="tab-stops: 0pt"}

 

CheckedListBox control provides support to check items on a single mouse click. This can be achieved by enabling the **CheckOnClick** property. The default value for this property is set to ***false***.

 

The following code example illustrates how to set this property.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<][syncfusion][:][CheckedListBox][ HorizontalAlignment][=\"Center\"][ VerticalAlignment][=\"Center\"][ CheckOnClick][=\"True\" \>][]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [                    ][\<][syncfusion][:][CheckedListBoxItem][ [ Content][=\"Chart\"][ ImageMargin][=\"5,5,15,5\"] [ LeftImageSource][=\"images\\chart.png\"][ LeftImageWidth][=\"70\"] [ ImageVerticalAlignment][=\"Center\"\>\</][syncfusion][:][CheckedListBoxItem][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [                    ][\<][syncfusion][:][CheckedListBoxItem][ [ Content][=\"Gauge\"][ ImageMargin][=\"5,5,15,5\"][ LeftImageSource][=\"images\\gauge.png\"] [ LeftImageWidth][=\"70\"][ IsChecked][=\"True\"\>\</][syncfusion][:][CheckedListBoxItem][\>]]                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [                    ][\<][syncfusion][:][CheckedListBoxItem][ [ Content][=\"ListBox\"][ ImageMargin][=\"5,5,15,5\"] [ LeftImageSource][=\"images\\List box.png\"][ LeftImageWidth][=\"70\"] [ \>\</][syncfusion][:][CheckedListBoxItem][\>]]                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [                ][\</][syncfusion][:][CheckedListBox][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                     |
|                                                                                                                                                                                                    |
| []                                                                                                                                               |
|                                                                                                                                                                                                    |
| [CheckedListBox][ checkedlistbox = [new] [CheckedListBox]();]       |
|                                                                                                                                                                                                    |
| [checkedlistbox.CheckOnClick = [true];]                                                                                                   |
|                                                                                                                                                                                                    |
| [CheckedListBoxItem][ checkeditem = [new] [CheckedListBoxItem]();]  |
|                                                                                                                                                                                                    |
| [checkeditem.Content = [\"Chart\"];]                                                                                                   |
|                                                                                                                                                                                                    |
| [CheckedListBoxItem][ checkeditem1 = [new] [CheckedListBoxItem]();] |
|                                                                                                                                                                                                    |
| [checkeditem1.Content = [\"Gauge\"];]                                                                                                  |
|                                                                                                                                                                                                    |
| [CheckedListBoxItem][ checkeditem2 = [new] [CheckedListBoxItem]();] |
|                                                                                                                                                                                                    |
| [checkeditem2.Content = [\"ListBox\"];]                                                                                                |
|                                                                                                                                                                                                    |
| [checklistbox.Items.Add(checkeditem);]                                                                                                                         |
|                                                                                                                                                                                                    |
| [checklistbox.Items.Add(checkeditem1);]                                                                                                                        |
|                                                                                                                                                                                                    |
| [checklistbox.Items.Add(checkeditem2);]                                                                                                                        |
|                                                                                                                                                                                                    |
| [pivotitem.Content = ][checkedlistbox][;]                                              |
|                                                                                                                                                                                                    |
| [LayoutRoot.Children.Add(pivotitem);]                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 43: CheckedListBox with CheckOnClick property set to \"True\"

*[]* 

*[]* 

*[]* 

*[]* 

*[]* 

Properties

Table 13: CheckOnClick Property Table

  -------------- ---------------------------------------------------------------- --------------------- ----------- -----------------
  Property       Description                                                      Type                  Data Type   Reference links
  CheckOnClick   Enables or disables the Checking Items by a single mouse-click   Dependency Property   False       
  -------------- ---------------------------------------------------------------- --------------------- ----------- -----------------

*[]* 

[]{#related-topics}

