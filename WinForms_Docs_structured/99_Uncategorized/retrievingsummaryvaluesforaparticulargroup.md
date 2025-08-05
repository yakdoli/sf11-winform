---
title: retrievingsummaryvaluesforaparticulargroup.md
original_path: WinForms_Docs/99_Uncategorized/retrievingsummaryvaluesforaparticulargroup.md
created_at: 2025-08-05
---








  









### Retrieving Summary Values for a Particular Group {#retrieving-summary-values-for-a-particular-group style="tab-stops: 0pt"}

[] 

After adding the **SummaryDescriptor**, the GroupingEngine will maintain these summary items in a group by group basis. You can access these summary values for any group. Here we will get the values for the **TopLevelGroup** and for our c1 group to illustrate how this is done.

[] 

To obtain a particular group\'s summary values, you need to get the group and access the summary through its **GetSummary** method. Once you have the summary, you can caste it to its **Int32AggregateSummary** type.

[] 

The following code snippet illustrates this.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                               |
|                                                                                                                                                                              |
| []                                                                                                                                                     |
|                                                                                                                                                                              |
| [// To simplify notation, add this statement at the top of the file.]                                                      |
|                                                                                                                                                                              |
| [using][ ISummary = Syncfusion.Collections.BinaryTree.ITreeTableSummary;] |
|                                                                                                                                                                              |
| []                                                                                                                         |
|                                                                                                                                                                              |
| [// At the bottom of the Main method, add these lines.]                                                                    |
|                                                                                                                                                                              |
| []                                                                                                                         |
|                                                                                                                                                                              |
| [// Now go through the group to get the Summary value for the group.]                                                      |
|                                                                                                                                                                              |
| [ISummary groupSummary = groupingEngine.Table.TopLevelGroup.GetSummary(\"BInt32Agg\");]                                    |
|                                                                                                                                                                              |
| [Int32AggregateSummary int32Summary = (Int32AggregateSummary) groupSummary;]                                               |
|                                                                                                                                                                              |
| []                                                                                                                         |
|                                                                                                                                                                              |
| [Console.WriteLine(\"whole table {0}, {1}, {2}\", int32Summary.Sum, int32Summary.Average, int32Summary.Maximum);]          |
|                                                                                                                                                                              |
| [         ]                                                                                                                |
|                                                                                                                                                                              |
| [// Value for \"c1\" group.]                                                                                               |
|                                                                                                                                                                              |
| [groupSummary = groupingEngine.Table.TopLevelGroup.Groups\[\"c1\"\].GetSummary(\"BInt32Agg\");]                            |
|                                                                                                                                                                              |
| [int32Summary = (Int32AggregateSummary) groupSummary;]                                                                     |
|                                                                                                                                                                              |
| []                                                                                                                         |
|                                                                                                                                                                              |
| [Console.WriteLine(\"c1-group {0}, {1}, {2}\", int32Summary.Sum, int32Summary.Average,int32Summary. Maximum);]             |
|                                                                                                                                                                              |
| []                                                                                                                         |
|                                                                                                                                                                              |
| [// Pause]                                                                                                                 |
|                                                                                                                                                                              |
| [Console.ReadLine(); ]                                                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\' At the bottom of the Main method, add these lines.]                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\' Now go through the group to get the Summary value for the group.]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Dim][ groupSummary ][As][ Syncfusion.Collections.BinaryTree.ITreeTable = groupingEngine.Table.TopLevelGroup.GetSummary(\"BInt32Agg\")]                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Dim][ int32Summary ][As][ Int32AggregateSummary = ][CType][(groupSummary, Int32AggregateSummary)] |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Console.WriteLine(\"whole table {0}, {1}, {2}\", int32Summary.Sum, int32Summary.Average, int32Summary.Maximum)]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\' Value for \"c1\" group.]                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| [groupSummary = groupingEngine.Table.TopLevelGroup.Groups(\"c1\").GetSummary(\"BInt32Agg\")]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| [int32Summary = ][CType][(groupSummary, Int32AggregateSummary)]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Console.WriteLine(\"c1-group {0}, {1}, {2}\", int32Summary.Sum, int32Summary.Average, int32Summary.Maximum)]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\' Pause]                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Console.ReadLine() ]                                                                                                                                                                                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[{border="0"}]

Figure 16: Summary Statistics Shown for the Whole Table and for Group c1

[]{#related-topics}

