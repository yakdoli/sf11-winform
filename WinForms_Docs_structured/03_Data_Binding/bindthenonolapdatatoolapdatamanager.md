---
title: bindthenonolapdatatoolapdatamanager.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\bindthenonolapdatatoolapdatamanager.md
created_at: 2025-07-03
---








  









## Bind the Non-OLAP data to OlapDataManager {#bind-the-non-olap-data-to-olapdatamanager style="tab-stops: 0pt"}

To bind the Non-OLAP data, you should bind an item source to the OlapDataManager's item source property and give the Non-OLAP data report to process the given item source. The item source can be an Enumerable collection or an ITyped List.

The following code will illustrate the binding of the Non-OLAP data**.** Here we have used a sample Enumerable collection "ProductSalesCollection" and a sample Olap report "salesReport":

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                             |
|                                                                                                                                                                              |
| [ProductSalesCollection][ productSales = [new] [ProductSalesCollection]();\ |
| olapDataManager.ItemSource = productSales;\                                                                                                                                  |
|  \                                                                                                                                                                           |
| olapDataManager.SetCurrentReport(salesReport);][]                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                 |
|                                                                                                                                                                                                                  |
| **[      ]**                                                                                                                                                                 |
|                                                                                                                                                                                                                  |
| [Dim][ productSales [As] ProductSalesCollection = [New] ProductSalesCollection()] |
|                                                                                                                                                                                                                  |
| [olapDataManager.ItemSource = productSales]                                                                                                                                  |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                  |
| [olapDataManager.SetCurrentReport(salesReport)]                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Sequential Diagram

The following sequential diagram shows the workflow of OlapBase when the input is a Non-OLAP data:

{border="0"}

 

Figure 11: Olap base Sequential diagram

 

[]{#related-topics}

