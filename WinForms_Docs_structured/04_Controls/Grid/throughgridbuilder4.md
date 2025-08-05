---
title: throughgridbuilder4.md
original_path: WinForms_Docs/04_Controls/Grid/throughgridbuilder4.md
created_at: 2025-08-05
---






#### Through GridBuilder {#through-gridbuilder style="tab-stops: 0pt"}

 

1.   Create a model in the application (Refer to [GettingStarted\>Adding a Model to the Application]{.UGHyperlink}).

2.   Create a strongly typed view (Refer to [[How to\>Strongly Typed View]]{.underline}).

3.   In the view you can use its **Model** property in **Datasource** to bind the data source.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                           |
| [\<%][=][Html.Syncfusion().Grid\<[Order]\>([\"OrderGrid\"])] |
|                                                                                                                                                                                                                                                           |
| **[       .Datasource(Model)]**                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                           |
| [       .Caption([\"Orders Grid\"]) ]                                                                                                                                                         |
|                                                                                                                                                                                                                                                           |
| [       [%\>]]                                                                                                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[][cshtml][\]]**                                                                  |
|                                                                                                                                                                                                        |
| []                                                                                                                                             |
|                                                                                                                                                                                                        |
| [\@{][ Html.Syncfusion().Grid\<[Order]\>([\"OrderGrid\"])] |
|                                                                                                                                                                                                        |
| **[       .Datasource(Model)]**                                                                                                                                    |
|                                                                                                                                                                                                        |
| [       .Caption([\"Orders Grid\"])]                                                                                                       |
|                                                                                                                                                                                                        |
| [       .Render(); ]                                                                                                                                               |
|                                                                                                                                                                                                        |
| [         [}]]                                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Specify the visible column collection using **ColumnBuilder** actions as follows.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                             |
|                                                                                                                                                                                                     |
| []                                                                                                                                                              |
|                                                                                                                                                                                                     |
| [  [\<%][=]Html.Syncfusion().Grid\<[Order]\>([\"OrderGrid\"])] |
|                                                                                                                                                                                                     |
| [       .Datasource(Model)]                                                                                                                                     |
|                                                                                                                                                                                                     |
| [       .Caption([\"Orders Grid\"])]                                                                                                    |
|                                                                                                                                                                                                     |
| [       **.Column( column =\> {**]                                                                                                                              |
|                                                                                                                                                                                                     |
| **[           column.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]**                                                                |
|                                                                                                                                                                                                     |
| **[           column.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]**                                                          |
|                                                                                                                                                                                                     |
| **[           column.Add(p =\> p.ShipCountry).HeaderText([\"Ship Country\"]);]**                                                        |
|                                                                                                                                                                                                     |
| **[           column.Add(p =\> p.ShipName).HeaderText([\"Ship Name\"]);]**                                                              |
|                                                                                                                                                                                                     |
| **[           column.Add(p =\> p.Freight).HeaderText([\"Freight\"]).Format([\"{Freight:c}\"]);]**               |
|                                                                                                                                                                                                     |
| **[        })]**[       ]                                                                                                   |
|                                                                                                                                                                                                     |
| [       [%\>]]                                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[][cshtml][\]]**                                                 |
|                                                                                                                                                                                       |
| []                                                                                                                                                |
|                                                                                                                                                                                       |
| [  [\@{] Html.Syncfusion().Grid\<[Order]\>([\"OrderGrid\"])]          |
|                                                                                                                                                                                       |
| [       .Datasource(Model)]                                                                                                                       |
|                                                                                                                                                                                       |
| [       .Caption([\"Orders Grid\"])]                                                                                      |
|                                                                                                                                                                                       |
| [       **.Column( column =\> {**]                                                                                                                |
|                                                                                                                                                                                       |
| **[           column.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]**                                                  |
|                                                                                                                                                                                       |
| **[           column.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]**                                            |
|                                                                                                                                                                                       |
| **[           column.Add(p =\> p.ShipCountry).HeaderText([\"Ship Country\"]);]**                                          |
|                                                                                                                                                                                       |
| **[           column.Add(p =\> p.ShipName).HeaderText([\"Ship Name\"]);]**                                                |
|                                                                                                                                                                                       |
| **[           column.Add(p =\> p.Freight).HeaderText([\"Freight\"]).Format([\"{Freight:c}\"]);]** |
|                                                                                                                                                                                       |
| **[        })]**[]                                                                                            |
|                                                                                                                                                                                       |
| [}][]                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   In column mapping, add the unbound column using the **Add(string)** method. In this case a "Delete" column has been added as an unbound column which is used to delete records in the grid.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**[ ]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                           |
| [ [\<%][=]Html.Syncfusion().Grid\<[Order]\>([\"OrderGrid\"])]                                                                                        |
|                                                                                                                                                                                                                                                                                           |
| [       .Datasource(Model)]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                           |
| [       .Caption([\"Orders Grid\"])]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                           |
| [       .Column( column =\> {]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                           |
| [           column.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                           |
| [           column.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                           |
| [           column.Add(p =\> p.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                           |
| [           column.Add(p =\> p.ShipName).HeaderText([\"Ship Name\"]);]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                           |
| [           column.Add(p =\> p.Freight).HeaderText([\"Freight\"]).Format([\"{Freight:c}\"]);]                                                                                                         |
|                                                                                                                                                                                                                                                                                           |
| [           **column.Add([\"Delete\"]).HeaderText([\"Delete Record\"]).Format([\"\<a class=\\\"TemplateCell\\\" href=\\\"DeleteRecord?id={OrderID}\\\"\>Delete\</a\>\"]);** ] |
|                                                                                                                                                                                                                                                                                           |
| [        })           ]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                           |
| [       [%\>]]                                                                                                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[][cshtml][\]]**[ ]                                                                                                              |
|                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                           |
| [ [\@{] Html.Syncfusion().Grid\<[Order]\>([\"OrderGrid\"])]                                                                                                               |
|                                                                                                                                                                                                                                                                                           |
| [       .Datasource(Model)]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                           |
| [       .Caption([\"Orders Grid\"])]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                           |
| [       .Column( column =\> {]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                           |
| [           column.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                           |
| [           column.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                           |
| [           column.Add(p =\> p.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                           |
| [           column.Add(p =\> p.ShipName).HeaderText([\"Ship Name\"]);]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                           |
| [           column.Add(p =\> p.Freight).HeaderText([\"Freight\"]).Format([\"{Freight:c}\"]);]                                                                                                         |
|                                                                                                                                                                                                                                                                                           |
| [           **column.Add([\"Delete\"]).HeaderText([\"Delete Record\"]).Format([\"\<a class=\\\"TemplateCell\\\" href=\\\"DeleteRecord?id={OrderID}\\\"\>Delete\</a\>\"]);** ] |
|                                                                                                                                                                                                                                                                                           |
| [        }).Render();     ]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                           |
| [       [}]]                                                                                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

6.   Add two methods (one for loading the view and one for handling the delete actions).

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**[]                                                                                                         |
|                                                                                                                                                                                                                                |
| ***[]***                                                                                                                                                                   |
|                                                                                                                                                                                                                                |
| [///][ ][\<summary\>][]                |
|                                                                                                                                                                                                                                |
| [        [///][ Used to bind the grid. ]]                                                                                                       |
|                                                                                                                                                                                                                                |
| [        [///][ ][\</summary\>]]                                                                                           |
|                                                                                                                                                                                                                                |
| [        [///][ ][\<returns\>][View page; it displays the grid.][\</returns\>]] |
|                                                                                                                                                                                                                                |
| [        [public] [ActionResult] Index()]                                                                                                     |
|                                                                                                                                                                                                                                |
| [        {]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [     var][ data = [new] [NorthwindDataContext]().Orders.Take(15);]                          |
|                                                                                                                                                                                                                                |
| [            [return] View(data);]                                                                                                                                    |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [ \[[AcceptVerbs]([HttpVerbs].Get)\]]                                                                                                      |
|                                                                                                                                                                                                                                |
| [        [public] [ActionResult] DeleteRecord([int] id)]                                                                 |
|                                                                                                                                                                                                                                |
| [        {]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [            [NorthwindDataContext] context = [new] [NorthwindDataContext]();]                                        |
|                                                                                                                                                                                                                                |
| [            [Order] order = ([Order])context.Orders.Single(p =\> p.OrderID == id);]                                                       |
|                                                                                                                                                                                                                                |
| [            context.Orders.DeleteOnSubmit(order);]                                                                                                                                        |
|                                                                                                                                                                                                                                |
| [            context.SubmitChanges();]                                                                                                                                                     |
|                                                                                                                                                                                                                                |
| [            [return] RedirectToAction([\"Index\"]);]                                                                                         |
|                                                                                                                                                                                                                                |
| [ }]                                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

7.   Run the application. The grid will appear as shown below.

 

{border="0"}

Figure 93: Grid with Unbound  Column

[]{#related-topics}

