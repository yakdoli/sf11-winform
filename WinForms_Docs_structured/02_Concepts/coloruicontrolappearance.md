---
title: coloruicontrolappearance.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\coloruicontrolappearance.md
created_at: 2025-07-03
---






##### ColorUIControl Appearance {#coloruicontrol-appearance style="tab-stops: 0pt"}

[] 

This section discusses the appearance, border styles and size settings of the ColorUIControl.

[] 

Border Styles

[] 

The border styles for the ColorUIControl can be set through BorderStyle property.

[] 


+-----------------------------------+-----------------------------------------------------+
| ColorUIControl Properties         | Description                                         |
+-----------------------------------+-----------------------------------------------------+
| BorderStyle                       | Sets border style for the control. The options are, |
|                                   |                                                     |
|                                   |                                                     |
|                                   |                                                     |
|                                   | *FixedSingle,*                                      |
|                                   |                                                     |
|                                   | *Fixed3D (default) and*                             |
|                                   |                                                     |
|                                   | *None.*                                             |
+-----------------------------------+-----------------------------------------------------+


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                   |
|                                                                                                                                                                                                  |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                  |
| [this][.colorUIControl1.BorderStyle = System.Windows.Forms.[BorderStyle].FixedSingle;] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                             |
|                                                                                                                                                                                                |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                |
| [Me][.colorUIControl1.BorderStyle = System.Windows.Forms.[BorderStyle].FixedSingle] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

[] 

Figure 296: BorderStyle = \"FixedSingle\"

**[]** 

Panel Sizing

**[]** 

The Custom and User color panels can be stretched according to the size of the control using the below properties respectively.

**[]** 


  ---------------------------- ------------------------------------------------------------
  ColorUIControl Properties    Description
  CustomColorStretchOnResize   Gets or Sets enable stretch Custom colors panel on resize.
  UserColorStretchOnResize     Gets or Sets enable stretch User colors panel on resize.
  ---------------------------- ------------------------------------------------------------


**[]** 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                           |
|                                                                                                                                                                          |
| []                                                                                                                                               |
|                                                                                                                                                                          |
| [this][.colorUIControl1.CustomColorsStretchOnResize = [true];] |
|                                                                                                                                                                          |
| [this][.colorUIControl1.UserColorsStretchOnResize = [true];]   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                    |
|                                                                                                                                                                       |
| []                                                                                                                                            |
|                                                                                                                                                                       |
| [Me][.colorUIControl1.CustomColorsStretchOnResize = [True]] |
|                                                                                                                                                                       |
| [Me][.colorUIControl1.UserColorsStretchOnResize = [True]]   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

[] 

Figure 297: Custom Color Panel\'s Normal and Stretched View

 

[]{#p342} 

[]{#related-topics}

