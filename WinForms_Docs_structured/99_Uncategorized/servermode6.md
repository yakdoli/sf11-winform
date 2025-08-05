---
title: servermode6.md
original_path: WinForms_Docs/99_Uncategorized/servermode6.md
created_at: 2025-08-05
---






##### Server Mode {#server-mode style="tab-stops: 0pt"}

###### [5.9.2.1.1.1  ]Using GridBuilder[] {#using-gridbuilder style="tab-stops: 0pt"}

 

1.   Create a model in the application (Refer to [[Getting Started\>Adding a Model to the Application]]{.underline}).

2.   Create a strongly typed view (Refer to [[How to\>Strongly Typed View]]{.underline}).

3.   In the view, you can use its **Model** property in **Datasource()** to bind the data source.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                                      |
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
| [                column.Add(c =\> c.UnitPrice).HeaderText([\"Unit Price\"]);]                                                                                                                    |
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

 

 

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**                                                                                                                                                                                                    |
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
| [            }).Render();]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                              |
| [        [}]]                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.   Configure the **QueryCellInfo()** action as shown below to perform custom formatting at the cell level.

 

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                             |
| [\<%][=][Html.Syncfusion().Grid\<Product\>(\"CustomGrid\")]                                                                    |
|                                                                                                                                                                                                                                                                             |
| [            .Datasource(Model)]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                             |
| [            .Caption(\"Products\")            ]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                             |
| [            **.QueryCellInfo( cell =\>** ]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                             |
| **[                {]**                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                             |
| **[                    [if] (cell.TableCellType == [GridTableCellType].RecordFieldCell \|\| cell.TableCellType == [GridTableCellType].AlternateRecordFieldCell)]** |
|                                                                                                                                                                                                                                                                             |
| **[                    {]**                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                             |
| **[                        ]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                             |
| **[                        [if] (cell.Column.MappingName == [\"UnitsInStock\"])]**                                                                                                         |
|                                                                                                                                                                                                                                                                             |
| **[                        {]**                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                             |
| **[                            [if] (cell.Data.UnitsInStock \<= 30)]**                                                                                                                                             |
|                                                                                                                                                                                                                                                                             |
| **[                                cell.HtmlAttributes\[[\"style\"]\] = [\"color:Blue;background-color:Chocolate;\"];                                ]**                                |
|                                                                                                                                                                                                                                                                             |
| **[                        }]**                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                             |
| **[                        [if] (cell.Column.MappingName == [\"ReorderLevel\"])]**                                                                                                         |
|                                                                                                                                                                                                                                                                             |
| **[                        {]**                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                             |
| **[                            [if] (cell.Data.UnitsInStock \< 25)]**                                                                                                                                              |
|                                                                                                                                                                                                                                                                             |
| **[                                cell.HtmlAttributes\[[\"style\"]\] = [\"color:#ac0c0c;background-color:Bisque;\"];]**                                                                |
|                                                                                                                                                                                                                                                                             |
| **[                        }               ]**                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                             |
| **[       })]**[     ]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                             |
| [ [%\>]]                                                                                                                                                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                             |
| [\@{][ ][Html.Syncfusion().Grid\<Product\>(\"CustomGrid\")]                                                                    |
|                                                                                                                                                                                                                                                                             |
| [            .Datasource(Model)]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                             |
| [            .Caption(\"Products\")            ]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                             |
| [            **.QueryCellInfo( cell =\>** ]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                             |
| **[                {]**                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                             |
| **[                    [if] (cell.TableCellType == [GridTableCellType].RecordFieldCell \|\| cell.TableCellType == [GridTableCellType].AlternateRecordFieldCell)]** |
|                                                                                                                                                                                                                                                                             |
| **[                    {]**                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                             |
| **[                        ]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                             |
| **[                        [if] (cell.Column.MappingName == [\"UnitsInStock\"])]**                                                                                                         |
|                                                                                                                                                                                                                                                                             |
| **[                        {]**                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                             |
| **[                            [if] (cell.Data.UnitsInStock \<= 30)]**                                                                                                                                             |
|                                                                                                                                                                                                                                                                             |
| **[                                cell.HtmlAttributes\[[\"style\"]\] = [\"color:Blue;background-color:Chocolate;\"];                                ]**                                |
|                                                                                                                                                                                                                                                                             |
| **[                        }]**                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                             |
| **[                        [if] (cell.Column.MappingName == [\"ReorderLevel\"])]**                                                                                                         |
|                                                                                                                                                                                                                                                                             |
| **[                        {]**                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                             |
| **[                            [if] (cell.Data.UnitsInStock \< 25)]**                                                                                                                                              |
|                                                                                                                                                                                                                                                                             |
| **[                                cell.HtmlAttributes\[[\"style\"]\] = [\"color:#ac0c0c;background-color:Bisque;\"];]**                                                                |
|                                                                                                                                                                                                                                                                             |
| **[                        }     ]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                             |
| **[                 })]**[.Render();]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                             |
| [        [}]]                                                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

5.   Run the application. The grid will appear as shown below.

 

 

{border="0"}

Figure 207: Dynamic Formatting Applied to the Grid using QueryCellInfo

**[]** 

**[]** 

###### [5.9.2.1.1.2  ]Using GridPropertiesModel[] {#using-gridpropertiesmodel style="tab-stops: 0pt"}

1.   Create a model in the application (Refer to [[Getting Started\>Adding a Model to the Application]]{.underline}).

2.   Add the following code in the **Index.aspx** file to create the Grid control in the view.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]][]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                   |
| [\<%][=][Html.Syncfusion().Grid\<[Product]\>([\"Orders_Grid\"],[\"GridModel\"], column=\> {] |
|                                                                                                                                                                                                                                                                                                                   |
| [                    column.Add(c =\> c.ProductID).HeaderText([\"Product ID\"]);]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                   |
| [                    column.Add(c =\> c.ProductName).HeaderText([\"Product Name\"]);]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                   |
| [                    column.Add(c =\> c.SupplierID).HeaderText([\"Supplier ID\"]);]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                   |
| [                    column.Add(c =\> c.UnitPrice).HeaderText([\"Unit Price\"]);]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                   |
| [                    column.Add(c =\> c.UnitsInStock).HeaderText([\"Units In Stock\"]);]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                   |
| [                    column.Add(c =\> c.UnitsOnOrder).HeaderText([\"Units On Order\"]);]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                   |
| [                    column.Add(c =\> c.ReorderLevel).HeaderText([\"Reorder Level\"]);    })[%\>]]                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 


+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [ ][@(][new][ [HtmlString](][Html.Syncfusion().Grid\<[Product]\>([\"Orders_Grid\"],[\"GridModel\"], column=\> {] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                    column.Add(c =\> c.ProductID).HeaderText([\"Product ID\"]);]                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                    column.Add(c =\> c.ProductName).HeaderText([\"Product Name\"]);]                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                    column.Add(c =\> c.SupplierID).HeaderText([\"Supplier ID\"]);]                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                    column.Add(c =\> c.UnitPrice).HeaderText([\"Unit Price\"]);]                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                    column.Add(c =\> c.UnitsInStock).HeaderText([\"Units In Stock\"]);]                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                    column.Add(c =\> c.UnitsOnOrder).HeaderText([\"Units On Order\"]);]                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [                    column.Add(c =\> c.ReorderLevel).HeaderText([\"Reorder Level\"]);    }).][ToString())[)]    ][    ][]                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[                                                                     ][  ]**[]**

[] 

3.   Create a **GridPropertiesModel** in the **Index** method. Assign grid properties in this model and pass the model from the controller to the view using the **ViewData** class as shown below.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                           |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [        [// Create a model and assign a data source.]]                                                              |
|                                                                                                                                                                                |
| [        [GridPropertiesModel] model = [new] [GridPropertiesModel]()] |
|                                                                                                                                                                                |
| [        {]                                                                                                                                |
|                                                                                                                                                                                |
| [  DataSource=[new] [NorthwindDataClassesDataContext]().Products,]                            |
|                                                                                                                                                                                |
| [            Caption=[\"Product\"] ,]                                                                              |
|                                                                                                                                                                                |
| [            AutoFormat=[Skins].Sandune]                                                                           |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [        };]                                                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.   Create an action for the **QueryCellInfo()** action as shown below to perform custom formatting in cell level.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                 |
| [        \[[ChildActionOnly]\]]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                 |
| [        [public] [void] QueryAction([GridTableCell]\<[Product]\> cell)]                                                          |
|                                                                                                                                                                                                                                                                 |
| [        {]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                 |
| [            [// TableCellType is validation. Check for Record field cells.]]                                                                                                                         |
|                                                                                                                                                                                                                                                                 |
| [            [if] (cell.TableCellType == [GridTableCellType].RecordFieldCell \|\| cell.TableCellType == [GridTableCellType].AlternateRecordFieldCell)] |
|                                                                                                                                                                                                                                                                 |
| [            {]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                 |
| [        ]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                 |
| [                [if] (cell.Column.MappingName == [\"UnitsInStock\"])]                                                                                                         |
|                                                                                                                                                                                                                                                                 |
| [                {]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                 |
| [                    [if] (cell.Data.UnitsInStock \<= 30)]                                                                                                                                             |
|                                                                                                                                                                                                                                                                 |
| [                    {]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                 |
| [                        [// Apply background color and font style for the record field cell.]]                                                                                                       |
|                                                                                                                                                                                                                                                                 |
| [                        cell.HtmlAttributes\[[\"style\"]\] = [\"color:Blue;background-color:Chocolate;\"];]                                                                |
|                                                                                                                                                                                                                                                                 |
| [                    }]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                 |
| [                }]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                 |
| [                [if] (cell.Column.MappingName == [\"ReorderLevel\"])]                                                                                                         |
|                                                                                                                                                                                                                                                                 |
| [                {]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                 |
| [                    [if] (cell.Data.UnitsInStock \< 25)]                                                                                                                                              |
|                                                                                                                                                                                                                                                                 |
| [                    {]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                 |
| [                        [// Apply background color and font style for the record field cell.]]                                                                                                       |
|                                                                                                                                                                                                                                                                 |
| [                        cell.HtmlAttributes\[[\"style\"]\] = [\"color:#ac0c0c;background-color:Bisque;\"];]                                                                |
|                                                                                                                                                                                                                                                                 |
| [                    }]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                 |
| [                }]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                 |
| [            }]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

5.   Bind the action to **GridPropertiesModel** and pass the model to the view using the **View Data** method as given below:

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                         |
| [           GridPropertiesModel][\<[Product]\> model = [new] [GridPropertiesModel]\<[Product]\>()] |
|                                                                                                                                                                                                                                                                                         |
| [            {]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                         |
| [                DataSource = [new] [NorthwindDataContext]().Products.Take(20).ToList(),]                                                                                                              |
|                                                                                                                                                                                                                                                                                         |
| [                Caption = [\"Product\"],]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                         |
| [                AutoFormat = [Skins].Sandune]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                         |
| [            };]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                         |
| **[            model.QueryCellInfo = QueryAction;]**                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                         |
| [            ViewData\[[\"GridModel\"]\] = model;]                                                                                                                                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

6.   Run the application. The grid will appear as shown below.

 

{border="0"}

Figure 208: Dynamic Formatting Applied to Grid Using QueryCellInfo

 

[]{#related-topics}

