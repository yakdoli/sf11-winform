---
title: "][;][] |
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\conceptsandfeatures138.md
created_at: 2025-07-03
---






##### Concepts and Features {#concepts-and-features style="tab-stops: 0pt"}

###### 3.3.8.8.3.1 [[Mask Settings]](http://help.syncfusion.com/ug_82/WindowsFormsUI_Tools/AppearanceAndBehaviorSettings17.html) {#mask-settings style="tab-stops: 0pt"}

This section deals with the mask settings of MaskedEditBox control.[]

[] 

The format / behavior for the MaskedEditBox control is defined through the property given below.[]

[] 


  ------------------------------------------------ ----------------------------------------------------------------------------------
  MaskedEditBox Property[]   Description[]
  Mask[]                     Specifies the mask string for the MaskedEditBox control.[]
  ------------------------------------------------ ----------------------------------------------------------------------------------


[] 

The Mask is a string that is composed of literal characters and mask characters.[]

[] 

Literal characters give visual cues about the type of data being used. Mask characters are the placeholders for the data input. For example, a US telephone number can be represented by the following mask.[]

[] 

(###) - \### \#### Extn \####[]

[] 

In the above Mask, all the non \# characters are Literal characters and the #'s are Mask characters.[]

[] 

The MaskedEditBox control supports the following masks.[]

[] 


  ----------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Mask Characters[]   Description[]
  \#[]                Digit placeholder.[]
  .[]                 Decimal placeholder. The actual character used is the one specified as the decimal placeholder in your international settings. This character is treated as a literal for masking purposes.[]
  ,[]                 Thousands separator. The actual character used is the one specified as the thousands separator in your international settings. This character is treated as a literal for masking purposes.[]
  :[]                 Time separator. The actual character used is the one specified as the time separator in your international settings. This character is treated as a literal for masking purposes.[]
  /[]                 Date separator. The actual character used is the one specified as the date separator in your international settings. This character is treated as a literal for masking purposes.[]
  \\[]                Treat the next character in the mask string as a literal. This allows you to include the \"#\", \"&\", \"A\", and \"?\" characters in the mask. This character is treated as a literal for masking purposes.[]
  ;[]                 Character placeholder. Valid values for this placeholder are ANSI characters in the following ranges: 32-126 and 128-255.[]
  \>[ ]               Convert all the characters that follow to uppercase.[]
  \<[ ]               Convert all the characters that follow to lowercase.[]
  A[]                 Alphanumeric character placeholder (entry required). For example: a - z, A - Z, or 0 - 9.[]
  a[]                 Alphanumeric character placeholder (entry optional).[]
  9[]                 Digit placeholder (entry optional). For example: 0 - 9.[]
  C[]                 Character or space placeholder (entry optional). This operates exactly like the \"&\" placeholder and ensures compatibility with Microsoft Access.[]
  ?[]                 Letter placeholder. For example: a - z or A - Z.[]
  Literal[]           All other symbols are displayed as literals; that is, as themselves.[]
  ----------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                    |
| [this][.maskedEditBox1.Mask = ][\"##-##-####\"][;][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                                  |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                             |
| [Me][.maskedEditBox1.Mask = ][\"##-##-####\"][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 531: Mask property Set

[] 

A Sample which demonstrates the Mask Settings of MaskedEditBox control is available in the below sample installation path.[]

[] 

..My Documents\\Syncfusion\\EssentialStudio***\\Version Number***\\Windows\\Tools.Windows\\Samples\\2.0\\Editors Package\\EditorControls[]

 

###### 3.3.8.8.3.2 [[Mode Settings]](http://help.syncfusion.com/ug_82/WindowsFormsUI_Tools/ModeSettings.html) {#mode-settings style="tab-stops: 0pt"}

This section discusses the mode settings of the MaskedEditBox control.[]

[] 

MaskedEditBox control uses the following modes.[]

[] 


+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| MaskedEditBox Properties[] | Description[]                                                                                                            |
+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| ClipMode[]                 | Specifies the format of the text that will be returned by the MaskedEdit control. The options included are as follows.[] |
|                                                  |                                                                                                                                                |
|                                                  | []                                                                                                                       |
|                                                  |                                                                                                                                                |
|                                                  | *IncludeLiterals and*[]                                                                                                  |
|                                                  |                                                                                                                                                |
|                                                  | *ExcludeLiterals.*[]                                                                                                     |
|                                                  |                                                                                                                                                |
|                                                  | []                                                                                                                       |
|                                                  |                                                                                                                                                |
|                                                  | The default value is \'IncludeLiterals\'.[]                                                                              |
+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| InputMode[]                | Specifies the input mode for the MaskedEditBox control. The options included are as follows.[]                           |
|                                                  |                                                                                                                                                |
|                                                  | []                                                                                                                       |
|                                                  |                                                                                                                                                |
|                                                  | *OvertypeOnly and*[]                                                                                                     |
|                                                  |                                                                                                                                                |
|                                                  | *Normal.*[]                                                                                                              |
|                                                  |                                                                                                                                                |
|                                                  | []                                                                                                                       |
|                                                  |                                                                                                                                                |
|                                                  | The default value is \'OvertypeOnly\'.[]                                                                                 |
+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| UsageMode[]                | Specifies if the MaskedEditBox control is to behave as a numeric control.[]                                              |
+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

Clip mode[]

[] 

At runtime, we can copy / paste the entries of MaskedEditBox. The entries that are copied can be specified whether to include literals using the **ClipMode** property.[]

[] 

Setting the **ClipMode** property of the MaskedEditBox to \'ExcludeLiterals\', will get rid of the literals from the text that is returned by the control. The default value is set to \'IncludeLiterals\'.[]

[] 

InputMode[]

[] 

The different modes of the input can be determined by the** InputMode** property.[]

[] 

Setting the InputMode to \'Normal\', allows the user to work in insert mode and the INSERT key is not allowed. In OvertypeOnly mode, the INSERT key will not have any effect.[]

[] 

UsageMode[]

[] 

The **UsageMode** property modifies the behavior of the MaskedEditBox as detailed below.[]

[] 

Normal mode[]

[] 

When the UsageMode is set to \'Normal\', there is no change in the behavior. This is the default mode for a MaskedEditBox control.[]

[] 

Numeric Mode[]

[] 

When the UsageMode is set to \'Numeric\', the control creates internally two data groups and one decimal separator character in the mask. These groups are created such that the first group holds the mask value before the decimal separator and the second group holds the mask value after the decimal separator. For example, let us specify the mask as follows:[]

[] 

###.####[]

[] 

The first group will contain the value for the first 3 \### characters of the mask (the number group) and the second group (the decimal group) will contain the 5 characters (.####). The default group alignment for the number group will be right and the alignment for the decimal group will be left. Refer to the information on [[DataGroups]](http://help.syncfusion.com/ug_82/WindowsFormsUI_Tools/DisplaySettings2.html) for more information on how this works.[]

[] 

The **MaxValue** and **MinValue** properties are enforced only when the UsageMode is set to \'Numeric\'.[]

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                |
| [this][.maskedEditBox1.ClipMode = Syncfusion.Windows.Forms.Tools.][ClipModes][.ExcludeLiterals;][] |
|                                                                                                                                                                                                                                                                                                                                |
| [this][.maskedEditBox1.InputMode = Syncfusion.Windows.Forms.Tools.][MaskInputMode][.Normal;][]     |
|                                                                                                                                                                                                                                                                                                                                |
| [this][.maskedEditBox1.UsageMode = Syncfusion.Windows.Forms.Tools.][MaskedUsageMode][.Numeric;][]  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                           |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                      |
| [Me][.maskedEditBox1.ClipMode = Syncfusion.Windows.Forms.Tools.ClipModes.ExcludeLiterals][] |
|                                                                                                                                                                                                                      |
| [Me][.maskedEditBox1.InputMode = Syncfusion.Windows.Forms.Tools.MaskInputMode.Normal][]     |
|                                                                                                                                                                                                                      |
| [Me][.maskedEditBox1.UsageMode = Syncfusion.Windows.Forms.Tools.MaskedUsageMode.Numeric][]  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

###### 3.3.8.8.3.3 [[Display Settings]](http://help.syncfusion.com/ug_82/WindowsFormsUI_Tools/DisplaySettings2.html) {#display-settings style="tab-stops: 0pt"}

This section discusses the display settings of the MaskedEditBox control.[]

[] 

Separators[]

[] 

The user data can be displayed along with separators at run time for specifying date, time, decimals and thousands. It is not required to type separators at run time. Separators can be specified in the mask character itself.[]

[] 


+--------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| MaskedEditBox Properties[] | Description[]                                                                      |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| DateSeparator[]            | Specifies the character to use when a date separator position is specified.[]      |
|                                                  |                                                                                                          |
|                                                  | []                                                                                 |
|                                                  |                                                                                                          |
|                                                  | The default separator is \'/\'.[]                                                  |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| DecimalSeparator[]         | Specifies the character to use when a decimal separator position is specified.[]   |
|                                                  |                                                                                                          |
|                                                  | []                                                                                 |
|                                                  |                                                                                                          |
|                                                  | The default separator is \'.\'.[]                                                  |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| ThousandSeparator[]        | Specifies the character to use when a thousands separator position is specified.[] |
|                                                  |                                                                                                          |
|                                                  | []                                                                                 |
|                                                  |                                                                                                          |
|                                                  | The default separator is \',\'.[]                                                  |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| TimeSeparator[]            | Specifies the character to use when a time separator position is specified.[]      |
|                                                  |                                                                                                          |
|                                                  | []                                                                                 |
|                                                  |                                                                                                          |
|                                                  | The default separator is \':\'.[]                                                  |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------+


[] 

For example, if you want to display the user data in date time format say mm/dd/yy, the mask character should be \'##/##/##\'.[]

[] 

We can change the default separators used. If you want to display the date time as \'mm-dd-yy\', change the **DateSeparator**property from \'/\' to \'-\'.[]

[] 

Similarly other separators can be used.[]

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                        |
| [this][.maskedEditBox1.DateSeparator = ][\'-\'][;][]     |
|                                                                                                                                                                                                                                                                                        |
| [this][.maskedEditBox1.DecimalSeparator = ][\'.\'][;][]  |
|                                                                                                                                                                                                                                                                                        |
| [this][.maskedEditBox1.ThousandSeparator = ][\',\'][;][] |
|                                                                                                                                                                                                                                                                                        |
| [this][.maskedEditBox1.TimeSeparator = ][\':\'][;][]     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                  |
|                                                                                                                                                                             |
| []                                                                                                                                                    |
|                                                                                                                                                                             |
| [Me][.maskedEditBox1.DateSeparator = \"-\"C][]     |
|                                                                                                                                                                             |
| [Me][.maskedEditBox1.DecimalSeparator = \".\"C][]  |
|                                                                                                                                                                             |
| [Me][.maskedEditBox1.ThousandSeparator = \",\"C][] |
|                                                                                                                                                                             |
| [Me][.maskedEditBox1.TimeSeparator = \":\"C][]     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

 

Figure 532: Date Separator Set

[] 

{border="0"}

[] 

Figure 533: Decimal Separator Set

[] 

{border="0"}

[] 

Figure 534: Thousand Separator Set

[] 

{border="0"}

Figure 535: Time Separator Set

[] 

Cursor Position[]

[] 

The cursor position of the MaskedEditBox control can be specified using the options provided by the following properties.[]

[] 


+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| MaskedEditBox Properties[] | Description[]                                                                                                         |
+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| PositionAt[]               | Defines the control\'s cursor position behavior on getting the focus. The options included are as follows:[]          |
|                                                  |                                                                                                                                             |
|                                                  | []                                                                                                                    |
|                                                  |                                                                                                                                             |
|                                                  | *Decimal*[]                                                                                                           |
|                                                  |                                                                                                                                             |
|                                                  | *FirstPosition and*[]                                                                                                 |
|                                                  |                                                                                                                                             |
|                                                  | *FirstMaskPosition.*[]                                                                                                |
|                                                  |                                                                                                                                             |
|                                                  | []                                                                                                                    |
|                                                  |                                                                                                                                             |
|                                                  | The default value is \'FirstPosition\'.[]                                                                             |
+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| PositionAtDecimal[]        | Indicates whether the cursor is to be positioned at the decimal separator (if any) when the control receives focus.[] |
+--------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                      |
| [this][.maskedEditBox1.PositionAt = Syncfusion.Windows.Forms.Tools.][SpecialCursorPosition][.Decimal;][] |
|                                                                                                                                                                                                                                                                                                                                      |
| [this][.maskedEditBox1.PositionAtDecimal = ][true][;][]                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                   |
| [Me][.maskedEditBox1.PositionAt = Syncfusion.Windows.Forms.Tools.SpecialCursorPosition.Decimal][]                                                        |
|                                                                                                                                                                                                                                                                                   |
| [Me][.maskedEditBox1.PositionAtDecimal = ][true][;][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

DataGroups[]

[] 

Text can be split up and aligned using the options provided by the below given property.[]

[] 


  ------------------------------------------------ -----------------------------------------------------------------------------------------------
  MaskedEditBox Property[]   Description[]
  DataGroups[]               Specifies the data groups that can be used for splitting up the text.[]
  ------------------------------------------------ -----------------------------------------------------------------------------------------------


[] 

The **DataGroups** property of the MaskedEditBox defines a virtual grouping of the mask value. Each group is defined by a**MaskedEditDataGroupInfo** object (the DataGroups property is a collection of these objects).[]

[] 

A data group is defined by its **GroupLength **property. For example, if the mask is given as follows,[]

[] 

###.###.###.###[]

[] 

and there are 4 groups specified with group lengths of 4, 4, 4, 3 respectively, the groups will be defined as:[]

[] 

Group1 ###.[]

Group2 ###.[]

Group3 ###.[]

Group4 \###[]

[] 

The **DataAlignment** property of the MaskedEditDataGroupInfo object specifies the type of alignment to be used for the group. The data alignment behavior will be defined as given below:[]

[] 

[·      ]**Left :** All the filled-in mask fields in the group will be grouped to the left-most positions.[]

[·      ]**Right :** All the filled-in mask fields in the group will be grouped to the right-most positions.[]

[·      ]**Center :** All the filled-in mask fields in the group will be grouped to the center-most positions.[]

[] 

The group alignments will only be enforced after the control has lost focus.[]

[] 

The **MaskedEditDataGroupInfo.Value** property can be used to get the value of a group without any parsing. For example, if the mask is given as follows,[]

[] 

(###) - \### \#### Extn \####[]

[] 

3 groups can be defined as follows:[]

[] 

Group1 - (###)[]

Group2 - \### \####[]

Group3 Extn - \####[]

[] 

The value of Group 1 will be the area code, Group 2 will be the phone number, and Group 3 will be the extension.[]

[] 

The following code snippet uses two groups.[]

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                  |
| [// Adding DataGroups.][]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                  |
| [this][.maskedEditBox1.DataGroups.Add(][this][.maskedEditDataGroupInfo1);][]                                         |
|                                                                                                                                                                                                                                                                                                                                                  |
| [this][.maskedEditBox1.DataGroups.Add(][this][.maskedEditDataGroupInfo2);][]                                         |
|                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                  |
| [// Defining maskedEditDataGroupInfo1.][]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                  |
| [this][.maskedEditDataGroupInfo1.DataGroupAlignment = Syncfusion.Windows.Forms.Tools.][MaskGroupAlignment][.Left;][] |
|                                                                                                                                                                                                                                                                                                                                                  |
| [this][.maskedEditDataGroupInfo1.DataGroupName = ][\"One\"][;][]                                                   |
|                                                                                                                                                                                                                                                                                                                                                  |
| [this][.maskedEditDataGroupInfo1.DataGroupSize = 3;][]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                  |
| [// Defining maskedEditDataGroupInfo2.][]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                  |
| [this][.maskedEditDataGroupInfo2.DataGroupAlignment = Syncfusion.Windows.Forms.Tools.][MaskGroupAlignment][.None;][] |
|                                                                                                                                                                                                                                                                                                                                                  |
| [this][.maskedEditDataGroupInfo2.DataGroupName = ][\"Two\"][;][]                                                   |
|                                                                                                                                                                                                                                                                                                                                                  |
| [this][.maskedEditDataGroupInfo2.DataGroupSize = 4;][]                                                                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                     |
| [\' Adding DataGroups.][]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                     |
| [Me][.maskedEditBox1.DataGroups.Add(][Me][.maskedEditDataGroupInfo1)][] |
|                                                                                                                                                                                                                                                                                                     |
| [Me][.maskedEditBox1.DataGroups.Add(][Me][.maskedEditDataGroupInfo2)][] |
|                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                     |
| [\' Defining maskedEditDataGroupInfo1.][]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                     |
| [Me][.maskedEditDataGroupInfo1.DataGroupAlignment = Syncfusion.Windows.Forms.Tools.MaskGroupAlignment.Left][]                                                              |
|                                                                                                                                                                                                                                                                                                     |
| [Me][.maskedEditDataGroupInfo1.DataGroupName = ][\"One\"][]                                                             |
|                                                                                                                                                                                                                                                                                                     |
| [Me][.maskedEditDataGroupInfo1.DataGroupSize = 3][]                                                                                                                        |
|                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                     |
| [\' Defining maskedEditDataGroupInfo2.][]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                     |
| [Me][.maskedEditDataGroupInfo2.DataGroupAlignment = Syncfusion.Windows.Forms.Tools.MaskGroupAlignment.None][]                                                              |
|                                                                                                                                                                                                                                                                                                     |
| [Me][.maskedEditDataGroupInfo2.DataGroupName = ][\"Two\"][]                                                             |
|                                                                                                                                                                                                                                                                                                     |
| [Me][.maskedEditDataGroupInfo2.DataGroupSize = 4][]                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

3.3.8.8.3.3.1      Displaying Characters as Substitutes for User Input

We can display different characters as substitutes for the user input. This can be done using the below given properties.[]

[] 


  -------------------------------------------------- --------------------------------------------------------------------------------------------------------------
  MaskedEditBox Properties[]   Description[]
  Sequentially[]               Indicates whether the control can sequentially display mask characters.[]
  PasswordChar[]               Indicates the character to display for password input for single-line edit controls.[]
  -------------------------------------------------- --------------------------------------------------------------------------------------------------------------


[] 

The **MaskedEditBox.Sequentially** property indicates whether the control can sequentially display mask characters. After setting the Sequentially property to \'True\', you can use the **PasswordChar** property in order to set the character, that is to be displayed as a substitute for the user input.[]

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [private][ ][void][ Form1_Load(][object][ sender, System.][EventArgs][ e)][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [{][]                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [this][.maskedEditBox1.Sequentially = ][true][;][]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [this][.maskedEditBox1.PasswordChar = ][\'\$\'][;][]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [}][]                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Private Sub][ Form1_Load(ByVal sender ][As Object][, ][ByVal][ e ][As][ System.EventArgs)][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Me][.maskedEditBox1.Sequentially = ][True][]                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Me][.maskedEditBox1.PasswordChar = \"\$\"c][]                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [End Sub][]                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 536: \'\$\' Character displayed Sequentially

[] 

A Sample which demonstrates the PasswordChar property of MaskedEditBox control is available in the below sample installation path.[]

[] 

..My Documents\\Syncfusion\\EssentialStudio***\\Version Number***\\Windows\\Tools.Windows\\Samples\\2.0\\Editors Package\\EditorControls[]

 

###### 3.3.8.8.3.4 [[Culture Settings]](http://help.syncfusion.com/ug_82/WindowsFormsUI_Tools/CultureSettings2.html) {#culture-settings style="tab-stops: 0pt"}

This section discusses the culture settings of the MaskedEditBox control.[]

[] 


+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MaskedEditBox Properties[] | Description[]                                                                                                                              |
+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Culture[]                  | Gets / sets the culture that is to be used for formatting the numeric display.[]                                                           |
+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SpecialCultureValue[]      | Gets / sets the mode for the cultures.[]                                                                                                   |
|                                                  |                                                                                                                                                                  |
|                                                  | []                                                                                                                                         |
|                                                  |                                                                                                                                                                  |
|                                                  | It includes the below given options:[]                                                                                                     |
|                                                  |                                                                                                                                                                  |
|                                                  | []                                                                                                                                         |
|                                                  |                                                                                                                                                                  |
|                                                  | *None,*[]                                                                                                                                  |
|                                                  |                                                                                                                                                                  |
|                                                  | *CurrentCulture,*[]                                                                                                                        |
|                                                  |                                                                                                                                                                  |
|                                                  | *UICulture and*[]                                                                                                                          |
|                                                  |                                                                                                                                                                  |
|                                                  | *InstalledCulture.*[]                                                                                                                      |
+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| UseUserOverride[]          | Specifies if the NumberFormatInfo used for formatting will use the User Overrides for the culture. The default value is set to \'True\'.[] |
+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [this][.maskedEditBox1.Culture = ][new][ System.Globalization.][CultureInfo][(][\"ar-SA\"][);][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [this][.maskedEditBox1.SpecialCultureValue = Syncfusion.Windows.Forms.Tools.][SpecialCultureValues][.None;][]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [this][.maskedEditBox1.UseUserOverride = ][true][;][]                                                                                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Me][.maskedEditBox1.Culture = ][New][ System.Globalization.CultureInfo(][\"ar-SA\"][)][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Me][.maskedEditBox1.SpecialCultureValue = Syncfusion.Windows.Forms.Tools.SpecialCultureValues.None][]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [Me][.maskedEditBox1.UseUserOverride = ][True][]                                                                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 537: Culture Set for the MaskedEditBox Control[]

 

###### 3.3.8.8.3.5 [[Text Settings]](http://help.syncfusion.com/ug_82/WindowsFormsUI_Tools/TextSettings31.html) {#text-settings style="tab-stops: 0pt"}

This section discusses the text settings of the MaskedEditBox control.[]

[] 

The text associated with the MaskedEditBox control can be set and customized using the below given settings.[]

[] 


+--------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| MaskedEditBox Properties[] | Description[]                                                                      |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| CharacterCasing[]          | Gets / sets the case of character as they are typed.[]                             |
|                                                  |                                                                                                          |
|                                                  | []                                                                                 |
|                                                  |                                                                                                          |
|                                                  | It includes the below given options:[]                                             |
|                                                  |                                                                                                          |
|                                                  | []                                                                                 |
|                                                  |                                                                                                          |
|                                                  | *Normal,*[]                                                                        |
|                                                  |                                                                                                          |
|                                                  | *Upper and*[]                                                                      |
|                                                  |                                                                                                          |
|                                                  | *Lower.*[]                                                                         |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| TextAlign[]                | Indicates how the text should be aligned for edit controls.[]                      |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| SelectedText[]             | Gets / sets the selected text in the MaskedEditBox.[]                              |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| HideSelection[]            | Indicates that the selection should be hidden when the edit control loses focus.[] |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| ClipText[]                 | Returns the clipped text without the formatting.[]                                 |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| DrawActiveWhenDisabled[]   | Specifies if the text should be drawn active, even when disabled.[]                |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------------+


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                         |
| [this][.maskedEditBox1.CharacterCasing = System.Windows.Forms.][CharacterCasing][.Upper;][] |
|                                                                                                                                                                                                                                                                                                                         |
| [this][.maskedEditBox1.TextAlign = System.Windows.Forms.][HorizontalAlignment][.Center;][]  |
|                                                                                                                                                                                                                                                                                                                         |
| [this][.maskedEditBox1.SelectedText = ][\"34\"][;][]                                      |
|                                                                                                                                                                                                                                                                                                                         |
| [this][.maskedEditBox1.HideSelection = ][true][;][]                                         |
|                                                                                                                                                                                                                                                                                                                         |
| [this][.maskedEditBox1.ClipText = ][\"34\"][;][]                                          |
|                                                                                                                                                                                                                                                                                                                         |
| [this][.maskedEditBox1.DrawActiveWhenDisabled = ][true][;][]                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                                        |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                   |
| [Me][.maskedEditBox1.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper][]                     |
|                                                                                                                                                                                                                                   |
| [Me][.maskedEditBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center][]                      |
|                                                                                                                                                                                                                                   |
| [Me][.maskedEditBox1.SelectedText = ][\"34\"][]       |
|                                                                                                                                                                                                                                   |
| [Me][.maskedEditBox1.HideSelection = ][True][]          |
|                                                                                                                                                                                                                                   |
| [Me][.maskedEditBox1.ClipText = ][\"34\"][]           |
|                                                                                                                                                                                                                                   |
| [Me][.maskedEditBox1.DrawActiveWhenDisabled = ][True][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 538: Character Case set to \"Upper\"

[] 

{border="0"}

[] 

Figure 539: Text Aligned to the \"Center\"

[] 

The methods associated with the above properties are given below.[]

[] 


  -------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------
  Methods[]                    Description[]
  AppendText[]                 Appends the text to the current text of a textbox.[]
  OnCharacterCasingChanged[]   Raises the CharacterCasingChanged event.[]
  Cut[]                        Cuts the selected data to the clipboard.[]
  Copy[]                       Copies the content of the NumberTextBox to the clipboard. The ClipMode property dictates what gets copied.[]
  Paste[]                      Pastes the data in the clipboard into the NumberTextBox control.[]
  Select[]                     Selects a range of text in the TextBox.[]
  -------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------


[] 

Clip Mode[]

[] 

The formatting for the text can be enabled or disabled using the property given below.[]

[] 


+------------------------------------------------+--------------------------------------------------------------------------------------------------------------+
| MaskedEditBox Property[] | Description[]                                                                          |
+------------------------------------------------+--------------------------------------------------------------------------------------------------------------+
| ClipMode[]               | Specifies the format of the text that will be returned by the MaskedEditBox control.[] |
|                                                |                                                                                                              |
|                                                | []                                                                                     |
|                                                |                                                                                                              |
|                                                | It includes the below given options:[]                                                 |
|                                                |                                                                                                              |
|                                                | []                                                                                     |
|                                                |                                                                                                              |
|                                                | *IncludeLiterals and*[]                                                                |
|                                                |                                                                                                              |
|                                                | *ExcludeLiterals.*[]                                                                   |
+------------------------------------------------+--------------------------------------------------------------------------------------------------------------+


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                |
| [this][.maskedEditBox1.ClipMode = Syncfusion.Windows.Forms.Tools.][ClipModes][.IncludeLiterals;][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                           |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                      |
| [Me][.maskedEditBox1.ClipMode = Syncfusion.Windows.Forms.Tools.ClipModes.IncludeLiterals][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

OverflowIndicatorToolTipText[]

[] 

The tooltip that should be displayed when an overflow of text occurs can be set using the below given properties.[]

[] 


  ------------------------------------------------------ --------------------------------------------------------------------------
  MaskedEditBox Properties[]       Description[]
  OverflowIndicatorToolTipText[]   Specifies the overflow indicator tooltip text.[]
  ShowOverflowIndicator[]          Gets / sets overflow indicator visibility.[]
  ShowOverflowIndicatorToolTip[]   Gets / sets can show overflow indicator tooltip.[]
  ------------------------------------------------------ --------------------------------------------------------------------------


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                               |
| [this][.maskedEditBox1.OverflowIndicatorToolTipText = ][\"Text Overflow\"][;][] |
|                                                                                                                                                                                                                                                                                                               |
| [this][.maskedEditBox1.ShowOverflowIndicator = ][true][;][]                       |
|                                                                                                                                                                                                                                                                                                               |
| [this][.maskedEditBox1.ShowOverflowIndicatorToolTip = ][true][;][]                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                                                              |
|                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                         |
| [Me][.maskedEditBox1.OverflowIndicatorToolTipText = ][\" Text Overflow\"][] |
|                                                                                                                                                                                                                                                         |
| [Me][.maskedEditBox1.ShowOverflowIndicator = ][True][]                        |
|                                                                                                                                                                                                                                                         |
| [Me][.maskedEditBox1.ShowOverflowIndicatorToolTip = ][True][]                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 540: Overflow Indicator ToolTip Text Set

[] 

A Sample which demonstrates the Text Align and Character Casing features of MaskedEditBox control is available in the below sample installation path.[]

[] 

..My Documents\\Syncfusion\\EssentialStudio***\\Version Number***\\Windows\\Tools.Windows\\Samples\\2.0\\Editors Package\\EditorControls[]

 

###### 3.3.8.8.3.6 [[Value Settings]](http://help.syncfusion.com/ug_82/WindowsFormsUI_Tools/ValueSettings2.html) {#value-settings style="tab-stops: 0pt"}

The value settings of the MaskedEditBox control are discussed below.[]

[] 

MinValue and MaxValue[]

[] 

The minimum and maximum values of the MaskedEditBox control can be set using the below given properties.

 


+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| MaskedEditBox Properties[] | Description[]                                                                                               |
+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| MinValue[]                 | Specifies the minimum value that can be set through the MaskedEditBox. The default value is set to \'0\'.[] |
+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| MaxValue[]                 | Specifies the maximum value that can be set through the MaskedEditBox.[]                                    |
|                                                  |                                                                                                                                   |
|                                                  | []                                                                                                          |
|                                                  |                                                                                                                                   |
|                                                  | The default value is set to \'79228162514264337593543950335\'.[]                                            |
+--------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [this][.maskedEditBox1.MinValue = ][new][ ][decimal][(][new][ ][int][\[\] {50, 0, 0, 0});][]  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [this][.maskedEditBox1.MaxValue = ][new][ ][decimal][(][new][ ][int][\[\] {100, 0, 0, 0});][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Me][.maskedEditBox1.MinValue = ][New][ ][Decimal][(][New][ ][Integer][() {50, 0, 0, 0})][]  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Me][.maskedEditBox1.MaxValue = ][New][ ][Decimal][(][New][ ][Integer][() {100, 0, 0, 0})][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

###### 3.3.8.8.3.7 [[Appearance Settings]](http://help.syncfusion.com/ug_82/WindowsFormsUI_Tools/AppearanceSettings51.html) {#appearance-settings style="tab-stops: 0pt"}

3.3.8.8.3.7.1      Background Settings

The background settings of the MaskedEditBox control are discussed below.[]

[] 

Background Color[]

[] 

The background color of the control can be set using the properties given below.[]

[] 


  ------------------------------------------------ --------------------------------------------------------------------------
  MaskedEditBox Property[]   Description[]
  BackColor[]                Specifies the background color of the component.[]
  ------------------------------------------------ --------------------------------------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                           |
| [this][.maskedEditBox1.BackColor = System.Drawing.][Color][.PaleGoldenrod;][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                      |
|                                                                                                                                                                                                 |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                 |
| [Me][.maskedEditBox1.BackColor = System.Drawing.Color.PaleGoldenrod][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

 

Figure 541: Background Color set for MaskedEditBox

[] 

The method associated with the above property is given below.[]

[] 


  ---------------------------------------- ---------------------------------------------------------------------------------
  Method[]           Description[]
  ResetBackColor[]   Resets the **BackColor** property to its default value.[]
  ---------------------------------------- ---------------------------------------------------------------------------------


[] 

A sample which demonstrates the Background Settings of MaskedEditBox control is available in the below sample installation path.[]

[] 

..My Documents\\Syncfusion\\EssentialStudio\\***Version Number***\\Windows\\Tools.Windows\\Samples\\2.0\\Editors Package\\EditorControls[]

3.3.8.8.3.7.2       Foreground Settings

The foreground settings of the MaskedEditBox control are discussed below.[]

[] 

Foreground Color[]

[] 

The foreground color of the control can be set using the properties given below.[]

[] 


  ------------------------------------------------ ----------------------------------------------------------------------------------------------------------
  MaskedEditBox Property[]   Description[]
  ForeColor[]                Specifies the foreground color of this component, which is used to display text.[]
  ------------------------------------------------ ----------------------------------------------------------------------------------------------------------


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                         |
| [this][.maskedEditBox1.ForeColor = System.Drawing.][Color][.DarkMagenta;][] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                    |
|                                                                                                                                                                                               |
| []                                                                                                                                                                      |
|                                                                                                                                                                                               |
| [Me][.maskedEditBox1.ForeColor = System.Drawing.Color.DarkMagenta][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 542: Foreground Color set for MaskedEditBox[]

[] 

A Sample which demonstrates the Foreground Settings of MaskedEditBox control is available in the below sample installation path.[]

[] 

..My Documents\\Syncfusion\\EssentialStudio\\***Version Number***\\Windows\\Tools.Windows\\Samples\\2.0\\Editors Package\\EditorControls[]

 

###### 3.3.8.8.3.8 [[Behavior Settings]](http://help.syncfusion.com/ug_82/WindowsFormsUI_Tools/BehaviorSettings41.html) {#behavior-settings style="tab-stops: 0pt"}

The behavior settings of the MaskedEditBox control are discussed below.[]

[] 

Prompt and Padding Character Settings[]

[] 

MaskedEditBox control allows  you to add prompt characters in the input.[]

[] 


  --------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  MaskedEditBox Properties[]    Description[]
  AllowPrompt[]                 Specifies if the prompt character can be allowed to be entered as an input character.[]
  PaddingCharacter[]            Specifies the character that will be used instead of mask characters when the mask position has not been filled when the text property is used.[]
  PaddingCharacterInt[]         Gets / sets the integer version of the padding character.[]
  Prompt Character[]            Gets / sets the character that will be used instead of the mask characters when the mask position has not been filled.[]
  PrompCharacterInt[]           Gets / sets the integer version of the PromptCharacter.[]
  PassivePromptCharacter[]      Gets / sets the character that will be used instead of the mask characters when the mask position has not been filled (when the control does not have the focus).[]
  PassivePromptCharacterInt[]   Gets / sets the integer version of the PassivePromptCharacter.[]
  --------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                               |
| [this][.maskedEditBox1.AllowPrompt = ][true][;][] |
|                                                                                                                                                                                                                                                                               |
| [this][.maskedEditBox.PaddingCharacterInt = 0;][]                                                                                                    |
|                                                                                                                                                                                                                                                                               |
| [this][.maskedEditBox1.PromptCharacterInt = 37;][]                                                                                                   |
|                                                                                                                                                                                                                                                                               |
| [this][.maskedEditBox1.PassivePromptCharacterInt = 47;][]                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                             |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                        |
| [Me][.maskedEditBox1.AllowPrompt = ][True][] |
|                                                                                                                                                                                                                        |
| [Me][.maskedEditBox.PaddingCharacterInt = 0][]                                                |
|                                                                                                                                                                                                                        |
| [Me][.maskedEditBox1.PromptCharacterInt = 37][]                                               |
|                                                                                                                                                                                                                        |
| [Me][.maskedEditBox1.PassivePromptCharacterInt = 47][]                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


[{border="0"}] Note: We can trim the additional spaces present in the mask by setting the PaddingCharacterInt property to \'0\'.[]


[] 

MaxLength[]

[] 

The maximum length of the text can be set using the property given below.[]

[] 


  ------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------
  MaskedEditBox Property[]   Description[]
  MaxLength[]                Specifies the maximum number of characters that can be entered into the edit control. The default value is set to \'32767\'.[]
  ------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                   |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                          |
| [this][.maskedEditBox1.MaxLength = 32800; ][              ][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**[]                                                                             |
|                                                                                                                                                                    |
| []                                                                                                                                           |
|                                                                                                                                                                    |
| [Me][.maskedEditBox1.MaxLength = 32800][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

ReadOnly[]

[] 

The ReadOnly mode can be enabled for the MaskedEditBox control using the below given property.[]

[] 


  ------------------------------------------------ -----------------------------------------------------------------------------------------------
  MaskedEditBox Property[]   Description[]
  ReadOnly[]                 Specifies whether the text in the edit control can be changed or not.[]
  ------------------------------------------------ -----------------------------------------------------------------------------------------------


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                            |
| [this][.maskedEditBox1.ReadOnly = ][true][;][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**[]                                                                                                                              |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                     |
| [Me][.maskedEditBox1.ReadOnly = ][True][] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

###### 3.3.8.8.3.9 [[Border Settings]](http://help.syncfusion.com/ug_82/WindowsFormsUI_Tools/BorderStyles5.html) {#border-settings style="tab-stops: 0pt"}

The border settings of the MaskedEditBox control are discussed in this section.[]

[] 

The wide variety of border options that are available for the MaskedEditBox control are given below.[]

[] 


+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| MaskedEditBox Properties[] | Description[]                                                                                    |
+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| Border3DStyle[]            | Indicates the style of the 3D border. The options included are as follows:[]                     |
|                                                  |                                                                                                                        |
|                                                  | []                                                                                               |
|                                                  |                                                                                                                        |
|                                                  | *RaisedOuter,*[]                                                                                 |
|                                                  |                                                                                                                        |
|                                                  | *SunkenOuter,*[]                                                                                 |
|                                                  |                                                                                                                        |
|                                                  | *RaisedInner,*[]                                                                                 |
|                                                  |                                                                                                                        |
|                                                  | *SunkenInner,*[]                                                                                 |
|                                                  |                                                                                                                        |
|                                                  | *Raised,*[]                                                                                      |
|                                                  |                                                                                                                        |
|                                                  | *Etched,*[]                                                                                      |
|                                                  |                                                                                                                        |
|                                                  | *Bump,*[]                                                                                        |
|                                                  |                                                                                                                        |
|                                                  | *Sunken,*[]                                                                                      |
|                                                  |                                                                                                                        |
|                                                  | *Adjust and*[]                                                                                   |
|                                                  |                                                                                                                        |
|                                                  | *Flat.*[]                                                                                        |
|                                                  |                                                                                                                        |
|                                                  | []                                                                                               |
|                                                  |                                                                                                                        |
|                                                  | The default value is set to \'Sunken\'.[]                                                        |
+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| BorderColor[]              | Specifies the color of the 2D border.[]                                                          |
+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| BorderSides[]              | Indicates the border sides of the panel. The options included are as follows:[]                  |
|                                                  |                                                                                                                        |
|                                                  | []                                                                                               |
|                                                  |                                                                                                                        |
|                                                  | *Left,*[]                                                                                        |
|                                                  |                                                                                                                        |
|                                                  | *Top,*[]                                                                                         |
|                                                  |                                                                                                                        |
|                                                  | *Right,*[]                                                                                       |
|                                                  |                                                                                                                        |
|                                                  | *Bottom,*[]                                                                                      |
|                                                  |                                                                                                                        |
|                                                  | *Middle and*[]                                                                                   |
|                                                  |                                                                                                                        |
|                                                  | *All.*[]                                                                                         |
+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| BorderStyle[]              | Indicates whether the edit control should have a border. The options included are given below:[] |
|                                                  |                                                                                                                        |
|                                                  | []                                                                                               |
|                                                  |                                                                                                                        |
|                                                  | *FixedSingle,*[]                                                                                 |
|                                                  |                                                                                                                        |
|                                                  | *Fixed3D and*[]                                                                                  |
|                                                  |                                                                                                                        |
|                                                  | *None.*[]                                                                                        |
+--------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                       |
| [this][.maskedEditBox1.Border3DStyle = System.Windows.Forms.][Border3DStyle][.Bump;][]    |
|                                                                                                                                                                                                                                                                                                                       |
| [this][.maskedEditBox1.BorderColor = System.Drawing.][Color][.Lime;][]                    |
|                                                                                                                                                                                                                                                                                                                       |
| [this][.maskedEditBox1.BorderSides = System.Windows.Forms.][Border3DSide][.All;][]        |
|                                                                                                                                                                                                                                                                                                                       |
| [this][.maskedEditBox1.BorderStyle = System.Windows.Forms.][BorderStyle][.FixedSingle;][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                  |
|                                                                                                                                                                                                             |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                             |
| [Me][.maskedEditBox1.Border3DStyle = System.Windows.Forms.Border3DStyle.Bump][]    |
|                                                                                                                                                                                                             |
| [Me][.maskedEditBox1.BorderColor = System.Drawing.Color.Magenta][]                 |
|                                                                                                                                                                                                             |
| [Me][.maskedEditBox1.BorderSides = System.Windows.Forms.Border3DSide.All][]        |
|                                                                                                                                                                                                             |
| [Me][.maskedEditBox1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 543: MaskedEditBox with Border Set

[] 

A Sample which demonstrates the Border Settings of MaskedEditBox control is available in the below sample installation path.[]

[] 

..My Documents\\Syncfusion\\EssentialStudio\\***Version Number***\\Windows\\Tools.Windows\\Samples\\2.0\\Editors Package\\EditorControls[]

 

###### 3.3.8.8.3.10        [[Layout Settings]](http://help.syncfusion.com/ug_82/WindowsFormsUI_Tools/LayoutSettings2.html) {#layout-settings style="tab-stops: 0pt"}

The layout settings of the MaskedEditBox control are discussed in this section.[]

[] 

The size of the MaskedEditBox control can be set according to the needs of the user using the properties discussed below.[]

[] 


  -------------------------------------------------- -----------------------------------------------------------------------
  MaskedEditBox Properties[]   Description[]
  MaximumSize[]                Gets / sets the maximum size for the control.[]
  MinimumSize[]                Gets / sets the minimum size for the control.[]
  -------------------------------------------------- -----------------------------------------------------------------------


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [this][.maskedEditBox1.MaximumSize = ][new][ System.Drawing.][Size][(150, 20);][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [this][.maskedEditBox1.MinimumSize = ][new][ System.Drawing.][Size][(150, 20);][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                        |
| [Me][.maskedEditBox1.MaximumSize = ][New][ System.Drawing.Size(150, 20)][] |
|                                                                                                                                                                                                                                                                                                        |
| [Me][.maskedEditBox1.MinimumSize = ][New][ System.Drawing.Size(150, 20)][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 544: Size of the MaskedEditBox control Set

 

###### 3.3.8.8.3.11        [[Applying Themes]](http://help.syncfusion.com/ug_82/WindowsFormsUI_Tools/ApplyingThemes12.html) {#applying-themes style="tab-stops: 0pt"}

Themes can be applied to the MaskedEditBox control using the property given below.[]

[] 


  ------------------------------------------------ --------------------------------------------------------------------------------------------------------------------
  MaskedEditBox Property[]   Description[]
  ThemesEnabled[]            Specifies whether or not to use XP themes when BorderStyle property is set to \'Fixed3D\'.[]
  ------------------------------------------------ --------------------------------------------------------------------------------------------------------------------


[] 


[{border="0"}][ Note:][ ][Refer ][[Border Settings]](http://help.syncfusion.com/ug_82/WindowsFormsUI_Tools/BorderStyles5.html)[ topic to know about the BorderStyle property.][]


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                 |
| [this][.maskedEditBox1.ThemesEnabled = ][true][;][] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                               |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                          |
| [Me][.maskedEditBox1.ThemesEnabled = ][true][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 545: Themes Applied to MaskedEditBox Control[]

 

 

[]{#related-topics}

