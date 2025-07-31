---
title: disableeditinginspecifiedcolumns.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\disableeditinginspecifiedcolumns.md
created_at: 2025-07-03
---






##### Disable Editing in Specified Columns {#disable-editing-in-specified-columns style="tab-stops: 0pt"}

 

Essential Grid provides support for restricting the editing operations in a column. This can be done by setting the **AllowEditing** property of particular columns to **False**.

[] 

1.   [Create a model in the application (Refer to]{.NumberedListChar} [Getting Started\>Adding a Model to the Application](http://help.syncfusion.com/ug_91/User%20Interface/ASP.NET%20MVC/Grid/Documents/addingamodeltotheapplication.htm)).

2.   [Create a strongly typed view (Refer to]{.NumberedListChar} [How to\>Strongly Typed View](http://help.syncfusion.com/ug_91/User%20Interface/ASP.NET%20MVC/Grid/Documents/stronglytypedview.htm)).

3.   Create the Grid control in the view and configure its properties.

4.   Set the **AllowEditing** property of a particular column to **False**.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**[ ]                                                                                                                                                   |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                  |
| [\<%][=][Html.Grid\<[EditableOrder]\>([\"Grid1\"])] |
|                                                                                                                                                                                                                                                  |
| [    .Datasource(Model)]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                  |
| [    .Caption([\"Orders\"])]                                                                                                                                                         |
|                                                                                                                                                                                                                                                  |
| [    .Column(column =\>]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                  |
| [    {]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                  |
| [      column.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                      |
|                                                                                                                                                                                                                                                  |
| [      column.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"])**.AllowEditing([false])**;]                                                                 |
|                                                                                                                                                                                                                                                  |
| [      column.Add(p =\> p.ShipCountry).HeaderText([\"Ship Country\"])**.AllowEditing([false])**;]                                                               |
|                                                                                                                                                                                                                                                  |
| [      column.Add(p =\> p.OrderDate).HeaderText([\"Order Date\"]).Format([\"{OrderDate:dd/MM/yyyy}\"]);]                                                     |
|                                                                                                                                                                                                                                                  |
| [      column.Add(p =\> p.Freight).HeaderText([\"Freight\"]);]                                                                                                                       |
|                                                                                                                                                                                                                                                  |
| [                          ]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                  |
| [                            ]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                  |
| [                         })]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                  |
| [    [%\>]][]                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[   ]

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[cshtml\]]**[ ]                                                                                              |
|                                                                                                                                                                                               |
| [\@{][ Html.Grid\<[EditableOrder]\>([\"Grid1\"])] |
|                                                                                                                                                                                               |
| [    .Datasource(Model)]                                                                                                                                  |
|                                                                                                                                                                                               |
| [    .Caption([\"Orders\"])]                                                                                                      |
|                                                                                                                                                                                               |
| [    .Column(column =\>]                                                                                                                                  |
|                                                                                                                                                                                               |
| [    {]                                                                                                                                                   |
|                                                                                                                                                                                               |
| [      column.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                   |
|                                                                                                                                                                                               |
| [      column.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"])**.AllowEditing([false])**;]              |
|                                                                                                                                                                                               |
| [      column.Add(p =\> p.ShipCountry).HeaderText([\"Ship Country\"])**.AllowEditing([false])**;]            |
|                                                                                                                                                                                               |
| [      column.Add(p =\> p.OrderDate).HeaderText([\"Order Date\"]).Format([\"{OrderDate:dd/MM/yyyy}\"]);]  |
|                                                                                                                                                                                               |
| [      column.Add(p =\> p.Freight).HeaderText([\"Freight\"])**;**]                                                                |
|                                                                                                                                                                                               |
| [                          ]                                                                                                                              |
|                                                                                                                                                                                               |
| [                            ]                                                                                                                            |
|                                                                                                                                                                                               |
| [                         })]                                                                                                                             |
|                                                                                                                                                                                               |
| []                                                                                                                                                        |
|                                                                                                                                                                                               |
| [                        .Render();]                                                                                                                      |
|                                                                                                                                                                                               |
| [}][]                                                                                             |
|                                                                                                                                                                                               |
| **[]**[]                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


{border="0"}Note: In the code snippets, the "Customer ID" and "Ship Country" columns cannot be editable.


5.   Render the view.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**[]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                |
| [ ][        [public] [ActionResult] Index()][] |
|                                                                                                                                                                                                                                                                                |
| [        {][]                                                                                                                                                |
|                                                                                                                                                                                                                                                                                |
| [           [var] data = [new] [NorthwindDataContext]().Orders;]                                                                                            |
|                                                                                                                                                                                                                                                                                |
| [            [return] View(data);][]                                                                                                   |
|                                                                                                                                                                                                                                                                                |
| [        }][]                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

6.   Run the application and edit the particular record. The grid will appear as shown below.

 

{border="0"}

Figure 145: Grid Columns with Editing Disabled

 

[]{#related-topics}

