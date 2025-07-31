---
title: throughgridpropertiesmodel54.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\throughgridpropertiesmodel54.md
created_at: 2025-07-03
---






#### Through GridPropertiesModel {#through-gridpropertiesmodel style="tab-stops: 0pt"}

The steps to work with the auto wrap feature through **GridPropertiesModel** are as follows:

1.   Create a model in the application.

2.   Create a strongly typed view.

3.   Add the following code to the view.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                        |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [\<%][=][Html.Syncfusion().Grid\<[EditableOrder]\>(] |
|                                                                                                                                                                                                                           |
| [                     [\"Grid1\"], [\"GridModel\"],]                                                                                  |
|                                                                                                                                                                                                                           |
| [            column =\>]                                                                                                                                                              |
|                                                                                                                                                                                                                           |
| [             {]                                                                                                                                                                      |
|                                                                                                                                                                                                                           |
| [                  column.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                                                                                   |
|                                                                                                                                                                                                                           |
| [                  column.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                                                                             |
|                                                                                                                                                                                                                           |
| [                  column.Add(p =\> p.ShipCountry).HeaderText([\"Ship Country\"]);]                                                                           |
|                                                                                                                                                                                                                           |
| [                  column.Add(p =\> p.OrderDate).HeaderText([\"Order Date\"]);]                                                                               |
|                                                                                                                                                                                                                           |
| [                  column.Add(p =\> p.Freight).HeaderText([\"Freight\"]);]                                                                                    |
|                                                                                                                                                                                                                           |
| [              }) ]                                                                                                                                                                   |
|                                                                                                                                                                                                                           |
| [                                                                              ]                                                                                                      |
|                                                                                                                                                                                                                           |
| [%\>]                                                                                                                                                             |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                   |
|                                                                                                                                                                       |
| []                                                                                                                                |
|                                                                                                                                                                       |
| [\@{][Html.Syncfusion().Grid\<[EditableOrder]\>(] |
|                                                                                                                                                                       |
| [                     [\"Grid1\"], [\"GridModel\"],]                              |
|                                                                                                                                                                       |
| [            column =\>]                                                                                                          |
|                                                                                                                                                                       |
| [             {]                                                                                                                  |
|                                                                                                                                                                       |
| [                  column.Add(p =\> p.OrderID).HeaderText([\"Order ID\"]);]                               |
|                                                                                                                                                                       |
| [                  column.Add(p =\> p.CustomerID).HeaderText([\"Customer ID\"]);]                         |
|                                                                                                                                                                       |
| [                  column.Add(p =\> p.ShipCountry).HeaderText([\"Ship Country\"]);]                       |
|                                                                                                                                                                       |
| [                  column.Add(p =\> p.OrderDate).HeaderText([\"Order Date\"]);]                           |
|                                                                                                                                                                       |
| [                  column.Add(p =\> p.Freight).HeaderText([\"Freight\"]);]                                |
|                                                                                                                                                                       |
| [              }) ]                                                                                                               |
|                                                                                                                                                                       |
| [                                                                              ]                                                  |
|                                                                                                                                                                       |
| [%\>]                                                                                                         |
|                                                                                                                                                                       |
| []                                                                                                                                |
|                                                                                                                                                                       |
| []                                                                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.   Create a **GridPropertiesModel** and assign the grid properties in the model.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                              |
| [GridPropertiesModel][\<[EditableOrder]\> gridModel = [new] [GridPropertiesModel]\<[EditableOrder]\>()] |
|                                                                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                              |
| [        DataSource = [OrderRepository].GetAllRecords(),]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                              |
| [        \-\-\-\-\-\-\--]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                              |
| [        AllowResizing = [true],]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                              |
| [        AllowAutoWrap = [true,]]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                              |
| [        Height = 225,]                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                              |
| [        AutoFormat = [Skins].Sandune,]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                              |
| [};]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                              |
| [GridResizing][ resize = [new] [GridResizing]()]                                                                                                        |
|                                                                                                                                                                                                                                                                                              |
| [{ ]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                              |
| [      ResizeToFit = [true,]     ]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                              |
| [      ClipContent =[ true,]]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                              |
| [};]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                              |
| [gridModel.ResizeSettings = resize;]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

5.   Create a **Post** method for **AutoWrap** actions and bind the data source to the grid as given in the following code:

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| [\[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                     |
| [public][ [ActionResult] AutoWrap([PagingParams] args, [int]? OrderID, [GridEditMode]? GridMode)] |
|                                                                                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                     |
| [       [IEnumerable] data = [OrderRepository].GetAllRecords();]                                                                                                                                |
|                                                                                                                                                                                                                                                                                     |
| [       [return] data.GridJSONActions\<[EditableOrder]\>();]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                     |
| [}]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

6.   Run the application and resize columns as desired.

[] 

[]{#related-topics}

