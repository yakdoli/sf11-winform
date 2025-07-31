---
title: settingpanelvisibilities.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\settingpanelvisibilities.md
created_at: 2025-07-03
---






#### Setting Panel Visibilities {#setting-panel-visibilities style="tab-stops: 0pt"}

The ColorPickerPalette control includes three panels namely ThemePanel, StandardColorPanel, RecentlyUsedPanel. You can set the visibility of these panels by using the ThemePanelVisibility, StandardPanelVisibility, RecentlyUsedPanelVisibility properties respectively. The ThemePanel displays the palette of selected theme colors and their variant colors in the panel. The StandardColorPanel displays a palette of 8 preset colors in panel. The RecentlyUsedColor panel displays the most recently used colors.

 

Use Case Scenarios

You can use the ColorPickerPalette control to view the panels of your choice.

 

Adding Setting Panel Visibilities to an Application

Setting Panel Visibilities can be added to an application by using XAML or C# code.

The following code example illustrates how to add the Setting Panel Visibilities feature to an application through XAML.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\<][sync][:][ColorPickerPalette][ x][:][Name][=\"ColorPicker\" ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [                         ][ThemePanelVisibility][=\"Collapsed\"/\>]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\<][sync][:][ColorPickerPalette][ x][:][Name][=\"ColorPicker\" ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [                         ][StandardPanelVisibility][=\"Collapsed\"/\>]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\<][sync][:][ColorPickerPalette][ x][:][Name][=\"ColorPicker\" ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [                         ][RecentlyUsedPanelVisibility][=\"Collapsed\"/\>]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [              ]                                                                                                                                                                                                                                                                                                                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The following code example illustrates how to add the Setting Panel Visibilities feature to an application through C#.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                      |
|                                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                                         |
| [ColorPickerPalette][ colorpicker = [new] [ColorPickerPalette]();] |
|                                                                                                                                                                                                         |
| [colorpicker.ThemePanelVisibility = System.Windows.[Visibility].Collapsed;]                                                                 |
|                                                                                                                                                                                                         |
| [colorpicker.StandardPanelVisibility = System.Windows.[Visibility].Collapsed;]                                                              |
|                                                                                                                                                                                                         |
| [colorpicker.RecentlyUsedPanelVisibility = System.Windows.]                                                                                                         |
|                                                                                                                                                                                                         |
| [                                          [Visibility].Collapsed;]                                                                         |
|                                                                                                                                                                                                         |
| [              ]                                                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 190: ThemePanelVisibility, StandardPanelVisibility RecentlyUsedPanelVisibility is set to True

{border="0"}

Figure 191: ThemePanelVisibility is set to False

 

{border="0"}

Figure 192: StandaradPanelVisibility is set to False

 

{border="0"}

Figure 193: RecentlyUsedPanelVisibility is set to False[]

 

Properties

Table 18: Panel Visibility Properties Table


  ----------------------------- --------------------------------------------------------------------- -------------------- ------------------------------------- -----------------
  Property                      Description                                                           Type                 Data Type                             Reference links
  ThemePanelVisibility          Enables or disables the visibility of the ThemePanel.                 DependencyProperty   ThemePanelVisibility.Visible          
  StandardPanelVisibility       Enables or disables the visibility of the StandardColorPanel.         DependencyProperty   StandardPanelVisibility.Visible        
  RecentlyUsedPanelVisibility   Enables or disables the visibility of the Recently Used ColorPanel.   DependencyProperty   RecentlyUsedPanelVisibility.Visible    
  ----------------------------- --------------------------------------------------------------------- -------------------- ------------------------------------- -----------------


**[]** 

Sample Link

To view samples:

1.   Select Start -\> Programs -\> Syncfusion -\> Essential Studio x.x.xx -\> Dashboard.

2.   Select Run Locally Installed Samples in WPF Button.

3.   Now expand the DragAndDropManagerDemo tree-view item in the Sample Browser.

4.   Choose any one of the samples listed under it to launch.

[] 

[]{#related-topics}

