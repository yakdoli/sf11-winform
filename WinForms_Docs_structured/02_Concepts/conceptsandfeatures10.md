---
title: conceptsandfeatures10.md
original_path: WinForms_Docs/02_Concepts/conceptsandfeatures10.md
created_at: 2025-08-05
---






##### Concepts and Features {#concepts-and-features style="tab-stops: 0pt"}

 

 This section discusses the various features of the PercentTextBox control.

 

###### 5.1.2.6.2.1 Behavior Settings {#behavior-settings style="tab-stops: 0pt"}

[] 

Setting Limits for the Value

[] 

**MaxValue** and **MinValue** allows to set the maximum and the minimum percent values beyond which the user is restricted to enter any values. Setting **IncrementStep** increases the values in steps of the number when the arrow keys are pressed.

[] 


+-----------------------------------+----------------------------------------------------+
|                                   |                                                    |
|                                   |                                                    |
| Property                          | Description                                        |
+-----------------------------------+----------------------------------------------------+
| IncrementStep                     | Specifies the increment value. Default value is 1. |
+-----------------------------------+----------------------------------------------------+
| MaxValue                          | Specifies maximum value the control allows.        |
+-----------------------------------+----------------------------------------------------+
| MinValue                          | Specifies minimum value the control allows.        |
+-----------------------------------+----------------------------------------------------+


[] 

Programmatically the limit and increment properties can be set as follows.

[] 

