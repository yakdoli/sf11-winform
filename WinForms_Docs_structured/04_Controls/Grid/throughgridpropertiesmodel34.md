---
title: throughgridpropertiesmodel34.md
original_path: WinForms_Docs/04_Controls/Grid/throughgridpropertiesmodel34.md
created_at: 2025-08-05
---






#### Through GridPropertiesModel {#through-gridpropertiesmodel style="tab-stops: 0pt"}

 

1.   Create a model in the application (Refer to [[Getting Started\>Adding a Model to the Application]]{.underline}).

2.   Add the following code in the **Index.aspx** file to create the Grid control in the view.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                 |
| [\<%][=][Html.Syncfusion().Grid\<[Order]\>([\"Orders_Grid\"],[\"GridModel\"], column=\> {] |
|                                                                                                                                                                                                                                                                                                                 |
| [           column.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                 |
| [           column.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                 |
| [           column.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                 |
| [           column.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                 |
| [           column.Add(p =\> p.ShipCity).HeaderText([\"Ship City\"]);  ]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                 |
| [    })[%\>]]                                                                                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [@(][new][ [HtmlString](][Html.Syncfusion().Grid\<[Order]\>([\"Orders_Grid\"],[\"GridModel\"], column=\> {] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [           column.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [           column.Add(p =\> p.EmployeeID).HeaderText([\"Employee ID\"]);]                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [           column.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [           column.Add(P =\> P.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [           column.Add(p =\> p.ShipCity).HeaderText([\"Ship City\"]);  ]                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [    })][.][ToString())[)] ]***[]***                                                                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Create a **GridPropertiesModel** in the **Index** method. Assign grid properties in this model.[]

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                            |
| [  GridPropertiesModel][\<[Order]\> model = [new] [GridPropertiesModel]\<[Order]\>()] |
|                                                                                                                                                                                                                                                                            |
| [            {]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                            |
| [                DataSource = [new] [NorthwindDataContext]().Orders.Take(500),]                                                                                                           |
|                                                                                                                                                                                                                                                                            |
| [                Caption = [\"Orders\"],]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                            |
| [                AllowPaging = [true],]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                            |
| [                AllowSorting = [true]                             ]                                                                                                                                              |
|                                                                                                                                                                                                                                                                            |
| [            };]                                                                                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Specify the skin name using the **AutoFormat** property and pass the model to the view using the **ViewData()** method.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                          |
| [GridPropertiesModel][\<[Order]\> model = [new] [GridPropertiesModel]\<[Order]\>()] |
|                                                                                                                                                                                                                                                                          |
| [            {]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                          |
| [                DataSource = [new] [NorthwindDataContext]().Orders.Take(500),]                                                                                                         |
|                                                                                                                                                                                                                                                                          |
| [                Caption = [\"Orders\"],]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                          |
| [                AllowPaging = [true],]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                          |
| [                AllowSorting = [true,]                             ]                                                                                                                                           |
|                                                                                                                                                                                                                                                                          |
| **[ ][ AutoFormat = [Skins].Almond]**                                                                                                                    |
|                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                          |
| [  };[]]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                          |
| [            ViewData\[[\"GridModel\"]\] = model;]                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Run the application. The grid will appear as shown below.

 

{border="0"}

Figure 260: Grid with Almond Skin

 

[]{#related-topics}

