---
title: customizationsettings.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\customizationsettings.md
created_at: 2025-07-03
---






##### Customization Settings {#customization-settings style="tab-stops: 0pt"}

[] 

ColorPickerButton displays the ColorUIControl as its dropdown. ColorPickerButton has properties to customize the ColorUIControl. Refer the [User Guide]{.UGHyperlink} for ColorUIControl. The size for the dropdown, i.e, ColorUIControl can be set using **ColorUISize** property.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                  |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                 |
| [this][.colorPickerButton1.ColorUISize = [new] System.Drawing.[Size](250, 280);] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                            |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                               |
| [Me][.colorPickerButton1.ColorUISize = [New] System.Drawing.[Size](250, 280)] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

**[]** 

Figure 306: ColorUISize-Width = 250, Height = 280

[] 

ColorPicker Appearance

[] 

The appearance and behavior of the ColorPickerButton can be controlled using the below properties.

[] 


  ------------------------------ ----------------------------------------------------------------------------------------
  ColorPickerButton Properties   Description
  SelectedAsBackColor            Specifies whether **ColorPickerButton.SelectedColor** is set as the button backcolor.
  SelectedAsText                 Specifies whether **ColorPickerButton.SelectedColor** is set as the button text value.
  ------------------------------ ----------------------------------------------------------------------------------------


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                      |
|                                                                                                                                                                     |
| []                                                                                                                                          |
|                                                                                                                                                                     |
| [this][.colorPickerButton1.SelectedAsBackcolor = [true];] |
|                                                                                                                                                                     |
| [this][.colorPickerButton1.SelectedAsText = [true];]      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                               |
|                                                                                                                                                                  |
| []                                                                                                                                       |
|                                                                                                                                                                  |
| [Me][.colorPickerButton1.SelectedAsBackcolor = [True]] |
|                                                                                                                                                                  |
| [Me][.colorPickerButton1.SelectedAsText = [True]]      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

[] 

Figure 307: AntiqueWhite Text and Background color for ColorPickerButton

[] 

See Also

[] 

[Color Groups,]{.UGHyperlink}[ ]{.UGHyperlink}[Tab Text]{.UGHyperlink}[, ]{.UGHyperlink}[ColorUIControl]{.UGHyperlink}[ ]{.UGHyperlink}[Appearance]{.UGHyperlink}[, ]{.UGHyperlink}[Runtime Settings]{.UGHyperlink}[ of ColorUIControl.]{.UGHyperlink}

[]{#related-topics}

