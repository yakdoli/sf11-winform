---
title: conceptsandfeatures135.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\conceptsandfeatures135.md
created_at: 2025-07-03
---






##### Concepts and Features[[]]{.MsoHyperlink} {#concepts-and-features style="tab-stops: 0pt"}

The following Editors controls (DoubleTextBox, IntegerTextBox, PercentTextBox, and CurrencyTextBox) have been revamped, click here to see the details of revamping.

###### 3.3.8.5.3.1 [[Display Settings]](http://help.syncfusion.com/ug_82/WindowsFormsUI_Tools/PercentSettings.html) {#display-settings style="tab-stops: 0pt"}

This section discusses the display settings of the PercentTextBox control.[]

[] 

The PercentTextBox provides a list of properties to set the display characteristics of the percentage.[]

[] 


  --------------------------------------------------- -------------------------------------------------------------------------------------------------------------
  PercentTextBox Properties[]   Description[]
  PercentDecimalDigits[]        Gets / sets the maximum number of digits for the decimal portion of the percentage.[]
  PercentDecimalSeparator[]     Gets / sets the decimal separator character that will be used for the display.[]
  PercentGroupSeparator[]       Gets / sets the separator to be used for grouping digits.[]
  PercentGroupSizes[]           Gets / sets the grouping of percent digits in the PercentTextBox.[]
  PercentNegativePattern[]      Gets / sets the pattern to use when the value is negative.[]
  NegativeSign[]                Gets / sets the sign that is to be used to indicate a negative value.[]
  PercentPositivePattern[]      Gets / sets the pattern to use when the value is positive.[]
  PercentSymbol[]               Gets / sets the percent symbol which represents the Percentage.[]
  --------------------------------------------------- -------------------------------------------------------------------------------------------------------------


[] 

