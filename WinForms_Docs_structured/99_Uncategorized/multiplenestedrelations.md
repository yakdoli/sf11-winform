---
title: multiplenestedrelations.md
original_path: WinForms_Docs/99_Uncategorized/multiplenestedrelations.md
created_at: 2025-08-05
---






##### Multiple Nested Relations {#multiple-nested-relations style="tab-stops: 0pt"}

[] 

Grid Data Bound Grid control supports multiple nested relations. A relation can be added in the data source and the data source can be set to the Grid Data Bound Grid. Then the name of the relation can be passed through the **Grid.Binder.AddRelation** function to show a hierarchical pattern.

 

**Example:**

 

This following code example illustrates the display of a DataSet with multiple nested relations. The sample displays the NorthWind\'s \'Category\', \'Products\' and the \'Orders_Details\' table, and allows you to expand and collapse the order details for each order and the products for each category. After adding a relation in the dataset and setting the DataSource to the grid, the name of the relation is passed through the Grid.Binder.AddRelation function in order to show a hierarchical pattern.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                        |
|                                                                                                                                                                                                                       |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                                       |
| [GridHierarchyLevel][ hlCategory_Products = gridBinder.AddRelation([\"Category_Products\"]);]         |
|                                                                                                                                                                                                                       |
| [GridHierarchyLevel][ hlProducts_OrderDetails = gridBinder.AddRelation([\"Products_OrderDetails\"]);] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                              |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                 |
| [Dim][ hlCategory_Products [As] GridHierarchyLevel = gridBinder.AddRelation([\"Category_Products\"])]         |
|                                                                                                                                                                                                                                                 |
| [Dim][ hlProducts_OrderDetails [As] GridHierarchyLevel = gridBinder.AddRelation([\"Products_OrderDetails\"])] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

*[Figure ][216][: Expand Grid]*

[] 

A sample demonstrating this feature is available under the following sample installation path.

[] 

***\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Windows\\Samples\\2.0\\Data Bound\\Hierarchy\\Expand Grid Demo***

 

[]{#p380} 

 

[]{#related-topics}

