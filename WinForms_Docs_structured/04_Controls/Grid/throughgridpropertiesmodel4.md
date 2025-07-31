---
title: throughgridpropertiesmodel4.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\throughgridpropertiesmodel4.md
created_at: 2025-07-03
---






#### Through GridPropertiesModel {#through-gridpropertiesmodel style="tab-stops: 0pt"}

1.   Create a model in the application (Refer to [Getting Started\>Adding a Model to the Application]{.UGHyperlink}).

2.   Create the grid in the view and create visible a column collection using **IRootColumnBuilder\<T\>** as shown below.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                         |
| [\<%][=][Html.Syncfusion().Grid\<[Order]\>(\"UnBoundColumn_Grid\", \"GridModel\",] |
|                                                                                                                                                                                                                                                         |
| [          **column =\>**]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                         |
| **[          {]**                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                         |
| [              column.Add(p =\> p.OrderID).HeaderText(\"Order ID\");]                                                                                                                                               |
|                                                                                                                                                                                                                                                         |
| **[              column.Add(p =\> p.CustomerID).HeaderText(\"Customer ID\");]**                                                                                                                                     |
|                                                                                                                                                                                                                                                         |
| **[              column.Add(p =\> p.ShipCountry).HeaderText(\"Ship Country\");]**                                                                                                                                   |
|                                                                                                                                                                                                                                                         |
| **[              column.Add(p =\> p.ShipName).HeaderText(\"Ship Name\");]**                                                                                                                                         |
|                                                                                                                                                                                                                                                         |
| **[              column.Add(p =\> p.Freight).HeaderText(\"Freight\").Format(\"{Freight:c}\");]**                                                                                                                    |
|                                                                                                                                                                                                                                                         |
| **[          }]**[)[%\>]]                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[][cshtml][\]]**                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [@(][new][ [HtmlString](][Html.Syncfusion().Grid\<[Order]\>(\"UnBoundColumn_Grid\", \"GridModel\",] |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [          **column =\>**]                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                             |
| **[          {]**                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                             |
| **[              column.Add(p =\> p.OrderID).HeaderText(\"Order ID\");]**                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                             |
| **[              column.Add(p =\> p.CustomerID).HeaderText(\"Customer ID\");]**                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                             |
| **[              column.Add(p =\> p.ShipCountry).HeaderText(\"Ship Country\");]**                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                             |
| **[              column.Add(p =\> p.ShipName).HeaderText(\"Ship Name\");]**                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                             |
| **[              column.Add(p =\> p.Freight).HeaderText(\"Freight\").Format(\"{Freight:c}\");]**                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                             |
| **[          }]**[)][.ToString())[)]    ]                                                                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

3.   In column mapping, add the unbound column using the **Add(string)** method. In this case a "Delete" column has been added as an unbound column which is used to delete records in the grid.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                             |
| [\<%][=][Html.Syncfusion().Grid\<[Order]\>([\"UnBoundColumn_Grid\"], [\"GridModel\"],] |
|                                                                                                                                                                                                                                                                                                             |
| [          column =\>]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                             |
| [          {]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                             |
| [              column.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                             |
| [              column.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                             |
| [              column.Add(p =\> p.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                             |
| [              column.Add(p =\> p.ShipName).HeaderText([\"Ship Name\"]);]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                             |
| [              column.Add(p =\> p.Freight).HeaderText([\"Freight\"]).Format([\"{Freight:c}\"]);]                                                                                                                        |
|                                                                                                                                                                                                                                                                                                             |
| [             ** column.Add([\"Delete\"]).HeaderText([\"Delete Record\"]).Format([\"\<a class=\\\"TemplateCell\\\" href=\\\"DeleteRecord?id={OrderID}\\\"\>Delete\</a\>\"]);            ** ]    |
|                                                                                                                                                                                                                                                                                                             |
| [          })[%\>]  ]                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[][cshtml][\]]**[]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [@(][new][ [HtmlString](][Html.Syncfusion().Grid\<[Order]\>([\"UnBoundColumn_Grid\"], [\"GridModel\"],] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [          column =\>]                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [          {]                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [              column.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [              column.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [              column.Add(p =\> p.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [              column.Add(p =\> p.ShipName).HeaderText([\"Ship Name\"]);]                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [              column.Add(p =\> p.Freight).HeaderText([\"Freight\"]).Format([\"{Freight:c}\"]);]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [             ** column.Add([\"Delete\"]).HeaderText([\"Delete Record\"]).Format([\"\<a class=\\\"TemplateCell\\\" href=\\\"DeleteRecord?id={OrderID}\\\"\>Delete\</a\>\"]);            ** ]                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [          })][.ToString())[)]    ][]                                                                                                                                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Create a **GridPropertiesModel** in the **Index** method. Assign grid properties in this model and pass the model from controller to view using the **ViewData** class as given below.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [public][ [ActionResult] Index()]                                                                                                                  |
|                                                                                                                                                                                                                                                                 |
| [        {]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                 |
| [              [GridPropertiesModel]\<[Order]\> gridModel = [new] [GridPropertiesModel]\<[Order]\> ()] |
|                                                                                                                                                                                                                                                                 |
| [            {]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                 |
| [                DataSource = [new] [NorthwindDataContext]().Orders.Take(15),]                                                                                                 |
|                                                                                                                                                                                                                                                                 |
| [                Caption = [\"Orders\"]                          ]                                                                                                                                  |
|                                                                                                                                                                                                                                                                 |
| [            };]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                 |
| [            ViewData\[[\"GridModel\"]\] = gridModel; [// Pass the model from controller to view using ViewData.]]                                                            |
|                                                                                                                                                                                                                                                                 |
| [            [return] View();]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                 |
| [        }]                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

5.   Create a **Delete** action method which is used to delete the record from the database. This is shown below.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[[AcceptVerbs]([HttpVerbs].Get)\]]                                                                |
|                                                                                                                                                                                         |
| [        [public] [ActionResult] DeleteRecord([int] id)]                          |
|                                                                                                                                                                                         |
| [        {]                                                                                                                                         |
|                                                                                                                                                                                         |
| [            [NorthwindDataContext] context = [new] [NorthwindDataContext]();] |
|                                                                                                                                                                                         |
| [            [Order] order = ([Order])context.Orders.Single(p =\> p.OrderID == id);]                |
|                                                                                                                                                                                         |
| [            context.Orders.DeleteOnSubmit(order);]                                                                                                 |
|                                                                                                                                                                                         |
| [            context.SubmitChanges();]                                                                                                              |
|                                                                                                                                                                                         |
| [            [return] RedirectToAction([\"Index\"]);]                                                  |
|                                                                                                                                                                                         |
| [        }]                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

6.   Run the application. The grid will appear as shown below.

 

{border="0"}

Figure 94: Grid with Unbound Column

[] 

[]{#related-topics}