The grouping size of the percent digits can be set using the **Int32 Collection Editor **which will be displayed on selecting the**PercentGroupSizes** property in the property grid.[]

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [this][.percentTextBox1.PercentDecimalDigits = 3;][]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [this][.percentTextBox1.PercentDecimalSeparator = ][\".\"][;][]                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [this][.percentTextBox1.PercentGroupSeparator = ][\",\"][;][]                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [this][.percentTextBox1.PercentGroupSizes = ][new][ ][int][\[\] {5};][] |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [this][.percentTextBox1.PercentNegativePattern = 2;][]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [this][.percentTextBox1.NegativeSign = ][\"-\"][;][]                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [this][.percentTextBox1.PercentPositivePattern = 2;][]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                        |
| [this][.percentTextBox1.PercentSymbol = ][\"%\"][;][]                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Me][.percentTextBox1.PercentDecimalDigits = 3][]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Me][.percentTextBox1.PercentDecimalSeparator = ][\".\"][]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Me][.percentTextBox1.PercentGroupSeparator = ][\",\"][]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Me][.percentTextBox1.PercentGroupSizes = ][New][ ][Integer][() {5}][] |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Me][.percentTextBox1.PercentNegativePattern = 2][]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Me][.percentTextBox1.NegativeSign = ][\"-\"][;][]                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Me][.percentTextBox1.PercentPositivePattern = 2][]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                       |
| [Me][.percentTextBox1.PercentSymbol = ][\"%\"][]                                                                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following screen shot illustrates the above settings.[]

[] 

{border="0"}

[] 

Figure 481: Display Settings of PercentTextBox[]

[] 

A sample which demonstrates the Display Settings of PercentTextBox control is available in the below sample installation path.[]

[] 

..My Documents\\Syncfusion\\EssentialStudio\\***Version Number***\\Windows\\Tools.Windows\\Samples\\2.0\\Editors Package\\EditorControls[]

 

###### 3.3.8.5.3.2 [[Value Settings]](http://help.syncfusion.com/ug_82/WindowsFormsUI_Tools/ValueSettings.html) {#value-settings style="tab-stops: 0pt"}

The various values of the PercentTextBox control and their settings are given below.[]

[] 


  --------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------
  PercentTextBox Properties[]   Description[]
  PercentValue[]                Specifies the double value of the PercentTextBox control.[]
  DefaultValue[]                Specifies the default value. The default value is set to \'Null\'.[]
  BindableValue[]               Wrapper property that indicates the value. This property can be used to set the value of the control to \'Null\'.[]
  BindablePercentValue[]        Wrapper property that indicates the percent value. This property can be used to set the value of the control to \'Null\'.[]
  DoubleValue[]                 Gets / sets the double value of the control. This will be formatted and displayed.[]
  --------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                        |
|                                                                                                                                                                               |
| []                                                                                                                                                      |
|                                                                                                                                                                               |
| [this][.percentTextBox1.PercentValue = 5;][]         |
|                                                                                                                                                                               |
| [this][.percentTextBox1.DefaultValue = 0;][]         |
|                                                                                                                                                                               |
| [this][.percentTextBox1.BindableValue = 0.05;][]     |
|                                                                                                                                                                               |
| [this][.percentTextBox1.BindablePercentValue = 5;][] |
|                                                                                                                                                                               |
| [this][.percentTextBox1.DoubleValue = 0.05;][]       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                 |
|                                                                                                                                                                            |
| []                                                                                                                                                   |
|                                                                                                                                                                            |
| [Me][.percentTextBox1.PercentValue = 5][]         |
|                                                                                                                                                                            |
| [Me][.percentTextBox1.DefaultValue = 0][]         |
|                                                                                                                                                                            |
| [Me][.percentTextBox1.BindableValue = 0.05][]     |
|                                                                                                                                                                            |
| [Me][.percentTextBox1.BindablePercentValue = 5][] |
|                                                                                                                                                                            |
| [Me][.percentTextBox1.DoubleValue = 0.05][]       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

 

Figure 482: Percent Value Set

[] 

Null Value Settings[]

[] 

There are various settings that can be applied to the PercentTextBox control, when the value of the control is set to \'Null\'. These settings are illustrated below.[]

[] 


  --------------------------------------------------- ---------------------------------------------------------------------------------------------
  PercentTextBox Properties[]   Description[]
  AllowNull[]                   Specifies if the NullString will be used when the value is Null.[]
  NullString[]                  Specifies the string to be displayed when the DecimalValue is Null.[]
  NullFormat[]                  Returns the NumberFormatInfo object for the null display.[]
  --------------------------------------------------- ---------------------------------------------------------------------------------------------


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                           |
| [this][.percentTextBox1.NullString = ][\"Null Value\"][;][] |
|                                                                                                                                                                                                                                                                                           |
| [this][.percentTextBox1.AllowNull = ][true][;][]              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                                          |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                     |
| [Me][.percentTextBox1.NullString = ][\"Null Value\"][] |
|                                                                                                                                                                                                                                     |
| [Me][.percentTextBox1.AllowNull = ][True][]               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 483: Null String Set

[] 

Min and Max Value Settings[]

[] 

The minimum and maximum values of the IntegerTextBox can be set using the below given properties.[]

[] 


  ------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------
  PercentTextBox Properties[]       Description[]
  MaxValue[]                        Gets / sets the maximum value that can be set through the PercentTextBox. The default value is set to \'1\'.[]
  MinValue[]                        Gets / sets the minimum value that can be set through the PercentTextBox. The default value is set to \'-1\'.[]
  EnforceMinMaxDuringValidating[]   If the min and max values are not met, the Validating event will be handled and cancelled if this property is set to \'True\'.[]
  ------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                  |
| [this][.percentTextBox1.MaxValue = 6;][]                                                                                                                                |
|                                                                                                                                                                                                                                                                                                  |
| [this][.percentTextBox1.MinValue = -6;][]                                                                                                                               |
|                                                                                                                                                                                                                                                                                                  |
| [this][.percentTextBox1.EnforceMinMaxDuringValidating = ][true][;][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                                                |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                           |
| [Me][.percentTextBox1.MaxValue = 6][]                                                                            |
|                                                                                                                                                                                                                                           |
| [Me][.percentTextBox1.MinValue = -6][]                                                                           |
|                                                                                                                                                                                                                                           |
| [Me][.percentTextBox1.EnforceMinMaxDuringValidating = ][True][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The methods associated with the above properties are given below.[]

[] 


  --------------------------------------- ------------------------------------------------------------------------------
  Methods[]         Description[]
  ResetMaxValue[]   Resets the MaxValue property to it\'s default value.[]
  ResetMinValue[]   Resets the MinValue property to it\'s default value.[]
  --------------------------------------- ------------------------------------------------------------------------------


 

###### 3.3.8.5.3.3 [[Culture Settings]](http://help.syncfusion.com/ug_82/WindowsFormsUI_Tools/CultureSettings1.html) {#culture-settings style="tab-stops: 0pt"}

This section discusses the Culture settings of the PercentTextBox control.[]

 


+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| PercentTextBox Properties         | Description                                                                                                                              |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Culture                           | Gets / sets the culture that is to be used for formatting the numeric display.                                                           |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| CurrentCultureRefresh             | Indicates whether the Culture property is to be refreshed when the culture changes.                                                      |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| SpecialCultureValue               | Gets / sets the mode for the cultures.                                                                                                   |
|                                   |                                                                                                                                          |
|                                   |                                                                                                                                          |
|                                   |                                                                                                                                          |
|                                   | It includes the below given options.                                                                                                     |
|                                   |                                                                                                                                          |
|                                   |                                                                                                                                          |
|                                   |                                                                                                                                          |
|                                   | *None,*                                                                                                                                  |
|                                   |                                                                                                                                          |
|                                   | *CurrentCulture,*                                                                                                                        |
|                                   |                                                                                                                                          |
|                                   | *UICulture and*                                                                                                                          |
|                                   |                                                                                                                                          |
|                                   | *InstalledCulture.*                                                                                                                      |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| UseUserOverride                   | Specifies if the NumberFormatInfo used for formatting will use the User Overrides for the culture. The default value is set to \'True\'. |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [this][.percentTextBox1.Culture = ][new][ System.Globalization.][CultureInfo][(][\"ar-JO\"][);][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [this][.percentTextBox1.CurrentCultureRefresh = ][true][;][]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [this][.percentTextBox1.SpecialCultureValue = Syncfusion.Windows.Forms.Tools.][SpecialCultureValues][.None;][]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [this][.percentTextBox1.UseUserOverride = ][true][;][]                                                                                                                                                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Me][.percentTextBox1.Culture = ][New][ System.Globalization.CultureInfo(][\"ar-JO\"][)][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Me][.percentTextBox1.CurrentCultureRefresh = ][True][]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Me][.percentTextBox1.SpecialCultureValue = Syncfusion.Windows.Forms.Tools.SpecialCultureValues.None][]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Me][.percentTextBox1.UseUserOverride = ][True][]                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

 

Figure 484: Culture Set for the PercentTextBox Control

[] 


[{border="0"}] Note: The RefreshCulture() method can be used to refresh and reapply the culture specific settings.[]


[] 

A sample which demonstrates the Culture Settings of the PercentTextBox control is available in the below sample installation path.[]

[] 

..My Documents\\Syncfusion\\EssentialStudio\\***Version Number***\\Windows\\Tools.Windows\\Samples\\2.0\\Editors Package\\EditorControls[]

 

###### 3.3.8.5.3.4 [[Text Settings]](http://help.syncfusion.com/ug_82/WindowsFormsUI_Tools/TextSettings11.html) {#text-settings style="tab-stops: 0pt"}

This section discusses the text settings of the PercentTextBox control.[]

[] 

The text associated with the PercentTextBox control can be set and customized using the below given settings.[]

[] 


+---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| PercentTextBox Properties[] | Description[]                                                                                        |
+---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| Text[]                      | Specifies the text associated with the control.[]                                                    |
+---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| CharacterCasing[]           | Gets / sets the case of character as they are typed.[]                                               |
|                                                   |                                                                                                                            |
|                                                   | []                                                                                                   |
|                                                   |                                                                                                                            |
|                                                   | It includes the below given options.[]                                                               |
|                                                   |                                                                                                                            |
|                                                   | []                                                                                                   |
|                                                   |                                                                                                                            |
|                                                   | *Normal,*[]                                                                                          |
|                                                   |                                                                                                                            |
|                                                   | *Upper and*[]                                                                                        |
|                                                   |                                                                                                                            |
|                                                   | *Lower.*[]                                                                                           |
+---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| TextAlign[]                 | Indicates how the text should be aligned for edit controls.[]                                        |
+---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| SelectedText[]              | Gets / sets the selected text in the PercentTextBox.[]                                               |
+---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| SelectAllOnFocus[]          | Specifies if the text should be selected when the control gets the focus.[]                          |
+---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| SwitchModeOnFocus[]         | Indicates whether the PercentTextBox should allow editing in numeric mode, when it receives focus.[] |
+---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| HideSelection[]             | Indicates that the selection should be hidden when the edit control loses focus.[]                   |
+---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| ClipText[]                  | Returns the clipped text without the formatting.[]                                                   |
+---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| DrawActiveWhenDisabled[]    | Specifies if the text should be drawn active, even when disabled.[]                                  |
+---------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                          |
| [this][.percentTextBox1.CharacterCasing = System.Windows.Forms.][CharacterCasing][.Upper;][] |
|                                                                                                                                                                                                                                                                                                                          |
| [this][.percentTextBox1.TextAlign = System.Windows.Forms.][HorizontalAlignment][.Center;][]  |
|                                                                                                                                                                                                                                                                                                                          |
| [this][.percentTextBox1.SelectedText = ][\"34\"][;][]                                      |
|                                                                                                                                                                                                                                                                                                                          |
| [this][.percentTextBox1.SelectAllOnFocus = ][true][;][]                                      |
|                                                                                                                                                                                                                                                                                                                          |
| [this][.percentTextBox1.SwitchModeOnFocus = ][true][;][]                                     |
|                                                                                                                                                                                                                                                                                                                          |
| [this][.percentTextBox1.HideSelection = ][true][;][]                                         |
|                                                                                                                                                                                                                                                                                                                          |
| [this][.percentTextBox1.ClipText = ][\"34\"][;][]                                          |
|                                                                                                                                                                                                                                                                                                                          |
| [this][.percentTextBox1.DrawActiveWhenDisabled = ][true][;][]                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                                         |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                    |
| [Me][.percentTextBox1.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper][]                     |
|                                                                                                                                                                                                                                    |
| [Me][.percentTextBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center][]                      |
|                                                                                                                                                                                                                                    |
| [Me][.percentTextBox1.SelectedText = ][\"34\"][]       |
|                                                                                                                                                                                                                                    |
| [Me][.percentTextBox1.SelectAllOnFocus = ][true][]       |
|                                                                                                                                                                                                                                    |
| [Me][.percentTextBox1.SwitchModeOnFocus = ][True][]      |
|                                                                                                                                                                                                                                    |
| [Me][.percentTextBox1.HideSelection = ][True][]          |
|                                                                                                                                                                                                                                    |
| [Me][.percentTextBox1.ClipText = ][\"34\"][]           |
|                                                                                                                                                                                                                                    |
| [Me][.percentTextBox1.DrawActiveWhenDisabled = ][True][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 485: Character Case set to \"Upper\"

[] 

{border="0"}

[] 

Figure 486: Text Aligned to the \"Center\"

[] 

{border="0"}

[] 

Figure 487: \"SelectAllOnFocus\" property Set

[] 

The methods associated with the above properties are given below.[]

[] 


  -------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------
  Methods[]                    Description[]
  AppendText[]                 Appends text to the current text of a textbox.[]
  ResetText[]                  Resets the Text property to its default value.[]
  OnCharacterCasingChanged[]   Raises the CharacterCasingChanged event.[]
  GetClipText[]                Gets / sets the clipped text without the formatting.[]
  Cut[]                        Cuts the selected data to the clipboard.[]
  Copy[]                       Copies the content of the NumberTextBox to the clipboard. The ClipMode property dictates what gets copied.[]
  Delete[]                     Deletes the current selection of the TextBox.[]
  Paste[]                      Pastes the data in the clipboard into the NumberTextBox control.[]
  SelectAll[]                  Selects all text in the TextBox.[]
  -------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------


[] 

Multiline Text Settings[]

[] 

The text settings of the PercentTextBox control can be customized to display multiline text using the below given properties.[]

[] 


+---------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| PercentTextBox Properties[] | Description[]                                                                              |
+---------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| Multiline[]                 | Controls whether the text of the edit control can span more than one line.[]               |
+---------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| Lines[]                     | The lines of text in a multiline edit, as an array of string values.[]                     |
+---------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| WordWrap[]                  | Indicates if lines are automatically word-wrapped for multiline edit controls.[]           |
+---------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ScrollBars[]                | Indicates, for multiline edit controls, which scrollbars will be shown for this control.[] |
|                                                   |                                                                                                                  |
|                                                   | []                                                                                         |
|                                                   |                                                                                                                  |
|                                                   | It includes the below given options.[]                                                     |
|                                                   |                                                                                                                  |
|                                                   | []                                                                                         |
|                                                   |                                                                                                                  |
|                                                   | *None,*[]                                                                                  |
|                                                   |                                                                                                                  |
|                                                   | *Horizontal,*[]                                                                            |
|                                                   |                                                                                                                  |
|                                                   | *Vertical and*[]                                                                           |
|                                                   |                                                                                                                  |
|                                                   | *Both.*[]                                                                                  |
+---------------------------------------------------+------------------------------------------------------------------------------------------------------------------+


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                   |
| [this][.percentTextBox1.Multiline = ][true][;][]                                      |
|                                                                                                                                                                                                                                                                                                                   |
| [this][.percentTextBox1.WordWrap = ][true][;][]                                       |
|                                                                                                                                                                                                                                                                                                                   |
| [this][.percentTextBox1.ScrollBars = System.Windows.Forms.][ScrollBars][.Vertical;][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                            |
|                                                                                                                                                                                                                       |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                       |
| [Me][.percentTextBox1.Multiline = ][True][] |
|                                                                                                                                                                                                                       |
| [Me][.percentTextBox1.WordWrap = ][True][]  |
|                                                                                                                                                                                                                       |
| [Me][.percentTextBox1.ScrollBars = System.Windows.Forms.ScrollBars.Vertical][]               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 488: Multiline Text

[] 

{border="0"}

[] 

Figure 489: WordWrap property Set

[] 

{border="0"}

 

Figure 490: ScrollBars set for PercentTextBox Control

[] 

Clip Mode[]

[] 

The formatting for the text can be enabled or disabled using the property given below.[]

[] 


+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| PercentTextBox Property[] | Description[]                                                                                                  |
+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| ClipMode[]                | Determines whether to include or exclude the literal characters in the input mask when doing a copy command.[] |
|                                                 |                                                                                                                                      |
|                                                 | []                                                                                                             |
|                                                 |                                                                                                                                      |
|                                                 | It includes the below given options.[]                                                                         |
|                                                 |                                                                                                                                      |
|                                                 | []                                                                                                             |
|                                                 |                                                                                                                                      |
|                                                 | *IncludeFormatting and*[]                                                                                      |
|                                                 |                                                                                                                                      |
|                                                 | *ExcludeFormatting.*[]                                                                                         |
+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                           |
| [this][.percentTextBox1.ClipMode = Syncfusion.Windows.Forms.Tools.][CurrencyClipModes][.IncludeFormatting;][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                                      |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                 |
| [Me][.percentTextBox1.ClipMode = Syncfusion.Windows.Forms.Tools.CurrencyClipModes.IncludeFormatting][] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Formatted Text[]

[] 

Formatted text can be displayed using the below given property.[]

[] 


  ------------------------------------------------- -------------------------------------------------------------------------
  PercentTextBox Property[]   Description[]
  FormattedText[]             Returns the formatted text with the formatting.[]
  ------------------------------------------------- -------------------------------------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                         |
| [this][.percentTextBox1.FormattedText = ][\"Hello\"][;][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                                       |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                  |
| [Me][.percentTextBox1.FormattedText = ][\"Hello\"][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

RightToLeft[]

[] 

The text can be displayed from right to left for RTL languages using this property.[]

[] 


  ------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------
  PercentTextBox Property[]   Description[]
  RightToLeft[]               Indicates whether the component should draw right-to-left for RTL languages. The default value is set to \'False\'.[]
  ------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------


[] 


[{border="0"}] Note:[ ]The RightToLeft property will be automatically set to \'True\' for RTL languages.[]


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                |
| [this][.percentTextBox1.RightToLeft = System.Windows.Forms.][RightToLeft][.Yes;][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                           |
|                                                                                                                                                                                                      |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                      |
| [Me][.percentTextBox1.RightToLeft = System.Windows.Forms.RightToLeft.Yes][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 491: Text displayed from Right To Left

[] 


[{border="0"}] Note:[ ]The ResetRightToLeft() method can be used to reset the RightToLeft property to it\'s default value.[]


[] 

OverflowIndicatorToolTipText[]

[] 

The tooltip that should be displayed when an overflow of text occurs can be set using the below given properties.[]

 


  ------------------------------------------------------ -----------------------------------------------------------------------------------
  [PercentTextBox Properties]    [Description]
  OverflowIndicatorToolTipText[]   Specifies the overflow indicator tooltip text.[]
  ShowOverflowIndicator[]          Gets / sets overflow indicator visibility.[]
  ShowOverflowIndicatorToolTip[]   Indicates whether to show the overflow indicator tooltip.[]
  ------------------------------------------------------ -----------------------------------------------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                           |
| [this][.percentTextBox1.OverflowIndicatorToolTipText = ][\"Overflow\"][;][] |
|                                                                                                                                                                                                                                                                                                           |
| [this][.percentTextBox1.ShowOverflowIndicator = ][true][;][]                  |
|                                                                                                                                                                                                                                                                                                           |
| [this][.percentTextBox1.ShowOverflowIndicatorToolTip = ][true][;][]           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                                                         |
|                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                    |
| [Me][.percentTextBox1.OverflowIndicatorToolTipText = ][\"Overflow\"][] |
|                                                                                                                                                                                                                                                    |
| [Me][.percentTextBox1.ShowOverflowIndicator = ][True][]                  |
|                                                                                                                                                                                                                                                    |
| [Me][.percentTextBox1.ShowOverflowIndicatorToolTip = ][True][]           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 492: Overflow Indicator ToolTip Text Set

[] 

Banner Text Support[]

[] 

The PercentTextBox control can display banner text in the text field, at run time. A [[BannerTextProvider Component][ ]](http://help.syncfusion.com/ug_82/WindowsFormsUI_Tools/BannerText.html)should be available for this purpose. Also, We need to set AllowNull, NullString and Text properties as below to make this feature effective.[]

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                              |
| [this][.percentTextBox1.AllowNull = ][true][;][] |
|                                                                                                                                                                                                                                                                              |
| [this][.percentTextBox1.NullString = \"\";][]                                                                                                       |
|                                                                                                                                                                                                                                                                              |
| [this][.percentTextBox1.Text = \"\";][]                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                            |
|                                                                                                                                                                                                                       |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                       |
| [Me][.percentTextBox1.AllowNull = ][True][] |
|                                                                                                                                                                                                                       |
| [Me][.percentTextBox1.NullString = \"\"][]                                                   |
|                                                                                                                                                                                                                       |
| [Me][.percentTextBox1.Text = \"\"][]                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

A sample which demonstrates the Text, Text Align and Overflow Indicator features of the PercentTextBox control is available in the below sample installation path.[]

[] 

..My Documents\\Syncfusion\\EssentialStudio\\***Version Number***\\Windows\\Tools.Windows\\Samples\\2.0\\Editors Package\\EditorControls[]

 

###### 3.3.8.5.3.5 [[Appearance Settings]](http://help.syncfusion.com/ug_82/WindowsFormsUI_Tools/AppearanceSettings22.html) {#appearance-settings style="tab-stops: 0pt"}

3.3.8.5.3.5.1      [[Background Settings]](http://help.syncfusion.com/ug_82/WindowsFormsUI_Tools/BackgroundSettings13.html)

The Background settings of the PercentTextBox control are discussed below.[]

[] 

Background Color[]

[] 

The background color of the control can be set using the properties given below.[]

[] 


  --------------------------------------------------- ------------------------------------------------------------------------------------------------------
  PercentTextBox Properties[]   Description[]
  BackColor[]                   Specifies the background color of the component.[]
  ReadOnlyBackColor[]           Specifies the backcolor to be used when the control is in the ReadOnly mode.[]
  --------------------------------------------------- ------------------------------------------------------------------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                           |
| [this][.percentTextBox1.BackColor = System.Drawing.][Color][.LightCyan;][]    |
|                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                           |
| [this][.percentTextBox1.ReadOnly = ][true][;][]                               |
|                                                                                                                                                                                                                                                                                                           |
| [this][.percentTextBox1.ReadOnlyBackColor = System.Drawing.][Color][.Pink;][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                               |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                          |
| [Me][.percentTextBox1.BackColor = System.Drawing.Color.LightCyan][]                             |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                          |
| [Me][.percentTextBox1.\[ReadOnly\] = ][True][] |
|                                                                                                                                                                                                                          |
| [Me][.percentTextBox1.ReadOnlyBackColor = System.Drawing.Color.Pink][]                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 493: PercentTextBox with Background Color Set[]

[] 

{border="0"}

[] 

Figure 494: \"ReadOnlyBackColor\" property Set

[] 


[{border="0"}] Note:[ ]The ReadOnly property must be set to \'True\' for the above setting to take effect.[]


[] 

The methods associated with the above properties are given below.[]

[] 


  ------------------------------------------------ ---------------------------------------------------------------------------------------
  Methods[]                  Description[]
  ResetBackColor[]           Resets the BackColor property to it\'s default value.[]
  ResetReadOnlyBackColor[]   Resets the ReadOnlyBackColor property to it\'s default value.[]
  ------------------------------------------------ ---------------------------------------------------------------------------------------


 

3.3.8.5.3.5.2      [[Foreground Settings]](http://help.syncfusion.com/ug_82/WindowsFormsUI_Tools/ForegroundSettings12.html)

The Foreground settings of the PercentTextBox control are discussed below.[]

[] 

Foreground Color[]

[] 

The foreground color of the control can be set using the properties given below.[]

[] 


  --------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------
  PercentTextBox Properties[]   Description[]
  PositiveColor[]               Gets / sets the forecolor when the current value is positive.[]
  NegativeColor[]               Gets / sets the forecolor when the current value is negative. The default value is set to \'Red\'.[]
  ZeroColor[]                   Gets / sets the forecolor when the current value is zero.[]
  --------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                              |
| [this][.percentTextBox1.PositiveColor = System.Drawing.][Color][.ForestGreen;][] |
|                                                                                                                                                                                                                                                                                                              |
| [this][.percentTextBox1.NegativeColor = System.Drawing.][Color][.Orange;][]      |
|                                                                                                                                                                                                                                                                                                              |
| [this][.percentTextBox1.ZeroColor = System.Drawing.][Color][.Orchid;][]          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                         |
|                                                                                                                                                                                                    |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                    |
| [Me][.percentTextBox1.PositiveColor = System.Drawing.Color.ForestGreen][] |
|                                                                                                                                                                                                    |
| [Me][.percentTextBox1.NegativeColor = System.Drawing.Color.Orange][]      |
|                                                                                                                                                                                                    |
| [Me][.percentTextBox1.ZeroColor = System.Drawing.Color.Orchid][]          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 495: Foreground Settings of PercentTextBox[]

[] 

The methods associated with the above properties are given below.[]

[] 


  ------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------
  Methods[]                        Description[]
  ResetForeColor[]                 Resets the forecolor of the control to it\'s default value.[]
  ResetPositiveColor[]             Resets the PositiveColor property to it\'s default value.[]
  ResetNegativeColor[]             Resets the NegativeColor property to it\'s default value.[]
  ResetZeroColor[]                 Resets the ZeroColor property to it\'s default value.[]
  SetControlColor[]                Sets the forecolor of the control depending on whether the current value is negative.[]
  ShouldSerializePositiveColor[]   Serializes the PositiveColor property.[]
  ShouldSerializeNegativeColor[]   Serializes the NegativeColor property.[]
  ShouldSerializeZeroColor[]       Serializes the ZeroColor property.[]
  ------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------


[] 

A sample which demonstrates the Foreground Settings of PercentTextBox control is available in the below sample installation path.[]

[] 

..My Documents\\Syncfusion\\EssentialStudio\\Version Number\\Windows\\Tools.Windows\\Samples\\2.0\\Editors Package\\EditorControls[]

 

###### 3.3.8.5.3.6 [[Behavior Settings]](http://help.syncfusion.com/ug_82/WindowsFormsUI_Tools/BehaviorSettings12.html) {#behavior-settings style="tab-stops: 0pt"}

The Behavior settings of the PercentTextBox control are discussed below.[]

[] 

NegativeInputPendingOnSelectAll[]

[] 

The percent value of the PercentTextBox can be changed to a negative value using the properties given below.[]

[] 


+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PercentTextBox Property[]         | Description[]                                                                                                                                                                                                                        |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| NegativeInputPendingOnSelectAll[] | This property defines the behavior when the contents of the IntegerTextBox is fully selected and the negative key is pressed by the user.[]                                                                                          |
|                                                         |                                                                                                                                                                                                                                                            |
|                                                         | []                                                                                                                                                                                                                                   |
|                                                         |                                                                                                                                                                                                                                                            |
|                                                         | When set to \'True\', the current value is not changed at all. The next key stroke is taken to be a new value and the entire contents of the PercentTextBox is replaced by the negative value of the key stroke character entered.[] |
|                                                         |                                                                                                                                                                                                                                                            |
|                                                         | []                                                                                                                                                                                                                                   |
|                                                         |                                                                                                                                                                                                                                                            |
|                                                         | When set to \'False\', the current value is changed to the negative value immediately.[]                                                                                                                                             |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                    |
| [this][.percentTextBox1.NegativeInputPendingOnSelectAll = ][true][;][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                                                  |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                             |
| [Me][.percentTextBox1.NegativeInputPendingOnSelectAll = ][True][] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

###### 3.3.8.5.3.7 [[Border Settings]](http://help.syncfusion.com/ug_82/WindowsFormsUI_Tools/BorderSettings13.html) {#border-settings style="tab-stops: 0pt"}

Color and Styles can be applied to the Border of the PercentTextBox control as discussed below.[]

[] 


+---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| PercentTextBox Properties[] | Description[]                                                                                    |
+---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| Border3DStyle[]             | Indicates the style of the 3D border. The options included are as follows:[]                     |
|                                                   |                                                                                                                        |
|                                                   | []                                                                                               |
|                                                   |                                                                                                                        |
|                                                   | *RaisedOuter,*[]                                                                                 |
|                                                   |                                                                                                                        |
|                                                   | *SunkenOuter,*[]                                                                                 |
|                                                   |                                                                                                                        |
|                                                   | *RaisedInner,*[]                                                                                 |
|                                                   |                                                                                                                        |
|                                                   | *SunkenInner,*[]                                                                                 |
|                                                   |                                                                                                                        |
|                                                   | *Raised,*[]                                                                                      |
|                                                   |                                                                                                                        |
|                                                   | *Etched,*[]                                                                                      |
|                                                   |                                                                                                                        |
|                                                   | *Bump,*[]                                                                                        |
|                                                   |                                                                                                                        |
|                                                   | *Sunken,*[]                                                                                      |
|                                                   |                                                                                                                        |
|                                                   | *Adjust and*[]                                                                                   |
|                                                   |                                                                                                                        |
|                                                   | *Flat.*[]                                                                                        |
|                                                   |                                                                                                                        |
|                                                   | []                                                                                               |
|                                                   |                                                                                                                        |
|                                                   | The default value is set to \'Sunken\'.[]                                                        |
+---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| BorderColor[]               | Specifies the color of the 2D border.[]                                                          |
+---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| BorderSides[]               | Indicates the border sides of the panel. The options included are as follows:[]                  |
|                                                   |                                                                                                                        |
|                                                   | []                                                                                               |
|                                                   |                                                                                                                        |
|                                                   | *Left,*[]                                                                                        |
|                                                   |                                                                                                                        |
|                                                   | *Top,*[]                                                                                         |
|                                                   |                                                                                                                        |
|                                                   | *Right,*[]                                                                                       |
|                                                   |                                                                                                                        |
|                                                   | *Bottom,*[]                                                                                      |
|                                                   |                                                                                                                        |
|                                                   | *Middle and*[]                                                                                   |
|                                                   |                                                                                                                        |
|                                                   | *All.*[]                                                                                         |
+---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| BorderStyle[]               | Indicates whether the edit control should have a border. The options included are given below.[] |
|                                                   |                                                                                                                        |
|                                                   | []                                                                                               |
|                                                   |                                                                                                                        |
|                                                   | *FixedSingle,*[]                                                                                 |
|                                                   |                                                                                                                        |
|                                                   | *Fixed3D and*[]                                                                                  |
|                                                   |                                                                                                                        |
|                                                   | *None.*[]                                                                                        |
+---------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                        |
| [this][.percentTextBox1.Border3DStyle = System.Windows.Forms.][Border3DStyle][.Etched;][]  |
|                                                                                                                                                                                                                                                                                                                        |
| [this][.percentTextBox1.BorderColor = System.Drawing.][Color][.Orange;][]                  |
|                                                                                                                                                                                                                                                                                                                        |
| [this][.percentTextBox1.BorderSides = System.Windows.Forms.][Border3DSide][.All;][]        |
|                                                                                                                                                                                                                                                                                                                        |
| [this][.percentTextBox1.BorderStyle = System.Windows.Forms.][BorderStyle][.FixedSingle;][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                   |
|                                                                                                                                                                                                              |
| []                                                                                                                                                                                     |
|                                                                                                                                                                                                              |
| [Me][.percentTextBox1.Border3DStyle = System.Windows.Forms.Border3DStyle.Etched][]  |
|                                                                                                                                                                                                              |
| [Me][.percentTextBox1.BorderColor = System.Drawing.Color.Orange][]                  |
|                                                                                                                                                                                                              |
| [Me][.percentTextBox1.BorderSides = System.Windows.Forms.Border3DSide.All][]        |
|                                                                                                                                                                                                              |
| [Me][.percentTextBox1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 496: PercentTextBox with Border Set

[] 

A Sample which demonstrates the Border Settings of PercentTextBox control is available in the below sample installation path.[]

[] 

..My Documents\\Syncfusion\\EssentialStudio\\***Version Number***\\Windows\\Tools.Windows\\Samples\\2.0\\Editors Package\\EditorControls[]

 

###### 3.3.8.5.3.8 [[Size Settings]](http://help.syncfusion.com/ug_82/WindowsFormsUI_Tools/SizeSettings.html) {#size-settings style="tab-stops: 0pt"}

The size of the PercentTextBox control can be set according to the needs of the user using the properties discussed below.[]

[] 


  --------------------------------------------------- -----------------------------------------------------------------------
  PercentTextBox Properties[]   Description[]
  MaximumSize[]                 Gets / sets the maximum size for the control.[]
  MinimumSize[]                 Gets / sets the minimum size for the control.[]
  --------------------------------------------------- -----------------------------------------------------------------------


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [this][.percentTextBox1.MaximumSize = ][new][ System.Drawing.][Size][(100, 25);][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [this][.percentTextBox1.MinimumSize = ][new][ System.Drawing.][Size][(100, 25);][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                         |
| [Me][.percentTextBox1.MaximumSize = ][New][ System.Drawing.Size(100, 25)][] |
|                                                                                                                                                                                                                                                                                                         |
| [Me][.percentTextBox1.MinimumSize = ][New][ System.Drawing.Size(100, 25)][] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 497: Size of the PercentTextBox control Set[]

 

###### 3.3.8.5.3.9 [[Key Settings]](http://help.syncfusion.com/ug_82/WindowsFormsUI_Tools/KeySettings1.html) {#key-settings style="tab-stops: 0pt"}

Sometimes there may occur some situations for entering large values, like in Mega, Kilo etc. In such situations if we add some sort of keyboard support, it will be very much useful for the users.[]

[] 

For example if the user wants to enter 32000, he just needs to enter 32 and then press the \'K\'. The value will change to 32000 automatically. This is illustrated in the code snippet given below.[]

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                           |
| [private void][ percentTextBox1_KeyDown(][object][ sender, KeyEventArgs e)][] |
|                                                                                                                                                                                                                                                                                                           |
| [{][]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                           |
| [double][ v = percentTextBox1.PercentValue;][]                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                           |
| [switch][(e.KeyCode)][]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                           |
| [{][]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                           |
| [// Enter the value as multiples of thousand.][]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                           |
| [case][ Keys.G : v = v \* 1000000000;][]                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                           |
| [break][;][]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                           |
| [case][ Keys.M : v = v \* 1000000;][]                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                           |
| [break][;][]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                           |
| [case][ Keys.K : v = v \* 1000;][]                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                           |
| [break][;][]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                           |
| [}][]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                           |
| [percentTextBox.PercentValue = v;][]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                           |
| [}][]                                                                                                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Private Sub][ percentTextBox1_KeyDown(][ByVal][ sender ][As Object][, ][ByVal][ e ][As][ KeyEventArgs)][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Dim][ v ][As Double][ = percentTextBox1.PercentValue][]                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Select][ e.KeyCode][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\' Enter the value as multiples of thousand.][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Case][ Keys.G][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [v = v \* 1000000000][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Case][ Keys.M][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [v = v \* 1000000][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Case][ Keys.K][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [v = v \* 1000][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [End Select][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [percentTextBox.PercentValue = v][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [End Sub][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

3.3.8.5.3.9.1      [[Shortcut Keys]](http://help.syncfusion.com/ug_82/WindowsFormsUI_Tools/ShortcutKeys1.html)

Sometimes there may occur some situations for incrementing or decrementing the value in the PercentTextBox. In such situations it is better to use shortcut keys.[]

[] 

The following implementation will illustrate how this can be achieved. Here we are using **Up** and **Down** keys for incrementing and decrementing respectively. We cannot use the \'-\' key because it is already reserved to enter the minus sign.[]

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                           |
| [private void][ percentTextBox1_KeyDown(][object][ sender, KeyEventArgs e)][] |
|                                                                                                                                                                                                                                                                                                           |
| [{][]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                           |
| [// Increments the PercentTextBoxValue.][]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                           |
| [double][ v = percentTextBox1.PercentValue;][]                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                           |
| [switch][(e.KeyCode)][]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                           |
| [{][]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                           |
| [case][ Keys.Up : v++;][]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                           |
| [break][;][//you can change by a step like v+=10;][]                                                                           |
|                                                                                                                                                                                                                                                                                                           |
| [case][ Keys.Down : v\--;][]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                           |
| [break][;][]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                           |
| [}][]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                           |
| [percentTextBox1.PercentValue = v;][]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                           |
| [}][]                                                                                                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Private Sub][ percentTextBox1_KeyDown(][ByVal][ sender ][As Object][, ][ByVal][ e ][As][ KeyEventArgs)][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\' Increments the PercentTextBoxValue.][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Dim][ v ][As Double][ = percentTextBox1.PercentValue][]                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Select][ e.KeyCode][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Case][ Keys.Up][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [v = v+1][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Case][ Keys.Down][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [v = v-1][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [End Select][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [percentTextBox1.PercentValue = v][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [End Sub][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

###### 3.3.8.5.3.10        [[Applying Themes]](http://help.syncfusion.com/ug_82/WindowsFormsUI_Tools/ApplyingThemes4.html) {#applying-themes style="tab-stops: 0pt"}

Themes can be applied to the PercentTextBox control using the property given below.[]

[] 


  ------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------
  PercentTextBox Property[]   Description[]
  ThemesEnabled[]             Specifies whether or not to use XP themes when BorderStyle  property is set to \'Fixed3D\'.[]
  ------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------


[] 


[{border="0"}][ ]Note: Refer [[Border Settings]{.UGHyperlink}](http://help.syncfusion.com/ug_82/WindowsFormsUI_Tools/BorderSettings13.html) topic to know about the BorderStyle property.


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                  |
| [this][.percentTextBox1.ThemesEnabled = ][true][;][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                                |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                           |
| [Me][.percentTextBox1.ThemesEnabled = ][true][] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 498: Themes Applied to PercentTextBox Control[]

[] 

A Sample which demonstrates the ThemesEnabled property of the PercentTextBox control is available in the below sample installation path.[]

[] 

..My Documents\\Syncfusion\\EssentialStudio\\***Version Number***\\Windows\\Tools.Windows\\Samples\\2.0\\Editors Package\\EditorControls[]

 

 

[]{#related-topics}

