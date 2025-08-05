---
title: enhancednumericupdown.md
original_path: WinForms_Docs/99_Uncategorized/enhancednumericupdown.md
created_at: 2025-08-05
---






##### Enhanced Numeric Up Down {#enhanced-numeric-up-down style="tab-stops: 0pt"}

[] 

The Numeric Up Down cell type has been enhanced to provide more styles and properties that can be added to the numeric up down control by using the **FloatNumericUpDownStyleProperties** class. It enables you to set the limitations of the numeric values and several other properties.

[] 


  -------------------------------------- --------------------------------------------------------------------
  Float Numeric Up Down Style Property   Description
  BackColor                              Specifies the back color of the container.
  Maximum                                Indicates the maximum value that the cell can have.
  StartValue                             The starting value of the embedded cell.
  Step                                   The value that has to be incremented for each click of the button.
  WrapValue                              The bool value that will allow to wrap the text.
  DecimalPlaces                          The decimal values after the decimal point.
  Orientation                            Orientation of the cell container on NumericUpDown.
  InterceptArrowkeys                     Allows to change the value by using ARROW keys from keyboard.
  ThousandsSeparator                     The bool value which allows to separate the thousand basis.
  -------------------------------------- --------------------------------------------------------------------


[] 

The following code examples illustrate how to set the cell type to FNumericUpDown.

[] 

1.   Using C#

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                    |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                                   |
| [RegisterCellModel][.GridCellType([this].gridControl1, [CustomCellTypes].FNumericUpDown);]   |
|                                                                                                                                                                                                                                   |
| [GridStyleInfo][ style = [this].gridControl1\[1, 1\];]                                                               |
|                                                                                                                                                                                                                                   |
| [style.Text = [\"Allow Decimal Increment and Decrement(step by 0.2,0.01,0.001)\"];]                                                                                   |
|                                                                                                                                                                                                                                   |
| [style.TextColor = [Color].MidnightBlue;]                                                                                                                             |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                   |
| [// Set up FNumericUpDown Cell.]                                                                                                                                                |
|                                                                                                                                                                                                                                   |
| [style = gridControl1\[2, 2\];]                                                                                                                                                               |
|                                                                                                                                                                                                                                   |
| [style.CellType = [CustomCellTypes].FNumericUpDown.ToString();]                                                                                                       |
|                                                                                                                                                                                                                                   |
| [style.Text = [\"0.5\"];]                                                                                                                                             |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                   |
| [// Assign the Style Properties of Up Down Control.]                                                                                                                            |
|                                                                                                                                                                                                                                   |
| [FloatNumericUpDownStyleProperties][ sp = [new] [FloatNumericUpDownStyleProperties](style);] |
|                                                                                                                                                                                                                                   |
| [sp.StyleInfo.BackColor = [SystemColors].Window;]                                                                                                                     |
|                                                                                                                                                                                                                                   |
| [sp.FloatNumericUpDownProperties.Maximum = 15.0;]                                                                                                                                             |
|                                                                                                                                                                                                                                   |
| [sp.FloatNumericUpDownProperties.Minimum = 0.0;]                                                                                                                                              |
|                                                                                                                                                                                                                                   |
| [sp.FloatNumericUpDownProperties.StartValue = 0.5;]                                                                                                                                           |
|                                                                                                                                                                                                                                   |
| [sp.FloatNumericUpDownProperties.Step = 0.2;]                                                                                                                                                 |
|                                                                                                                                                                                                                                   |
| [sp.FloatNumericUpDownProperties.WrapValue = [true];]                                                                                                                    |
|                                                                                                                                                                                                                                   |
| [sp.FloatNumericUpDownProperties.DecimalPlaces = 1;]                                                                                                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                                   |
| [RegisterCellModel.GridCellType(gridControl1, CustomCellTypes.FNumericUpDown)]                                                                                                                |
|                                                                                                                                                                                                                                   |
| [Dim][ style [As] GridStyleInfo = [Me].gridControl1(1, 1)]                                         |
|                                                                                                                                                                                                                                   |
| [style.Text = [\"Allow Decimal Increment and Decrement(step by 0.2,0.01,0.001)\"]]                                                                                    |
|                                                                                                                                                                                                                                   |
| [style.TextColor = Color.MidnightBlue]                                                                                                                                                        |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                   |
| [\' Set up FNumericUpDown Cell.]                                                                                                                                                |
|                                                                                                                                                                                                                                   |
| [style = gridControl1(2, 2)]                                                                                                                                                                  |
|                                                                                                                                                                                                                                   |
| [style.CellType = CustomCellTypes.FNumericUpDown.ToString()]                                                                                                                                  |
|                                                                                                                                                                                                                                   |
| [style.Text = [\"0.5\"]]                                                                                                                                              |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                                   |
| [\' Assign the Style Properties of Up Down Control.]                                                                                                                            |
|                                                                                                                                                                                                                                   |
| [Dim][ sp [As] FloatNumericUpDownStyleProperties = [New] FloatNumericUpDownStyleProperties(style)] |
|                                                                                                                                                                                                                                   |
| [sp.StyleInfo.BackColor = SystemColors.Window]                                                                                                                                                |
|                                                                                                                                                                                                                                   |
| [sp.FloatNumericUpDownProperties.Maximum = 15.0]                                                                                                                                              |
|                                                                                                                                                                                                                                   |
| [sp.FloatNumericUpDownProperties.Minimum = 0.0]                                                                                                                                               |
|                                                                                                                                                                                                                                   |
| [sp.FloatNumericUpDownProperties.StartValue = 0.5]                                                                                                                                            |
|                                                                                                                                                                                                                                   |
| [sp.FloatNumericUpDownProperties.Step = 0.2]                                                                                                                                                  |
|                                                                                                                                                                                                                                   |
| [sp.FloatNumericUpDownProperties.WrapValue = [True]]                                                                                                                     |
|                                                                                                                                                                                                                                   |
| [sp.FloatNumericUpDownProperties.DecimalPlaces = 1]                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

*[Figure ][109][: Enhanced Numeric Up Down Cells]*

 

[]{#p98} 

 

[]{#related-topics}

