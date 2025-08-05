---
title: conceptsandfeatures9.md
original_path: WinForms_Docs/02_Concepts/conceptsandfeatures9.md
created_at: 2025-08-05
---






##### []{#p95}Concepts and Features {#concepts-and-features style="tab-stops: 0pt"}

 

 This section discusses the various features of the NumericTextBox control.

 

###### 5.1.2.5.2.1 Behavior Settings {#behavior-settings style="tab-stops: 0pt"}

[] 

Setting limits for the value

[] 

Limits can be set for the control, while entering data, by setting the minimum and maximum values, beyond which the control will not let you enter any values. To set the limits the **MinValue** and **MaxValue** properties can be used.

The values can be incremented in steps of a number, when that value is set to the **IncrementStep** property.

[] 


  --------------- ---------------------------------------------
  Property        Description
  IncrementStep   Specifies the increment value.
  MaxValue        Specifies maximum value the control allows.
  MinValue        Specifies minimum value the control allows.
  --------------- ---------------------------------------------


[] 

Programmatically the limit and increment properties can be set as follows.

[] 

+------------------------------------------------------------------------------------------+
| **[\[C#\]]**                         |
|                                                                                          |
| []                      |
|                                                                                          |
| [NumericTextBox1.IncrementStep = 1;] |
|                                                                                          |
| [NumericTextBox1.MaxValue = 100;]    |
|                                                                                          |
| [NumericTextBox1.MinValue = 20;]     |
+------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                   |
|                                                                                                                                                                    |
| []                                                                                                |
|                                                                                                                                                                    |
| [Private][ NumericTextBox1.IncrementStep = 1] |
|                                                                                                                                                                    |
| [Private][ NumericTextBox1.MaxValue = 100]    |
|                                                                                                                                                                    |
| [Private][ NumericTextBox1.MinValue = 20]     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

{border="0"}

[] 

Figure 65: Range and Align settings

[] 

Aligning the control\'s value

[] 

The value of the control inside the textbox can be aligned accordingly by setting the **TextAlignment** to the required option.

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
| [NumericTextBox1.TextAlignment = Syncfusion.Web.UI.[TextAlign].Right;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                   |
|                                                                                                                                                                                                    |
| []                                                                                                                                |
|                                                                                                                                                                                                    |
| [Private][ NumericTextBox1.TextAlignment = Syncfusion.Web.UI.TextAlign.Right] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

RightToLeft property

[] 

You can align the elements of the NumericTextBox using this property.

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
| [NumericTextBox1.RightToLeft = [true];] |
+------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                           |
|                                                                                                                                                                                            |
| []                                                                                                                        |
|                                                                                                                                                                                            |
| [Private][ NumericTextBox1.RightToLeft = [True]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

###### 5.1.2.5.2.2 Culture Settings {#culture-settings style="tab-stops: 0pt"}

[] 

Setting **CultureSource** property to **UserOverride** displays a set of properties that allows you to customize the entered values. Setting it to **FromClient** or **FromServer**, obtains the values from client and server respectively.

[] 


+-----------------------------------+--------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                  |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------+
| CultureSource                     | Specifies the source for culture settings. Default value is FromClient. The options included are as follows: |
|                                   |                                                                                                              |
|                                   | [·      ]*FromClient*: culture is obtained from data posted by browser          |
|                                   |                                                                                                              |
|                                   | [·      ]*FromServer*: culture is obtained from web-server hosting page         |
|                                   |                                                                                                              |
|                                   | [·      ]*UserOverride*: user-defined culture                                   |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------+


[] 

Globalization

[] 

**UserOvrrideCulture** allows you to set the required culture to represent the value to the specific requirement.

[] 


+-----------------------------------+----------------------------------------------------------------------------+
|                                   |                                                                            |
|                                   |                                                                            |
| Property                          | Description                                                                |
+-----------------------------------+----------------------------------------------------------------------------+
| UserOverrideCulture               | Specifies the culture to use. The default value is English(United States). |
+-----------------------------------+----------------------------------------------------------------------------+


[] 

Programmatically the culture settings can be coded as follows.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                             |
|                                                                                                                                              |
| []                                                                          |
|                                                                                                                                              |
| [NumericTextBox1.CultureSource = [CultureSourceType].UserOverride;] |
+----------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                |
|                                                                                                                                                                                                 |
| []                                                                                                                             |
|                                                                                                                                                                                                 |
| [Private][ NumericTextBox1.CultureSource = CultureSourceType.UserOverride] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Customizing value format

[] 

**DecimalDigits** allows to set the number of digits to be allowed after the decimal separator and **DecimalSeparator** allows to set the separator to be used as the decimal point.

 

For example: Setting DecimalDigits property to \'**2\'** and DecimalSeparator property to \'**.\'**, displays the value as \'**0.28\'**.

[] 


+-----------------------------------+-----------------------------------------------------------------------------------+
|                                   |                                                                                   |
|                                   |                                                                                   |
| Property                          | Description                                                                       |
+-----------------------------------+-----------------------------------------------------------------------------------+
| DecimalDigits                     | Specifies the number of decimal digits that will be allowed. Default value is 0.  |
+-----------------------------------+-----------------------------------------------------------------------------------+
| DecimalSeparator                  | Specifies the string to be used as decimal separator. The default value is \'.\'. |
+-----------------------------------+-----------------------------------------------------------------------------------+


[] 

Programmatically the culture properties can be set as follows.

[] 

+--------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                         |
|                                                                                                                          |
| []                                                      |
|                                                                                                                          |
| [NumericTextBox1.DecimalSeparator = [\".\"];] |
|                                                                                                                          |
| [NumericTextBox1.DecimalDigits = 2;]                                 |
+--------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                   |
|                                                                                                                                                                                                    |
| []                                                                                                                                |
|                                                                                                                                                                                                    |
| [Private][ NumericTextBox1.DecimalSeparator = [\".\"]] |
|                                                                                                                                                                                                    |
| [Private][ NumericTextBox1.DecimalDigits = 2]                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

**GroupSize** allows to set the number of digits in a group which will be separated by the **GroupSeparator** which is the character to be used as the separator of the groups.

For example: Setting GroupSize property to \'**3\'** and GroupSeparator property to \'**,\'** displays the value as \'**4,567,234\'**.

[] 


  ---------------- ----------------------------------------------------------------------------
  Property         Description
  GroupSeparator   Specifies the string to be used when GroupSeparator position is specified.
  GroupSizes       The integer to use when GroupSize is specified. The default value is 0.
  ---------------- ----------------------------------------------------------------------------


[] 

Programmatically the culture properties can be set as follows.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                 |
|                                                                                                                                                  |
| []                                                                              |
|                                                                                                                                                  |
| [NumericTextBox1.GroupSeparator = [\",\"];]                           |
|                                                                                                                                                  |
| [NumericTextBox1.GroupSizes = [new] [int]\[\]{3};] |
+--------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                             |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                          |
|                                                                                                                                                                                                                              |
| [Private][ NumericTextBox1.GroupSeparator = [\",\"]]                             |
|                                                                                                                                                                                                                              |
| [Private][ NumericTextBox1.GroupSizes = [New] [Integer](){3}] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Customizing Negative Values

[] 

The format in which the numeric value for negative numbers should appear inside the textbox can be set to any of the pre-defined format (given in the table below), through the **NegativePattern** property. The sign to be used for negative values can be specified using **NegativeSign**.

[] 


+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                                                                          |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| NegativePattern                   | Specifies the format pattern for negative numeric values. The default value is 1, which represents \'-n\', where n is a number. The options included are as follows: |
|                                   |                                                                                                                                                                      |
|                                   |                                                                                                                                                                      |
|                                   |                                                                                                                                                                      |
|                                   | 
|                                   |   ------- -----------------------------                                                                                                                              |
|                                   |   Value   Format                                                                                                                                                     |
|                                   |   0       \(n\)                                                                                                                                                      |
|                                   |   1       -n                                                                                                                                                         |
|                                   |   2       \- n                                                                                                                                                       |
|                                   |   3       n-                                                                                                                                                         |
|                                   |   4       [n -]                                                                                                                                |
|                                   |   ------- -----------------------------                                                                                                                              |
|                                   | 
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| NegativeSign                      | The string which denotes that the associated number is negative. The default is \'-\'.                                                                               |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

Programmatically the positive and negative pattern and sign can be set as follows.

[] 

+----------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                     |
|                                                                                                                      |
| []                                                  |
|                                                                                                                      |
| [NumericTextBox1.NegativePattern = 2;]                           |
|                                                                                                                      |
| [NumericTextBox1.NegativeSign = [\"-\"];] |
+----------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                     |
|                                                                                                                                                                      |
| []                                                                                                  |
|                                                                                                                                                                      |
| [Private][ NumericTextBox1.NegativePattern = 8] |
|                                                                                                                                                                      |
| [Private][ NumericTextBox1.NegativeSign = -]    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

###### 5.1.2.5.2.3 ClientObjectID {#clientobjectid style="tab-stops: 0pt"}

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
| [NumericTextBox1.ClientObjectID = [\"Custom ID\"];] |
+--------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                         |
|                                                                                                                                                                                                          |
| []                                                                                                                                      |
|                                                                                                                                                                                                          |
| [Private][ NumericTextBox1.ClientObjectID = [\"Custom ID\"]] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p99} 

###### 5.1.2.5.2.4 AutoFormat Style Options {#autoformat-style-options style="tab-stops: 0pt"}

[] 

The NumericTextBox control provides pre-defined set of styles that can be applied to your control just on a click of the button. You can set the desired look and feel for the control that includes some popular styles too.

Right-clicking the control and selecting the \'Auto Format\...\' option opens the following Auto Format dialog box.

[] 

{border="0"}

Figure 66

[] 

The left pane lists the various pre-defined style scheme that are available. The right pane shows the preview of the currently selected scheme. Select the required style, and click **OK** to apply the selected scheme to the control.

[] 

Example of a popular look and feel

[] 

The following image shows the NumericTextBox with **MSDN** style setting.

[] 

{border="0"}

 

Figure 67

###### 5.1.2.5.2.5 Client-Side Object Model {#client-side-object-model style="tab-stops: 0pt"}

[] 

The client side methods can be used to control the behavior of the NumericTextBox, that allows to interact with it. The various client side methods supported by NumericTextBox are as follows.

[] 


  ---------- ----------- ------------- ----------------------------------------------
  Method     Parameter   Return Type   Description
  Validate   string      bool          Verifies whether value has valid expression.
  GetText    \-          string        Get text of NumericTextBox.
  SetText    string      \-            Set text of NumericTextBox.
  GetValue   \-          Date          Get value of NumericTextBox.
  SetValue   Date        \-            Set value of NumericTextBox.
  ---------- ----------- ------------- ----------------------------------------------


[] 

The following code example demonstrates how to change the value for NumericTextBox.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<][ssw][:][NumericTextBox][ [ID][=\"NumericTextBox1\"] [ClientObjectId][=\"\_sfNumericTextBox1\"] [runat][=\"server\"] [ShowButtons][=\"false\"/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<][input][ [type][=\"button\"] [value][=\"+1\"] [onclick][=\"Add(1)\"] [/\>]]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<][input][ [class][=\"Btn\"] [type][=\"button\"] [value][=\"-1\"] [onclick][=\"Add(-1)\"] [/\>]]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **[\[javascript\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [function][ Add( nDelta )]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [    ][var][ nVal = **\_sfNumericTextBox1.GetValue()**;]                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [    nVal += nDelta;]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [    ]**[\_sfNumericTextBox1.SetValue]**[(nVal);]                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [}]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

ClientEventData object for NumericTextBox client-side events

**[]** 


+-----------------------+-----------------------+-----------------------------------------------------------------------------+
|                       |                       |                                                                             |
|                       |                       |                                                                             |
| Property              | Type                  | Description                                                                 |
+-----------------------+-----------------------+-----------------------------------------------------------------------------+
| ID                    | string                | Specifies the client side identifier.                                       |
+-----------------------+-----------------------+-----------------------------------------------------------------------------+
| Text                  | string                | Specifies the text of textbox.                                              |
+-----------------------+-----------------------+-----------------------------------------------------------------------------+
| Tooltip               | string                | Specifies the help message that showing when user moves mouse over control. |
+-----------------------+-----------------------+-----------------------------------------------------------------------------+
| Value                 | Date                  | Specifies optional internal string value of this node.                      |
+-----------------------+-----------------------+-----------------------------------------------------------------------------+
| InstanceName          | string                | Specifies the client-side NumericTextBox object identifier.                 |
+-----------------------+-----------------------+-----------------------------------------------------------------------------+
| Instance              | object                | Represents NumericTextBox client-side object.                               |
+-----------------------+-----------------------+-----------------------------------------------------------------------------+
| HtmlID                | string                | Specifies NumericTextBox HTML-element identifier.                           |
+-----------------------+-----------------------+-----------------------------------------------------------------------------+
| Element               | object                | Represents NumericTextBox HTML-element.                                     |
+-----------------------+-----------------------+-----------------------------------------------------------------------------+
| TextBox               | object                | Represents textbox HTML-element.                                            |
+-----------------------+-----------------------+-----------------------------------------------------------------------------+
| Event                 | object                | Represents event.                                                           |
+-----------------------+-----------------------+-----------------------------------------------------------------------------+


[] 

See Also

[] 

[Client-Side Events]{.UGHyperlink}[]{.UGHyperlink}

 

[]{#related-topics}

