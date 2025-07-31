---
title: howtomakethegridfilterbaruseanautocompletecombobox.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\howtomakethegridfilterbaruseanautocompletecombobox.md
created_at: 2025-07-03
---








  









### How to Make the GridFilterBar Use an Autocomplete Combo Box {#how-to-make-the-gridfilterbar-use-an-autocomplete-combo-box style="tab-stops: 0pt"}

[] 

Introduction

[] 

To get autocomplete using the standard **GridFilterBar**, try the following code.

[] 

Example

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                             |
|                                                                                                                                                                                                            |
| []                                                                                                                                                       |
|                                                                                                                                                                                                            |
| [// Bind FilterBar to the grid.]                                                                                                                         |
|                                                                                                                                                                                                            |
| [theFilterBar.WireGrid(][this][.gridDataBoundGrid1);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                      |
|                                                                                                                                                                                                         |
| []                                                                                                                                                    |
|                                                                                                                                                                                                         |
| [\' Bind FilterBar to the grid.]                                                                                                                      |
|                                                                                                                                                                                                         |
| [theFilterBar.WireGrid(][Me][.gridDataBoundGrid1)] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                             |
| [// Set up a GridStyleInfo object.]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                             |
| [   GridStyleInfo style = ][new][ GridStyleInfo(); ]                                                                   |
|                                                                                                                                                                                                                                                                             |
| [    style.ModifyStyle(][this][.gridDataBoundGrid1.BaseStylesMap\[\"Header\"\].StyleInfo,     StyleModifyType.Copy); ] |
|                                                                                                                                                                                                                                                                             |
| [    ]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [        // Set cell type of the style object to ComboBox.]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [    style.CellType = \"ComboBox\"; ]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                             |
| [    style.ExclusiveChoiceList = ][true][;]                                                                            |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                             |
| [        // Apply style settings. ]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                             |
| [    style.BaseStyle = \"Standard\"; ]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [    style.Font.Bold = ][false][; ]                                                                                    |
|                                                                                                                                                                                                                                                                             |
| [    style.BackColor = ][this][.gridDataBoundGrid1.TableStyle.BackColor;]                                              |
|                                                                                                                                                                                                                                                                             |
| [    style.Borders.Bottom = ][new][ GridBorder(GridBorderStyle.Dashed);]                                               |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                             |
| [        // Set DropDownStyle to Autocomplete. ]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                             |
| [    style.DropDownStyle = GridDropDownStyle.AutoComplete;]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                             |
| [        // Apply the StyleInfo object to FilterBar.]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                             |
| [    theFilterBar.WireGrid(][this][.gridDataBoundGrid1, style);]                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

And replace it with this code.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                               |
| [\' Set up a GridStyleInfo object.]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                               |
| [Dim][ style ][As New][ GridStyleInfo]                  |
|                                                                                                                                                                                                                                                               |
| [style.ModifyStyle(][Me][.gridDataBoundGrid1.BaseStylesMap(\"Header\").StyleInfo, StyleModifyType.Copy)] |
|                                                                                                                                                                                                                                                               |
| [    ]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                               |
| [\' Set cell type of the style object to ComboBox.]                                                                                                                                                         |
|                                                                                                                                                                                                                                                               |
| [style.CellType = \"ComboBox\"]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                               |
| [style.ExclusiveChoiceList = ][True]                                                                                                                       |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                               |
| [\' Apply style settings.]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                               |
| [style.BaseStyle = \"Standard\"]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                               |
| [style.Font.Bold = ][False]                                                                                                                                |
|                                                                                                                                                                                                                                                               |
| [style.BackColor = ][Me][.gridDataBoundGrid1.TableStyle.BackColor]                                       |
|                                                                                                                                                                                                                                                               |
| [style.Borders.Bottom = ][New][ GridBorder(GridBorderStyle.Dashed)]                                      |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                               |
| [\' Set DropDownStyle to Autocomplete.]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                               |
| [style.DropDownStyle = GridDropDownStyle.AutoComplete]                                                                                                                                                      |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                               |
| [\' Apply the StyleInfo object to FilterBar.]                                                                                                                                                               |
|                                                                                                                                                                                                                                                               |
| [theFilterBar.WireGrid(][Me][.gridDataBoundGrid1, style)]                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

This adds the **DropDownStyle** = Autocomplete, setting it to the default combobox.

 

[]{#p593} 

 

[]{#related-topics}

