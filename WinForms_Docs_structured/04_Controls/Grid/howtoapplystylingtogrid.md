---
title: howtoapplystylingtogrid.md
original_path: WinForms_Docs/04_Controls/Grid/howtoapplystylingtogrid.md
created_at: 2025-08-05
---








  









## How to apply Styling to Grid? {#how-to-apply-styling-to-grid style="tab-stops: 0pt"}

Custom styling can be either applied by changing the following properties of OlapGrid or by using the Grid Style Dialog:

[·      ]ColumnHeaderStyle

[·      ]RowHeaderStyle

[·      ]SummaryColumnStyle

[·      ]SummaryRowStyle

[·      ]ValueCellsStyle

The custom styling can be changed by using the Grid Style Dialog as follows:

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][Syncfusion][:][OlapGrid][ x][:][Name][=\"OlapGrid1\"\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [  ][\<][Syncfusion][:][OlapGrid.ColumnHeaderStyle][\>]                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [    ][\<][Syncfusion][:][OlapGridCellStyle][ Background][=\"Blue\"/\> ]                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [  ][\</][Syncfusion][:][OlapGrid.ColumnHeaderStyle][\>]                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\</][Syncfusion][:][OlapGrid][\>]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                               |
|                                                                                                                                                                                |
| [// Applying Background Color for Column Header ]                                                                            |
|                                                                                                                                                                                |
| [this][.OlapGrid1.ColumnHeaderStyle.Background = [Brushes].Blue;] |
|                                                                                                                                                                                |
| [// To Display Style Dialog ]                                                                                                |
|                                                                                                                                                                                |
| [this][.OlapGrid1.ShowStyleDialog();   ]                                                  |
|                                                                                                                                                                                |
| [         ]                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                  |
|                                                                                                                                                   |
| []                                                                                                            |
|                                                                                                                                                   |
| [\' Applying Background Color for Column Header ][]         |
|                                                                                                                                                   |
| [Me][.OlapGrid1.ColumnHeaderStyle.Background = Brushes.Blue] |
|                                                                                                                                                   |
| [\' To Display Style Dialog ][]                             |
|                                                                                                                                                   |
| [Me][.OlapGrid1.ShowStyleDialog()]                           |
|                                                                                                                                                   |
| []                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

