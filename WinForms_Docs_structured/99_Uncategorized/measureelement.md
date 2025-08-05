---
title: measureelement.md
original_path: WinForms_Docs/99_Uncategorized/measureelement.md
created_at: 2025-08-05
---








  









### Measure Element {#measure-element style="tab-stops: 0pt"}

In a cube, a measure is a set of values that are based on a column in the cube\'s [[fact table]](http://msdn.microsoft.com/en-us/library/aa178239(SQL.80).aspx#olap:fact_table) and are usually numeric. In addition, measures are the central values of a cube that are analyzed. That is, measures are the numeric data of primary interest to end users browsing a cube. The measures you select depend on the types of information end users request. Some common measures are sales, cost, expenditures, and production count.

We can create a measure element just by specifying its name. The following code will illustrate the creation of a measure element:

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                             |
|                                                                                                                                                                                                              |
| **[      ]**                                                                                                                                                             |
|                                                                                                                                                                                                              |
| [MeasureElements][ measureElementColumn = [new] [MeasureElements]();]   |
|                                                                                                                                                                                                              |
| [//Specifying the Measure Elements]                                                                                                                        |
|                                                                                                                                                                                                              |
| [measureElementColumn.Elements.Add([new] [MeasureElement] { Name = [\"Internet Sales Amount\"] });] |
|                                                                                                                                                                                                              |
| [         ]                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                             |
|                                                                                                                                                                                                              |
| [      ]                                                                                                                                                                 |
|                                                                                                                                                                                                              |
| [Dim][ measureElementColumn [As] MeasureElements = [New] MeasureElements()]   |
|                                                                                                                                                                                                              |
| [\'Specifying the Measure Elements][]                                                                                  |
|                                                                                                                                                                                                              |
| [measureElementColumn.Elements.Add([New] MeasureElement [With] {.Name = [\"Internet Sales Amount\"]})] |
|                                                                                                                                                                                                              |
| []                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

