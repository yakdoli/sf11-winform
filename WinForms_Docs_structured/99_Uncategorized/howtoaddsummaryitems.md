---
title: howtoaddsummaryitems.md
original_path: WinForms_Docs/99_Uncategorized/howtoaddsummaryitems.md
created_at: 2025-08-05
---








  









## How to Add Summary Items? {#how-to-add-summary-items style="tab-stops: 0pt"}

[] 

Essential Grouping lets you summarize data by adding **SummaryDescriptor** objects to the schema information stored in the **Engine.TableDescriptor.Summaries** collection. You can have multiple summaries by adding several SummaryDescriptors.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                          |
| [// Create a summary that computes the Int32Aggregate calculations on field B.]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                          |
| [SummaryDescriptor][ sdBInt32Agg = [new] [SummaryDescriptor]([\"BInt32Agg\"], [\"B\"], [SummaryType].Int32Aggregate);] |
|                                                                                                                                                                                                                                                                                                                          |
| [        ]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                          |
| [// Add this summary to the Summaries collection.]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                          |
| [groupingEngine.TableDescriptor.Summaries.Add(sdBInt32Agg);]                                                                                                                                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [\' Create a summary that computes the Int32Aggregate calculations on property B.]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [Dim][ sdBInt32Agg ][As New][ SummaryDescriptor(\"BInt32Agg\", \"B\", SummaryType.Int32Aggregate)] |
|                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [\' Add this summary to the Summaries collection.]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [groupingEngine.TableDescriptor.Summaries.Add(sdBInt32Agg)]                                                                                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

{border="0"}Note: There are several overloads of the constructor for the SummaryDescriptor. We are using the overload that accepts a SummaryType enum as the third argument. This SummaryType will allow you to pick out some predefined calculations such as the Int32Aggregate functions like Max, Min, Sum and Average. There are enums that specify double, boolean, and other aggregate types. Here we choose Int32 as that is the type of value we see in the B property in the data.


 

[]{#related-topics}