+------------------------------------------------------------------------------------------+
| **[\[C#\]]**                         |
|                                                                                          |
| []                      |
|                                                                                          |
| [PercentTextBox1.IncrementStep = 1;] |
|                                                                                          |
| [PercentTextBox1.MaxValue = 100;]    |
|                                                                                          |
| [PercentTextBox1.MinValue = 20;]     |
+------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                   |
|                                                                                                                                                                    |
| []                                                                                                |
|                                                                                                                                                                    |
| [Private][ PercentTextBox1.IncrementStep = 1] |
|                                                                                                                                                                    |
| [Private][ PercentTextBox1.MaxValue = 100]    |
|                                                                                                                                                                    |
| [Private][ PercentTextBox1.MinValue = 20]     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 71: Value range with Text align settings

[] 

Aligning the Value

[] 

The value can be aligned by setting the **TextAlignment** property to the required options.

[] 


+-----------------------------------+------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                    |
+-----------------------------------+------------------------------------------------------------------------------------------------+
| TextAlignment                     | Specifies the alignment for text. Default value is Right. The options included are as follows: |
|                                   |                                                                                                |
|                                   | [·      ]Left                                                     |
|                                   |                                                                                                |
|                                   | [·      ]Right                                                    |
|                                   |                                                                                                |
|                                   | [·      ]Center                                                   |
|                                   |                                                                                                |
|                                   | [·      ]Justify                                                  |
+-----------------------------------+------------------------------------------------------------------------------------------------+


[] 

Programmatically the text can be aligned as follows.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                |
|                                                                                                                                                 |
| []                                                                             |
|                                                                                                                                                 |
| [PercentTextBox1.TextAlignment = Syncfusion.Web.UI.[TextAlign].Right;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                   |
|                                                                                                                                                                                                    |
| []                                                                                                                                |
|                                                                                                                                                                                                    |
| [Private][ PercentTextBox1.TextAlignment = Syncfusion.Web.UI.TextAlign.Right] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

RightToLeft property

[] 

You can align the elements of the PercentTextBox using this property.

[] 


  ------------- ------------------------------------------------------------------------------------------------------------------------------
  Property      Description
  RightToLeft   Gets / sets a value indicating whether the elements of the control are aligned to support locales using right-to-left fonts.
  ------------- ------------------------------------------------------------------------------------------------------------------------------


[] 

+------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                 |
|                                                                                                                  |
| []                                              |
|                                                                                                                  |
| [PercentTextBox1.RightToLeft = [true];] |
+------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                           |
|                                                                                                                                                                                            |
| []                                                                                                                        |
|                                                                                                                                                                                            |
| [Private][ PercentTextBox1.RightToLeft = [True]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 72: Elements of the PercentTextBox is Aligned to Right

 

###### 5.1.2.6.2.2 Culture Settings {#culture-settings style="tab-stops: 0pt"}

[] 

Setting **CultureSource** property to **UserOverride** displays a set of properties that allows you to customize the entered values. Setting it to the **FromClient** or **FromServer**, obtains the values from client and server respectively.

[] 


+-----------------------------------+------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                      |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------+
| CultureSource                     | Specifies the source for the culture settings. Default value is FromClient. The options included are as follows: |
|                                   |                                                                                                                  |
|                                   | [·      ]*FromClient*: culture is obtained from data posted by browser              |
|                                   |                                                                                                                  |
|                                   | [·      ]*FromServer*: culture is obtained from web-server hosting page             |
|                                   |                                                                                                                  |
|                                   | [·      ]*UserOverride*: user-defined culture                                       |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------+


[] 

Globalization

[] 

**PercentSymbol** allows you to specify the symbol to use instead of the default percent symbol. **UserOvrrideCulture** allows you to set the required culture to represent the value to the specific requirement.

[] 


  --------------------- ---------------------------------------------------------------------------------------------------
  Property              Description
  PercentSymbol         Specifies the PercentSymbol for this control. The default value is English(United States).
  UserOverrideCulture   When CultureSource is set to UserOverride, culture is obtained from UserOverrideCulture property.
  --------------------- ---------------------------------------------------------------------------------------------------


[] 

Programmatically the culture settings can be coded as follows.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                             |
|                                                                                                                                              |
| []                                                                          |
|                                                                                                                                              |
| [PercentTextBox1.CultureSource = [CultureSourceType].UserOverride;] |
|                                                                                                                                              |
| [PercentTextBox1.PercentSymbol = [\" %\"];]                       |
+----------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                 |
|                                                                                                                                                                                                  |
| []                                                                                                                              |
|                                                                                                                                                                                                  |
| [Private][ PercentTextBox1.CultureSource = CultureSourceType.UserOverride]  |
|                                                                                                                                                                                                  |
| [Private][ PercentTextBox1.PercentSymbol = [\" %\"]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Customizing value format

[] 

**DecimalDigits** allows to set the number of digits to be allowed after the decimal separator and **DecimalSeparator** allows to set the separator to be used as the decimal point.

For example: Setting DecimalDigits property to \'**2\'** and DecimalSeparator property to \'**.\'**, displays the value as \'**0.28\'**.

**GroupSize** allows to set the number of digits in a group which will be separated by the **GroupSeparator** which is the character to be used as the separator of the groups.

For example: Setting GroupSize property to \'**3\'** and GroupSeparator property to \'**,\'**, displays the value as \'**4,567,234\'**.

[] 


  ------------------ --------------------------------------------------------------------------------------------------------
  Property           Description
  DecimalDigits      Specifies the number of decimal digits that will be allowed.
  DecimalSeparator   Specifies the string to be used as decimal separator. The default value is \'.\'.
  GroupSeparator     Specifies the string to be used when GroupSeparator position is specified. The default value is \',\'.
  GroupSizes         The integer to use when GroupSize is specified. The default value is 3.
  ------------------ --------------------------------------------------------------------------------------------------------


[] 

Programmatically the culture properties can be set as follows.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                 |
|                                                                                                                                                  |
| []                                                                              |
|                                                                                                                                                  |
| [PercentTextBox1.GroupSeparator = [\",\"];]                           |
|                                                                                                                                                  |
| [PercentTextBox1.GroupSizes = [new] [int]\[\]{3};] |
|                                                                                                                                                  |
| [PercentTextBox1.DecimalSeparator = [\".\"];]                         |
|                                                                                                                                                  |
| [PercentTextBox1.DecimalDigits = 2;]                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                             |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                          |
|                                                                                                                                                                                                                              |
| [Private][ PercentTextBox1.GroupSeparator = [\",\"]]                             |
|                                                                                                                                                                                                                              |
| [Private][ PercentTextBox1.GroupSizes = [New] [Integer](){3}] |
|                                                                                                                                                                                                                              |
| [Private][ PercentTextBox1.DecimalSeparator = [\".\"]]                           |
|                                                                                                                                                                                                                              |
| [Private][ PercentTextBox1.DecimalDigits = 2]                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Customizing Positive and Negative values

[] 

Positive and negative patterns in which the values should be set can be specified by the user with one of the provided options.

[] 

{border="0"}

[] 

Figure 73: Positive and Negative patterns

[] 


+-----------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                          |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------+
| NegativePattern                   | Specifies format pattern for negative percent values. This property can have one of the values:                      |
|                                   |                                                                                                                      |
|                                   |                                                                                                                      |
|                                   |                                                                                                                      |
|                                   | 
|                                   |   ------- --------                                                                                                   |
|                                   |   Value   Format                                                                                                     |
|                                   |   0       -n %                                                                                                       |
|                                   |   1       -n%                                                                                                        |
|                                   |   2        -%n                                                                                                       |
|                                   |   ------- --------                                                                                                   |
|                                   | 
|                                   |                                                                                                                      |
|                                   |                                                                                                                      |
|                                   |                                                                                                                      |
|                                   | \'%\' is the percent symbol , \'-\' is negative sign and n is a number. The default is 0, which represents \'-n %\'. |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------+
| NegativeSign                      | The string which, denotes that the associated number is negative. The default value is \'-\'.                        |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------+
| PositivePattern                   | Specifies the format Pattern for positive percent values. This property can take one of the following values:        |
|                                   |                                                                                                                      |
|                                   |                                                                                                                      |
|                                   |                                                                                                                      |
|                                   | 
|                                   |   ------- --------                                                                                                   |
|                                   |   Value   Format                                                                                                     |
|                                   |   0        n %                                                                                                       |
|                                   |   1        n%                                                                                                        |
|                                   |   2       %n                                                                                                         |
|                                   |   ------- --------                                                                                                   |
|                                   | 
|                                   |                                                                                                                      |
|                                   | []                                                                                             |
|                                   |                                                                                                                      |
|                                   | \'%\' is the percent symbol and n is a number. The default is 0.                                                     |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------+


[] 

Programmatically the positive and negative pattern and sign can be set as follows.

[] 

+----------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                     |
|                                                                                                                      |
| []                                                  |
|                                                                                                                      |
| [PercentTextBox1.PositivePattern = 1;]                           |
|                                                                                                                      |
| [PercentTextBox1.NegativePattern = 1;]                           |
|                                                                                                                      |
| [PercentTextBox1.NegativeSign = [\"-\"];] |
+----------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                     |
|                                                                                                                                                                      |
| []                                                                                                  |
|                                                                                                                                                                      |
| [Private][ PercentTextBox1.PositivePattern = 1] |
|                                                                                                                                                                      |
| [Private][ PercentTextBox1.NegativePattern = 1] |
|                                                                                                                                                                      |
| [Private][ PercentTextBox1.NegativeSign = -]    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

###### 5.1.2.6.2.3 ClientObjectID {#clientobjectid style="tab-stops: 0pt"}

[] 

The ClientObjectID can be used to access the control\'s object model on the client side.

ClientObjectID can be effectively used to refer the control\'s objects when used with MasterPages and UserControls. By default, a client object id is computed by concatenating \'\_sf\' and the control\'s **ID** property. However in the case of hosting the control in a MasterPage or UserControl, the computed client object id is very unintuitive. To make things simpler you can specify a custom value on this property and access the client side object model using that value.

[] 


  ---------------- ------------------------------------------------------------------------
  Property         Description
  ClientObjectID   Specifies the user defined id for accessing the object on client side.
  ---------------- ------------------------------------------------------------------------


[] 

Programmatically the ClientObjectID can be set as follows.

[  ]

+--------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                               |
|                                                                                                                                |
| []                                                            |
|                                                                                                                                |
| [PercentTextBox1.ClientObjectID = [\"Custom ID\"];] |
+--------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                         |
|                                                                                                                                                                                                          |
| []                                                                                                                                      |
|                                                                                                                                                                                                          |
| [Private][ PercentTextBox1.ClientObjectID = [\"Custom ID\"]] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

###### 5.1.2.6.2.4 AutoFormat Style Options {#autoformat-style-options style="tab-stops: 0pt"}

[] 

The PercentTextBox control provides pre-defined set of styles that can be applied to your control just on a click of the button. You can set the desired look and feel for the control that includes some popular styles too.

Right clicking the control and selecting the \'Auto Format\...\' option opens the following Auto Format dialog box.

[] 

{border="0"}

Figure 74

[] 

The left pane lists the various pre-defined style scheme that are available. The right pane shows the preview of the currently selected scheme. Select the required style and click OK to apply the selected scheme to the control.

[] 

Example of a popular look and feel

[] 

The following image shows the PercentTextBox with **Custom** style setting.

[] 

{border="0"}

Figure 75

 

###### 5.1.2.6.2.5 Client-Side Object Model {#client-side-object-model style="tab-stops: 0pt"}

[] 

The client side methods can be used to control the behavior of the PercentTextBox, that allows to interact with it. All the following methods are inherited from PercentTextBox client side object.

[] 


  ---------- ----------- ------------- ----------------------------------------------
  Method     Parameter   Return Type   Description
  Validate   string      bool          Verifies whether value has valid expression.
  GetText    \-          string        Get text of PercentTextBox.
  GetValue   \-          Date          Get value of PercentTextBox.
  SetValue   Date        \-            Set value of PercentTextBox.
  ---------- ----------- ------------- ----------------------------------------------


[] 

The following code example demonstrates how to change value for PercentTextBox.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<][ssw][:][PercentTextBox][ [ID][=\"PercentTextBox1\"] [ClientObjectId][=\"\_sfPercentTextBox1\"] [runat][=\"server\"/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<][input][ [type][=\"button\"] [value][=\"Set 100%\"] [onclick][=\"\_sfPercentTextBox1.SetText(\'100%\')\"] [/\>]]                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

ClientEventData object for PercentTextBox client-side events

**[]** 


  -------------- -------- -----------------------------------------------------------------------------
  Property       Type     Description
  ID             string   Specifies the client side identifier.
  Text           string   Specifies the text of textbox.
  Tooltip        string   Specifies the help message that showing when user moves mouse over control.
  Value          int      Specifies optional internal string value of this node.
  InstanceName   string   Specifies the client-side PercentTextBox object identifier.
  Instance       object   Represents PercentTextBox client-side object.
  HtmlID         string   Specifies PercentTextBox HTML-element identifier.
  Element        object   Represents PercentTextBox HTML-element.
  TextBox        object   Represents textbox HTML-element.
  Event          object   Represents event.
  -------------- -------- -----------------------------------------------------------------------------


[] 

See Also

[] 

[Client-Side Events]{.UGHyperlink}[]{.UGHyperlink}

 

 

[]{#related-topics}

