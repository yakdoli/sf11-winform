---
title: newuserinterfacesupport.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\newuserinterfacesupport.md
created_at: 2025-07-03
---






#### New User Interface Support {#new-user-interface-support style="tab-stops: 0pt"}

[]{#p84}The feature adds new additional User Interface to the Color Picker, so that you can have two more User Interfaces for the ColorPicker Control. Both will have same functionality, except that the User Interface will change. ColorPicker and ColorEdit controls can be displayed in four different modes. They are HSV, Classic HSV, RGB and Classic RGB modes. The VisualizationStyle property is used to switch between these modes. The HSV and RGB are the two User Interfaces which are user-friendly, more attractive and in general, it looks more professional.

 

Use Case Scenarios

New User Interface support enables you to create the ColorPicker control with a visually rich interface.

[] 

Adding New User Interface support to an Application

New User Interface support can be added to an application by using XAML or with C#.

**[]** 

Adding through XAML

The following code example illustrates how to add the New User Interface support feature to an application through XAML.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<][sync][:][ColorPicker][ VisualizationStyle][=\"HSV\"][ BrushMode][=\"Solid\"/\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<][sync][:][ColorEdit ][VisualizationStyle][=\"HSV\"/\>]                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [              ]                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Adding through C#

The following code example illustrates how to add the New User Interface support feature to an application through C#.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                            |
|                                                                                                                                                             |
| **[]**                                                                                                                  |
|                                                                                                                                                             |
| [   [ColorPicker] Picker = [new] [ColorPicker]();] |
|                                                                                                                                                             |
| [   Picker.VisualizationStyle = ]                                                                                       |
|                                                                                                                                                             |
| [                         Syncfusion.Windows.Tools.[ColorSelectionMode].HSV;]                   |
|                                                                                                                                                             |
| []                                                                                                                      |
|                                                                                                                                                             |
| [   [ColorEdit] ColEdit = [new] [ColorEdit]();]    |
|                                                                                                                                                             |
| [   ColEdit.VisualizationStyle = ]                                                                                      |
|                                                                                                                                                             |
| [                         Syncfusion.Windows.Tools.[ColorSelectionMode].HSV;]                   |
|                                                                                                                                                             |
| [   ]                                                                                                                   |
|                                                                                                                                                             |
| [           ]                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

{border="0"}

Figure 157: ColorPicker with VisualizationStyle is set to HSV

 

{border="0"}

Figure 158: ColorPicker with VisualizationStyle is set to RGB

[] 

{border="0"}

Figure 159: ColorEdit with VisualizationStyle is set to HSV

{border="0"}

Figure 160: ColorEdit with VisualizationStyle is set to RGB

**[]** 

Properties

Table 17: New User Interface Support Property Table


  -------------------- --------------------------------------------------------------------------- -------------------- ------------------------ -----------------
  Property             Description                                                                 Type                 Data Type                Reference links
  VisualizationStyle   Specifies the style that can be used to set ColorPicker /or ColorEdit UI.   DependencyProperty   ColorSelectionMode.HSV   
  -------------------- --------------------------------------------------------------------------- -------------------- ------------------------ -----------------


**[]** 

Sample Link

To view samples:

1.   Select Start -\> Programs -\> Syncfusion -\> Essential Studio x.x.xx -\> Dashboard.

2.   Select Run Locally Installed Samples in WPF Button.

3.   Now expand the DragAndDropManagerDemo tree-view item in the Sample Browser.

4.   Choose any one of the samples listed under it to launch.

 

Theme Appearance

The appearance of the ColorPicker can be customized using Styles. The following are the various built-in visual styles for ColorPicker.

[] 

{border="0"}

Figure 161: Default Style

 

{border="0"}

Figure 162: Blend Style

 

{border="0"}

Figure 163: Office2003 Style

 

{border="0"}

Figure 164: Office2007Black Style

 

{border="0"}

Figure 165: Office2007Blue Style

 

{border="0"}

Figure 166: Office2007Silver Style

 

 

 

[]{#related-topics}

