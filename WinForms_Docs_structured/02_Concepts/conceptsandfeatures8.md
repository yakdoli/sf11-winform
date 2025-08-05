---
title: "] [PassivePromptCharacter][=\"\_\"/\>]] |
original_path: WinForms_Docs/02_Concepts/conceptsandfeatures8.md
created_at: 2025-08-05
---






##### Concepts and Features {#concepts-and-features style="tab-stops: 0pt"}

 

 This section discusses the various features of the MaskedEditTextBox control.

 

###### 5.1.2.4.2.1 Mask Input and Mask Characters {#mask-input-and-mask-characters style="tab-stops: 0pt"}

[] 

MaskedEditControl allows you to set the values, by specifying the type and format of the input mask to be entered and also the number of place holders.

The format in which the values should be entered in the textbox can be set using the **Mask** property.

[] 


  ---------- ------------------------------------------------------
  Property   Description
  Mask       Specifies the mask string for the MaskedEditTextBox.
  ---------- ------------------------------------------------------


[] 

+-------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                              |
|                                                                                                                               |
| []                                                           |
|                                                                                                                               |
| [maskededittextbox1.Mask=[\"(\>???)###(\<???)\"];] |
+-------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                        |
|                                                                                                                                                                                                         |
| []                                                                                                                                     |
|                                                                                                                                                                                                         |
| [Private][ maskededittextbox1.Mask=[\"(\>???)###(\<???)\"]] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

While defining the input mask, each character position in the MaskedEditTextBox control maps to either a placeholder of a specified type or a literal character. Literal characters, or literals can give visual cues about the type of data being used. For example: (919), the parentheses surrounding the area code of a telephone number are literals.

The MaskedEditTextBox control supports the following masks.

[] 


  ---------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Mask Character   Description
  \#               Digit placeholder.
  ?                Letter placeholder. For example: a - z or A - Z.
  \>               Convert all the characters that follows to uppercase.
  \<               Convert all the characters that follows to lowercase.
  .                Decimal placeholder. The actual character used is specified as the decimal placeholder in your international settings. This character is treated as a literal for masking purpose.
  ,                Thousands separator. The actual character used is specified as the thousands separator in your international settings. This character is treated as a literal for masking purpose.
  :                Time separator. The actual character used is specified as the time separator in your international settings. This character is treated as a literal for masking purposes.
  /                Date separator. The actual character used is specified as the date separator in your international settings. This character is treated as a literal for masking purpose.
  A                Alphanumeric character placeholder (Entry required). For example: a - z, A - Z, or 0 - 9.
  a                Alphanumeric character placeholder (entry optional).
  9                Digit placeholder (entry optional). For example: 0 - 9.
  C                Character or space placeholder (entry optional). This operates exactly like the \"&\" placeholder and ensures compatibility with Microsoft Access.
  Literal          All other symbols are displayed as literals, i.e, as themselves.
  ---------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


[] 


[{border="0"}]Note: The mask characters \'\>/\<\' will have effect only when CharacterCasing property is set to Normal.


 

###### 5.1.2.4.2.2 Behavior Settings {#behavior-settings style="tab-stops: 0pt"}

[] 

Input appearance settings

[] 

The character casing of the input value can be handled by setting the **CharacterCasing** property. The **UsageMode** property allows you to set the control to accept either only numeric values or alphabets and numeric values as input.

[] 


+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| CharacterCasing                   | Specifies the casing of the input characters. The default option is Normal. The options included are as follows:                                      |
|                                   |                                                                                                                                                       |
|                                   | [·      ]Normal                                                                                                          |
|                                   |                                                                                                                                                       |
|                                   | [·      ]Upper                                                                                                           |
|                                   |                                                                                                                                                       |
|                                   | [·      ]Lower                                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| UsageMode                         | Specifies whether the control should allow only numeric input or numeric and alphabets. Default value is Normal. The options included are as follows: |
|                                   |                                                                                                                                                       |
|                                   | [·      ]Normal                                                                                                          |
|                                   |                                                                                                                                                       |
|                                   | [·      ]Numeric                                                                                                         |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

[] 

Initially before the focus is set on the control, the mask characters can be replaced or represented with any symbol by setting it to the **PassivePromptCharacter**.

 

When focus is on the control, the mask characters can be represented by the symbol set to the **PromptCharacter**. Default prompt character is \'\_\'. By handling the **AllowPrompt** property, you can either allow or deny using the prompt character as an input.

 

After the values are entered, if all the placeholders are not filled with any characters, then it can be represented using the **PaddingCharacter**.

[] 


  ------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------
  Property                 Description
  AllowPrompt              Specifies if the prompt character could be entered as an input character.
  PaddingCharacter         Specifies the character that will be used instead of a mask character when the mask position has not been filled while using text property.
  PassivePromptCharacter   It will serve as a placeholder for mask characters when control does not have the focus.
  PromptCharacter          Specifies the character to be used instead of mask characters when mask position has not been filled.
  ------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------


[] 

+---------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                      |
|                                                                                                                                       |
| []                                                                  |
|                                                                                                                                       |
| [maskededittextbox1.AllowPrompt = [false];]                  |
|                                                                                                                                       |
| [maskededittextbox1.Mask= \"\>?\<????????????\";]                                 |
|                                                                                                                                       |
| [maskededittextbox1.ClipMode = ClipModes.IncludeLiterals;                       ] |
|                                                                                                                                       |
| [maskededittextbox1.PassivePromptCharacter = \'\_\';]                             |
+---------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                               |
|                                                                                                                                                                                                |
| []                                                                                                                            |
|                                                                                                                                                                                                |
| [Private ][maskededittextbox1.AllowPrompt = [False]] |
|                                                                                                                                                                                                |
| [Private ][maskededittextbox1.Mask= \"\>?\<????????????\"]                |
|                                                                                                                                                                                                |
| [Private ][maskededittextbox1.ClipMode = ClipModes.IncludeLiterals]       |
|                                                                                                                                                                                                |
| [Private ][maskededittextbox1.PassivePromptCharacter = \"\_\"c]           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[    ]

Aligning Control Value

[] 

The value of the calendar control inside the textbox can be aligned accordingly by setting the **TextAlignment** to the required option.

 


+-----------------------------------+----------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                        |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| TextAlignment                     | Specifies the alignment of the value. Default value is Right. The options included are as follows: |
|                                   |                                                                                                    |
|                                   | [·      ]Left                                                         |
|                                   |                                                                                                    |
|                                   | [·      ]Right                                                        |
|                                   |                                                                                                    |
|                                   | [·      ]Center                                                       |
|                                   |                                                                                                    |
|                                   | [·      ]Justify                                                      |
+-----------------------------------+----------------------------------------------------------------------------------------------------+


[] 

Programmatically the text can be aligned as follows.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                   |
|                                                                                                                                                    |
| []                                                                                |
|                                                                                                                                                    |
| [MaskedEditTextBox1.TextAlignment = Syncfusion.Web.UI.[TextAlign].Right;] |
+----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                      |
|                                                                                                                                                                                                       |
| []                                                                                                                                   |
|                                                                                                                                                                                                       |
| [Private][ MaskedEditTextBox1.TextAlignment = Syncfusion.Web.UI.TextAlign.Right] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

RightToLeft property

[] 

You can align the elements of the MaskedEditTextBox using this property.

[] 


  ------------- ------------------------------------------------------------------------------------------------------------------------------
  Property      Description
  RightToLeft   Gets / sets a value indicating whether the elements of the control are aligned to support locales using right-to-left fonts.
  ------------- ------------------------------------------------------------------------------------------------------------------------------


[] 

+---------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                    |
|                                                                                                                     |
| []                                                 |
|                                                                                                                     |
| [MaskedEditTextBox1.RightToLeft = [true];] |
+---------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                              |
|                                                                                                                                                                                               |
| []                                                                                                                           |
|                                                                                                                                                                                               |
| [Private][ MaskedEditTextBox1.RightToLeft = [True]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 61: Elements of the MaskedEditTextBox is Aligned to Right

 

###### 5.1.2.4.2.3 Culture Settings {#culture-settings style="tab-stops: 0pt"}

[] 

The culture information can be obtained either from the data posted by the browser (By setting the FromClient option) else from the web-server hosting page (By setting the FromServer option) or the user can define the culture settings.

 

The drop down calendar control allows you to override the default culture information (Decimal/Thousand Separator, Date/Time Separator properties) when the **CultureSource** property is set to **UserOverride**.

[] 


+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Property                          | Description                                                                                                                                       |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| CultureSource                     | Specifies the current culture for the control. The values included are as follows:                                                                |
|                                   |                                                                                                                                                   |
|                                   | [·      ]*FromClient*:*[ ]*culture is obtained from the data posted by browser |
|                                   |                                                                                                                                                   |
|                                   | [·      ]*FromServer*: culture is obtained from web-server hosting page                                              |
|                                   |                                                                                                                                                   |
|                                   | [·      ]*UserOverride*: user-defined culture                                                                        |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

Globalization

[] 

**UserOvrrideCulture** allows you to set the required culture to represent the value to the specific requirement whose default value is **English(United States)**.

[] 


  --------------------- -------------------------------------------
  Property              Description
  UserOverrideCulture   Specifies the various cultures supported.
  --------------------- -------------------------------------------


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                |
|                                                                                                                                                 |
| []                                                                             |
|                                                                                                                                                 |
| [MaskedEditTextBox1.CultureSource = [CultureSourceType].UserOverride;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                   |
|                                                                                                                                                                                                    |
| []                                                                                                                                |
|                                                                                                                                                                                                    |
| [Private][ MaskedEditTextBox1.CultureSource = CultureSourceType.UserOverride] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Designators and Separators for time and date

[] 

The separators for the date and time can be customized using the **DateSeparator** and **TimeSeparator** properties.

[] 


  --------------- ------------------------------------------------------------------
  Property        Description
  DateSeparator   Specifies the separator to use for date. Default value is \'/\'.
  TimeSeparator   Specifies the separator to use for time. Default value is \':\'.
  --------------- ------------------------------------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                         |
|                                                                                                                          |
| []                                                      |
|                                                                                                                          |
| [MaskedEditTextBox1.DateSeparator = [\"-\"];] |
|                                                                                                                          |
| [MaskedEditTextBox1.TimeSeparator=[\".\"];]   |
+--------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                    |
|                                                                                                                                                                                                     |
| []                                                                                                                                 |
|                                                                                                                                                                                                     |
| [Private][ MaskedEditTextBox1.DateSeparator = [\"-\"];] |
|                                                                                                                                                                                                     |
| [Private][ MaskedEditTextBox1.TimeSeparator=[\".\"]]    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

###### 5.1.2.4.2.4 ClientObjectID {#clientobjectid style="tab-stops: 0pt"}

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

+-----------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                  |
|                                                                                                                                   |
| []                                                               |
|                                                                                                                                   |
| [MaskedEditTextBox1.ClientObjectID = [\"Custom ID\"];] |
+-----------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                            |
|                                                                                                                                                                                                             |
| []                                                                                                                                         |
|                                                                                                                                                                                                             |
| [Private][ MaskedEditTextBox1.ClientObjectID = [\"Custom ID\"]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

###### 5.1.2.4.2.5 Client-Side Object Model {#client-side-object-model style="tab-stops: 0pt"}

[] 

The client side methods can be used to control the behavior of the MaskedEditTextBox, that allows to interact with it. All the following methods of MaskedEditTextBox client side object are as follows.

[] 


  ---------- ----------- ------------- --------------------------------------------
  Method     Parameter   Return Type   Description
  GetText    \-          string        Get text of MaskedEditTextBox.
  Validate   string      \-            Verify whether value has valid expression.
  GetValue   \-          Date          Get value of MaskedEditTextBox.
  SetValue   Date        \-            Set value of DropDownCalendarControl.
  ---------- ----------- ------------- --------------------------------------------


[] 

The following code example demonstrates how to reset value for MaskedEditTextBox in client side.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<][ssw][:][MaskedEditTextBox][ [ID][=\"MaskedEditTextBox1\"] [ClientObjectId][=\"\_sfMask\"] [runat][=\"server\"] [Mask][=\"8-(###)-###-##-##\"] [PassivePromptCharacter][=\"\_\"/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][input][ [type][=\"button\"] [value][=\"Reset\"] [onclick][=\"\_sfMask.**SetValue**(\'8-(\_\_\_)-\_\_\_-\_\_-\_\_\')\"] [/\>]]                                                                                                                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

ClientEventData object for MaskedEditTextBox client side events

**[]** 


  -------------- -------- -----------------------------------------------------------------------------
  Property       Type     Description
  ID             string   Specifies the client side identifier.
  Text           string   Specifies the text of textbox.
  Tooltip        string   Specifies the help message that showing when user moves mouse over control.
  Value          Date     Specifies optional internal string value of this node.
  InstanceName   string   Specifies the client-side MaskedEditTextBox object identifier.
  Instance       object   Represents MaskedEditTextBox client-side object.
  HtmlID         string   Specifies MaskedEditTextBox HTML-element identifier.
  Element        object   Represents MaskedEditTextBox HTML-element.
  TextBox        object   Represents textbox HTML-element.
  Event          object   Represents event.
  -------------- -------- -----------------------------------------------------------------------------


[] 

See Also

[] 

[Client-Side Events]{.UGHyperlink}[]{.UGHyperlink}

 

[]{#related-topics}

