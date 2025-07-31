---
title: featuresofcomboboxadvcontrol1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\featuresofcomboboxadvcontrol1.md
created_at: 2025-07-03
---






##### Features of ComboBoxAdv control {#features-of-comboboxadv-control style="tab-stops: 0pt"}

###### 3.11.2.1.3.1        Multiple Selections {#multiple-selections style="tab-stops: 0pt"}

If we want to select more than one item in the ComboBoxAdv, **AllowMultiSelect** property will be helpful to do this. It allows you to select multiple items in the drop down list. The selected items will be displayed in ascending order as shown in the drop down list. When AllowMutliSelect property is true, the SelectedItems property exposes the items that are selected in the drop down list.

**[]** 

Properties

Table 9: Properties Table


  ------------------ -------------------------------------- --------------------- -------------------------------- -----------------
  Property           Description                            Type                  Data Type                        Reference links
  AllowMultiSelect   Multiple items can be selected.        Dependency Property   Boolean                          NA
  SelectedItems      It contains the selected items value   Dependency Property   ObservableCollection\<object\>   NA
  ------------------ -------------------------------------- --------------------- -------------------------------- -----------------


 

Adding Multiple Selections to an Application

**AllowMultiSelect** property can be added directly to an application using the following code snippet.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [      ][\<][syncfusion][:][ComboBoxAdv][ AllowMultiSelect][=\"True\"\>][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [                            ][]                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [        ][\</][syncfusion][:][ComboBoxAdv][\>]                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                    |
| [      ][ComboBoxAdv][ comboBox = [new] [ComboBoxAdv]();] |
|                                                                                                                                                                                                                                    |
| [       comboBox.AllowMultiSelect = [true];]                                                                                                                              |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 215: ComboBoxAdv Control in Multiple selections

 

 

###### 3.11.2.1.3.2        Default Text {#default-text style="tab-stops: 0pt"}

It displays the default text in the ComboBoxAdv when none of the items is selected in the drop down list.[]

 

Properties

Table 10: Properties Table


  ------------- --------------------------------------------- --------------------- ----------- -----------------
  Property      Description                                   Type                  Data Type   Reference links
  DefaultText   It is possible to display the default text.   Dependency Property   String      NA
  ------------- --------------------------------------------- --------------------- ----------- -----------------


 

Adding DefaultText property to an Application

**DefaultText** property can be added directly to an application in the following way:

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [      ][\<][syncfusion][:][ComboBoxAdv][ DefaultText][=\"..Choose Items..\"\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                            ][]                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [        ][\</][syncfusion][:][ComboBoxAdv][\>]                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                    |
| [      ][ComboBoxAdv][ comboBox = [new] [ComboBoxAdv]();] |
|                                                                                                                                                                                                                                    |
| [       comboBox.DefaultText = [\"..Choose Items..\"];]                                                                                                                |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

{border="0"}

Figure 216: Default Text in ComboBoxAdv control

###### 3.11.2.1.3.3        Delimiter String Customization {#delimiter-string-customization style="tab-stops: 0pt"}

A delimiter string in a ComboBoxAdv is "A string that can be displayed between the selected items in the ComboBoxAdv". We can customize this string by using the property called "SelectedValueDelimiter" in the ComboBoxAdv.

[] 

Properties

Table 11: Property/Properties Table


  Property                 Description                                                Type                  Data Type   Reference links
  ------------------------ ---------------------------------------------------------- --------------------- ----------- -----------------
  SelectedValueDelimiter   The selected items can be separated by the given string.   Dependency Property   String      NA


 

Adding Delimiter String Customization to an Application

**Delimiter string customization** can be added directly to an application using the following code snippet:

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [      ][\<][syncfusion][:][ComboBoxAdv][ SelectedValueDelimiter][=\"#\"\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [                            ][]                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [        ][\</][syncfusion][:][ComboBoxAdv][\>]                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                    |
| [      ][ComboBoxAdv][ comboBox = [new] [ComboBoxAdv]();] |
|                                                                                                                                                                                                                                    |
| [       comboBox.SelectedValueDelimiter = [\"#\"];]                                                                                                                    |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

{border="0"}

Figure 217: Customized Delimiter string.

[]{#related-topics}

