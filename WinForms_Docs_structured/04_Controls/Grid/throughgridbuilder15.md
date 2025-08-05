---
title: throughgridbuilder15.md
original_path: WinForms_Docs/04_Controls/Grid/throughgridbuilder15.md
created_at: 2025-08-05
---






#### Through GridBuilder {#through-gridbuilder style="tab-stops: 0pt"}

1.   Create a model in the application (Refer to [[Getting Started\>Adding a Model to the Application]]{.underline}).

2.   Create a strongly typed view (Refer to [[How to\>Strongly Typed View]]{.underline}).

3.   In the view you can use its **Model** property in **Datasource()** to bind the data source.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                              |
| [\<%][=][Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])] |
|                                                                                                                                                                                                                                                                                              |
| **[       .Datasource(Model)]**                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                              |
| [       .Caption([\"Orders\"])]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                              |
| [       .EnablePaging()]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                              |
| [       .EnableSorting()]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                              |
| [       .EnableGrouping()       ]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                              |
| [       .Column( columns =\> {]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                              |
| [           columns.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                                               |
|                                                                                                                                                                                                                                                                                              |
| [           columns.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                                                         |
|                                                                                                                                                                                                                                                                                              |
| [           columns.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);           ]                                                                                                                              |
|                                                                                                                                                                                                                                                                                              |
| [           columns.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                              |
| [           columns.Add(p =\> p.ShipCity).HeaderText([\"Ship City\"]);]                                                                                                                                             |
|                                                                                                                                                                                                                                                                                              |
| [           })]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                              |
| [       [%\>]]                                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**                                                                                                                                                                    |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                      |
|                                                                                                                                                                                                                              |
| [\@{][ Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])] |
|                                                                                                                                                                                                                              |
| **[       .Datasource(Model)]**                                                                                                                                             |
|                                                                                                                                                                                                                              |
| [       .Caption([\"Orders\"])]                                                                                                                     |
|                                                                                                                                                                                                                              |
| [       .EnablePaging()]                                                                                                                                                    |
|                                                                                                                                                                                                                              |
| [       .EnableSorting()]                                                                                                                                                   |
|                                                                                                                                                                                                                              |
| [       .EnableGrouping()       ]                                                                                                                                           |
|                                                                                                                                                                                                                              |
| [       .Column( columns =\> {]                                                                                                                                             |
|                                                                                                                                                                                                                              |
| [           columns.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                               |
|                                                                                                                                                                                                                              |
| [           columns.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                                         |
|                                                                                                                                                                                                                              |
| [           columns.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);           ]                                                              |
|                                                                                                                                                                                                                              |
| [           columns.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                       |
|                                                                                                                                                                                                                              |
| [           columns.Add(p =\> p.ShipCity).HeaderText([\"Ship City\"]);]                                                                             |
|                                                                                                                                                                                                                              |
| [           }).Render();]                                                                                                                                                   |
|                                                                                                                                                                                                                              |
| [       [}]]                                                                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   To enable the grouping feature for your grid you should use the **EnableGrouping()** method.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                              |
| [\<%][=][Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])] |
|                                                                                                                                                                                                                                                                                              |
| [       .Datasource(Model)]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                              |
| [       .Caption([\"Orders\"])]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                              |
| [       .EnablePaging()]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                              |
| [       .EnableSorting()]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                              |
| [      ** .EnableGrouping()      ** ]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                              |
| [       .Column( columns =\> {]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                              |
| [           columns.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                                               |
|                                                                                                                                                                                                                                                                                              |
| [           columns.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                                                         |
|                                                                                                                                                                                                                                                                                              |
|            columns.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                              |
| [           columns.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                              |
| [           columns.Add(p =\> p.ShipCity).HeaderText([\"Ship City\"]);]                                                                                                                                             |
|                                                                                                                                                                                                                                                                                              |
| [           })]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                              |
| [       [%\>]]                                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                              |
| [\@{][ ][Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])] |
|                                                                                                                                                                                                                                                                                              |
| [       .Datasource(Model)]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                              |
| [       .Caption([\"Orders\"])]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                              |
| [       .EnablePaging()]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                              |
| [       .EnableSorting()]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                              |
| [      ** .EnableGrouping()      ** ]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                              |
| [       .Column( columns =\> {]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                              |
| [           columns.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                                               |
|                                                                                                                                                                                                                                                                                              |
| [           columns.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                                                         |
|                                                                                                                                                                                                                                                                                              |
|            columns.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                              |
| [           columns.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                              |
| [           columns.Add(p =\> p.ShipCity).HeaderText([\"Ship City\"]);]                                                                                                                                             |
|                                                                                                                                                                                                                                                                                              |
| [           }).Render();]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                              |
| [       [}]]                                                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Set its data source and render the view.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                     |
| [///][ ][\<summary\>][] |
|                                                                                                                                                                                                                                                                     |
| [        [///][ Used to bind the grid. ]]                                                                                                                               |
|                                                                                                                                                                                                                                                                     |
| [        [///][ ][\</summary\>]]                                                                                                                   |
|                                                                                                                                                                                                                                                                     |
| [        [///][ ][\<returns\>][View page; it displays the grid.][\</returns\>]]                         |
|                                                                                                                                                                                                                                                                     |
| [        [public] [ActionResult] Index()]                                                                                                                             |
|                                                                                                                                                                                                                                                                     |
| [        {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                     |
| [            [var] data = [new] [NorthwindDataContext]().Orders;]                                                                                |
|                                                                                                                                                                                                                                                                     |
| [            [return] View(data);]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

6.   In order to work with sorting actions, create a **Post** method for **Index** actions and bind the data source to the grid as shown in the following code sample.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                     |
| [///][ ][\<summary\>][] |
|                                                                                                                                                                                                                                                                     |
| [        [///][ Paging and sorting requests are mapped to this method. This method invokes the HtmlActionResult]]                                                       |
|                                                                                                                                                                                                                                                                     |
| [        [///][ from the grid. The required response is generated.]]                                                                                                    |
|                                                                                                                                                                                                                                                                     |
| [        [///][ ][\</summary\>]]                                                                                                                   |
|                                                                                                                                                                                                                                                                     |
| [        [///][ ][\<param name=\"args\"\>][Contains paging properties. ][\</param\>]]                   |
|                                                                                                                                                                                                                                                                     |
| [        [///][ ][\<returns\>]]                                                                                                                    |
|                                                                                                                                                                                                                                                                     |
| [        [///][ HtmlActionResult returns the data displayed on the grid.]]                                                                                              |
|                                                                                                                                                                                                                                                                     |
| [        [///][ ][\</returns\>]]                                                                                                                   |
|                                                                                                                                                                                                                                                                     |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                                                                      |
|                                                                                                                                                                                                                                                                     |
| [        [public] [ActionResult] Index([PagingParams] args)]                                                                                  |
|                                                                                                                                                                                                                                                                     |
| [        {]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                     |
| [            [IEnumerable] data = [new] [NorthwindDataContext]().Orders;]                                                                     |
|                                                                                                                                                                                                                                                                     |
| [            [return] data.GridActions\<[Order]\>();]                                                                                                                 |
|                                                                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

7.   Run the application. The grid will appear as shown below.

 

{border="0"}

Figure 131: Grid with Grouping Enabled

 

Drag and drop any columns in the group drop area. After grouping, the grid will appear as shown below.

 

{border="0"}

Figure 132: Grid with Grouped Column

More:





