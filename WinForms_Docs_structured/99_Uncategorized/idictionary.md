---
title: idictionary.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\idictionary.md
created_at: 2025-07-03
---






##### IDictionary  {#idictionary style="tab-stops: 0pt"}

IDictionary supports for binding the Dictionary list to the chart series **BindingPathX** and **BindingPathsY** Values.

[] 

Sample Data Source

IDictionary is useful to bind this kind of data source.


Note: In this sample data, 0, 1, 2, 3 ...6 are the Keys and the CompanyExpenses are the Values.


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[]**                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [            ][SortedList][ Expenditure = [new] [SortedList]();] |
|                                                                                                                                                                                                                                                       |
| [            expenditure.Add(0, [new] [CompanyExpense]() { x = [\"Production\"], y = 20d });]                                                |
|                                                                                                                                                                                                                                                       |
| [            expenditure.Add(1, [new] [CompanyExpense]() { x = [\"Facilities\"], y = 23d });]                                                |
|                                                                                                                                                                                                                                                       |
| [            expenditure.Add(2, [new] [CompanyExpense]() { x = [\"Insurance\"], y = 12d });]                                                 |
|                                                                                                                                                                                                                                                       |
| [            expenditure.Add(3, [new] [CompanyExpense]() { x = [\"Licenses\"], y = 3d });]                                                   |
|                                                                                                                                                                                                                                                       |
| [            expenditure.Add(4, [new] [CompanyExpense]() { x = [\"Labor\"], y = 28d });]                                                     |
|                                                                                                                                                                                                                                                       |
| [            expenditure.Add(5, [new] [CompanyExpense]() { x = [\"Legal\"], y = 2d });]                                                      |
|                                                                                                                                                                                                                                                       |
| [            expenditure.Add(6, [new] [CompanyExpense]() { x = [\"Taxes\"], y = 10d });]                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

[            ]

Binding Data Source

Bind the data source, by using the following code.


{border="0"}Note: Set BindingPath to Key to bind the key of the dictionary to BindingPathX or BindingPathsY.


**[]** 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Xaml\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][syncfusion][:][ChartSeries][ BindingPathX][=\"Key\"][ BindingPathsY][=\"y\" ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [DataSource={StaticResource ][expenditure][}\>]                                                                                                                                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+-------------------------------------------------------------------------------+
| **[\[C#\]]**                              |
|                                                                               |
| []                                        |
|                                                                               |
| [Series.BindingPathX="Key";] |
|                                                                               |
| [Series.BindingPathsY ="y";] |
+-------------------------------------------------------------------------------+

[] 

[] 

[]{#related-topics}

