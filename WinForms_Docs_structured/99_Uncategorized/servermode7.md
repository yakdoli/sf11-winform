---
title: servermode7.md
original_path: WinForms_Docs/99_Uncategorized/servermode7.md
created_at: 2025-08-05
---






##### Server Mode {#server-mode style="tab-stops: 0pt"}

###### [5.9.2.2.1.1  ]Using GridBuilder[] {#using-gridbuilder style="tab-stops: 0pt"}

 

1.   Create a model in the application (Refer to [[Getting Started\>Adding a Model to the Application]]{.underline}).

2.   Create a strongly typed view (Refer to [[How to\>Strongly Typed View]]{.underline}).

3.   In the view, use the **Model** property in **Datasource()** to bind the data source.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**[]                                                                                                                                            |
|                                                                                                                                                                                                                                                              |
| [\<%][=][Html.Syncfusion().Grid\<[Product]\>([\"CustomGrid\"])] |
|                                                                                                                                                                                                                                                              |
| **[            .Datasource(Model)]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                              |
| [            .Caption([\"Products\"])]                                                                                                                                                           |
|                                                                                                                                                                                                                                                              |
| [            .ShowRowHeader([false])]                                                                                                                                                               |
|                                                                                                                                                                                                                                                              |
| [            .AutoFormat([Skins].Sandune)      ]                                                                                                                                                 |
|                                                                                                                                                                                                                                                              |
| [            .Column(column =\>{]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [                column.Add(c =\> c.ProductID).HeaderText([\"Product ID\"]);]                                                                                                                    |
|                                                                                                                                                                                                                                                              |
| [                column.Add(c =\> c.ProductName).HeaderText([\"Product Name\"]);]                                                                                                                |
|                                                                                                                                                                                                                                                              |
| [                column.Add(c =\> c.SupplierID).HeaderText([\"Supplier ID\"]);]                                                                                                                  |
|                                                                                                                                                                                                                                                              |
| [                column.Add(c =\> c.UnitPrice).HeaderText([\"Unit Price\"]);]                                                                                                                    |
|                                                                                                                                                                                                                                                              |
| [                column.Add(c =\> c.UnitsInStock).HeaderText([\"Units In Stock\"]);]                                                                                                             |
|                                                                                                                                                                                                                                                              |
| [                column.Add(c =\> c.UnitsOnOrder).HeaderText([\"Units On Order\"]);]                                                                                                             |
|                                                                                                                                                                                                                                                              |
| [                column.Add(c =\> c.ReorderLevel).HeaderText([\"Reorder Level\"]);]                                                                                                              |
|                                                                                                                                                                                                                                                              |
| [            }) ]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                              |
| [        [%\>]]                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**[]                                                                                                                                          |
|                                                                                                                                                                                                                                                              |
| [\@{][ ][Html.Syncfusion().Grid\<[Product]\>([\"CustomGrid\"])] |
|                                                                                                                                                                                                                                                              |
| **[            .Datasource(Model)]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                              |
| [            .Caption([\"Products\"])]                                                                                                                                                           |
|                                                                                                                                                                                                                                                              |
| [            .ShowRowHeader([false])]                                                                                                                                                               |
|                                                                                                                                                                                                                                                              |
| [            .AutoFormat([Skins].Sandune)      ]                                                                                                                                                 |
|                                                                                                                                                                                                                                                              |
| [            .Column(column =\>{]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                              |
| [                column.Add(c =\> c.ProductID).HeaderText([\"Product ID\"]);]                                                                                                                    |
|                                                                                                                                                                                                                                                              |
| [                column.Add(c =\> c.ProductName).HeaderText([\"Product Name\"]);]                                                                                                                |
|                                                                                                                                                                                                                                                              |
| [                column.Add(c =\> c.SupplierID).HeaderText([\"Supplier ID\"]);]                                                                                                                  |
|                                                                                                                                                                                                                                                              |
| [                column.Add(c =\> c.UnitPrice).HeaderText([\"Unit Price\"]);]                                                                                                                    |
|                                                                                                                                                                                                                                                              |
| [                column.Add(c =\> c.UnitsInStock).HeaderText([\"Units In Stock\"]);]                                                                                                             |
|                                                                                                                                                                                                                                                              |
| [                column.Add(c =\> c.UnitsOnOrder).HeaderText([\"Units On Order\"]);]                                                                                                             |
|                                                                                                                                                                                                                                                              |
| [                column.Add(c =\> c.ReorderLevel).HeaderText([\"Reorder Level\"]);]                                                                                                              |
|                                                                                                                                                                                                                                                              |
| [            }).Render(); ]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                              |
| [        [}]]                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Configure the **RowDataBound()** action as given below to perform custom formatting at the row level.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**[]                                                                                                                             |
|                                                                                                                                                                                                                                               |
| [\<%][=][Html.Syncfusion().Grid\<Product\>(\"CustomGrid\")]                                      |
|                                                                                                                                                                                                                                               |
| [            .Datasource(Model)]                                                                                                                                                                          |
|                                                                                                                                                                                                                                               |
| [            .Caption(\"Products\")            ]                                                                                                                                                          |
|                                                                                                                                                                                                                                               |
| [            ]**[.RowDataBound(row =\>]**                                                                                                             |
|                                                                                                                                                                                                                                               |
| **[                    {]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                               |
| **[                        [//Apply format to row whose unitPrices less than 20.]]**                                                                                                |
|                                                                                                                                                                                                                                               |
| **[                        [if] (row.Data.UnitPrice \< 20)]**                                                                                                                        |
|                                                                                                                                                                                                                                               |
| **[                            row.HtmlAttributes\[[\"style\"]\] = [\"background-color:#C3C3F2;color:#13771a;font-family:Verdana;font-weight:bold;\"];]** |
|                                                                                                                                                                                                                                               |
| **[                    })]**[    ]                                                                                                                    |
|                                                                                                                                                                                                                                               |
| [        [%\>]]                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**[]                                                                                                                           |
|                                                                                                                                                                                                                                               |
| [\@{][ ][Html.Syncfusion().Grid\<Product\>(\"CustomGrid\")]                                      |
|                                                                                                                                                                                                                                               |
| [            .Datasource(Model)]                                                                                                                                                                          |
|                                                                                                                                                                                                                                               |
| [            .Caption(\"Products\")            ]                                                                                                                                                          |
|                                                                                                                                                                                                                                               |
| [            ]**[.RowDataBound(row =\>]**                                                                                                             |
|                                                                                                                                                                                                                                               |
| **[                    {]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                               |
| **[                        [//Apply format to row whose unitPrices less than 20.]]**                                                                                                |
|                                                                                                                                                                                                                                               |
| **[                        [if] (row.Data.UnitPrice \< 20)]**                                                                                                                        |
|                                                                                                                                                                                                                                               |
| **[                            row.HtmlAttributes\[[\"style\"]\] = [\"background-color:#C3C3F2;color:#13771a;font-family:Verdana;font-weight:bold;\"];]** |
|                                                                                                                                                                                                                                               |
| **[                    })]**[.Render();[]]                                                                                                    |
|                                                                                                                                                                                                                                               |
| [        [}]]                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Run the application. The grid will appear as shown below.

{border="0"}

Figure 211: Dynamic Formatting Applied to the Grid Using RowDataBound()

 

###### [5.9.2.2.1.2  ]Using GridPropertiesModel[] {#using-gridpropertiesmodel style="tab-stops: 0pt"}

1.   Create a model in the application (Refer to [[Getting Started\>Adding a Model to the Application]]{.underline}).

2.   Add the following code in the **Index.aspx** file to create the Grid control in the view.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\][]]**                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                    |
| [\<%][=][Html.Syncfusion().Grid\<[Product]\>([\"Product_Grid\"],[\"GridModel\"], column=\> {] |
|                                                                                                                                                                                                                                                                                                                    |
| [                    column.Add(c =\> c.ProductID).HeaderText([\"Product ID\"]);]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                    |
| [                    column.Add(c =\> c.ProductName).HeaderText([\"Product Name\"]);]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                    |
| [                    column.Add(c =\> c.SupplierID).HeaderText([\"Supplier ID\"]);]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                    |
| [                    column.Add(c =\> c.UnitPrice).HeaderText([\"Unit Price\"]);]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                    |
| [                    column.Add(c =\> c.UnitsInStock).HeaderText([\"Units In Stock\"]);]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                    |
| [                    column.Add(c =\> c.UnitsOnOrder).HeaderText([\"Units On Order\"]);]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                    |
| [                    column.Add(c =\> c.ReorderLevel).HeaderText([\"Reorder Level\"]);]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                    |
| [    })[%\>]]                                                                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 


+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [ ][@(][new][ [HtmlString](][Html.Syncfusion().Grid\<[Product]\>([\"Product_Grid\"],[\"GridModel\"], column=\> {                    column.Add(c =\> c.ProductID).HeaderText([\"Product ID\"]);] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [                    column.Add(c =\> c.ProductName).HeaderText([\"Product Name\"]);]                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [                    column.Add(c =\> c.SupplierID).HeaderText([\"Supplier ID\"]);]                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [                    column.Add(c =\> c.UnitPrice).HeaderText([\"Unit Price\"]);]                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [                    column.Add(c =\> c.UnitsInStock).HeaderText([\"Units In Stock\"]);]                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [                    column.Add(c =\> c.UnitsOnOrder).HeaderText([\"Units On Order\"]);]                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [                    column.Add(c =\> c.ReorderLevel).HeaderText([\"Reorder Level\"]);  ]                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [  }).][ToString())[)] ][]                                                                                                                                                                                                                                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[                ][]

3.   Create a **GridPropertiesModel** in the **Index** method. Assign grid properties in this model and pass the model from the controller to the view using the **ViewData** class as shown below.

[        ]

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                               |
|                                                                                                                                                                                    |
| []                                                                                                                               |
|                                                                                                                                                                                    |
| [//Create a model and assign the data source.][]                                             |
|                                                                                                                                                                                    |
| [            [GridPropertiesModel] model = [new] [GridPropertiesModel]()] |
|                                                                                                                                                                                    |
| [            {]                                                                                                                                |
|                                                                                                                                                                                    |
| [  DataSource=[new] [NorthwindDataClassesDataContext]().Products,]                                |
|                                                                                                                                                                                    |
| [                Caption=[\"Product\"] ,]                                                                              |
|                                                                                                                                                                                    |
| [                AutoFormat=[Skins].Sandune]                                                                           |
|                                                                                                                                                                                    |
| []                                                                                                                                             |
|                                                                                                                                                                                    |
| [            };]                                                                                                                               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Create an action for the **RowDataBound()** action as given below to perform custom formatting at the row level.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                          |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                               |
| [       \[[ChildActionOnly]\]]                                                                                                                                    |
|                                                                                                                                                                                                                               |
| [        [public] [void] RowAction([GridTableRow]\<[Product]\> row)]                            |
|                                                                                                                                                                                                                               |
| [        {]                                                                                                                                                                               |
|                                                                                                                                                                                                                               |
| [            [//Apply style to row whose UnitPrices are less than 20.]]                                                                                             |
|                                                                                                                                                                                                                               |
| [            [if] (row.Data.UnitPrice \< 20)]                                                                                                                        |
|                                                                                                                                                                                                                               |
| [                row.HtmlAttributes\[[\"style\"]\] = [\"background-color:#C3C3F2;color:#13771a;font-family:Verdana;font-weight:bold;\"];] |
|                                                                                                                                                                                                                               |
| [        }]                                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Bind the action to **GridPropertiesModel** and pass the model to the view using the **ViewData** method as given below:

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**[]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [   GridPropertiesModel][\<[Product]\> model = [new] [GridPropertiesModel]\<[Product]\>()] |
|                                                                                                                                                                                                                                                                                 |
| [            {]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                 |
| [                DataSource = [new] [NorthwindDataContext]().Products.Take(20).ToList(),]                                                                                                      |
|                                                                                                                                                                                                                                                                                 |
| [                Caption = [\"Product\"],]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [                AutoFormat = [Skins].Sandune]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                 |
| [            };]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                 |
| **[            model.RowDataBound = RowAction;]**                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                 |
| [            ViewData\[[\"GridModel\"]\] = model;]                                                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

6.   Run the application. The grid will appear as shown below.

 

 

{border="0"}

Figure 212: Dynamic Formatting Applied to a Grid using RowDataBound()

[]{#related-topics}

