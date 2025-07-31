---
title: morecoloroption.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\morecoloroption.md
created_at: 2025-07-03
---






#### MoreColor Option {#morecolor-option style="tab-stops: 0pt"}

In addition to colors in Theme colors and Standard colors, MoreColor feature allows you to select wide range of color options. MoreColor feature includes two categories namely Standard Colors and Custom Colors. The Standard Colors includes 140 colors clustered in the shape of a Hexagon. The color chosen from this cluster will also be added in the RecentlyUsedPanel. You can also set the visibility of the MoreColor Option by using the MoreColorOptionVisibility property.

 

Use Case Scenarios

MoreColor Option can be used when you want to select colors using standard and custom colors.

 

Adding MoreColor Option to an Application

MoreColor Option can be added to an application by using XAML or C# code.

 

The following code example illustrates how to add the MoreColor Option to an Application through XAML.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\<][sync][:][ColorPickerPalette][ x][:][Name][=\"ColorPicker\"][ ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [                         MoreColorOptionVisibility][=\"Visible\" /\>]                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The following code example illustrates how to add the MoreColor Option to an Application through C#.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                        |
|                                                                                                                                                                                                         |
| **[]**                                                                                                                                                              |
|                                                                                                                                                                                                         |
| [ColorPickerPalette][ colorpicker = [new] [ColorPickerPalette]();] |
|                                                                                                                                                                                                         |
| [colorpicker.MoreColorOptionVisibility = System.[Visibility].Visible;]                                                                      |
|                                                                                                                                                                                                         |
|                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

{border="0"}

Figure 197: More Color Window with standard colors

[] 

{border="0"}

Figure 198: More Color Window with Custom colors[]

 

Properties

Table 20: MoreColorOptionVisibility Property Table


  --------------------------- ------------------------------------------------------------- --------------------- -------------------- -----------------
  Property                    Description                                                   Type                  Data Type            Reference links
  MoreColorOptionVisibility   Enables or disables the visibility of the MoreColor Window.   Dependency Property   Visibility.Visible   
  --------------------------- ------------------------------------------------------------- --------------------- -------------------- -----------------


**[]** 

Sample Link

To view samples:

1.   Select Start -\> Programs -\> Syncfusion -\> Essential Studio x.x.xx -\> Dashboard.

2.   Select   Run Locally Installed Samples in WPF Button.

3.   Now expand the DragAndDropManagerDemo tree-view item in the Sample Browser.

4.   Choose any one of the samples listed under it to launch.

[]{#related-topics}

