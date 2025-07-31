---
title: colorthemes.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\colorthemes.md
created_at: 2025-07-03
---






#### Color Themes {#color-themes style="tab-stops: 0pt"}

The ColorPickerPalette control includes a list of predefined themes. It allows you to set the required themes. Based on the selected themes, combination of selected theme colors will be displayed on the ThemePanel. The default theme if set to "Office" theme. You can also set the visibility of the ThemePanel by using the ThemePanelVisibility Property.

 

Use Case Scenarios

You can use the Color Themes to have colors based on specific themes.

[] 

Adding Color Theme to an Application

Color themes can be added to an application by using XAML or C# code.

 

The following code example illustrates how to add the Color Theme feature to an application through XAML.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][sync][:][ColorPickerPalette][ x][:][Name][=\"ColorPicker\"][ Themes][=\"Apex\" /\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The following code example illustrates how to add the Color Theme feature to an application through C#.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                        |
|                                                                                                                                                                                                         |
| **[]**                                                                                                                                                              |
|                                                                                                                                                                                                         |
| [ColorPickerPalette][ colorpicker = [new] [ColorPickerPalette]();] |
|                                                                                                                                                                                                         |
| [colorpicker.Themes = [PaletteTheme].Apex;]                                                                                                 |
|                                                                                                                                                                                                         |
|                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 194: ColorPickerPalette with "Office" Theme

 

{border="0"}

Figure 195: ColorPickerPalette with "Apex" Theme

[] 

{border="0"}

Figure 196: ColorPickerPalette with "Metro" Theme

 

Properties

Table 19: Color Theme Properties Table


  ---------- ---------------------------------------------------------------------------------------------------------- --------------------- --------------------- -----------------
  Property   Description                                                                                                Type                  Data Type             Reference links
  Themes     Describes the enum which contains Palette Themes that can be applied to ColorPickerPalette Themes Panel.   Dependency Property   PaletteTheme.Office   
  ---------- ---------------------------------------------------------------------------------------------------------- --------------------- --------------------- -----------------


[] 

Sample Link

To view samples:

1.   Select Start -\> Programs -\> Syncfusion -\> Essential Studio x.x.xx -\> Dashboard.

2.   Select   Run Locally Installed Samples in WPF Button.

3.   Now expand the DragAndDropManagerDemo tree-view item in the Sample Browser.

4.   Choose any one of the samples listed under it to launch.

[]{#related-topics}

