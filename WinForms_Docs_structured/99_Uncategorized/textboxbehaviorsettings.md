---
title: textboxbehaviorsettings.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\textboxbehaviorsettings.md
created_at: 2025-07-03
---






##### TextBox Behavior Settings {#textbox-behavior-settings style="tab-stops: 0pt"}

 

Multiple line entries and Password entry

[] 

The textbox can be used as single line entry textbox or can be made to display multiple lines of text. **TextMode** property can be used to set to one of the modes. When it is used in multiline mode, the number of rows that should be visible (when the text exceeds, automatically scrollbar will appear) can be set using **Rows** property.

 

It could also be used in password mode, where the input text will be masked using circular dots.

[] 


+-----------------------------------+------------------------------------------------------------------------------------------------------------------------+
|                                   |                                                                                                                        |
|                                   |                                                                                                                        |
| Property                          | Description                                                                                                            |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------+
| Rows                              | Specifies the number of lines to display in a multi-line textbox.                                                      |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------+
| TextMode                          | Specifies the mode in which the textbox can be used. Default value is SingleLine. The options included are as follows: |
|                                   |                                                                                                                        |
|                                   | [·      ]SingleLine                                                                       |
|                                   |                                                                                                                        |
|                                   | [·      ]MultiLine                                                                        |
|                                   |                                                                                                                        |
|                                   | [·      ]Password                                                                         |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------+


[] 

Programmatically these properties can be set as follows.

[] 

+---------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                    |
|                                                                                                                     |
| **[]**                                                                          |
|                                                                                                                     |
| [AutoCompleteTextBox1.TextMode = [TextBoxMode].MultiLine;] |
|                                                                                                                     |
| [AutoCompleteTextBox1.Rows = 3;]                                                |
+---------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                       |
|                                                                                                                                                        |
| **[]**                                                                                                             |
|                                                                                                                                                        |
| [Private][ AutoCompleteTextBox1.TextMode = TextBoxMode.MultiLine] |
|                                                                                                                                                        |
| [Private][ AutoCompleteTextBox1.Rows = 3]                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Setting character limits

[] 

The maximum character length inside the textbox can be specified by setting the **MaxLength** property, which allows to specify limits to the values entered in the textbox.

[] 


  ----------- -----------------------------------------------------------------------------------
  Property    Description
  MaxLength   Specifies the maximum number of characters that should be allowed in the textbox.
  ----------- -----------------------------------------------------------------------------------


[] 

**ReadOnly** property when enabled does not allows to edit the textbox entries.

[] 


  ---------- ----------------------------------------------------------------------------------
  Property   Description
  ReadOnly   Specifies whether the text in the textbox can be edited. Default value is False.
  ---------- ----------------------------------------------------------------------------------


[] 

Programmatically these properties can be set as follows.

[] 

+----------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                   |
|                                                                                                    |
| **[]**                                                         |
|                                                                                                    |
| [AutoCompleteTextBox1.MaxLength = 5;]                          |
|                                                                                                    |
| [AutoCompleteTextBox1.ReadOnly = [true];] |
+----------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                             |
|                                                                                                                                                              |
| **[]**                                                                                                                   |
|                                                                                                                                                              |
| [Private][ AutoCompleteTextBox1.MaxLength = 5]                          |
|                                                                                                                                                              |
| [Private][ AutoCompleteTextBox1.ReadOnly = [True]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

