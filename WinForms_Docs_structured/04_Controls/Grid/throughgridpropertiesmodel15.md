---
title: throughgridpropertiesmodel15.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\throughgridpropertiesmodel15.md
created_at: 2025-07-03
---






#### Through GridPropertiesModel {#through-gridpropertiesmodel style="tab-stops: 0pt"}

1.   Create a model in the application (Refer to [[Getting Started\>Adding a Model to the Application]]{.underline}).

2.   Add the following code in the **Index.aspx** file to create the Grid control in the view.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                    |
| [\<%][=][Html.Syncfusion().Grid\<[Order]\>([\"GroupingGrid\"],[\"GridModel\"], columns =\> {] |
|                                                                                                                                                                                                                                                                                                                    |
| [            columns.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                    |
| [            columns.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                    |
| [            columns.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                    |
| [            columns.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                    |
| [            columns.Add(p =\> p.ShipCity).HeaderText([\"Ship City\"]);]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                    |
| [     })[%\>]]                                                                                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [@(][new][ [HtmlString](][Html.Syncfusion().Grid\<[Order]\>([\"GroupingGrid\"],[\"GridModel\"], columns =\> {] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [            columns.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [            columns.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [            columns.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);]                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [            columns.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [            columns.Add(p =\> p.ShipCity).HeaderText([\"Ship City\"]);]                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [     })][.ToString())[)]    ][    ]                                                                                                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Create a **GridPropertiesModel** in the **Index** method. Use **AllowGrouping** property to enable the grouping feature.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Controller]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                             |
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
| [                AllowSorting=[true],]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                              |
| [                AllowMultiSorting=[true],]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                              |
| **[                AllowGrouping=[true],]**                                                                                                                                                                         |
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

4.   In order to work with grouping actions, create a **Post** method for **Index** actions and bind the data source to the grid as done in the following code sample.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [Controller][ ]                                                                                                   |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                  |
|                                                                                                                                                                                                                                      |
| [///][ ][\<summary\>][]                      |
|                                                                                                                                                                                                                                      |
| [        [///][ Paging, sorting, and grouping requests are mapped to this method. This method invokes the HtmlActionResult]]                          |
|                                                                                                                                                                                                                                      |
| [        [///][ from the grid. The required response is generated.]]                                                                                  |
|                                                                                                                                                                                                                                      |
| [        [///][ ][\</summary\>]]                                                                                                 |
|                                                                                                                                                                                                                                      |
| [        [///][ ][\<param name=\"args\"\>][Contains paging properties. ][\</param\>]] |
|                                                                                                                                                                                                                                      |
| [        [///][ ][\<returns\>]]                                                                                                  |
|                                                                                                                                                                                                                                      |
| [        [///][ HtmlActionResult returns the data displayed on the grid.]]                                                                            |
|                                                                                                                                                                                                                                      |
| [        [///][ ][\</returns\>]]                                                                                                 |
|                                                                                                                                                                                                                                      |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                                                    |
|                                                                                                                                                                                                                                      |
| [        [public] [ActionResult] Index([PagingParams] args)]                                                                |
|                                                                                                                                                                                                                                      |
| [        {]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                      |
| [            [IEnumerable] data = [new] [NorthwindDataContext]().Orders;]                                                   |
|                                                                                                                                                                                                                                      |
| [            [return] data.GridActions\<[Order]\>();]                                                                                               |
|                                                                                                                                                                                                                                      |
| [        }]                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

5.   Run the application. The grid will appear as shown below.

 

{border="0"}

Figure 133: Grid with Grouping Enabled

 

Drag and drop any columns in the group drop area. After grouping, the grid will appear as given below.

{border="0"}

Figure 134: Grid with Grouped Column

More:





