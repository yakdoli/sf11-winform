---
title: textfield.md
original_path: WinForms_Docs/99_Uncategorized/textfield.md
created_at: 2025-08-05
---






##### Text Field {#text-field style="tab-stops: 0pt"}

The text field of a CurrencyTextBox control can be customized using the properties available. The below image illustrates the various sections of the control.[]

[] 

{border="0"}

[] 

Figure 501: TextField of CurrencyTextBox

 

###### 3.3.8.6.4.1 Text {#text style="tab-stops: 0pt"}

The default text in the CurrencyTextBox can be edited through **Text** property. Default value is \$2.00. The text can be aligned to Left, Right or Center using **TextAlign** property.[]

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                         |
| [this][.currencyTextBox2.Text = ][\"\$25.00\"][;][]                                       |
|                                                                                                                                                                                                                                                                                                                         |
| [this][.currencyTextBox1.TextAlign = System.Windows.Forms.][HorizontalAlignment][.Right;][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                                 |
|                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                            |
| [Me][.currencyTextBox2.Text = ][\"\$25.00\"][] |
|                                                                                                                                                                                                                            |
| [Me][.currencyTextBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Right][]              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 502: Text = \"\$2500\"

[] 

Multiline Feature[]

[] 

The CurrencyTextBox control can be made multiline by setting **Multiline **property to true. Using the below properties we can control the behavior of control. []

[       ][]


+----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| CurrencyTextBox Properties[] | Description[]                                                                                                                  |
+----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Lines[]                      | This property can hold an array of string values when multiline feature is enabled.[]                                          |
+----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| WordWrap[]                   | Setting this property to true, will automatically wrap the digits if the textbox is resized.[]                                 |
+----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| ScrollBar[]                  | We can show scrollbars for the control when multiline feature is enabled. The different options are,[]                         |
|                                                    |                                                                                                                                                      |
|                                                    | []                                                                                                                             |
|                                                    |                                                                                                                                                      |
|                                                    | Horizontal - Displays horizontal scrollbar,[]                                                                                  |
|                                                    |                                                                                                                                                      |
|                                                    | Vertical - Displays vertical scrollbar,[]                                                                                      |
|                                                    |                                                                                                                                                      |
|                                                    | Both - Enables horizontal scrollbar, when WordWrap = false  and enables vertical scrollbar when WordWrap is set to true, and[] |
|                                                    |                                                                                                                                                      |
|                                                    | None.[]                                                                                                                        |
+----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                |
| [this][.currencyTextBox1.Multiline = ][true][;][]                                  |
|                                                                                                                                                                                                                                                                                                                |
| [this][.currencyTextBox2.Text = ][\"\$12,456,456,456,456,456,456,456.00\"][;][]  |
|                                                                                                                                                                                                                                                                                                                |
| [this][.currencyTextBox2.WordWrap = \"][true][\"][]                                |
|                                                                                                                                                                                                                                                                                                                |
| [this][.currencyTextBox1.ScrollBars = System.Windows.Forms.][ScrollBars][.Both;][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                                                             |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                        |
| [Me][.currencyTextBox1.Multiline = ][True][]                                 |
|                                                                                                                                                                                                                                                        |
| [Me][.currencyTextBox2.Text = ][\"\$12,456,456,456,456,456,456,456.00\"][] |
|                                                                                                                                                                                                                                                        |
| [Me][.currencyTextBox2.WordWrap = ][True][]                                  |
|                                                                                                                                                                                                                                                        |
| [Me][.currencyTextBox1.ScrollBars = System.Windows.Forms.ScrollBars.Both][]                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 503: Multiline = \"True\"

[] 

{border="0"}[]

[] 

Figure 504: CurrencyTextBox Being Resized at Run Time, When WordWrap = \"True\"[]

[] 

{border="0"}

 

Figure 505: CurrencyTextBox Control with Horizontal and Vertical Scrollbars

[] 

Password Character[]

[] 

We can display password characters instead of the digits in the text field using **PasswordChar** property. To use the system password character in the text field, set **UseSystemPasswordChar** property to true.[]

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                            |
| [this][.currencyTextBox1.UseSystemPasswordChar = ][false][;][] |
|                                                                                                                                                                                                                                                                                            |
| [this][.currencyTextBox1.PasswordChar = ][\'\*\'][;][]       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                                          |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                     |
| [Me][.currencyTextBox1.UseSystemPasswordChar = ][False][] |
|                                                                                                                                                                                                                                     |
| [Me][.currencyTextBox1.PasswordChar = ][\'\*\'][]       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 506: PasswordChar = \'\*\'

[] 

Banner Text Support[]

[] 

We can set banner text for the CurrencyTextBox control. Refer [[BannerTextProvider Component]](http://help.syncfusion.com/ug_82/WindowsFormsUI_Tools/BannerText.html) topic for more details.[]

We need to do the below settings to make Banner text feature available for the control.[]

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                               |
| [this][.currencyTextBox1.AllowNull = ][true][;][] |
|                                                                                                                                                                                                                                                                               |
| [this][.currencyTextBox1.NullString = \"\";][]                                                                                                       |
|                                                                                                                                                                                                                                                                               |
| [this][.currencyTextBox1.Text = \"\";][]                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                             |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                        |
| [Me][.currencyTextBox1.AllowNull = ][True][] |
|                                                                                                                                                                                                                        |
| [Me][.currencyTextBox1.NullString = \"\"][]                                                   |
|                                                                                                                                                                                                                        |
| [Me][.currencyTextBox1.Text = \"\"][]                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 507: Banner Text set for CurrencyTextBox[]

 

###### 3.3.8.6.4.2 [[Number and Decimal Digits]](http://help.syncfusion.com/ug_82/WindowsFormsUI_Tools/DecimalSettings.html) {#number-and-decimal-digits style="tab-stops: 0pt"}

The CurrencyTextBox text field has a number part and a decimal part. The properties which controls appearance and behavior of the text field are discussed in this section.[]

[] 

Number part[]

[] 

The below properties lets you decide the formatting of the number part of CurrencyTextBox control.[]

[] 


  ---------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  CurrencyTextBox Properties[]   Description[]
  CurrencyNumberDigits[]         Specifies the number of digits for the number part. This is not part of the globalization structure. The default value is 27.[]
  CurrencyPositivePattern[]      This property specifies the pattern to use when the value is positive.[]
  CurrencyNegativePattern[]      This property specifies the pattern to use when the value is negative. For example, set CurrencyNegativePattern to be 2 or 3 and then hit -ve symbol, you will know the change of display.[]
  ---------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                            |
|                                                                                                                                                                                   |
| []                                                                                                                                                          |
|                                                                                                                                                                                   |
| [this][.currencyTextBox1.NumberDigits = 10;][]           |
|                                                                                                                                                                                   |
| [this][.currencyTextBox1.CurrencyPositivePattern = 1;][] |
|                                                                                                                                                                                   |
| [this][.currencyTextBox1.CurrencyNegativePattern = 2;][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                     |
|                                                                                                                                                                                |
| []                                                                                                                                                       |
|                                                                                                                                                                                |
| [Me][.currencyTextBox1.NumberDigits = 10][]           |
|                                                                                                                                                                                |
| [Me][.currencyTextBox1.CurrencyPositivePattern = 1][] |
|                                                                                                                                                                                |
| [Me][.currencyTextBox1.CurrencyNegativePattern = 2][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Decimal Part[]

[] 

The below properties lets you decide the formatting of the CurrencyTextBox control\'s number part.[]

[] 


  ---------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  CurrencyTextBox Properties[]   Description[]
  CurrencyDecimalDigits[]        Gets or sets the maximum number of digits for the decimal portion of the currency. The default value is 2.[]
  CurrencyDecimalSeparator[]     Gets or sets the decimal separator character that will be used for the display. The default decimal character \'.\' can be overridden by other special characters that can be specified by this property**.**[]
  CurrencyGroupSeparator[]       Gets or sets the separator used for grouping the digits.[]
  CurrencyGroupSizes[]           Gets or sets the grouping of CurrencyDigits in the CurrencyTextBox.[]
  DecimalValue[]                 Specifies the decimal value of the control. **Decimal values** can be entered in the CurrencyTextBox by clicking inside the decimal part of the text and then typing. Alternatively, the decimal character can be entered by clicking on the decimal character on the keyboard first and the cursor will move to the decimal part of the text. The decimal part is truncated based on the number of characters allowed.[]
  RemoveDecimalZeros[]           Specifies whether to remove last decimal zeros in the currency value.[]
  ---------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


[] 

{border="0"}[]

 

Figure 508: Specifying the GroupSize Through CurrencyGroupSizes Property

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                   |
| [this][.currencyTextBox1.CurrencyDecimalDigits = 3;][]                                                                                                                   |
|                                                                                                                                                                                                                                                                                                   |
| [this][.currencyTextBox1.CurrencyDecimalSeparator = \".\";][]                                                                                                            |
|                                                                                                                                                                                                                                                                                                   |
| [this][.currencyTextBox1.CurrencyGroupSeparator = \",\";][]                                                                                                              |
|                                                                                                                                                                                                                                                                                                   |
| [this][.currencyTextBox1.CurrencyGroupSizes = ][new][ int\[\] {3};][] |
|                                                                                                                                                                                                                                                                                                   |
| [this][.currencyTextBox1.RemoveDecimalZeros = ][true][;][]            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Me][.currencyTextBox1.CurrencyDecimalDigits = 3][]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Me][.currencyTextBox1.CurrencyDecimalSeparator = ][\".\"][]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Me][.currencyTextBox1.CurrencyGroupSeparator = ][\",\"][]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Me][.currencyTextBox1.CurrencyGroupSizes = ][New][ ][Integer][() {3}][] |
|                                                                                                                                                                                                                                                                                                                                                                                                         |
| [Me][.currencyTextBox1.RemoveDecimalZeros = ][True][]                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 509: CurrencyDecimalDigits = \"3\"; Separator = \".\"; GroupSeparator = \",\"; GroupSizes = \"3\"[]

[] 

{border="0"}

Figure 510: RemoveDecimalZeros = \"True\"

 

###### 3.3.8.6.4.3 [[Negative Part]](http://help.syncfusion.com/ug_82/WindowsFormsUI_Tools/NegativePart.html) {#negative-part style="tab-stops: 0pt"}

The default negative sign \'-\' can be changed by **NegativeSign** property to any other special characters. We can specify the behavior of the Currency TextBox by **NegativeInputPendingOnSelectAll** when its content is fully selected and negative key is pressed by the user. when NegativeInputPendingOnSelectAll set to \'True\', the current value is not changed. The next key stroke is taken to a new value and the entire content of the TextBox is replaced by the negative value of the key stroke entered.[]

[] 

For example, if the current value of the TextBox is 1.00 with all the text being selected and when the user presses the negative key followed by key 5, the value will be  \'-5\'.[]

[] 

When it is set to false, the current value is changed to negative value immediately. For example, if the current value of the TextBox is 1.00 awith all the text being selected and when the user presses the negative key, the value is \'-1\'.[]

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                     |
| [this][.currencyTextBox1.NegativeSign = \"-\";][]                                                                                                                          |
|                                                                                                                                                                                                                                                                                                     |
| [this][.currencyTextBox1.NegativeInputPendingOnSelectAll = ][true][;][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                                                   |
|                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                              |
| [Me][.currencyTextBox1.NegativeSign = ][\"-\"][]                 |
|                                                                                                                                                                                                                                              |
| [Me][.currencyTextBox1.NegativeInputPendingOnSelectAll = ][True][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

###### 3.3.8.6.4.4 [[Values]](http://help.syncfusion.com/ug_82/WindowsFormsUI_Tools/Values1.html) {#values style="tab-stops: 0pt"}

The maximum and minimum value of the currency can be specified by MaxValue and MinValue properties.[]

[] 


  ------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------
  CurrencyTextBox Properties[]      Description[]
  MaxValue[]                        It sets the maximum value to the currency TextBox. The default value is 79228162514264337593543950335.[]
  MinValue[]                        It sets the minimum value to the currency TextBox. The default value is 79228162514264337593543950335.[]
  EnforceMinMaxDuringValidating[]   If the minimum and maximum values are not met, the validating event will be handled and cancelled if this property is set to true.[]
  ------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                  |
| [this][.currencyTextBox1.MaxValue=10;][]                                                                                                                                |
|                                                                                                                                                                                                                                                                                                  |
| [this][.currencyTextBox1.MinValue=0;][]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                  |
| [this][.currencyTextBox1.EnforceMinMaxDuringValidating= ][true][;][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                 |
| [Me][.currencyTextBox1.MaxValue=10][]                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                 |
| [Me][.currencyTextBox1.MinValue=0][]                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                 |
| [Me][.currencyTextBox1.EnforceMinMaxDuringValidating = ][True][;][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Null String[]

[] 

If you want to display null string instead of actual [[decimal]](http://help.syncfusion.com/ug_82/WindowsFormsUI_Tools/DecimalSettings.html) values, you can set **NullString **property to any values. To display the null string set** AllowNull **to true.[]

[] 


  ---------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------
  CurrencyTextBox Properties[]   Description[]
  NullString[]                   Sets the Null string to be displayed when the decimal value is zero.[]
  AllowNull[]                    Specifies if the NullString will be used when the value is Null.**NullString** must be set to true.[]
  ---------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                      |
| [this][.currencyTextBox1.NullString = ][\"NULL\"][;][] |
|                                                                                                                                                                                                                                                                                      |
| [this][.currencyTextBox1.AllowNull = ][true][;][]        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                                    |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                               |
| [Me][.currencyTextBox1.NullString = ][\"NULL\"][] |
|                                                                                                                                                                                                                               |
| [Me][.currencyTextBox1.AllowNull = ][True][]        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 511: NullString = \"NULL\"

 

###### 3.3.8.6.4.5 [[Currency Symbol]](http://help.syncfusion.com/ug_82/WindowsFormsUI_Tools/CurrencySymbol.html) {#currency-symbol style="tab-stops: 0pt"}

The currency symbol that will be used for formatting the display is specified by setting **CurrencySymbol** to any special characters.[]

[] 


  -------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------
  CurrencyTextBox Property[]   Description[]
  CurrencySymbol[]             This property specifies the currency symbol to be used in the CurrencyTextBox. The default value is \'\$\'.[]
  -------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                       |
|                                                                                                                                                                              |
| []                                                                                                                                                     |
|                                                                                                                                                                              |
| [this][.currencyTextBox1.CurrencySymbol = \"#\";][] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                                     |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                |
| [Me][.currencyTextBox1.CurrencySymbol = ][\"#\"][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

