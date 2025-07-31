---
title: conceptsandfeatures145.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\conceptsandfeatures145.md
created_at: 2025-07-03
---






##### [      ]Concepts and Features {#concepts-and-features style="tab-stops: 0pt"}

[] 

The following topics will help you become more familiar in using the CheckBoxAdv control.

[] 

###### []{#p770}[]{#_CheckBoxAdv_Settings}3.3.11.1.3.1        CheckBoxAdv Settings {#checkboxadv-settings style="tab-stops: 0pt"}

[] 

This section discusses the various states of the CheckBoxAdv control and the method of associating values with the states.

 

It includes the below given topics.

 

[]{#p771}[]{#_CheckBoxAdv_States}3.3.11.1.3.1.1     CheckBoxAdv States

[] 

The CheckBoxAdv can be displayed in three different states which have been described below.

[] 


+-----------------------------------+------------------------------------------------+
| CheckBoxAdv Property              | Description                                    |
+-----------------------------------+------------------------------------------------+
| CheckState                        | Gets / sets the check state of the CheckBox.   |
|                                   |                                                |
|                                   |                                                |
|                                   |                                                |
|                                   | It includes the below given options.           |
|                                   |                                                |
|                                   |                                                |
|                                   |                                                |
|                                   | *Unchecked,*                                   |
|                                   |                                                |
|                                   | *Checked and*                                  |
|                                   |                                                |
|                                   | *Indeterminate.*                               |
+-----------------------------------+------------------------------------------------+
| Checked                           | Gets / sets the checked state of the CheckBox. |
+-----------------------------------+------------------------------------------------+


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                             |
|                                                                                                                                                                                            |
| []                                                                                                                                       |
|                                                                                                                                                                                            |
| [this][.checkBoxAdv1.CheckState = System.Windows.Forms.[CheckState].Checked;] |
|                                                                                                                                                                                            |
| [this][.checkBoxAdv1.Checked = [true];]                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                            |
|                                                                                                                                                               |
| []                                                                                                          |
|                                                                                                                                                               |
| [Me][.checkBoxAdv1.CheckState = System.Windows.Forms.CheckState.Checked] |
|                                                                                                                                                               |
| [Me][.checkBoxAdv1.Checked = [True]]                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 611: CheckBoxAdv States

**[]** 

{border="0"}

[] 

Figure 612: \"Checked\" property displaying the Checked States

[] 

See Also

[] 

[CheckBoxAdv Values]{.UGHyperlink}[, ]{.UGHyperlink}[Image Settings]{.UGHyperlink}[]{.UGHyperlink}

[]{#_CheckBoxAdv_Values}3.3.11.1.3.1.2     CheckBoxAdv Values

[]{#p772} 

This section discusses how values can be associated with the various check states.

 

Both integer and string values can be associated with the check states as follows.

[] 


  ------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------
  CheckBoxAdv Properties   Description
  CheckedInt               Specifies the integer value when checked.
  CheckedString            Specifies the string value when checked.
  IndeterminateInt         Specifies the integer value when indeterminate.
  IndeterminateString      Specifies the string value when indeterminate.
  UncheckedInt             Specifies the integer value when Unchecked.
  UncheckedString          Specifies the string value when Unchecked.
  StringValue              Gets or sets the string value.
  BoolValue                Gets / sets a value indicating the check state. This property can be set to use bool values for databinding. Refer Frequently Asked Questions section.
  IntValue                 Gets / sets the int value. Refer Frequently Asked Questions section.
  ------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                               |
|                                                                                                                                                                                              |
| []                                                                                                                                         |
|                                                                                                                                                                                              |
| [this][.checkBoxAdv1.CheckedInt = 3;]                                                                   |
|                                                                                                                                                                                              |
| [this][.checkBoxAdv1.CheckedString = [\"CheckBoxAdv is Checked\"];]             |
|                                                                                                                                                                                              |
| [this][.checkBoxAdv1.IndeterminateInt = 5;]                                                             |
|                                                                                                                                                                                              |
| [this][.checkBoxAdv1.IndeterminateString = [\"CheckBoxAdv is Indeterminate\"];] |
|                                                                                                                                                                                              |
| [this][.checkBoxAdv1.UncheckedInt = 3;]                                                                 |
|                                                                                                                                                                                              |
| [this][.checkBoxAdv1.UncheckedString = [\"CheckBoxAdv is Unchecked\"];]         |
|                                                                                                                                                                                              |
| [this][.checkBoxAdv1.StringValue = [\"String\"];]                               |
|                                                                                                                                                                                              |
| [this][.checkBoxAdv1.IntValue = 5;]                                                                     |
|                                                                                                                                                                                              |
| [this][.checkBoxAdv1.BoolValue = [true];]                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                        |
|                                                                                                                                                                                           |
| []                                                                                                                                      |
|                                                                                                                                                                                           |
| [Me][.checkBoxAdv1.CheckedInt = 3]                                                                   |
|                                                                                                                                                                                           |
| [Me][.checkBoxAdv1.CheckedString = [\"CheckBoxAdv is Checked\"]]             |
|                                                                                                                                                                                           |
| [Me][.checkBoxAdv1.IndeterminateInt = 5]                                                             |
|                                                                                                                                                                                           |
| [Me][.checkBoxAdv1.IndeterminateString = [\"CheckBoxAdv is Indeterminate\"]] |
|                                                                                                                                                                                           |
| [Me][.checkBoxAdv1.UncheckedInt = 3]                                                                 |
|                                                                                                                                                                                           |
| [Me][.checkBoxAdv1.UncheckedString = [\"CheckBoxAdv is Unchecked\"]]         |
|                                                                                                                                                                                           |
| [Me][.checkBoxAdv1.StringValue = [\"String\"]]                               |
|                                                                                                                                                                                           |
| [Me][.checkBoxAdv1.IntValue = 5]                                                                     |
|                                                                                                                                                                                           |
| [Me][.checkBoxAdv1.BoolValue = [True]]                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

See Also

[] 

[CheckBoxAdv States]{.UGHyperlink}[, ]{.UGHyperlink}[Image Settings]{.UGHyperlink}[]{.UGHyperlink}

###### []{#p773}3.3.11.1.3.2        Text Settings {#text-settings style="tab-stops: 0pt"}

[] 

This section discusses the text settings of the CheckBoxAdv.

 

Text in the CheckBoxAdv can be shadowed and wrapped as illustrated below.

 


  ------------------------ -------------------------------------------------------
  CheckBoxAdv Properties   Description
  TextShadow               Determines if the text shadow is visible.
  ShadowColor              The color of the text shadow.
  ShadowOffset             The offset of the text shadow.
  WrapText                 Determines if the text in the CheckBoxAdv is wrapped.
  ------------------------ -------------------------------------------------------


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                             |
|                                                                                                                                                                                                            |
| []                                                                                                                                                       |
|                                                                                                                                                                                                            |
| [this][.checkBoxAdv1.TextShadow = [true];]                                                       |
|                                                                                                                                                                                                            |
| [this][.checkBoxAdv1.ShadowColor = System.Drawing.[Color].BurlyWood;]                         |
|                                                                                                                                                                                                            |
| [this][.checkBoxAdv1.ShadowOffset = [new] System.Drawing.[Point](8, 8);] |
|                                                                                                                                                                                                            |
| [this][.checkBoxAdv1.WrapText = [true];]                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                            |
|                                                                                                                                                                               |
| []                                                                                                                          |
|                                                                                                                                                                               |
| [Me][.checkBoxAdv1.TextShadow = [True]]                             |
|                                                                                                                                                                               |
| [Me][.checkBoxAdv1.ShadowColor = System.Drawing.Color.BurlyWood]                         |
|                                                                                                                                                                               |
| [Me][.checkBoxAdv1.ShadowOffset = [New] System.Drawing.Point(8, 8)] |
|                                                                                                                                                                               |
| [Me][.checkBoxAdv1.WrapText = [True]]                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

 

Figure 613: Text Shadow Settings

**[]** 

{border="0"}

[] 

Figure 614: WrapText property Set

[] 

A sample which demonstrates the TextShadow property of CheckBoxAdv is available in the below sample installation path.

 

..My Documents\\Syncfusion\\EssentialStudio***\\Version Number***\\Windows\\Tools.Windows\\Samples\\2.0\\Editors Package\\OptionControls

[] 

See Also

[] 

[Alignment Settings]{.UGHyperlink}[]{.UGHyperlink}

###### []{#p774}3.3.11.1.3.3        Appearance and Behavior Settings {#appearance-and-behavior-settings style="tab-stops: 0pt"}

[] 

This section discusses the appearance and behavior settings of the CheckBoxAdv control.

[] 

Appearance Settings

[] 

DrawFocusRectangle

[] 

The focus rectangle can be hidden or made visible using the below given property.

[] 


  ---------------------- ------------------------------------------------------------------------------------------------------------
  CheckBoxAdv Property   Description
  DrawFocusRectangle     Determines if the focus rectangle is visible when it gets the focus. The default value is set to \'True\'.
  ---------------------- ------------------------------------------------------------------------------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                               |
|                                                                                                                                                              |
| []                                                                                                         |
|                                                                                                                                                              |
| [this][.checkBoxAdv1.DrawFocusRectangle = [true];] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                        |
|                                                                                                                                                           |
| []                                                                                                      |
|                                                                                                                                                           |
| [Me][.checkBoxAdv1.DrawFocusRectangle = [True]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Behavior Settings

[] 

The behavior settings of the CheckBoxAdv can be customized using the properties given below.

[] 


  ------------------------ -----------------------------------------------------------------------------
  CheckBoxAdv Properties   Description
  AutoHeight               Determines if the CheckBoxAdv will automatically calculate its height.
  ReadOnlyMode             Specifies the Read Only Mode of the CheckBoxAdv.
  Tristate                 Specifies whether the indeterminate state can be accessed through clicking.
  ------------------------ -----------------------------------------------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                         |
|                                                                                                                                                        |
| []                                                                                                   |
|                                                                                                                                                        |
| [this][.checkBoxAdv1.AutoHeight = [true];]   |
|                                                                                                                                                        |
| [this][.checkBoxAdv1.ReadOnlyMode = [true];] |
|                                                                                                                                                        |
| [this][.checkBoxAdv1.Tristate= [false];]     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                  |
|                                                                                                                                                     |
| []                                                                                                |
|                                                                                                                                                     |
| [Me][.checkBoxAdv1.AutoHeight = [True]]   |
|                                                                                                                                                     |
| [Me][.checkBoxAdv1.ReadOnlyMode = [True]] |
|                                                                                                                                                     |
| [Me][.checkBoxAdv1.Tristate= [False]]     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

A sample which demonstrates the ReadOnlyMode and Tristate properties of CheckBoxAdv is available in the below sample installation path.

 

..My Documents\\Syncfusion\\EssentialStudio\\***Version Number***\\Windows\\Tools.Windows\\Samples\\2.0\\Editors Package\\OptionControls

###### []{#_Alignment_Settings_1}3.3.11.1.3.4        Alignment Settings[]{#p775} {#alignment-settings style="tab-stops: 0pt"}

[] 

This section discusses the alignment settings of the CheckBoxAdv.

[] 

Text Alignment

[] 

Text in the CheckBoxAdv can be aligned to the desired location as given below.

[] 


+-----------------------------------+-------------------------------------------------------------------------------------------------------------------+
| CheckBoxAdv Properties            | Description                                                                                                       |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------+
| TextContentAlignment              | Indicates the alignment of the text. The default value is set to \'MiddleLeft\'.                                  |
|                                   |                                                                                                                   |
|                                   |                                                                                                                   |
|                                   |                                                                                                                   |
|                                   | The options included are as follows.                                                                              |
|                                   |                                                                                                                   |
|                                   |                                                                                                                   |
|                                   |                                                                                                                   |
|                                   | *TopLeft,*                                                                                                        |
|                                   |                                                                                                                   |
|                                   | *TopCenter,*                                                                                                      |
|                                   |                                                                                                                   |
|                                   | *TopRight,*                                                                                                       |
|                                   |                                                                                                                   |
|                                   | *MiddleLeft,*                                                                                                     |
|                                   |                                                                                                                   |
|                                   | *MiddleCenter,*                                                                                                   |
|                                   |                                                                                                                   |
|                                   | *MiddleRight,*                                                                                                    |
|                                   |                                                                                                                   |
|                                   | *BottomLeft,*                                                                                                     |
|                                   |                                                                                                                   |
|                                   | *BottomCenter and*                                                                                                |
|                                   |                                                                                                                   |
|                                   | *BottomRight.*                                                                                                    |
|                                   |                                                                                                                   |
|                                   |                                                                                                                   |
|                                   |                                                                                                                   |
|                                   | WrapText property must be set to \'False\'. Refer[ [Text Settings]] |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------+


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                            |
|                                                                                                                                                                                                           |
| []                                                                                                                                                      |
|                                                                                                                                                                                                           |
| [this][.checkBoxAdv1.TextContentAlignment = System.Drawing.[ContentAlignment].MiddleCenter;] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                           |
|                                                                                                                                                                              |
| []                                                                                                                         |
|                                                                                                                                                                              |
| [Me][.checkBoxAdv1.TextContentAlignment = System.Drawing.ContentAlignment.MiddleCenter] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

[] 

Figure 615: Text aligned to \"MiddleCenter\"

[] 

CheckBox Alignment

[] 

The CheckBox itself can be aligned to any desired location that can be chosen from the options given in the following property.

[] 


+-----------------------------------+--------------------------------------------------------------------------------------+
| CheckBoxAdv Properties            | Description                                                                          |
+-----------------------------------+--------------------------------------------------------------------------------------+
| CheckAlign                        | Indicates the alignment of the CheckBox. The default value is set to \'MiddleLeft\'. |
|                                   |                                                                                      |
|                                   |                                                                                      |
|                                   |                                                                                      |
|                                   | The options included are as follows.                                                 |
|                                   |                                                                                      |
|                                   |                                                                                      |
|                                   |                                                                                      |
|                                   | *TopLeft,*                                                                           |
|                                   |                                                                                      |
|                                   | *TopCenter,*                                                                         |
|                                   |                                                                                      |
|                                   | *TopRight,*                                                                          |
|                                   |                                                                                      |
|                                   | *MiddleLeft,*                                                                        |
|                                   |                                                                                      |
|                                   | *MiddleCenter,*                                                                      |
|                                   |                                                                                      |
|                                   | *MiddleRight,*                                                                       |
|                                   |                                                                                      |
|                                   | *BottomLeft,*                                                                        |
|                                   |                                                                                      |
|                                   | *BottomCenter and*                                                                   |
|                                   |                                                                                      |
|                                   | *BottomRight.*                                                                       |
+-----------------------------------+--------------------------------------------------------------------------------------+


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| []                                                                                                                                           |
|                                                                                                                                                                                                |
| [this][.checkBoxAdv1.CheckAlign = System.Drawing.[ContentAlignment].MiddleRight;] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                |
|                                                                                                                                                                   |
| []                                                                                                              |
|                                                                                                                                                                   |
| [Me][.checkBoxAdv1.CheckAlign = System.Drawing.ContentAlignment.MiddleRight] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 616: CheckBox aligned to \"MiddleRight\"

[] 

A sample which demonstrates the Text and CheckBox Alignment features of CheckBoxAdv is available in the below sample installation path.

 

..My Documents\\Syncfusion\\EssentialStudio\\***Version Number***\\Windows\\Tools.Windows\\Samples\\2.0\\Editors Package\\OptionControls

[] 

See Also

[] 

[Text Settings]{.UGHyperlink}[, ]{.UGHyperlink}[[CheckBoxAdv Settings]{.UGHyperlink}]()[]{.UGHyperlink}

###### []{#_Background_Settings_5}3.3.11.1.3.5        Background Settings {#background-settings style="tab-stops: 0pt"}

[]{#p776} 

The background settings of the CheckBoxAdv are discussed below.

 

The CheckBoxAdv can be provided with a gradient background using the properties given below.

[] 


+-----------------------------------+----------------------------------------------------------------------------+
| CheckBoxAdv Properties            | Description                                                                |
+-----------------------------------+----------------------------------------------------------------------------+
| BackgroundStyle                   | Sets the background style of the CheckBoxAdv.                              |
|                                   |                                                                            |
|                                   |                                                                            |
|                                   |                                                                            |
|                                   | The options included are as follows.                                       |
|                                   |                                                                            |
|                                   |                                                                            |
|                                   |                                                                            |
|                                   | *HorizontalGradient,*                                                      |
|                                   |                                                                            |
|                                   | *VerticalGradient and*                                                     |
|                                   |                                                                            |
|                                   | *Default.*                                                                 |
+-----------------------------------+----------------------------------------------------------------------------+
| GradientStart                     | Sets the start color of the gradient of the background of the CheckboxAdv. |
+-----------------------------------+----------------------------------------------------------------------------+
| GradientEnd                       | Sets the end color of the gradient of the background of the CheckboxAdv.   |
+-----------------------------------+----------------------------------------------------------------------------+


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                       |
|                                                                                                                                                                                                      |
| []                                                                                                                                                 |
|                                                                                                                                                                                                      |
| [this][.checkBoxAdv1.BackgroundStyle = Syncfusion.Windows.Forms.Tools.CheckBoxAdvBackStyle.HorizontalGradient;] |
|                                                                                                                                                                                                      |
| [this][.checkBoxAdv1.GradientStart = System.Drawing.Color.Aqua;]                                                |
|                                                                                                                                                                                                      |
| [this][.checkBoxAdv1.GradientEnd = System.Drawing.Color.Magenta;]                                               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                |
|                                                                                                                                                                                                   |
| []                                                                                                                                              |
|                                                                                                                                                                                                   |
| [Me][.checkBoxAdv1.BackgroundStyle = Syncfusion.Windows.Forms.Tools.CheckBoxAdvBackStyle.HorizontalGradient] |
|                                                                                                                                                                                                   |
| [Me][.checkBoxAdv1.GradientStart = System.Drawing.Color.Aqua]                                                |
|                                                                                                                                                                                                   |
| [Me][.checkBoxAdv1.GradientEnd = System.Drawing.Color.Magenta]                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 617: Gradient Background Displayed

[] 


{border="0"} Note: Gradient background cannot be applied to the CheckBoxAdv when its BackgroundStyle property is set to \'Default\'. Also, the background image cannot be displayed with gradient settings.


[] 

A sample which demonstrates the Background Settings of CheckBoxAdv is available in the below sample installation path.

[] 

..My Documents\\Syncfusion\\EssentialStudio\\***Version Number***\\Windows\\Tools.Windows\\Samples\\2.0\\Editors Package\\OptionControls

###### []{#p777}3.3.11.1.3.6        Border Settings {#border-settings style="tab-stops: 0pt"}

[] 

Color and Styles can be applied to the border of the CheckBoxAdv as discussed below.

[] 


+-----------------------------------+-----------------------------------------------------------------------------------------+
| CheckBoxAdv Properties            | Description                                                                             |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| Border3DStyle                     | Indicates the style of the 3D border. The options included are as follows.              |
|                                   |                                                                                         |
|                                   |                                                                                         |
|                                   |                                                                                         |
|                                   | *RaisedOuter,*                                                                          |
|                                   |                                                                                         |
|                                   | *SunkenOuter,*                                                                          |
|                                   |                                                                                         |
|                                   | *RaisedInner,*                                                                          |
|                                   |                                                                                         |
|                                   | *SunkenInner,*                                                                          |
|                                   |                                                                                         |
|                                   | *Raised,*                                                                               |
|                                   |                                                                                         |
|                                   | *Etched,*                                                                               |
|                                   |                                                                                         |
|                                   | *Bump,*                                                                                 |
|                                   |                                                                                         |
|                                   | *Sunken,*                                                                               |
|                                   |                                                                                         |
|                                   | *Adjust and*                                                                            |
|                                   |                                                                                         |
|                                   | *Flat*.                                                                                 |
|                                   |                                                                                         |
|                                   |                                                                                         |
|                                   |                                                                                         |
|                                   | The default value is set to \'Sunken\'.                                                 |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| BorderColor                       | Specifies the color of the 2D border.                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| BorderSingle                      | Indicates the 2D border style. The options included are as follows.                     |
|                                   |                                                                                         |
|                                   |                                                                                         |
|                                   |                                                                                         |
|                                   | *Dotted,*                                                                               |
|                                   |                                                                                         |
|                                   | *Dashed,*                                                                               |
|                                   |                                                                                         |
|                                   | *Solid,*                                                                                |
|                                   |                                                                                         |
|                                   | *Inset,*                                                                                |
|                                   |                                                                                         |
|                                   | *Outset and*                                                                            |
|                                   |                                                                                         |
|                                   | *None.*                                                                                 |
|                                   |                                                                                         |
|                                   |                                                                                         |
|                                   |                                                                                         |
|                                   | The BorderStyle property should be set to \'FixedSingle\'.                              |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| BorderStyle                       | Indicates whether the panel should have a border. The options included are given below. |
|                                   |                                                                                         |
|                                   |                                                                                         |
|                                   |                                                                                         |
|                                   | *FixedSingle,*                                                                          |
|                                   |                                                                                         |
|                                   | *Fixed3D and*                                                                           |
|                                   |                                                                                         |
|                                   | *None.*                                                                                 |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| HotBorderColor                    | Specifies the color of the FixedSingle border when MouseOver.                           |
+-----------------------------------+-----------------------------------------------------------------------------------------+


 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                     |
|                                                                                                                                                                                                    |
| []                                                                                                                                               |
|                                                                                                                                                                                                    |
| [this][.checkBoxAdv1.Border3DStyle = System.Windows.Forms.[Border3DStyle].Bump;]      |
|                                                                                                                                                                                                    |
| [this][.checkBoxAdv1.BorderColor = System.Drawing.[Color].Red;]                       |
|                                                                                                                                                                                                    |
| [this][.checkBoxAdv1.BorderSingle = System.Windows.Forms.[ButtonBorderStyle].Dotted;] |
|                                                                                                                                                                                                    |
| [this][.checkBoxAdv1.BorderStyle = System.Windows.Forms.[BorderStyle].FixedSingle;]   |
|                                                                                                                                                                                                    |
| []                                                                                                                                                             |
|                                                                                                                                                                                                    |
| [// BorderStyle must be set to \'FixedSingle\'.]                                                                                                 |
|                                                                                                                                                                                                    |
| [this][.checkBoxAdv1.HotBorderColor = System.Drawing.[Color].Blue;]                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                    |
|                                                                                                                                                                       |
| []                                                                                                                  |
|                                                                                                                                                                       |
| [Me][.checkBoxAdv1.Border3DStyle = System.Windows.Forms.Border3DStyle.Bump]      |
|                                                                                                                                                                       |
| [Me][.checkBoxAdv1.BorderColor = System.Drawing.Color.Red]                       |
|                                                                                                                                                                       |
| [Me][.checkBoxAdv1.BorderSingle = System.Windows.Forms.ButtonBorderStyle.Dotted] |
|                                                                                                                                                                       |
| [Me][.checkBoxAdv1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle]   |
|                                                                                                                                                                       |
| []                                                                                                                                |
|                                                                                                                                                                       |
| [\' BorderStyle must be set to \'FixedSingle\'.]                                                                    |
|                                                                                                                                                                       |
| [Me][.checkBoxAdv1.HotBorderColor = System.Drawing.Color.Blue]                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 618: Border Set for CheckBoxAdv

[] 

{border="0"}

[] 

Figure 619: \"HotBorderColor\" property Set

**[]** 

A Sample which demonstrates the Border Settings of CheckBoxAdv is available in the below sample installation path.

 

..My Documents\\Syncfusion\\EssentialStudio\\***Version Number***\\Windows\\Tools.Windows\\Samples\\2.0\\Editors Package\\OptionControls

###### []{#_Image_Settings_3}3.3.11.1.3.7        Image Settings {#image-settings style="tab-stops: 0pt"}

[]{#p778}[] 

The image settings of the CheckBoxAdv control has been discussed in this section.

 

Images can be set to the CheckBoxAdv when it is in the Checked, Unchecked or Indeterminate state. The CheckBoxAdv allows us to set the following properties in order to display images.

 


+-----------------------------------+------------------------------------------------------------------------------------+
| CheckBoxAdv Properties            | Description                                                                        |
+-----------------------------------+------------------------------------------------------------------------------------+
| ImageCheckBox                     | Indicates whether the CheckBox will be drawn using the images provided.            |
+-----------------------------------+------------------------------------------------------------------------------------+
| ImageCheckBoxSize                 | Gets / sets the size of the ImageCheckBox.                                         |
|                                   |                                                                                    |
|                                   |                                                                                    |
|                                   |                                                                                    |
|                                   | ImageCheckbox property must be set to \'True\'.                                    |
+-----------------------------------+------------------------------------------------------------------------------------+
| CheckedImage                      | Gets / sets the image used to draw the CheckBox when checked and mouse not over.   |
+-----------------------------------+------------------------------------------------------------------------------------+
| UncheckedImage                    | Gets / sets the image used to draw the CheckBox when unchecked and mouse not over. |
+-----------------------------------+------------------------------------------------------------------------------------+
| IndeterminateImage                | The image used to draw the CheckBox when indeterminate and mouse not over.         |
|                                   |                                                                                    |
|                                   |                                                                                    |
+-----------------------------------+------------------------------------------------------------------------------------+
| DisabledImage                     | Gets / sets the image used to draw the CheckBox when disabled.                     |
+-----------------------------------+------------------------------------------------------------------------------------+
| StretchImage                      | Indicates whether the state images of the CheckBox are stretched.                  |
+-----------------------------------+------------------------------------------------------------------------------------+


[] 


{border="0"} Note: Before setting the images, make sure the ImageCheckBox property is set to \'True\'.


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                         |
| [this][.checkBoxAdv1.ImageCheckBox = [true];]                                                                                                                 |
|                                                                                                                                                                                                                                                                         |
| [this][.checkBoxAdv1.ImageCheckBoxSize = [new] System.Drawing.[Size](15, 15);]                                                        |
|                                                                                                                                                                                                                                                                         |
| [this][.checkBoxAdv1.CheckedImage = ((System.Drawing.[Image])(resources.GetObject([\"checkBoxAdv1.CheckedImage\"])));]             |
|                                                                                                                                                                                                                                                                         |
| [this][.checkBoxAdv1.UncheckedImage = ((System.Drawing.[Image])(resources.GetObject([\"checkBoxAdv1.UncheckedImage\"])));]         |
|                                                                                                                                                                                                                                                                         |
| [this][.checkBoxAdv1.IndeterminateImage = ((System.Drawing.[Image])(resources.GetObject([\"checkBoxAdv1.IndeterminateImage\"])));] |
|                                                                                                                                                                                                                                                                         |
| [this][.checkBoxAdv1.DisabledImage = ((System.Drawing.[Image])(resources.GetObject([\"checkBoxAdv1.DisabledImage\"])));]           |
|                                                                                                                                                                                                                                                                         |
| [this][.checkBoxAdv1.StretchImage = [false];]                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                        |
| [Me][.checkBoxAdv1.ImageCheckBox = [True]]                                                                                                                   |
|                                                                                                                                                                                                                                                                        |
| [Me][.checkBoxAdv1.ImageCheckBoxSize = [New] System.Drawing.Size(15, 15)]                                                                                    |
|                                                                                                                                                                                                                                                                        |
| [Me][.checkBoxAdv1.CheckedImage = ([CType](Resources.GetObject([\"checkBoxAdv1.CheckedImage\"]), System.Drawing.Image))]             |
|                                                                                                                                                                                                                                                                        |
| [Me][.checkBoxAdv1.UncheckedImage = ([CType](Resources.GetObject([\"checkBoxAdv1.UncheckedImage\"]), System.Drawing.Image))]         |
|                                                                                                                                                                                                                                                                        |
| [Me][.checkBoxAdv1.IndeterminateImage = ([CType](Resources.GetObject([\"checkBoxAdv1.IndeterminateImage\"]), System.Drawing.Image))] |
|                                                                                                                                                                                                                                                                        |
| [Me][.checkBoxAdv1.DisabledImage = ([CType](Resources.GetObject([\"checkBoxAdv1.DisabledImage\"]), System.Drawing.Image))]           |
|                                                                                                                                                                                                                                                                        |
| [Me][.checkBoxAdv1.StretchImage = [False]]                                                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 620: Image displayed for Checked State

of CheckBoxAdv

[] 

Images displayed during Mouse Hover

[] 

Images can also be set when the mouse is hovered over the CheckBoxAdv control.

[] 


  ------------------------- ------------------------------------------------------------------------------------
  CheckBoxAdv Properties    Description
  MouseOverCheckedImage     Gets / sets the image used to draw the CheckBox when checked and mouse over.
  MouseOverDisabledImage    Gets / sets the image used to draw the CheckBox when indeterminate and mouse over.
  MouseOverUncheckedImage   Gets / sets the image used to draw the CheckBox when unchecked and mouse over.
  ------------------------- ------------------------------------------------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                   |
| [this][.checkBoxAdv1.MouseOverCheckedImage = ((System.Drawing.[Image])(resources.GetObject([\"checkBoxAdv1.MouseOverCheckedImage\"])));]     |
|                                                                                                                                                                                                                                                                                   |
| [this][.checkBoxAdv1.MouseOverIndetermImage = ((System.Drawing.[Image])(resources.GetObject([\"checkBoxAdv1.MouseOverIndetermImage\"])));]   |
|                                                                                                                                                                                                                                                                                   |
| [this][.checkBoxAdv1.MouseOverUncheckedImage = ((System.Drawing.[Image])(resources.GetObject([\"checkBoxAdv1.MouseOverUncheckedImage\"])));] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                  |
| [Me][.checkBoxAdv1.MouseOverCheckedImage = ([CType](Resources.GetObject([\"checkBoxAdv1.MouseOverCheckedImage\"]), System.Drawing.Image))]     |
|                                                                                                                                                                                                                                                                                  |
| [Me][.checkBoxAdv1.MouseOverIndetermImage = ([CType](Resources.GetObject([\"checkBoxAdv1.MouseOverIndetermImage\"]), System.Drawing.Image))]   |
|                                                                                                                                                                                                                                                                                  |
| [Me][.checkBoxAdv1.MouseOverUncheckedImage = ([CType](Resources.GetObject([\"checkBoxAdv1.MouseOverUncheckedImage\"]), System.Drawing.Image))] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 621: Image displayed for Unchecked State

of CheckBoxAdv during Mouse Hover

**[]** 

A Sample which demonstrates the ImageCheckBox property of CheckBoxAdv is available in the below sample installation path.

 

..My Documents\\Syncfusion\\EssentialStudio\\***Version Number***\\Windows\\Tools.Windows\\Samples\\2.0\\Editors Package\\OptionControls

###### []{#p779}3.3.11.1.3.8        Themes and Visual Styles {#themes-and-visual-styles style="tab-stops: 0pt"}

[] 

This section discusses the themes and visual style settings that are supported by the CheckBoxAdv control.

[] 

Themes

[] 

The CheckBoxAdv can be provided with a themed appearance using the below given property.

[] 


  ---------------------- -------------------------------------------------------
  CheckBoxAdv Property   Description
  ThemesEnabled          Specifies whether themes are enabled for CheckBoxAdv.
  ---------------------- -------------------------------------------------------


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                          |
|                                                                                                                                                         |
| []                                                                                                    |
|                                                                                                                                                         |
| [this][.checkBoxAdv1.ThemesEnabled = [true];] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                       |
|                                                                                                                                                      |
| []                                                                                                 |
|                                                                                                                                                      |
| [Me][.checkBoxAdv1.ThemesEnabled = [True]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 622: ThemesEnabled property Set

[] 

Visual Styles

[] 

The appearance of the CheckBoxAdv control can be customized using the various options provided by the following properties.

[] 


+-----------------------------------+---------------------------------------------------------+
| CheckBoxAdv Properties            | Description                                             |
+-----------------------------------+---------------------------------------------------------+
| Style                             | Gets / sets an advanced appearance for the CheckBoxAdv. |
|                                   |                                                         |
|                                   |                                                         |
|                                   |                                                         |
|                                   | The options included are as follows.                    |
|                                   |                                                         |
|                                   |                                                         |
|                                   |                                                         |
|                                   | *Default and*                                           |
|                                   |                                                         |
|                                   | *Office2007.*                                           |
+-----------------------------------+---------------------------------------------------------+
| Office2007ColorScheme             | Gets / sets Office 2007 color scheme.                   |
|                                   |                                                         |
|                                   |                                                         |
|                                   |                                                         |
|                                   | The options included are as follows.                    |
|                                   |                                                         |
|                                   |                                                         |
|                                   |                                                         |
|                                   | *Managed,*                                              |
|                                   |                                                         |
|                                   | *Blue,*                                                 |
|                                   |                                                         |
|                                   | *Silver and*                                            |
|                                   |                                                         |
|                                   | *Black.*                                                |
|                                   |                                                         |
|                                   |                                                         |
|                                   |                                                         |
|                                   | The Style property should be set to \"Office2007\".     |
+-----------------------------------+---------------------------------------------------------+


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                              |
|                                                                                                                                                                                                             |
| []                                                                                                                                                        |
|                                                                                                                                                                                                             |
| [this][.checkBoxAdv1.Style = Syncfusion.Windows.Forms.Tools.[CheckBoxAdvStyle].Office2007;]    |
|                                                                                                                                                                                                             |
| [this][.checkBoxAdv1.Office2007ColorScheme = Syncfusion.Windows.Forms.[Office2007Theme].Blue;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                 |
|                                                                                                                                                                                |
| []                                                                                                                           |
|                                                                                                                                                                                |
| [Me][.checkBoxAdv1.Style = Syncfusion.Windows.Forms.Tools.CheckBoxAdvStyle.Office2007]    |
|                                                                                                                                                                                |
| [Me][.checkBoxAdv1.Office2007ColorScheme = Syncfusion.Windows.Forms.Office2007Theme.Blue] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 623: CheckBoxAdv Styles

[] 

{border="0"}

[] 

Figure 624: Office 2007 Color Schemes

[] 

When the **Office2007ColorScheme** property is set to \'Managed\', the CheckBox in the CheckBoxAdv can be displayed using custom colors supported by the control.

 

This can be done programmatically as follows.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                 |
|                                                                                                                                                                                                                |
| []                                                                                                                                                           |
|                                                                                                                                                                                                                |
| [this][.checkBoxAdv1.Style = Syncfusion.Windows.Forms.Tools.[CheckBoxAdvStyle].Office2007;]       |
|                                                                                                                                                                                                                |
| [this][.checkBoxAdv1.Office2007ColorScheme = Syncfusion.Windows.Forms.[Office2007Theme].Managed;] |
|                                                                                                                                                                                                                |
| [Office2007Colors][.ApplyManagedColors([this], [Color].Pink);]            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                    |
|                                                                                                                                                                                   |
| []                                                                                                                              |
|                                                                                                                                                                                   |
| [Me][.checkBoxAdv1.Style = Syncfusion.Windows.Forms.Tools.CheckBoxAdvStyle.Office2007]       |
|                                                                                                                                                                                   |
| [Me][.checkBoxAdv1.Office2007ColorScheme = Syncfusion.Windows.Forms.Office2007Theme.Managed] |
|                                                                                                                                                                                   |
| [Office2007Colors.ApplyManagedColors([Me], Color.Pink)]                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 625: CheckBox displayed in \"Pink\"

[] 

A sample which demonstrates the Themes and Visual Styles of CheckBoxAdv is available in the below sample installation path.

[] 

..My Documents\\Syncfusion\\EssentialStudio\\***Version Number***\\Windows\\Tools.Windows\\Samples\\2.0\\Editors Package\\OptionControls

[]{#related-topics}

