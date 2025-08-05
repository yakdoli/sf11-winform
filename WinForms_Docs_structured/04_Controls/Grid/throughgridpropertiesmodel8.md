---
title: throughgridpropertiesmodel8.md
original_path: WinForms_Docs/04_Controls/Grid/throughgridpropertiesmodel8.md
created_at: 2025-08-05
---






#### Through GridPropertiesModel {#through-gridpropertiesmodel style="tab-stops: 0pt"}

1.   Create a model in the application (Refer to [[Getting Started\>Adding a Model to the Application]]{.underline}).

2.   Add the following code in the **Index.aspx** file to create the Grid control in the view.

[] 


+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                               |
| [        ][ ][   [\<%][=]Html.Grid\<[Order]\>([\"Grid1\"],[\"GridModel\"], columns =\> {\ |
|             columns.Add(p =\> p.OrderID)\                                                                                                                                                                                                                                                     |
|             columns.Add(p =\> p.CustomerID)\                                                                                                                                                                                                                                                  |
|             columns.Add(p =\> p.EmployeeID);  \                                                                                                                                                                                                                                               |
|             columns.Add(P =\> P.ShipCountry);]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                               |
| [            columns.Add(p =\> p.OrderDate).Format([\"{0:dd-MM-yyyy}\"]);]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                               |
| [           })[%\>]]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                               |
| [   ]                                                                                                                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[][cshtml][\]     ]**                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [@(][new][ [HtmlString](][Html.Grid\<[Order]\>([\"Grid1\"],[\"GridModel\"], columns =\> {\ |
|             columns.Add(p =\> p.OrderID)\                                                                                                                                                                                                                                                                                                                                      |
|             columns.Add(p =\> p.CustomerID)\                                                                                                                                                                                                                                                                                                                                   |
|             columns.Add(p =\> p.EmployeeID);  \                                                                                                                                                                                                                                                                                                                                |
|             columns.Add(P =\> P.ShipCountry);]                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [            columns.Add(p =\> p.OrderDate).Format([\"{0:dd-MM-yyyy}\"]);]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [           })][.ToString()]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [)[)]    ][]                                                                                                                                                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

3.   Create a **GridPropertiesModel** in the **Index** method. Use the **ActionMode** property to set  JSON mode.

4.   Use the **AllowPaging** property to enable the paging operations.

[] 


+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                |
| [   [public] [ActionResult] Index()\                                                                                                                                                                                                              |
|    {\                                                                                                                                                                                                                                                                                          |
|       ][   [GridPropertiesModel]\<[Order]\> gridModel = [new] [GridPropertiesModel]\<[Order]\>()] |
|                                                                                                                                                                                                                                                                                                |
| [      {]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                |
| [               Caption = [\"Orders\"],]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                |
| [               AutoFormat = Syncfusion.Mvc.Shared.[Skins].Sandune,]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                |
| [               **AllowPaging = true,**]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                |
| **[               ActionMode = ActionMode.JSON]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                |
| **[                ]**                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                |
| [      };]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                |
| [\                                                                                                                                                                                                                                                                                             |
|         ViewData\[[\"GridModel\"]\] = gridModel;\                                                                                                                                                                                                                      |
|         [return] View();\                                                                                                                                                                                                                                                 |
|    }][]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                |
| [   ]                                                                                                                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

5.   In order to work with paging actions, create a **Post** method for **Index** actions and  bind the data source to the grid as shown in the following code.[ ]

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**[]                                                                                                                                                              |
|                                                                                                                                                                                                                                                         |
| [ ][  ][     \[[AcceptVerbs]([HttpVerbs].Post)\]] |
|                                                                                                                                                                                                                                                         |
| [        [public] [ActionResult] Index([PagingParams] args)]                                                                                   |
|                                                                                                                                                                                                                                                         |
| [        {]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                         |
| [            [IEnumerable] data = [new] [NorthwindDataContext]().Orders.ToList();]                                                             |
|                                                                                                                                                                                                                                                         |
| **[            [return] data.GridJSONActions\<[Order]\>();]**                                                                                                          |
|                                                                                                                                                                                                                                                         |
| [        }][]                                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

6.   Run the application. The grid will appear as shown below.

[] 

{border="0"}

Figure 108: Paging Enabled Grid

*[]* 

More:





