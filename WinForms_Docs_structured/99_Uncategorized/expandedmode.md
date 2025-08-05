---
title: expandedmode.md
original_path: WinForms_Docs/99_Uncategorized/expandedmode.md
created_at: 2025-08-05
---






#### Expanded Mode {#expanded-mode style="tab-stops: 0pt"}

Expanded Mode allows you to pick colors from the ColorPickerPalette. By setting IsExpanded Property to True, the ColorPickerPalette control can be hosted in Expanded Mode. By default, this mode is set to False.

 

Use Case Scenarios

Expanded Mode can be used when you want to have the ColorPickerPalette without drop down.

[] 

Adding Expanded Mode to an Application

Expanded Mode can be added to an application by using XAML or C# code.

 

The following code example illustrates how to add the Expanded Mode to an application.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][sync][:][ColorPickerPalette][ IsExpanded][=\"True\"/\>] |
|                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                  |
|                                                                                                                                                                                   |
| **[]**                                                                                                                                        |
|                                                                                                                                                                                   |
| [      [ColorPickerPalette] colorpicker = [new] [ColorPickerPalette]();] |
|                                                                                                                                                                                   |
| [      ][colorpicker.IsExpanded = true;]                                                  |
|                                                                                                                                                                                   |
| [      ]                                                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 200: ColorPickerPalette with IsExpanded is set to True

 

Properties

Table 21: IsExpanded Property Table


  ------------ ---------------------------------------------------------------------- -------------------- ----------- -----------------
  Property     Description                                                            Type                 Data Type   Reference links
  IsExpanded   Enables or disables the Expanded Mode property of ColorPickerPalette   DependencyProperty   False       
  ------------ ---------------------------------------------------------------------- -------------------- ----------- -----------------


**[]** 

Sample Link

To view samples:

1.   Select Start -\> Programs -\> Syncfusion -\> Essential Studio x.x.xx -\> Dashboard.

2.   Select Run Locally Installed Samples in WPF Button.

3.   Now expand the DragAndDropManagerDemo tree-view item in the Sample Browser.

4.   Choose any one of the samples listed under it to launch.

[] 

[]{#related-topics}

