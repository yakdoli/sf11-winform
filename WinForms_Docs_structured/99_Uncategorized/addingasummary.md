---
title: addingasummary.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\addingasummary.md
created_at: 2025-07-03
---








  









### Adding a Summary {#adding-a-summary style="tab-stops: 0pt"}

 

Essential Grouping lets you summarize your data by adding **SummaryDescriptor** objects to the schema information that is stored in the **Engine.TableDescriptor.Summaries** collection. You can have multiple summaries by adding several **SummaryDescriptors**.

 

At the bottom of the Main method, add this code to create a summary item for the Engine.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                     |
| [// Create a summary that computes the Int32Aggregate calculations on property B.]                                                                                                                                |
|                                                                                                                                                                                                                                                                     |
| [SummaryDescriptor sdBInt32Agg = ][new][ SummaryDescriptor(\"BInt32Agg\", \"B\", SummaryType.Int32Aggregate);] |
|                                                                                                                                                                                                                                                                     |
| [        ]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                     |
| [// Add this summary to the Summaries collection.]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                     |
| [groupingEngine.TableDescriptor.Summaries.Add(sdBInt32Agg);]                                                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                          |
| [\' Create a summary that computes the Int32Aggregate calculations on property B.]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                          |
| [Dim][ sdBInt32Agg ][As New][ SummaryDescriptor(\"BInt32Agg\", \"B\", SummaryType.Int32Aggregate)] |
|                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                          |
| [\' Add this summary to the Summaries collection.]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                          |
| [groupingEngine.TableDescriptor.Summaries.Add(sdBInt32Agg)]                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"} There are several overloads of the constructor for SummaryDescriptor. Here, we are using the overload that accepts a **SummaryType** enum as the third argument. This SummaryType will allow you to pick out some predefined calculations such as the **Int32Aggregate** functions like **Max**, **Min**, **Sum**, and **Average**. There are enums that specify double, boolean, and other aggregate types. Here, we choose Int32 as that is the type of value you will see in the B property in the data.

 

[]{#related-topics}

