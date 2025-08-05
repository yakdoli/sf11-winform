---
title: conceptsandfeatures123.md
original_path: WinForms_Docs/02_Concepts/conceptsandfeatures123.md
created_at: 2025-08-05
---






##### Concepts and Features {#concepts-and-features style="tab-stops: 0pt"}

[] 

The following topics will help you become more familiar in using the ComboBoxAdv control.

[] 

###### []{#p389}[]{#_ComboBoxAdv}3.3.5.2.3.1 ComboBoxAdv {#comboboxadv style="tab-stops: 0pt"}

 

ComboBoxAdv control has a textbox which is the edit portion of the control and a dropdown. This section will discuss these components in detail in the below topics.

[] 

[]{#_TextBox}3.3.5.2.3.1.1      TextBox[]{#p390}

ComboBoxAdv control has properties which changes the appearance and behavior of the textbox or the edit portion of the control.

[] 

Text Appearance

[] 

The below properties customizes the text in the ComboBoxAdv control.

[] 


  -------------------------------- ---------------------------------------------------------------------------------------
  ComboBoxAdv TextBox Properties   Description
  Text                             Sets text for the textbox. The text can set to null to clear the text in the textbox.
  TextAlign                        Sets the alignment of the text in the textbox.
  ForeColor                        Sets the fore color for the text entered in the edit portion of the control.
  -------------------------------- ---------------------------------------------------------------------------------------


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                   |
|                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                         |
|                                                                                                                                                                                                                                  |
| [this][.comboBoxAdv1.TextBox.Text[ ]=[ ][\"Simple text in ComboBoxAdv\"];] |
|                                                                                                                                                                                                                                  |
| [this][.comboBoxAdv1.TextBox.TextAlign[ ]= HorizontalAlignment.Center;]                                                |
|                                                                                                                                                                                                                                  |
| [this][.comboBoxAdv1.TextBox.ForeColor[ ]= [Color].Red;]                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                              |
|                                                                                                                                                                                 |
| []                                                                                                                             |
|                                                                                                                                                                                 |
| [Me][.comboBoxAdv1.TextBox.Text = [\"Simple text in ComboBoxAdv\"]] |
|                                                                                                                                                                                 |
| [Me][.comboBoxAdv1.TextBox.TextAlign = HorizontalAlignment.Center]                         |
|                                                                                                                                                                                 |
| [Me][.comboBoxAdv1.TextBox.ForeColor = [Color].Red]                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Text Selection

[] 

The selection of text during run time can be controlled through below properties.

[] 


  -------------------------------- ----------------------------------------------------
  ComboBoxAdv TextBox Properties   Description
  SelectedText                     Sets the currently selected text at runtime.
  SelectionLength                  Sets the number of characters selected in textbox.
  SelectionStart                   Sets the starting point of the text selection.
  -------------------------------- ----------------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                        |
|                                                                                                                                                                       |
| **[]**                                                                                                              |
|                                                                                                                                                                       |
| [this.][comboBoxAdv1.TextBox.SelectedText = [\"Combo\"];] |
|                                                                                                                                                                       |
| [this.][comboBoxAdv1.TextBox.SelectionLength = 5;]                               |
|                                                                                                                                                                       |
| [this.][comboBoxAdv1.TextBox.SelectionStart = 2;]                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                 |
|                                                                                                                                                                    |
| []                                                                                                               |
|                                                                                                                                                                    |
| [Me][.comboBoxAdv1.TextBox.SelectedText = [\"Combo\"]] |
|                                                                                                                                                                    |
| [Me][.comboBoxAdv1.TextBox.SelectionLength = 5]                               |
|                                                                                                                                                                    |
| [Me][.comboBoxAdv1.TextBox.SelectionStart = 2]                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

ReadOnly Settings

[] 

The below properties deals with read-only settings for the ComboBoxAdv control.

[] 


+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ComboBoxAdv TextBox Properties    | Description                                                                                                                                                           |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ReadOnly                          | Specifies whether the control can be made read only. By default it is set to false.                                                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| DropDownStyle                     | Specifies the dropdown style of the ComboBoxAdv control. Based on its below options, it specifies whether the text in the control is editable or not. The styles are, |
|                                   |                                                                                                                                                                       |
|                                   |                                                                                                                                                                       |
|                                   |                                                                                                                                                                       |
|                                   | Simple - The text portion is editable. The list portion is always visible.                                                                                            |
|                                   |                                                                                                                                                                       |
|                                   | DropDown (default style) - The text portion is editable. Clicking the arrow button will display the list portion.                                                     |
|                                   |                                                                                                                                                                       |
|                                   | DropDownList - The text portion is not editable. Clicking the arrow button will display the list portion.                                                             |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                               |
|                                                                                                                                                                                              |
| **[]**                                                                                                                                     |
|                                                                                                                                                                                              |
| [this][.comboBoxAdv1.ReadOnly = [true];]                                           |
|                                                                                                                                                                                              |
| [this][.comboBoxAdv1.DropDownStyle = System.Windows.Forms.[ComboBoxStyle].Simple;] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                         |
|                                                                                                                                                                                            |
| []                                                                                                                                       |
|                                                                                                                                                                                            |
| [Me][.comboBoxAdv1.ReadOnly = [True]]                                            |
|                                                                                                                                                                                            |
| [Me][.comboBoxAdv1.DropDownStyle = System.Windows.Forms.[ComboBoxStyle.]Simple] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Behavior Settings

[] 

The below properties controls the behavior of the text typed in the Textbox.

[] 


+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ComboBoxAdv Properties            | Description                                                                                                                                                                                 |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| NumberOnly                        | Specifies whether the user should be allowed to enter only numbers in the edit portion of the ComboBoxAdv.                                                                                  |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| CharacterCasing                   | Specifies the case of the characters that are entered in the textbox. The options are,                                                                                                      |
|                                   |                                                                                                                                                                                             |
|                                   |                                                                                                                                                                                             |
|                                   |                                                                                                                                                                                             |
|                                   | Normal - Characters are left unchanged,                                                                                                                                                     |
|                                   |                                                                                                                                                                                             |
|                                   | UpperCase - Changes the case of the characters to UPPERCASE and                                                                                                                             |
|                                   |                                                                                                                                                                                             |
|                                   | LowerCase  - Changes the case of the characters to LOWERCASE.                                                                                                                               |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| TextBox.HideSelection             | When set to false will always highlight the selected text in the edit portion, even if the control losses focus.                                                                            |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| TextBox.WordWrap                  | Indicates whether the textbox automatically wraps words to the beginning of the next line. Note that the multiline property should be set to true, to make the word wrap feature effective. |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| AllowNewText                      | Indicates whether the user is allowed to enter new text at run time.                                                                                                                        |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| MaxLength                         | Specifies the maximum number of characters allowed in the edit portion of the ComboBoxAdv control. Default (32767).                                                                         |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                             |
|                                                                                                                                                                            |
| []                                                                                                                                     |
|                                                                                                                                                                            |
| [this][.comboBoxAdv1.NumberOnly = [true];]                       |
|                                                                                                                                                                            |
| [this][.comboBoxAdv1.CharacterCasing = [CharacterCasing].Upper;] |
|                                                                                                                                                                            |
| [this][.comboBoxAdv1.TextBox.HideSelection = [false];]           |
|                                                                                                                                                                            |
| [this][.comboBoxAdv1.TextBox.WordWrap = [true];]                 |
|                                                                                                                                                                            |
| []                                                                                                                                     |
|                                                                                                                                                                            |
| [this][.comboBoxAdv1.AllowNewText = [true];]                     |
|                                                                                                                                                                            |
| [this][.comboBoxAdv1.MaxLength = 32766;]                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                      |
|                                                                                                                                                                         |
| []                                                                                                                    |
|                                                                                                                                                                         |
| [Me][.comboBoxAdv1.NumberOnly = [True]]                       |
|                                                                                                                                                                         |
| [Me][.comboBoxAdv1.CharacterCasing = [CharacterCasing].Upper] |
|                                                                                                                                                                         |
| [Me][.comboBoxAdv1.TextBox.HideSelection = [false]]           |
|                                                                                                                                                                         |
| [Me][.comboBoxAdv1.TextBox.WordWrap = [True]]                 |
|                                                                                                                                                                         |
| []                                                                                                                                  |
|                                                                                                                                                                         |
| [Me][.comboBoxAdv1.AllowNewText = [True]]                     |
|                                                                                                                                                                         |
| [Me][.comboBoxAdv1.MaxLength = 32766]                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Banner Text Support

[] 

We can set banner text for the ComboBoxAdv control. Refer to BannerTextProvider Component topic for more details.

[] 

{border="0"}

[] 

Figure 346: Banner Text set for ComboBoxAdv

[] 

See Also

[] 

[DropDown Settings]{.UGHyperlink}[, ]{.UGHyperlink}[Data Settings]{.UGHyperlink}[]{.UGHyperlink}

[]{#_DropDown_Settings}3.3.5.2.3.1.2      DropDown Settings

[]{#p391}[] 

Dropdown for the ComboBoxAdv control can be customized using the below properties.

[] 


  ------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ComboBoxAdv Properties   Description
  DropDownWidth            Specifies the width of the dropdown. Default value is 100.
  IntegralHeight           Indicates whether the list portion will have only complete items. i.e when this property is set to true, it will display only those items that are fully visible in terms of height.
  MaxDropDownItems         Maximum number of entries that can be displayed in the dropdown. Set image for the dropdown items. Refer [Image Settings] topic.
  Sorted                   When set to true, will sort the dropdown items in the alphabetical order.
  ------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                           |
|                                                                                                                                                          |
| **[]**                                                                                                 |
|                                                                                                                                                          |
| [this][.comboBoxAdv1.DropDownWidth = 150;]                          |
|                                                                                                                                                          |
| [this][.comboBoxAdv1.IntegralHeight = [true];] |
|                                                                                                                                                          |
| [this][.comboBoxAdv1.MaxDropDownItems = 5;]                         |
|                                                                                                                                                          |
| [this][.comboBoxAdv1.Sorted = [true];]         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                    |
|                                                                                                                                                       |
| []                                                                                                  |
|                                                                                                                                                       |
| [Me][.comboBoxAdv1.DropDownWidth = 150]                          |
|                                                                                                                                                       |
| [Me][.comboBoxAdv1.IntegralHeight = [True]] |
|                                                                                                                                                       |
| [Me][.comboBoxAdv1.MaxDropDownItems = 5]                         |
|                                                                                                                                                       |
| [Me][.comboBoxAdv1.Sorted = [True]]         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 347: DropDownWidth = \"150\"; MaxDropDownItems = \"6\"; Sorted = \"True\"

[] 


{border="0"} Note: Data for the dropdown can be set using Items property. Refer Data Settings for details.

 

{border="0"} Note: To know about different dropdown styles available for the control, see ReadOnly Settings section in [TextBox]() topic.


[] 

See Also

[] 

[[TextBox]{.UGHyperlink}]()[, ]{.UGHyperlink}[Image Settings]{.UGHyperlink}[]{.UGHyperlink}

###### []{#p392}3.3.5.2.3.2 Data Settings {#data-settings style="tab-stops: 0pt"}

[] 

Data for the ComboBoxAdv is added through String Collection Editor, which is invoked through **ComboBoxAdv.Items** property.

[] 

{border="0"}

[] 

Figure 348: Adding DropDown Items to ComboBoxAdv Control

**[]** 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [this][.comboBoxAdv1.Items.AddRange([new] [object]\[\] {[\"Currency\"], [\"DateTimePicker\"], [\"ComboBoxAdv\"], [\"AutoComplete\"], [\"ListBox\"],[\"ContextMenu\"],[\"CurrencyEdit\"]});] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Me][.comboBoxAdv1.Items.AddRange([New] [Object]() {[\"Currency\"], [\"DateTimePicker\"], [\"ComboBoxAdv\"], [\"AutoComplete\"], [\"ListBox\"], [\"ContextMenu\"], \_ ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\"CurrencyEdit\"][}) ]                                                                                                                                                                                                                                                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 349: DropDown Items for ComboBoxAdv Control

[] 


{border="0"} Note: ComboBoxAdv can also be bound to an external Data source like Data Table. Refer Databinding topic.


[] 

To set image for dropdown items refer Image settings topic.

###### []{#p393}3.3.5.2.3.3 Advanced Features {#advanced-features style="tab-stops: 0pt"}

[] 

This section will discuss the auto complete support available for the ComboBoxAdv control and databinding using external source.

[]{#p394}[]{#_AutoComplete_Support}3.3.5.2.3.3.1      AutoComplete Support

[] 

ComboBoxAdv has in-built support of auto completion of the text entered in the control. This feature is automatically enabled for the control. To disable, set **ComboBoxAdv.AutoComplete** property to false.

[] 


  --------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ComboBoxAdv Properties      Description
  CaseSensitiveAutoComplete   Specifies whether search in the AutoComplete is case sensitive.
  MatchFirstCharacterOnly     It specifies the AutoComplete behavior in the dropdown mode. When set to true, it will match the first character in the drop list and returns the matching result.
  --------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                      |
|                                                                                                                                                                     |
| []                                                                                                                |
|                                                                                                                                                                     |
| [this][.comboBoxAdv1.AutoComplete = [true];]              |
|                                                                                                                                                                     |
| [this][.comboBoxAdv1.CaseSensitiveAutocomplete = [true];] |
|                                                                                                                                                                     |
| [this][.comboBoxAdv1.MatchFirstCharacterOnly = [true];]   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                               |
|                                                                                                                                                                  |
| **[]**                                                                                                         |
|                                                                                                                                                                  |
| [Me][.comboBoxAdv1.AutoComplete = [True]]              |
|                                                                                                                                                                  |
| [Me][.comboBoxAdv1.CaseSensitiveAutocomplete = [True]] |
|                                                                                                                                                                  |
| [Me][.comboBoxAdv1.MatchFirstCharacterOnly = [True]]   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 350: AutoComplete = \"True\"

[]{#p395}3.3.5.2.3.3.2      Data Binding

[] 

ComboBoxAdv control can be bound with external data source. Objects that can acts as Datasource to ComboBoxAdv are

 

[·      ]ArrayList

[·      ]DataView

[·      ]DataTable

[] 

We can add objects to the ComboBoxAdv by using the Items method. You can also add objects to a ComboBoxAdv using the **DataSource**, **DisplayMember** and **Valuemember** properties to fill the ComboBox.

 

When the DataSource property is set, we cannot modify the items collection. If setting the DataSource property causes the data source to change, the **Datasource** event is raised. If setting this property causes the data member to change, the **DisplayMember** event is raised.

 

When you set DataSource to a null reference, DisplayMember is set to an empty string (\"\").

 

ComboBoxAdv can be bound to DataView using the following code snippet.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                             |
|                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                            |
| [// Create a DataTable.        ][     ]                                                                                                |
|                                                                                                                                                                                                                                            |
| [DataTable dt = ][new][ DataTable(\"Table1\");]                                       |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                       |
|                                                                                                                                                                                                                                            |
| [// Adding Columns.]                                                                                                                                                                     |
|                                                                                                                                                                                                                                            |
| [dt.Columns.Add(\"FirstName\");]                                                                                                                                                         |
|                                                                                                                                                                                                                                            |
| [dt.Columns.Add(\"LastName\");]                                                                                                                                                          |
|                                                                                                                                                                                                                                            |
| [dt.Columns.Add(\"occupation\");]                                                                                                                                                        |
|                                                                                                                                                                                                                                            |
| [dt.Columns.Add(\"place\");]                                                                                                                                                             |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                       |
|                                                                                                                                                                                                                                            |
| [// Create a Data Set.]                                                                                                                                                                  |
|                                                                                                                                                                                                                                            |
| [DataSet ds = ][new][ DataSet();]                                                     |
|                                                                                                                                                                                                                                            |
| [ds.Tables.Add(dt);]                                                                                                                                                                     |
|                                                                                                                                                                                                                                            |
| [dt.Rows.Add(][new][ string\[\] { \"John\", \"Tina\", \"Doctor\", \"Italy\" });]      |
|                                                                                                                                                                                                                                            |
| [dt.Rows.Add(][new][ string\[\] { \"Mary\", \"anu\", \"Teacher\", \"America\" });]    |
|                                                                                                                                                                                                                                            |
| [dt.Rows.Add(][new][ string\[\] { \"asha\", \"roy\", \"Staff\", \"London\" });]       |
|                                                                                                                                                                                                                                            |
| [dt.Rows.Add(][new][ string\[\] { \"George\", \"Gaskin\", \"Nurse\", \"germany\" });] |
|                                                                                                                                                                                                                                            |
| [dt.Rows.Add(][new][ string\[\] { \"sam\", \"jens\", \"Engineer\", \"Russia\" });]    |
|                                                                                                                                                                                                                                            |
| [dt.Rows.Add(][new][ string\[\] { \"Ben\", \"Geo\", \"Developer\", \"India\" });]     |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                       |
|                                                                                                                                                                                                                                            |
| [// Create a DataView.]                                                                                                                                                                  |
|                                                                                                                                                                                                                                            |
| [DataView view = ][new][ DataView(dt);]                                               |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                       |
|                                                                                                                                                                                                                                            |
| [// Set DataSource.]                                                                                                                                                                     |
|                                                                                                                                                                                                                                            |
| [this][.comboBoxAdv1.DataSource = view;]                                                                                                |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                       |
|                                                                                                                                                                                                                                            |
| [// Set DisplayMember.]                                                                                                                                                                  |
|                                                                                                                                                                                                                                            |
| [this][.comboBoxAdv1.DisplayMember = \"place\";]                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [\' Create a DataTable.     ]                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [Dim][ dt ][As][ DataTable = ][New][ DataTable(\"Table1\") ] |
|                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [\' Adding Columns.]                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [dt.Columns.Add(\"FirstName\")\                                                                                                                                                                                                                                                                                                                                       |
| dt.Columns.Add(\"LastName\")\                                                                                                                                                                                                                                                                                                                                         |
| dt.Columns.Add(\"occupation\")\                                                                                                                                                                                                                                                                                                                                       |
| dt.Columns.Add(\"place\") ]                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [\' Create a Data Set.]                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [Dim][ ds ][As][ DataSet = ][New][ DataSet\                                                                    |
| ds.Tables.Add(dt)\                                                                                                                                                                                                                                                                                                                                                    |
| dt.Rows.Add(][New][ String() {\"John\", \"Tina\", \"Doctor\", \"Italy\"})\                                                                                                                                                                                         |
| dt.Rows.Add(][New][ String() {\"Mary\", \"anu\", \"Teacher\", \"America\"})\                                                                                                                                                                                       |
| dt.Rows.Add(][New][ String() {\"asha\", \"roy\", \"Staff\", \"London\"})\                                                                                                                                                                                          |
| dt.Rows.Add(][New][ String() {\"George\", \"Gaskin\", \"Nurse\", \"germany\"})\                                                                                                                                                                                    |
| dt.Rows.Add(][New][ String() {\"sam\", \"jens\", \"Engineer\", \"Russia\"})\                                                                                                                                                                                       |
| dt.Rows.Add(][New][ String() {\"Ben\", \"Geo\", \"Developer\", \"India\"}) ]                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [\' Create a DataView.]                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [Dim][ view ][As][ DataView = ][New][ DataView(dt)]          |
|                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [\' Set DataSource.\                                                                                                                                                                                                                                                                                                                                                  |
| ][Me][.comboBoxAdv1.DataSource = view ]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                       |
| [\' Set DisplayMember.\                                                                                                                                                                                                                                                                                                                                               |
| ][Me][.comboBoxAdv1.DisplayMember = \"place\" ]                                                                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

**[]** 

Figure 351: ComboBoxAdv databound with Data Table

###### []{#p396}[]{#_ComboBoxAdv_Appearance}3.3.5.2.3.4 ComboBoxAdv Appearance {#comboboxadv-appearance style="tab-stops: 0pt"}

This section discusses the below topics.

[] 

[]{#_Border_Styles_2}3.3.5.2.3.4.1      Border Styles[]{#p397}

This section discusses the border settings for the ComboBoxAdv control.

[] 


+-----------------------------------+------------------------------------------------------------------------------------------------------------------------+
| ComboBoxAdv Properties            | Description                                                                                                            |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------+
| Border3DStyle                     | Specifies the 3D BorderStyle for the control.                                                                          |
|                                   |                                                                                                                        |
|                                   | The options are,                                                                                                       |
|                                   |                                                                                                                        |
|                                   |                                                                                                                        |
|                                   |                                                                                                                        |
|                                   | *RaisedInner,*                                                                                                         |
|                                   |                                                                                                                        |
|                                   | *RaisedOuter,*                                                                                                         |
|                                   |                                                                                                                        |
|                                   | *Raised,*                                                                                                              |
|                                   |                                                                                                                        |
|                                   | *Sunken, (Default)*                                                                                                    |
|                                   |                                                                                                                        |
|                                   | *SunkenInner,*                                                                                                         |
|                                   |                                                                                                                        |
|                                   | *SunkenOuter,*                                                                                                         |
|                                   |                                                                                                                        |
|                                   | *Flat,*                                                                                                                |
|                                   |                                                                                                                        |
|                                   | *Bump and*                                                                                                             |
|                                   |                                                                                                                        |
|                                   | *Adjust.*                                                                                                              |
|                                   |                                                                                                                        |
|                                   |                                                                                                                        |
|                                   |                                                                                                                        |
|                                   | FlatStyle should be set to \"Standard\" to make this property setting effective.                                       |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------+
| BorderSides                       | Specifies the BorderSides of the control.                                                                              |
|                                   |                                                                                                                        |
|                                   | The options are,                                                                                                       |
|                                   |                                                                                                                        |
|                                   |                                                                                                                        |
|                                   |                                                                                                                        |
|                                   | *Left,*                                                                                                                |
|                                   |                                                                                                                        |
|                                   | *Top,*                                                                                                                 |
|                                   |                                                                                                                        |
|                                   | *Right,*                                                                                                               |
|                                   |                                                                                                                        |
|                                   | *Bottom,*                                                                                                              |
|                                   |                                                                                                                        |
|                                   | *Middle and*                                                                                                           |
|                                   |                                                                                                                        |
|                                   | *All. (Default)*                                                                                                       |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------+
| FlatStyle                         | Specifies the Flat Style. The options are                                                                              |
|                                   |                                                                                                                        |
|                                   |                                                                                                                        |
|                                   |                                                                                                                        |
|                                   | *Flat,*                                                                                                                |
|                                   |                                                                                                                        |
|                                   | *Standard (Default) and*                                                                                               |
|                                   |                                                                                                                        |
|                                   | *System.*                                                                                                              |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------+
| FlatBorderColor                   | Specifies the color with which flat border should be drawn. FlatStyle must be set to \'Flat\' to get the color effect. |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------+


**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                             |
|                                                                                                                                                                            |
| []                                                                                                                       |
|                                                                                                                                                                            |
| [this][.comboBoxAdv1.Border3DStyle = System.Windows.Forms.Border3DStyle.Flat;]        |
|                                                                                                                                                                            |
| [this][.comboBoxAdv1.BorderSides = System.Windows.Forms.Border3DSide.All;]            |
|                                                                                                                                                                            |
| [this][.comboBoxAdv1.FlatStyle = Syncfusion.Windows.Forms.Tools.ComboFlatStyle.Flat;] |
|                                                                                                                                                                            |
| [this][.comboBoxAdv1.FlatBorderColor = System.Drawing.Color.Blue;]                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                      |
|                                                                                                                                                                         |
| **[]**                                                                                                                |
|                                                                                                                                                                         |
| [Me][.comboBoxAdv1.Border3DStyle = System.Windows.Forms.Border3DStyle.Flat]        |
|                                                                                                                                                                         |
| [Me][.comboBoxAdv1.BorderSides = System.Windows.Forms.Border3DSide.All]            |
|                                                                                                                                                                         |
| [Me][.comboBoxAdv1.FlatStyle = Syncfusion.Windows.Forms.Tools.ComboFlatStyle.Flat] |
|                                                                                                                                                                         |
| [Me][.comboBoxAdv1.FlatBorderColor = System.Drawing.Color.Blue]                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

[] 

Figure 352: Border Settings

[]{#p398}3.3.5.2.3.4.2      Visual Styles

[] 

ComboBoxAdv supports visual styles such as Default, OfficeXP, Office2003, VS2005 and Office2007 with all three color schemes. The style can be set using **Style** property.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                 |
| [//To set Default Visual Style]                                                                                                                                                               |
|                                                                                                                                                                                                                                                 |
| [this][.comboBoxAdv1.Style = Syncfusion.Windows.Forms.[VisualStyle].Default;]                                                         |
|                                                                                                                                                                                                                                                 |
| [//To set Office2003 Visual Style]                                                                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [this][.comboBoxAdv1.Style = Syncfusion.Windows.Forms.[VisualStyle].Office2003;]                                                      |
|                                                                                                                                                                                                                                                 |
| [//To set OfficeXP Visual Style]                                                                                                                                                              |
|                                                                                                                                                                                                                                                 |
| [this][.comboBoxAdv1.Style = Syncfusion.Windows.Forms.[VisualStyle].OfficeXP;]                                                        |
|                                                                                                                                                                                                                                                 |
| [//To set VS2005 Visual Style]                                                                                                                                                                |
|                                                                                                                                                                                                                                                 |
| [this][.comboBoxAdv1.Style = Syncfusion.Windows.Forms.[VisualStyle].VS2005;]                                                          |
|                                                                                                                                                                                                                                                 |
| [//To set Office2007 Visual Style]                                                                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [this][.comboBoxAdv1.Style = Syncfusion.Windows.Forms.[VisualStyle].Office2007;][               ] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                   |
|                                                                                                                                                                  |
| []                                                                                                                                       |
|                                                                                                                                                                  |
| [\'To set Default Visual Style]                                                                                |
|                                                                                                                                                                  |
| [Me][.comboBoxAdv1.Style = Syncfusion.Windows.Forms.VisualStyle.Default]    |
|                                                                                                                                                                  |
| [\'To set Office2003 Visual Style]                                                                             |
|                                                                                                                                                                  |
| [Me][.comboBoxAdv1.Style = Syncfusion.Windows.Forms.VisualStyle.Office2003] |
|                                                                                                                                                                  |
| [\'To set OfficeXP Visual Style]                                                                               |
|                                                                                                                                                                  |
| [Me][.comboBoxAdv1.Style = Syncfusion.Windows.Forms.VisualStyle.OfficeXP]   |
|                                                                                                                                                                  |
| [\'To set VS2005 Visual Style]                                                                                 |
|                                                                                                                                                                  |
| [Me][.comboBoxAdv1.Style = Syncfusion.Windows.Forms.VisualStyle.VS2005]     |
|                                                                                                                                                                  |
| [\'To set Office2007 Visual Style]                                                                             |
|                                                                                                                                                                  |
| [Me][.comboBoxAdv1.Style = Syncfusion.Windows.Forms.VisualStyle.Office2007] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 353: Visual Styles Set for ComboBoxAdv Control

**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                |
| [//To set Blue Color scheme]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                |
| [this][.comboBoxAdv1.Office2007ColorTheme = Syncfusion.Windows.Forms.[Office2007Theme].Blue;]                                                        |
|                                                                                                                                                                                                                                                                |
| [//To set Silver Color scheme]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                |
| [this][.comboBoxAdv1.Office2007ColorTheme = Syncfusion.Windows.Forms.[Office2007Theme.]Silver;]                                                      |
|                                                                                                                                                                                                                                                                |
| [//To set Black Color scheme]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                |
| [this][.comboBoxAdv1.Office2007ColorTheme = Syncfusion.Windows.Forms.[Office2007Theme].Black;][                ] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                  |
|                                                                                                                                                                                 |
| []                                                                                                                                                      |
|                                                                                                                                                                                 |
| [\'To set Blue Color scheme]                                                                                                  |
|                                                                                                                                                                                 |
| [Me][.comboBoxAdv1.Office2007ColorTheme = Syncfusion.Windows.Forms.Office2007Theme.Blue]   |
|                                                                                                                                                                                 |
| [\'To set Silver Color scheme]                                                                                                |
|                                                                                                                                                                                 |
| [Me][.comboBoxAdv1.Office2007ColorTheme = Syncfusion.Windows.Forms.Office2007Theme.Silver] |
|                                                                                                                                                                                 |
| [\'To set Black Color scheme]                                                                                                 |
|                                                                                                                                                                                 |
| [Me][.comboBoxAdv1.Office2007ColorTheme = Syncfusion.Windows.Forms.Office2007Theme.Black]  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 354: Blue, Silver and Black OfficeColorSchemes

**[]** 

Custom Colors

[] 

We can also apply custom colors to the ComboBoxAdv control by setting Office2007ColorTheme to \"Managed\" and specifying the custom color through the ApplyManagedColors method as follows.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                             |
|                                                                                                                                                                                                            |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                            |
| [this][.comboBoxAdv1.Office2007ColorTheme = Syncfusion.Windows.Forms.[Office2007Theme].Managed;] |
|                                                                                                                                                                                                            |
| [Office2007Colors][.ApplyManagedColors([this], [Color].Orchid);]            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                       |
|                                                                                                                                                                                                          |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                          |
| [Me][.comboBoxAdv1.Office2007ColorTheme = Syncfusion.Windows.Forms.[Office2007Theme].Managed;] |
|                                                                                                                                                                                                          |
| [Office2007Colors.][ApplyManagedColors([Me], [Color].Orchid)]           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 355: Custom Color = \"Orchid\"

[]{#p399}3.3.5.2.3.4.3      Background Settings

[] 

When ComboBoxAdv control is set with some style, theme background will be drawn. We can override this background with **BackColor** property using **IgnoreThemeBackground** property. When this IgnoreThemeBackground is set to true, the control will ignore the theme background and draws the backcolor as the background.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                  |
|                                                                                                                                                                                 |
| []                                                                                                                            |
|                                                                                                                                                                                 |
| [this][.comboBoxAdv1.BackColor = System.Drawing.[SystemColors].Info;] |
|                                                                                                                                                                                 |
| [this][.comboBoxAdv1.IgnoreThemeBackground = [true];]                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                            |
|                                                                                                                                                                               |
| **[]**                                                                                                                      |
|                                                                                                                                                                               |
| [Me][.comboBoxAdv1.BackColor = System.Drawing.[SystemColors].Info] |
|                                                                                                                                                                               |
| [Me][.comboBoxAdv1.IgnoreThemeBackground = [True]]                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

**[]** 

Figure 356: Background set using BackColor

[]{#p400}3.3.5.2.3.4.4      Image Settings

 

Images can be easily associated with the items of the ComboBoxAdv control using the below properties.

[] 


  ------------------------ ----------------------------------------------------------------------------------
  ComboBoxAdv Properties   Description
  ImageList                Specifies the imagelist that is used for the ComboBoxAdv control.
  ShowImageInTextBox       It sets the selected image in the textbox of the ComboBoxAdv control.
  ItemsImageIndexes        Invokes an editor and lets you to set image index for individual dropdown items.
  ------------------------ ----------------------------------------------------------------------------------


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                          |
| [this][.comboBoxAdv1.ImageList = [this].imageList1;]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                          |
| [this][.comboBoxAdv1.ItemsImageIndexes.Add([new] Syncfusion.Windows.Forms.Tools.[ComboBoxAdv].[ImageIndexItem]([this].comboBoxAdv1, [\"Pointer\"], 0));] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                        |
| [Me][.comboBoxAdv1.ImageList = [Me].imageList1]                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                        |
| [Me][.comboBoxAdv1.ItemsImageIndexes.Add([New] Syncfusion.Windows.Forms.Tools.ComboBoxAdv.ImageIndexItem([Me].comboBoxAdv1, [\"Pointer\"], 0)) ] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Image in TextBox

**[]** 

The following code snippet is used to show the images together with the selected text in the TextArea of the ComboBoxAdv control.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                         |
|                                                                                                                                                                                                        |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                        |
| [// Show the images in the TextArea.]                                                                                                                |
|                                                                                                                                                                                                        |
|  [this][.comboBoxAdv1.ShowImageInTextBox = ][true] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                  |
|                                                                                                                                                                                                     |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                     |
| [\' Show the images in the TextArea.]                                                                                                             |
|                                                                                                                                                                                                     |
| [Me][.comboBoxAdv1.ShowImageInTextBox = ][True] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

[] 

Figure 357: TextArea with Image

***[]*** 

3.3.5.2.3.4.5      Customizable ComboBoxAdv height

** **ComboBoxAdv allows to customize the height of the Display area, making more space to display larger images and text items  by setting the **TextBoxHeight** property of the ComboBox.

+-----------------------------------------------------------------------------+
| **\[C#\]**                                                                  |
|                                                                             |
| // Sets the height of the ComboBox.                                         |
|                                                                             |
| [this.comboBoxAdv1.TextBoxHeight = 80;] |
+-----------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------+
| **\[VB.NET\]**                                                                                                              |
|                                                                                                                             |
| 'Sets the height of the ComboBox.                                                                                           |
|                                                                                                                             |
| [Me][.comboBoxAdv1.TextBoxHeight = 80] |
+-----------------------------------------------------------------------------------------------------------------------------+

***[]*** 

[]{#related-topics}

