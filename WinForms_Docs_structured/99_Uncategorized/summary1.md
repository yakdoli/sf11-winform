---
title: summary1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\summary1.md
created_at: 2025-07-03
---








  









## Summary {#summary style="tab-stops: 0pt"}

[] 

Summary Rows in GridGroupingControl

[] 

A summary row in a GridGroupingControl is a row that has column totals, averages, or some other type of summary information. A summary row is indispensible for a grid with many numbers.

 

The following are the summaries supported by the GridGroupingControl.

[] 

[·      ]Total summary

[·      ]Caption Summary

[] 

Pre-Built Summary types supported by the GridGroupingControl are given below.

[] 

[·      ]Int32Aggregate, DoubleAggregate (Count, Min, Max, Sum)

[·      ]StringAggregate (MaxLength, Count)

[·      ]Count

[·      ]DistinctCount (Count, Values array)

[·      ]Vector (Values)

[·      ]DoubleVector (statistical methods: Median, Min, Max, 25% Quartile, 75% Quartile)

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][TableDescriptor][ [AllowNew][=\"False\"] [AllowFilter][=\"False\"\>]]                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][SummaryRows][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][sfwg][:][GridSummaryRowDescriptor][ [Title][=\"Total (USD):\"] [Name][=\"MainSummaryRow\"] [\>]]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][SummaryColumns][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][sfwg][:][GridSummaryColumnDescriptor][ [DataMember][=\"CurShareValue\"] [Format][=\"{Sum:###.00}\"] [Name][=\"ValueTotal\"] [SummaryType][=\"DoubleAggregate\"] [DisplayColumn][=\"Value\"\>]]                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\</][sfwg][:][GridSummaryColumnDescriptor][\>]                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][sfwg][:][GridSummaryColumnDescriptor][ [DataMember][=\"DayValueChange\"] [Format][=\"{Sum:###.00}\"] [Name][=\"DayTotalValueChange\"] [SummaryType][=\"DoubleAggregate\"] [DisplayColumn][=\"Dollar Change\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\</][sfwg][:][GridSummaryColumnDescriptor][\>]                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][sfwg][:][GridSummaryColumnDescriptor][ [DataMember][=\"TotalSharePaidPrice\"] [Format][=\"{Maximum}\"] [Name][=\"TotalPaidPrice\"] [SummaryType][=\"DoubleAggregate\"] [DisplayColumn][=\"OpenPrice\"\>]]        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\</][sfwg][:][GridSummaryColumnDescriptor][\>]                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\</][SummaryColumns][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\</][sfwg][:][GridSummaryRowDescriptor][\>][ ]                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\</][SummaryRows][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\</][TableDescriptor][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Total Summary

[] 

These are aggregate function values calculated over all the records within the grouping grid and displayed within the grouping grid footer under a particular column. The following screen shot illustrates the total summary.

[] 

{border="0"}

Figure 96[]

CaptionRow Summary

[] 

These are the aggregate function values calculated over all the records within a group and displayed in the caption cells. The following screen shot illustrates the caption row summary.

[] 

{border="0"}

Figure 97

[]{#p76} 

More:











