---
title: captionsummary.md
original_path: WinForms_Docs/99_Uncategorized/captionsummary.md
created_at: 2025-08-05
---








  









### Caption Summary {#caption-summary style="tab-stops: 0pt"}

[] 

Through Designer

[] 

To define the Summary Row that should be used for displaying summaries on the Group Caption Bar, you need to set the following properties from the ChildGroupOptions.

[] 

[·      ]**ShowCaptionSummaryCells** - is to set for showing the summaries on the group caption bar.

[·      ]**CaptionSummaryRow** - accepts string values, which describes the name of the summary row.

[] 

{border="0"}

Figure 100

[] 

[·      ]Through Code

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [GridTableDescriptor][ mainTD = [this].GridGroupingControl1.TableDescriptor;]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [// Defines SummaryColumnDescriptor]                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [GridSummaryColumnDescriptor][ summaryColumn2 = [new] [GridSummaryColumnDescriptor]([\"FreightTotalAvg\"], SummaryType.DoubleAggregate, [\"Freight\"], [\"{Average:\$###.00}\"]);] |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [//Defines SummaryRowDescriptor]                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [GridSummaryRowDescriptor][ summaryRow2 = [new] [GridSummaryRowDescriptor]();]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [summaryRow2.Name = [\"Freight Average:\"];]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [summaryRow2.Visible = [true];]                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [summaryRow2.SummaryColumns.Add(summaryColumn2);]                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [mainTD.SummaryRows.Add(summaryRow2);]                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [// Here you define the summary row that should be used for displaying summaries in caption bar.]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [mainTD.ChildGroupOptions.ShowCaptionSummaryCells = [true];]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [mainTD.ChildGroupOptions.CaptionSummaryRow = [\"Freight Average:\"];]                                                                                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [GridTableDescriptor][ mainTD = [this].GridGroupingControl1.TableDescriptor;]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [// Defines SummaryColumnDescriptor]                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [GridSummaryColumnDescriptor][ summaryColumn2 = [new] [GridSummaryColumnDescriptor]([\"FreightTotalAvg\"], SummaryType.DoubleAggregate, [\"Freight\"], [\"{Average:\$###.00}\"]);] |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [//Defines SummaryRowDescriptor]                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [GridSummaryRowDescriptor][ summaryRow2 = [new] [GridSummaryRowDescriptor]();]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [summaryRow2.Name = [\"Freight Average:\"];]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [summaryRow2.Visible = [true];]                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [summaryRow2.SummaryColumns.Add(summaryColumn2);]                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [mainTD.SummaryRows.Add(summaryRow2);]                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [// Here you define the summary row that should be used for displaying summaries in caption bar.]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [mainTD.ChildGroupOptions.ShowCaptionSummaryCells = [true];]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                        |
| [mainTD.ChildGroupOptions.CaptionSummaryRow = [\"Freight Average:\"];]                                                                                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p78} 

[]{#related-topics}

