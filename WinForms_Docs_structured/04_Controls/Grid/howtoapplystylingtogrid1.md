---
title: howtoapplystylingtogrid1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\howtoapplystylingtogrid1.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






   


## How to apply Styling to Grid? {#how-to-apply-styling-to-grid style="tab-stops: 0pt"}

Custom styling can be either applied by changing the following properties of **OlapGrid**. They are:

[·      ]ColumnHeaderStyle

[·      ]RowHeaderStyle

[·      ]SummaryColumnStyle

[·      ]SummaryRowStyle

[·      ]ValueCellsStyle

Or

Using Grid Style Dialog

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[XAML\]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                 |
| [\<] [Syncfusion] [:] [OlapGrid] [ x] [:] [Name] [=\"OlapGrid1\"\>] |
|                                                                                                                                                                                                                                                 |
| [  ] [\<] [Syncfusion] [:] [OlapGrid.ColumnHeaderStyle] [\>]                                             |
|                                                                                                                                                                                                                                                 |
| [    ] [\<] [Syncfusion] [:] [OlapGridCellStyle] [ Background] [=\"Blue\"/\> ]       |
|                                                                                                                                                                                                                                                 |
| [  ] [\</] [Syncfusion] [:] [OlapGrid.ColumnHeaderStyle] [\>]                                            |
|                                                                                                                                                                                                                                                 |
| [\</] [Syncfusion] [:] [OlapGrid] [\>]                                                                                           |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                       |
|                                                                                                              |
| [// Applying Background Color for Column Header ]                                      |
|                                                                                                              |
| [this].OlapGrid1.ColumnHeaderStyle.Background = [Brushes].Blue; |
|                                                                                                              |
| [// To Display Style Dialog ]                                                          |
|                                                                                                              |
| [this].OlapGrid1.ShowStyleDialog();                                                     |
|                                                                                                              |
|                                                                                                              |
+--------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------+
| \[VB\]                                                                          |
|                                                                                 |
| [\' Applying Background Color for Column Header ]         |
|                                                                                 |
| [Me].OlapGrid1.ColumnHeaderStyle.Background = Brushes.Blue |
|                                                                                 |
| [\' To Display Style Dialog ]                             |
|                                                                                 |
| [Me].OlapGrid1.ShowStyleDialog()                           |
+---------------------------------------------------------------------------------+

[]{#related-topics}

