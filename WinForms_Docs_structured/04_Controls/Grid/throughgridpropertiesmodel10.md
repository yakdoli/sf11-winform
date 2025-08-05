---
title: throughgridpropertiesmodel10.md
original_path: WinForms_Docs/04_Controls/Grid/throughgridpropertiesmodel10.md
created_at: 2025-08-05
---






#### Through GridPropertiesModel {#through-gridpropertiesmodel style="tab-stops: 0pt"}

 

1.   Create a model in the application (Refer to [[Getting Started\>Adding a Model to the Application]]{.underline}).

2.   Add the following code in the **Index.aspx** file to create the Grid control in the view.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [ [\<%][=]Html.Syncfusion().Grid\<[Order]\>([\"SortingGrid\"],[\"GridModel\"], columns =\> {] |
|                                                                                                                                                                                                                                                            |
| [            columns.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                         |
|                                                                                                                                                                                                                                                            |
| [            columns.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                                   |
|                                                                                                                                                                                                                                                            |
| [            columns.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);]                                                                                                                   |
|                                                                                                                                                                                                                                                            |
| [            columns.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                                                                 |
|                                                                                                                                                                                                                                                            |
| [            columns.Add(p =\> p.ShipCity).HeaderText([\"Ship City\"]);]                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [     })[%\>]]                                                                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[][cshtml][\]     ]**                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [@(][new][ [HtmlString](][Html.Syncfusion().Grid\<[Order]\>([\"SortingGrid\"],[\"GridModel\"], columns =\> {] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [            columns.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [            columns.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [            columns.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);]                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [            columns.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [            columns.Add(p =\> p.ShipCity).HeaderText([\"Ship City\"]);]                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [     })][.ToString())[)]    ][]                                                                                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Create a **GridPropertiesModel** in the **Index** method. Use the **AllowSorting** property to enable the sorting feature.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                              |
| [public][ [ActionResult] Index()]                                                                                                                               |
|                                                                                                                                                                                                                                                                              |
| [        {]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                              |
| [GridPropertiesModel][\<[Order]\> gridModel = [new] [GridPropertiesModel]\<[Order]\>()] |
|                                                                                                                                                                                                                                                                              |
| [            {]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                              |
| [                DataSource=[new] [NorthwindDataContext]().Orders,]                                                                                                                         |
|                                                                                                                                                                                                                                                                              |
| [                Caption=[\"Orders\"],]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                              |
| [                AllowPaging=[true],]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                              |
| **[                AllowSorting=[true],]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                              |
| [                AutoFormat=[Skins].Sandune]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                              |
| [            };]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                              |
| [            ViewData\[[\"GridModel\"]\] = gridModel;[ // Pass the model from controller to view using ViewData.]]                                                                         |
|                                                                                                                                                                                                                                                                              |
| [            [return] View();]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                              |
| [        }]                                                                                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

4.   In order to work with sorting actions, create a **Post** method for **Index** actions and bind the data source to the grid as given in the following code sample.

[  ][]

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller][]**                                                                                                                                          |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                                     |
| [///][ ][\<summary\>][]                     |
|                                                                                                                                                                                                                                     |
| [        [///][ Paging/sorting requests are mapped to this method. This method invokes the HtmlActionResult]]                                        |
|                                                                                                                                                                                                                                     |
| [        [///][ from the grid. The required response is generated.]]                                                                                 |
|                                                                                                                                                                                                                                     |
| [        [///][ ][\</summary\>]]                                                                                                |
|                                                                                                                                                                                                                                     |
| [        [///][ ][\<param name=\"args\"\>][Contains paging properties.][\</param\>]] |
|                                                                                                                                                                                                                                     |
| [        [///][ ][\<returns\>]]                                                                                                 |
|                                                                                                                                                                                                                                     |
| [        [///][ HtmlActionResult returns the data displayed on the grid.]]                                                                           |
|                                                                                                                                                                                                                                     |
| [        [///][ ][\</returns\>]]                                                                                                |
|                                                                                                                                                                                                                                     |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                                                   |
|                                                                                                                                                                                                                                     |
| [        [public] [ActionResult] Index([PagingParams] args)]                                                               |
|                                                                                                                                                                                                                                     |
| [        {]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                     |
| [            [IEnumerable] data = [new] [NorthwindDataContext]().Products;]                                                |
|                                                                                                                                                                                                                                     |
| [            [return] data.GridActions\<[Product]\>();]                                                                                            |
|                                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

5.   Run the application. The grid will appear as shown below.

 

{border="0"}

Figure 112: Grid with Sorting Feature

 

More:





