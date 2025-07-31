---
title: subsetelement.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\subsetelement.md
created_at: 2025-07-03
---








  









### Subset Element {#subset-element style="tab-stops: 0pt"}

Subset Elements are used to filter the result set by their count. It will just filter the number records and number of fields in the result set.

The following codes will illustrate the creation of a Subset Element:

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]                                                  ]**                                                                 |
|                                                                                                                                                                    |
| [SubsetElement][ subSetElementColumn = [new] [SubsetElement](5);\ |
| subSetElementColumn.Name = [\"Top 5 Elements\"];\                                                                                          |
| [SubsetElement] subSetElementRow = [new] [SubsetElement](3);\                                 |
| subSetElementRow.Name = [\"Top 3 Elements\"];]                                                         |
|                                                                                                                                                                    |
| [olapReport.CategoricalElements.SubSetElement = subSetElementColumn;]                                                          |
|                                                                                                                                                                    |
| [olapReport.SeriesElements.SubSetElement = subSetElementRow;][]                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                       |
|                                                                                                                                                                                                        |
| [Dim][ subSetElementColumn [As] SubsetElement = [New] SubsetElement(5)] |
|                                                                                                                                                                                                        |
| [subSetElementColumn.Name = ][\"Top 5 Elements\"][]                        |
|                                                                                                                                                                                                        |
| [Dim][ subSetElementRow [As] SubsetElement = [New] SubsetElement(3)]    |
|                                                                                                                                                                                                        |
| [subSetElementRow.Name = ][\"Top 3 Elements\"][]                           |
|                                                                                                                                                                                                        |
| [olapReport.CategoricalElements.SubSetElement = subSetElementColumn]                                                                                               |
|                                                                                                                                                                                                        |
| [olapReport.SeriesElements.SubSetElement = subSetElementRow]                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

