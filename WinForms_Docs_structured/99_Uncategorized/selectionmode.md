---
title: selectionmode.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\selectionmode.md
created_at: 2025-07-03
---






#### Selection Mode {#selection-mode style="tab-stops: 0pt"}

ColorPicker and ColorEdit controls can be displayed in two different modes. They are HSV and RGB modes. The **VisualizationStyle** property is used to switch between these modes.

 

To set the ColorSelection Mode as \"HSV\" for ColorEdit control, use the below code.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<!\--][ Adding ColorEdit ][\--\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][syncfusion:ColorEdit][  ][Margin][=][\"[20]\"[ ][VisualizationStyle][=]\"[HSV]\"[ ][Name][=]\"[colorEdit]\"[/\>]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                     |
|                                                                                                                                                    |
| []                                                                               |
|                                                                                                                                                    |
| [//Creating an instance of color edit]                                           |
|                                                                                                                                                    |
| [ColorEdit colorEdit = [new] ColorEdit();]                                |
|                                                                                                                                                    |
| []                                                                               |
|                                                                                                                                                    |
| [//Setting selection mode as HSV]                                                |
|                                                                                                                                                    |
| [colorEdit.VisualizationStyle = ColorSelectionMode.HSV;    ]                                   |
|                                                                                                                                                    |
| []                                                                               |
|                                                                                                                                                    |
| [//Adding control to the window]                                                 |
|                                                                                                                                                    |
| [this][.Content = colorEdit;] |
+----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 152: ColorEdit with Color Selection Mode set to \"HSV\"

**[]** 

To set the ColorSelection Mode as \"HSV\" for ColorPicker control, use the below code.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                       |
|                                                                                                                                                      |
| []                                                                                 |
|                                                                                                                                                      |
| [//Creating an instance of color picker]                                           |
|                                                                                                                                                      |
| [ColorPicker colorPicker = [new] ColorPicker();]                            |
|                                                                                                                                                      |
| []                                                                                 |
|                                                                                                                                                      |
| [//Setting selection mode as HSV]                                                  |
|                                                                                                                                                      |
| [colorPicker.VisualizationStyle = ColorSelectionMode.HSV;    ]                                   |
|                                                                                                                                                      |
| []                                                                                 |
|                                                                                                                                                      |
| [//Adding control to the window]                                                   |
|                                                                                                                                                      |
| [this][.Content = colorPicker;] |
+------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 153: ColorPicker with Color Selection Mode set to \"HSV\"

 

To set the ColorSelection Mode as \"RGB\" for ColorEdit control, use the below code.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                     |
|                                                                                                                                                    |
| []                                                                               |
|                                                                                                                                                    |
| [//Creating an instance of color edit]                                           |
|                                                                                                                                                    |
| [ColorEdit colorEdit = [new] ColorEdit();]                                |
|                                                                                                                                                    |
| []                                                                                             |
|                                                                                                                                                    |
| [//Setting selection mode as RGB]                                                |
|                                                                                                                                                    |
| [colorEdit.VisualizationStyle = ColorSelectionMode.RGB; ]                                      |
|                                                                                                                                                    |
| [   ]                                                                                          |
|                                                                                                                                                    |
| [//Adding control to the window]                                                 |
|                                                                                                                                                    |
| [this][.Content = colorEdit;] |
+----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 154: ColorEdit with Color Selection Mode set to \"RGB\"

**[]** 

To set the ColorSelection Mode as \"RGB\" for ColorPicker control, use the below code.

+------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                       |
|                                                                                                                                                      |
| []                                                                                 |
|                                                                                                                                                      |
| [//Creating an instance of color picker]                                           |
|                                                                                                                                                      |
| [ColorPicker colorPicker = [new] ColorPicker();]                            |
|                                                                                                                                                      |
| []                                                                                               |
|                                                                                                                                                      |
| [//Setting selection mode as RGB]                                                  |
|                                                                                                                                                      |
| [colorPicker.VisualizationStyle = ColorSelectionMode.RGB;]                                       |
|                                                                                                                                                      |
| [    ]                                                                                           |
|                                                                                                                                                      |
| [//Adding control to the window]                                                   |
|                                                                                                                                                      |
| [this][.Content = colorPicker;] |
+------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 155: ColorPicker with Color Selection Mode set to \"RGB\"

[]{#p83} 

[]{#related-topics}

