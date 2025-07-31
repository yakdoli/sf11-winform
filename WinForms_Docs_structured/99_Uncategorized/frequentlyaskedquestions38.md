---
title: frequentlyaskedquestions38.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\frequentlyaskedquestions38.md
created_at: 2025-07-03
---






##### Frequently Asked Questions {#frequently-asked-questions style="tab-stops: 0pt"}

[] 

This section will help you become more familiar in using the CheckBoxAdv control.

[] 

###### 3.3.11.1.5.1        How to databind a CheckBoxAdv to an SQL database if the corresponding datatable field is a bit field {#how-to-databind-a-checkboxadv-to-an-sql-database-if-the-corresponding-datatable-field-is-a-bit-field style="tab-stops: 0pt"}

[]{#p784}[] 

The CheckBoxAdv\'s **IntValue** property can be used to databind bit values as illustrated below.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [private][ [void] Form1_Load([object] sender, System.[EventArgs] e)]                                |
|                                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                            |
| [// Using CheckBoxAdv\'s IntValue property for Databinding.]                                                                                                                                             |
|                                                                                                                                                                                                                                                            |
| [this][.oleDbDataAdapter1.Fill([this].dataSet11.Table1);]                                                                                        |
|                                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [this][.checkBoxAdv1.DataBindings.Add([\"IntValue\"], [this].dataSet11.Table1, [\"BitField\"]);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                |
| [Private][ [Sub] Form1_Load([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)] |
|                                                                                                                                                                                                                                                                                                                |
| [\' Using CheckBoxAdv\'s IntValue property for Databinding.]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                |
| [Me][.oleDbDataAdapter1.Fill([Me].dataSet11.Table1)]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                |
| [End][ [Sub]]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                |
| [Me][.checkBoxAdv1.DataBindings.Add([\"IntValue\"], [Me].dataSet11.Table1, [\"BitField\"])]                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

A sample which demonstrates how bit values are used to set the state of the CheckBoxAdv is available in the below sample installation path.

 

..My Documents\\Syncfusion\\EssentialStudio***\\Version Number***\\Windows\\Tools.Windows\\Samples\\2.0\\Editors Package\\OptionControls

###### 3.3.11.1.5.2        How to databind a CheckBoxAdv to an SQL database if the corresponding datatable field is boolean {#how-to-databind-a-checkboxadv-to-an-sql-database-if-the-corresponding-datatable-field-is-boolean style="tab-stops: 0pt"}

[]{#p785} 

The CheckBoxAdv\'s **BoolValue** property can be used to databind bool values as illustrated below.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                               |
| [private][ [void] Form1_Load([object] sender, System.[EventArgs] e)]                                   |
|                                                                                                                                                                                                                                                               |
| [{]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                               |
| [this][.oleDbDataAdapter1.Fill([this].dataSet11.Table1);]                                                                                           |
|                                                                                                                                                                                                                                                               |
| [}]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| [// Using CheckBoxAdv\'s BoolValue property for Databinding.]                                                                                                                                               |
|                                                                                                                                                                                                                                                               |
| [this][.checkBoxAdv1.DataBindings.Add([\"BoolValue\"], [this].dataSet11.Table1, [\"CheckValue\"]);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                |
| [Private][ [Sub] Form1_Load([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)] |
|                                                                                                                                                                                                                                                                                                                |
| [Me][.oleDbDataAdapter1.Fill([Me].dataSet11.Table1)]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                |
| [End][ [Sub]]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                |
| [\' Using CheckBoxAdv\'s BoolValue property for Databinding.]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                |
| [Me][.checkBoxAdv1.DataBindings.Add([\"BoolValue\"], [Me].dataSet11.Table1, [\"CheckValue\"])]                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 626: Databinding a CheckBoxAdv to an SQL Database if the corresponding Datatable Field is Boolean

[]{#related-topics}

