---
title: throughgridbuilder13.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\throughgridbuilder13.md
created_at: 2025-07-03
---






#### Through GridBuilder {#through-gridbuilder style="tab-stops: 0pt"}

 

1.   Create a model in the application (Refer to [[Getting Started\>Adding a Model to the Application]]{.underline}).

2.   Create a strongly typed view (Refer to [[How to\>Strongly Typed View]]{.underline}).

3.   Create the Grid control in the view and configure its properties.

4.   Set the JSON action mode using the **ActionMode** method.

5.   Enable filtering using the **EnableFiltering()** method.

[] 


+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                     |
| [ ][\<%][=][Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])\ |
|        .Caption([\"Orders\"])\                                                                                                                                                                                              |
|        .AutoFormat([Skins].Sandune)]                                                                                                                                                    |
|                                                                                                                                                                                                                                                     |
| **[       .ActionMode(ActionMode.JSON)]**                                                                                                                                                                       |
|                                                                                                                                                                                                                                                     |
| **[       .EnableFiltering()]**[\                                                                                                                                                                               |
|        .Column( columns =\> {\                                                                                                                                                                                                                      |
|            columns.Add(p =\> p.OrderID);\                                                                                                                                                                                                           |
|            columns.Add(p =\> p.CustomerID);\                                                                                                                                                                                                        |
|            columns.Add(p =\> p.EmployeeID);  \                                                                                                                                                                                                      |
|            columns.Add(P =\> P.ShipCountry);[]]                                                                                                                                           |
|                                                                                                                                                                                                                                                     |
| [           columns.Add(p =\> p.OrderDate).Format([\"{0:dd-MM-yyyy}\"]);\                                                                                                                                                   |
|            })\                                                                                                                                                                                                                                      |
|        [%\>]]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                     |
| [   ]                                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 


+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                     |
| [ ][\@{][ ][Html.Syncfusion().Grid\<[Order]\>([\"Grid1\"])\ |
|        .Caption([\"Orders\"])\                                                                                                                                                                                              |
|        .AutoFormat([Skins].Sandune)]                                                                                                                                                    |
|                                                                                                                                                                                                                                                     |
| **[       .ActionMode(ActionMode.JSON)]**                                                                                                                                                                       |
|                                                                                                                                                                                                                                                     |
| **[       .EnableFiltering()]**[\                                                                                                                                                                               |
|        .Column( columns =\> {\                                                                                                                                                                                                                      |
|            columns.Add(p =\> p.OrderID);\                                                                                                                                                                                                           |
|            columns.Add(p =\> p.CustomerID);\                                                                                                                                                                                                        |
|            columns.Add(p =\> p.EmployeeID);  \                                                                                                                                                                                                      |
|            columns.Add(P =\> P.ShipCountry);[]]                                                                                                                                           |
|                                                                                                                                                                                                                                                     |
| [           columns.Add(p =\> p.OrderDate).Format([\"{0:dd-MM-yyyy}\"]);\                                                                                                                                                   |
|            }).Render();]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                     |
| [       [}]]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                     |
| [   ]                                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

6.  Render the view.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**[]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                |
| [ ][        [public] [ActionResult] Index()][] |
|                                                                                                                                                                                                                                                                                |
| [        {][]                                                                                                                                                |
|                                                                                                                                                                                                                                                                                |
| [            [return] View();][]                                                                                                        |
|                                                                                                                                                                                                                                                                                |
| [        }][]                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

7.   In order to work with filtering actions, create a **Post** method for **Index** actions and bind the data source to the grid as given in the following code sample.[]

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

8.   Run the application. The grid will appear as shown below.

 

{border="0"}

Figure 123: Filtering Enabled Grid

More:





