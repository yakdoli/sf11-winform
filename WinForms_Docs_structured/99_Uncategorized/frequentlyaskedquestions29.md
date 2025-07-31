---
title: frequentlyaskedquestions29.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\frequentlyaskedquestions29.md
created_at: 2025-07-03
---






##### Frequently Asked Questions {#frequently-asked-questions style="tab-stops: 0pt"}

[] 

This section illustrates the solutions for various task-based queries about the control.

###### []{#_How_to_programmatically}[]{#_How_to_programmatically_1}3.3.5.2.5.1 How to programmatically select the record in the dropdown that matches the text typed in? {#how-to-programmatically-select-the-record-in-the-dropdown-that-matches-the-text-typed-in style="tab-stops: 0pt"}

[]{#p405}[] 

You can handle DropDown event of ComboBoxAdv control and set as shown in the following code snippet.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                      |
|                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                     |
| [private][ [void] comboBoxAdv1_DropDown([object] sender, System.[EventArgs] e)] |
|                                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                     |
| [    [this].comboBoxAdv1.ListBox.SelectedItem = [this].comboBoxAdv1.TextBox.Text;]                                                                    |
|                                                                                                                                                                                                                                     |
| [} ]                                                                                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                           |
| [Private][ [Sub] comboBoxAdv1_DropDown([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)] |
|                                                                                                                                                                                                                                                                                                                           |
| [    [Me].comboBoxAdv1.ListBox.SelectedItem = [Me].comboBoxAdv1.TextBox.Text]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                           |
| [End][ [Sub]]                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

###### []{#p406}3.3.5.2.5.2 How to select multiple items in the dropdown? {#how-to-select-multiple-items-in-the-dropdown style="tab-stops: 0pt"}

 

In order to perform multiple selection, we can use our ComboxAdv or MultiColumnComboBox controls, which internally contains a normal ListBox that allows you to select multiple items.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                    |
|                                                                                                                                                                                                   |
| **[]**                                                                                                                                          |
|                                                                                                                                                                                                   |
| [this][.comboBoxAdv1.ListBox.SelectionMode = [SelectionMode].MultiExtended;]         |
|                                                                                                                                                                                                   |
| [this][.multiColumnComboBox1.ListBox.SelectionMode = [SelectionMode].MultiExtended;] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                   |
|                                                                                                                                                                      |
| **[]**                                                                                                             |
|                                                                                                                                                                      |
| [Me][.comboBoxAdv1.ListBox.SelectionMode = SelectionMode.MultiExtended]         |
|                                                                                                                                                                      |
| [Me][.multiColumnComboBox1.ListBox.SelectionMode = SelectionMode.MultiExtended] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p407} 

[]{#related-topics}

