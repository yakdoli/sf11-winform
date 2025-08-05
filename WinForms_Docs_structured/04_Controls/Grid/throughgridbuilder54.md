---
title: throughgridbuilder54.md
original_path: WinForms_Docs/04_Controls/Grid/throughgridbuilder54.md
created_at: 2025-08-05
---






#### Through GridBuilder {#through-gridbuilder style="tab-stops: 0pt"}

The steps to work with the stacked header feature through **GridBuilder** are as follows:

1.   Create a model in the application.

2.   Create a strongly typed view.

3.   In the view use the **Model** property in the **Datasource()** to bind the data source.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                            |
| [\<%][=][Html.Grid\<[ProductCategory]\>([\"ProductGrid\"]).Datasource(Model)] |
|                                                                                                                                                                                                                                                                            |
| [        .Caption([\"Product\"])]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                            |
| [         \-\-\-\-\--]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                            |
| [        .Column(columns =\>]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                            |
| [        {]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                            |
| [            columns.Add(c =\> c.ProductID);]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                            |
| [            columns.Add(c =\> c.ProductName);]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                            |
| [            columns.Add(c =\> c.CategoryID);]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                            |
| [            columns.Add(c =\> c.CategoryName);]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                            |
| [            columns.Add(c =\> c.Description);]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                            |
| [            columns.Add(c =\> c.UnitsInStock);]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                            |
| [            columns.Add(c =\> c.UnitPrice);]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                            |
| [            columns.Add(c =\> c.QuantityPerUnit);]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                            |
| [        })]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                            |
| [        .StackedHeader(sh =\>]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                            |
| [        {]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                            |
| [            sh.StackedRows([\"Row1\"], sr1 =\>]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                            |
| [            {]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                            |
| [                 sr1.StackedColumn([\"Products\"], ac =\>]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                            |
| [                    {]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                            |
| [                        ac.Add(c =\> c.ProductID);]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                            |
| [                        ac.Add(c =\> c.ProductName);]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                            |
| [                        ac.Add(c =\> c.CategoryID);]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                            |
| [                        ac.Add(c =\> c.CategoryName);]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                            |
| [                        ac.Add(c =\> c.Description);]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                            |
| [                    });]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                            |
| [                sr1.StackedColumn([\"Orders\"], ac =\>]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                            |
| [                    {]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                            |
| [                        ac.Add(cc =\> cc.UnitsInStock);]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                            |
| [                        ac.Add(cc =\> cc.UnitPrice);]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                            |
| [                        ac.Add(cc =\> cc.QuantityPerUnit);]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                            |
| [                    });]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                            |
| [            });]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                            |
| [            sh.StackedRows([\"Row2\"], sr2 =\>]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                            |
| [            {]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                            |
| [                sr2.StackedColumn([\"Product Details\"], cc =\>]                                                                                                                                              |
|                                                                                                                                                                                                                                                                            |
| [                {]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                            |
| [                    cc.Add(c =\> c.ProductID);]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                            |
| [                    cc.Add(c =\> c.ProductName);]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                            |
| [                });]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                            |
| [                sr2.StackedColumn([\"Category Details\"], c =\>]                                                                                                                                              |
|                                                                                                                                                                                                                                                                            |
| [                {]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                            |
| [                    c.Add(cc =\> cc.CategoryID);]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                            |
| [                    c.Add(cc =\> cc.CategoryName);]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                            |
| [                    c.Add(cc =\> cc.Description);]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                            |
| [                });]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                            |
| [                sr2.StackedColumn([\"Order Details\"], c =\>]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                            |
| [                {]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                            |
| [                    c.Add(cc =\> cc.UnitsInStock);]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                            |
| [                    c.Add(cc =\> cc.UnitPrice);]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                            |
| [                    c.Add(cc =\> cc.QuantityPerUnit);]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                            |
| [                });]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                            |
| [        });]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                            |
| [        })]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                            |
| [        .ShowStackedHeader([true])]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                            |
| [        ]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                            |
| [    [%\>]]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                    |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [\@{][Html.Grid\<[ProductCategory]\>([\"ProductGrid\"]).Datasource(Model)] |
|                                                                                                                                                                                                                        |
| [        .Caption([\"Product\"])]                                                                                                                          |
|                                                                                                                                                                                                                        |
| [         \-\-\-\-\-\--]                                                                                                                                                           |
|                                                                                                                                                                                                                        |
| [        .Column(columns =\>]                                                                                                                                                      |
|                                                                                                                                                                                                                        |
| [        {]                                                                                                                                                                        |
|                                                                                                                                                                                                                        |
| [            columns.Add(c =\> c.ProductID);]                                                                                                                                      |
|                                                                                                                                                                                                                        |
| [            columns.Add(c =\> c.ProductName);]                                                                                                                                    |
|                                                                                                                                                                                                                        |
| [            columns.Add(c =\> c.CategoryID);]                                                                                                                                     |
|                                                                                                                                                                                                                        |
| [            columns.Add(c =\> c.CategoryName);]                                                                                                                                   |
|                                                                                                                                                                                                                        |
| [            columns.Add(c =\> c.Description);]                                                                                                                                    |
|                                                                                                                                                                                                                        |
| [            columns.Add(c =\> c.UnitsInStock);]                                                                                                                                   |
|                                                                                                                                                                                                                        |
| [            columns.Add(c =\> c.UnitPrice);]                                                                                                                                      |
|                                                                                                                                                                                                                        |
| [            columns.Add(c =\> c.QuantityPerUnit);]                                                                                                                                |
|                                                                                                                                                                                                                        |
| [        })]                                                                                                                                                                       |
|                                                                                                                                                                                                                        |
| [         ]                                                                                                                                                                        |
|                                                                                                                                                                                                                        |
| [        .StackedHeader(sh =\>]                                                                                                                                                    |
|                                                                                                                                                                                                                        |
| [        {]                                                                                                                                                                        |
|                                                                                                                                                                                                                        |
| [            sh.StackedRows([\"Row1\"], sr1 =\>]                                                                                                           |
|                                                                                                                                                                                                                        |
| [            {]                                                                                                                                                                    |
|                                                                                                                                                                                                                        |
| [                 sr1.StackedColumn([\"Products\"], ac =\>]                                                                                                |
|                                                                                                                                                                                                                        |
| [                    {]                                                                                                                                                            |
|                                                                                                                                                                                                                        |
| [                        ac.Add(c =\> c.ProductID);]                                                                                                                               |
|                                                                                                                                                                                                                        |
| [                        ac.Add(c =\> c.ProductName);]                                                                                                                             |
|                                                                                                                                                                                                                        |
| [                        ac.Add(c =\> c.CategoryID);]                                                                                                                              |
|                                                                                                                                                                                                                        |
| [                        ac.Add(c =\> c.CategoryName);]                                                                                                                            |
|                                                                                                                                                                                                                        |
| [                        ac.Add(c =\> c.Description);]                                                                                                                             |
|                                                                                                                                                                                                                        |
| [                    });]                                                                                                                                                          |
|                                                                                                                                                                                                                        |
| [                sr1.StackedColumn([\"Orders\"], ac =\>]                                                                                                   |
|                                                                                                                                                                                                                        |
| [                    {]                                                                                                                                                            |
|                                                                                                                                                                                                                        |
| [                        ac.Add(cc =\> cc.UnitsInStock);]                                                                                                                          |
|                                                                                                                                                                                                                        |
| [                        ac.Add(cc =\> cc.UnitPrice);]                                                                                                                             |
|                                                                                                                                                                                                                        |
| [                        ac.Add(cc =\> cc.QuantityPerUnit);]                                                                                                                       |
|                                                                                                                                                                                                                        |
| [                    });]                                                                                                                                                          |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [            });]                                                                                                                                                                  |
|                                                                                                                                                                                                                        |
| [            sh.StackedRows([\"Row2\"], sr2 =\>]                                                                                                           |
|                                                                                                                                                                                                                        |
| [            {]                                                                                                                                                                    |
|                                                                                                                                                                                                                        |
| [                sr2.StackedColumn([\"Product Details\"], cc =\>]                                                                                          |
|                                                                                                                                                                                                                        |
| [                {]                                                                                                                                                                |
|                                                                                                                                                                                                                        |
| [                    cc.Add(c =\> c.ProductID);]                                                                                                                                   |
|                                                                                                                                                                                                                        |
| [                    cc.Add(c =\> c.ProductName);]                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [                });]                                                                                                                                                              |
|                                                                                                                                                                                                                        |
| [                sr2.StackedColumn([\"Category Details\"], c =\>]                                                                                          |
|                                                                                                                                                                                                                        |
| [                {]                                                                                                                                                                |
|                                                                                                                                                                                                                        |
| [                    c.Add(cc =\> cc.CategoryID);]                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [                    c.Add(cc =\> cc.CategoryName);]                                                                                                                               |
|                                                                                                                                                                                                                        |
| [                    c.Add(cc =\> cc.Description);]                                                                                                                                |
|                                                                                                                                                                                                                        |
| [                });]                                                                                                                                                              |
|                                                                                                                                                                                                                        |
| [                sr2.StackedColumn([\"Order Details\"], c =\>]                                                                                             |
|                                                                                                                                                                                                                        |
| [                {]                                                                                                                                                                |
|                                                                                                                                                                                                                        |
| [                    c.Add(cc =\> cc.UnitsInStock);]                                                                                                                               |
|                                                                                                                                                                                                                        |
| [                    c.Add(cc =\> cc.UnitPrice);]                                                                                                                                  |
|                                                                                                                                                                                                                        |
| [                    c.Add(cc =\> cc.QuantityPerUnit);]                                                                                                                            |
|                                                                                                                                                                                                                        |
| [                });]                                                                                                                                                              |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [        });]                                                                                                                                                                      |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [        })]                                                                                                                                                                       |
|                                                                                                                                                                                                                        |
| [        .ShowStackedHeader([true]).Render();]                                                                                                                |
|                                                                                                                                                                                                                        |
| [        ]                                                                                                                                                                         |
|                                                                                                                                                                                                                        |
| [    [}]]                                                                                                                                              |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                             |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [public][ [ActionResult] StackedHeader()]                                                                           |
|                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [var][ data = [new] [NorthwindDataContext]().ProductCategories.ToList();]                      |
|                                                                                                                                                                                                                                  |
| [return][ View(data);]                                                                                                                      |
|                                                                                                                                                                                                                                  |
| [}[ PagingParams] args]                                                                                                                                              |
|                                                                                                                                                                                                                                  |
| [\[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                                                        |
|                                                                                                                                                                                                                                  |
| [public][ [ActionResult] StackedHeader([PagingParams] args)]                                |
|                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [IEnumerable][ data = [new] [NorthwindDataContext]().ProductCategories.Take(200).ToList();] |
|                                                                                                                                                                                                                                  |
| [return][ data.GridActions\<[ProductCategory]\>();]                                                                 |
|                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

[]{#related-topics}

