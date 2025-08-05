---
title: colorschemes1.md
original_path: WinForms_Docs/99_Uncategorized/colorschemes1.md
created_at: 2025-08-05
---






##### Color Schemes {#color-schemes style="tab-stops: 0pt"}

[] 

Office2007 Form supports all the three office color schemes which can be edited through **ColorSchemes** property.

[] 

{border="0"}

[] 

***[]*** 

Figure 1293: ColorScheme Property for Office2007Form[]{#p1095}

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                |
| [//To set Blue color scheme]                                                                                                                 |
|                                                                                                                                                                                                |
| [this][.ColorScheme = [Office2007Theme].Blue;][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1096}[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                   |
|                                                                                                                                                                      |
| []                                                                                                                                           |
|                                                                                                                                                                      |
| [\'To set Blue color scheme]                                                                                       |
|                                                                                                                                                                      |
| [Me][.ColorScheme = Office2007Theme.Blue][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

***[]*** 

Figure 1294: Blue, Silver and Black ColorSchemes in OfficeForm

 

Background Color for Office2007 Form

 

The background of the Office2007 form can be same, as the color scheme applied to the form. Set UseOffice2007SchemeBackColor property to true to make this effective.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                  |
|                                                                                                                                                                                                 |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                 |
| [this][.UseOffice2007SchemeBackColor = [true];][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p1097}[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                        |
|                                                                                                                                                                                                           |
| []                                                                                                                                                                                |
|                                                                                                                                                                                                           |
| [Me][.UseOffice2007SchemeBackColor = [True]][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1295: Office 2007 Scheme BackColor for Office2007Form

**[]** 

Vista Aero Theme

 

Vista Aero theme support is available for Office Form when used in Vista machine.

[] 

{border="0"}

**[]** 

Figure 1296: Vista Aero Theme for OfficeForm

 

 

 

Office2007Form Color Scheme Settings

Office2007Forms now have the ability to apply or not to apply AeroTheme on forms with a glassy effect. This can be done by **ApplyAeroTheme** property, setting its value either to **True** or **False**.

AeroTheme support is available for Office2007Form when used in Vista machine. Earlier ColorSchemes cannot be applied to Office2007Form when AeroTheme was enabled. Now ColorSchemes can be applied by disabling AeroTheme on Office2007Form.

The following code illustrates how ColorSchemes can be applied by disabling AeroTheme on Office2007Form.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                    |
| [// Disables Aero Theme on Office2007Form.]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                    |
| [this][.][ ApplyAeroTheme ][= [false];][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                  |
| ['Disables Aero Theme on Office2007Form.]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                  |
| [Me][.][ ApplyAeroTheme ][= [false];][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

