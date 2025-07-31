---
title: summarystyle.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\summarystyle.md
created_at: 2025-07-03
---






##### Summary Style {#summary-style style="tab-stops: 0pt"}

[] 

You can customize the appearance of summary cells by applying the desired formatting settings to the **GridDataSummaryColumn.ColumnStyle** and **GridDataSummaryRow.RowStyle** properties. The following code example illustrates this.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\<][syncfusion][:][GridDataSummaryRow][\>]                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    ][\<][syncfusion][:][GridDataSummaryRow.SummaryColumns][\>]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [        ][\<][syncfusion][:][GridDataSummaryColumn][\>]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            ][\<][syncfusion][:][GridDataSummaryColumn.ColumnStyle][\>]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [                ][\<][syncfusion][:][GridDataStyleInfo][ Background][=\"LightPink\"][ Foreground][=\"MidnightBlue\" /\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            ][\</][syncfusion][:][GridDataSummaryColumn.ColumnStyle][\>]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [        ][\</][syncfusion][:][GridDataSummaryColumn][\>]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    ][\</][syncfusion][:][GridDataSummaryRow.SummaryColumns][\>]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    ][\<][syncfusion][:][GridDataSummaryRow.RowStyle][\>]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [        ][\<][syncfusion][:][GridDataStyleInfo][ Background][=\"LightGreen\" /\>]                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [    ][\</][syncfusion][:][GridDataSummaryRow.RowStyle][\>]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\</][syncfusion][:][GridDataSummaryRow][\>]                                                                                                                                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                               |
|                                                                                                                                                                                                              |
| []                                                                                                                                                         |
|                                                                                                                                                                                                              |
| [GridDataSummaryColumn][ summaryCol = [new] [GridDataSummaryColumn]();] |
|                                                                                                                                                                                                              |
| [summaryCol.ColumnStyle = [new] [GridDataStyleInfo]();]                                                                     |
|                                                                                                                                                                                                              |
| [summaryCol.ColumnStyle.Background = [new] [SolidColorBrush]([Colors].LightPink);]                  |
|                                                                                                                                                                                                              |
| [summaryCol.ColumnStyle.Foreground = [new] [SolidColorBrush]([Colors].MidnightBlue);]               |
|                                                                                                                                                                                                              |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                              |
| [GridDataSummaryRow][ summaryRow = [new] [GridDataSummaryRow]();]       |
|                                                                                                                                                                                                              |
| [summaryRow.SummaryColumns.Add(summaryCol);]                                                                                                                             |
|                                                                                                                                                                                                              |
| [summaryRow.RowStyle = [new] [GridDataStyleInfo]();]                                                                        |
|                                                                                                                                                                                                              |
| [summaryRow.RowStyle.Background = [new] [SolidColorBrush]([Colors].LightGreen);]                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 133: Customized Row and Column Summary Styles

[]{#p255} 

[]{#related-topics}

