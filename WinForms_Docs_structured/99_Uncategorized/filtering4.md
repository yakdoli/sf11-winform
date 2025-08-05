---
title: filtering4.md
original_path: WinForms_Docs/99_Uncategorized/filtering4.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Filtering {#filtering style="tab-stops: 0pt"}

Filtered data displays only a subset of data that meets criteria that you specify and hides data that you do not want displayed. Filters are automatically reapplied every time the PivotGrid is refreshed or updated. In the PivotGrid, filters are additive, which means that each additional filter is based on the current filter and further reduces the subset of data. We can apply *n* number of filtering conditions to the grid at a time. Data is filtered based on the filter expression specified.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                          |
| [// Adding filters with filter expressions]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                          |
| [this] [.PivotGridControl1.Filters.Add([new][FilterExpression] { Expression=[\"Product = Bike\" ]Name=[\"Product Filter\"] });] [] |
|                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                |
| [\' Adding filters with filter expressions] []                                                                                                                           |
|                                                                                                                                                                                                                                                                |
| [Me] [.PivotGridControl1.Filters.Add([New] FilterExpression [With] {.Expression=\"Product = Bike\" .Name=\"Product Filter\" })] |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

