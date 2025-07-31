---
title: throughgridpropertiesmodel53.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\throughgridpropertiesmodel53.md
created_at: 2025-07-03
---






#### Through GridPropertiesModel {#through-gridpropertiesmodel style="tab-stops: 0pt"}

The steps to work with the stacked header feature through **GridPropertiesModel** are as follows:

1.   Create a model in the application.

2.   Create a strongly typed view

3.   Add the following code to the view.

                    []

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                       |
|                                                                                                                                                                          |
| []                                                                                                                                   |
|                                                                                                                                                                          |
| [\<%][=Html.Syncfusion().Grid\<[ProductCategory]\>(] |
|                                                                                                                                                                          |
| [                     [\"ProductGrid1\"], [\"GridModel\"],]                          |
|                                                                                                                                                                          |
| [           columns =\>]                                                                                                             |
|                                                                                                                                                                          |
| [           {]                                                                                                                       |
|                                                                                                                                                                          |
| [                 columns.Add(c =\> c.ProductID);]                                                                                   |
|                                                                                                                                                                          |
| [                 columns.Add(c =\> c.ProductName);]                                                                                 |
|                                                                                                                                                                          |
| [                 columns.Add(c =\> c.CategoryID);]                                                                                  |
|                                                                                                                                                                          |
| [                 columns.Add(c =\> c.CategoryName);]                                                                                |
|                                                                                                                                                                          |
| [                 columns.Add(c =\> c.Description);]                                                                                 |
|                                                                                                                                                                          |
| [                 columns.Add(c =\> c.UnitsInStock);]                                                                                |
|                                                                                                                                                                          |
| [                 columns.Add(c =\> c.UnitPrice);]                                                                                   |
|                                                                                                                                                                          |
| [                 columns.Add(c =\> c.QuantityPerUnit);]                                                                             |
|                                                                                                                                                                          |
| [            }).Render();]                                                                                                           |
|                                                                                                                                                                          |
| [                                                                              ]                                                     |
|                                                                                                                                                                          |
| [ [%\>]]                                                                                                 |
|                                                                                                                                                                          |
| []                                                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                     |
|                                                                                                                                                                         |
| []                                                                                                                                  |
|                                                                                                                                                                         |
| [\@{][Html.Syncfusion().Grid\<[ProductCategory]\>(] |
|                                                                                                                                                                         |
| [                     [\"ProductGrid\"], [\"GridModel\"],]                          |
|                                                                                                                                                                         |
| [           columns =\>]                                                                                                            |
|                                                                                                                                                                         |
| [           {]                                                                                                                      |
|                                                                                                                                                                         |
| [                 columns.Add(c =\> c.ProductID);]                                                                                  |
|                                                                                                                                                                         |
| [                 columns.Add(c =\> c.ProductName);]                                                                                |
|                                                                                                                                                                         |
| [                 columns.Add(c =\> c.CategoryID);]                                                                                 |
|                                                                                                                                                                         |
| [                 columns.Add(c =\> c.CategoryName);]                                                                               |
|                                                                                                                                                                         |
| [                 columns.Add(c =\> c.Description);]                                                                                |
|                                                                                                                                                                         |
| [                 columns.Add(c =\> c.UnitsInStock);]                                                                               |
|                                                                                                                                                                         |
| [                 columns.Add(c =\> c.UnitPrice);]                                                                                  |
|                                                                                                                                                                         |
| [                 columns.Add(c =\> c.QuantityPerUnit);]                                                                            |
|                                                                                                                                                                         |
| [            }).Render();]                                                                                                          |
|                                                                                                                                                                         |
| [                                                                              ]                                                    |
|                                                                                                                                                                         |
| [ [}]]                                                                                                  |
|                                                                                                                                                                         |
| []                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Create a **GridPropertiesModel** in the **Index** method and assign the grid properties in the model.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                  |
| [GridPropertiesModel][\<[ProductCategory]\> gridModel = [new] [GridPropertiesModel]\<[ProductCategory]\>()] |
|                                                                                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                  |
| [      DataSource =[new] [NorthwindDataContext]().ProductCategories.ToList(),]                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                  |
| [      Caption = [\"Product\"],]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                  |
| [      \-\-\-\-\-\--]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                  |
| [      ShowStackedHeader = [true]]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                  |
| [};]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                  |
| [ViewData\[[\"GridModel\"]\] = gridModel;]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

5.   Enable **Stacked Header** by using the following settings.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                               |
| [GridStackedRows][\<[ProductCategory]\> Row1 = [new] [GridStackedRows]\<[ProductCategory]\>();]          |
|                                                                                                                                                                                                                                                                                               |
| [GridStackedColumns][\<[ProductCategory]\> Columns = [new] [GridStackedColumns]\<[ProductCategory]\>();] |
|                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                               |
| [Row1.HeaderText = [\"Row1\"];]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                               |
| [Columns = [new] [GridStackedColumns]\<[ProductCategory]\>();]                                                                                                                       |
|                                                                                                                                                                                                                                                                                               |
| [Columns.HeaderText = [\"Products\"];]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                               |
| [Columns.NestedStackedColumns.Add([new] [GridStackedColumns]\<[ProductCategory]\>() { MappingName = [\"ProductID\"] });]                                     |
|                                                                                                                                                                                                                                                                                               |
| [Columns.NestedStackedColumns.Add([new] [GridStackedColumns]\<[ProductCategory]\>() { MappingName = [\"ProductName\"] });]                                   |
|                                                                                                                                                                                                                                                                                               |
| [Columns.NestedStackedColumns.Add([new] [GridStackedColumns]\<[ProductCategory]\>() { MappingName = [\"CategoryID\"] });]                                    |
|                                                                                                                                                                                                                                                                                               |
| [Columns.NestedStackedColumns.Add([new] [GridStackedColumns]\<[ProductCategory]\>() { MappingName = [\"CategoryName\"] });]                                  |
|                                                                                                                                                                                                                                                                                               |
| [Columns.NestedStackedColumns.Add([new] [GridStackedColumns]\<[ProductCategory]\>() { MappingName = [\"Description\"] });]                                   |
|                                                                                                                                                                                                                                                                                               |
| [Row1.StackedColumnsCollection.Add(Columns);]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                               |
| [Columns = [new] [GridStackedColumns]\<[ProductCategory]\>();]                                                                                                                       |
|                                                                                                                                                                                                                                                                                               |
| [Columns.HeaderText = [\"Orders\"];]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                               |
| [Columns.NestedStackedColumns.Add([new] [GridStackedColumns]\<[ProductCategory]\>() { MappingName = [\"UnitsInStock\"] });]                                  |
|                                                                                                                                                                                                                                                                                               |
| [Columns.NestedStackedColumns.Add([new] [GridStackedColumns]\<[ProductCategory]\>() { MappingName = [\"UnitPrice\"] });]                                     |
|                                                                                                                                                                                                                                                                                               |
| [Columns.NestedStackedColumns.Add([new] [GridStackedColumns]\<[ProductCategory]\>() { MappingName = [\"QuantityPerUnit\"] });]                               |
|                                                                                                                                                                                                                                                                                               |
| [Row1.StackedColumnsCollection.Add(Columns);]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                               |
| [gridModel.GridStackedRows.Add(Row1);]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                               |
| [GridStackedRows][\<[ProductCategory]\> Row2 = [new] [GridStackedRows]\<[ProductCategory]\>();]          |
|                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                               |
| [Row2.HeaderText = [\"Row2\"];]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                               |
| [Columns = [new] [GridStackedColumns]\<[ProductCategory]\>();]                                                                                                                       |
|                                                                                                                                                                                                                                                                                               |
| [Columns.HeaderText = [\"Product Details\"];]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                               |
| [Columns.NestedStackedColumns.Add([new] [GridStackedColumns]\<[ProductCategory]\>() { MappingName = [\"ProductID\"] });]                                     |
|                                                                                                                                                                                                                                                                                               |
| [Columns.NestedStackedColumns.Add([new] [GridStackedColumns]\<[ProductCategory]\>() { MappingName = [\"ProductName\"] });]                                   |
|                                                                                                                                                                                                                                                                                               |
| [Row2.StackedColumnsCollection.Add(Columns);]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                               |
| [Columns = [new] [GridStackedColumns]\<[ProductCategory]\>();]                                                                                                                       |
|                                                                                                                                                                                                                                                                                               |
| [Columns.HeaderText = [\"Category Details\"];]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                               |
| [Columns.NestedStackedColumns.Add([new] [GridStackedColumns]\<[ProductCategory]\>() { MappingName = [\"CategoryID\"] });]                                    |
|                                                                                                                                                                                                                                                                                               |
| [Columns.NestedStackedColumns.Add([new] [GridStackedColumns]\<[ProductCategory]\>() { MappingName = [\"CategoryName\"] });]                                  |
|                                                                                                                                                                                                                                                                                               |
| [Columns.NestedStackedColumns.Add([new] [GridStackedColumns]\<[ProductCategory]\>() { MappingName = [\"Description\"] });]                                   |
|                                                                                                                                                                                                                                                                                               |
| [Row2.StackedColumnsCollection.Add(Columns);]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                               |
| [Columns = [new] [GridStackedColumns]\<[ProductCategory]\>();]                                                                                                                       |
|                                                                                                                                                                                                                                                                                               |
| [Columns.HeaderText = [\"Order Details\"];]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                               |
| [Columns.NestedStackedColumns.Add([new] [GridStackedColumns]\<[ProductCategory]\>() { MappingName = [\"UnitsInStock\"] });]                                  |
|                                                                                                                                                                                                                                                                                               |
| [Columns.NestedStackedColumns.Add([new] [GridStackedColumns]\<[ProductCategory]\>() { MappingName = [\"UnitPrice\"] });]                                     |
|                                                                                                                                                                                                                                                                                               |
| [Columns.NestedStackedColumns.Add([new] [GridStackedColumns]\<[ProductCategory]\>() { MappingName = [\"QuantityPerUnit\"] });]                               |
|                                                                                                                                                                                                                                                                                               |
| [Row2.StackedColumnsCollection.Add(Columns);]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                               |
| [gridModel.GridStackedRows.Add(Row2);]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

6.   Create a post method for Stacked Header action and bind the data source to grid as like below code.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                             |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [\[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                                                        |
|                                                                                                                                                                                                                                  |
| [public][ [ActionResult] StackedHeader([PagingParams] args)]                                |
|                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [IEnumerable][ data = [new] [NorthwindDataContext]().ProductCategories.Take(200).ToList();] |
|                                                                                                                                                                                                                                  |
| [return][ data.GridJSONActions\<[ProductCategory]\>();]                                                             |
|                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

