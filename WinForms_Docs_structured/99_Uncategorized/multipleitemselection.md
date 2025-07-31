---
title: multipleitemselection.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\multipleitemselection.md
created_at: 2025-07-03
---






##### Multiple Item Selection {#multiple-item-selection style="tab-stops: 0pt"}

[] 

Delimiters or the visual separators can be used to delimit when multiple entries are allowed or required. AutoComplete allows you to set the required delimiter from the pre-defined options.

[] 

Set DelimiterChars property to any special characters like comma, semicolon, from the options.

[] 

Only when the delimiter character is set, using which, multiple entries can be made in the textbox with autocomplete feature.

[  ]


+-----------------------------------+-----------------------------------------------------------------------------------------------------+
|                                   |                                                                                                     |
|                                   |                                                                                                     |
| Property                          | Description                                                                                         |
+-----------------------------------+-----------------------------------------------------------------------------------------------------+
| DelimiterChars                    | Specifies the character to use as delimiter when multiple items are to be displayed in the textbox. |
+-----------------------------------+-----------------------------------------------------------------------------------------------------+


[] 

Programmatically it can be set as follows.

[] 

+-------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                            |
|                                                                                                             |
| **[]**                                                                  |
|                                                                                                             |
| [AutoCompleteTextBox1.DelimiterChars = [\",\"];] |
+-------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                      |
|                                                                                                                                                                       |
| **[]**                                                                                                                            |
|                                                                                                                                                                       |
| [Private][ AutoCompleteTextBox1.DelimiterChars = [\",\"]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Select an item and insert the special character. Unless the special character is used, you will not be able to input another item.

[] 

{border="0"}

**[]** 

Figure 31: Multiple selection with delimiter and autocomplete feature

 

[]{#related-topics}

