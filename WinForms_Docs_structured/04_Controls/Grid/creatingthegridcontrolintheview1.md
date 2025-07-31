---
title: creatingthegridcontrolintheview1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\creatingthegridcontrolintheview1.md
created_at: 2025-07-03
---








  









### Creating the Grid Control in the View {#creating-the-grid-control-in-the-view style="tab-stops: 0pt"}

1.   Create a model into application (Refer to [Getting Started\>Adding a Model to the Application]{.UGHyperlink}[[)]]{.UGHyperlink}

2.   Create a strongly typed view (Refer to [How to\>Strongly Typed View]{.UGHyperlink})

3.   Add the following code in the **Index.cshtml** file to create the Grid control in the view:

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[cshtml\]]**                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\@{][ Html.Syncfusion().Grid\<Sample.Models.[Order]\>([\"]][FlatGrid][\"][)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [      .Datasource(Model)]                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [      ][.EnablePaging()]                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [     .EnableSorting()][]                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [      .Column( ][column =\> {]                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [          column.Add(c =\> c.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [          column.Add(c =\> c.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [          column.Add(c =\> c.EmployeeID).HeaderText([\"Employee ID\"]);]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [          column.Add(c =\> c.OrderDate).HeaderText([\"Order Date\"]).Format([\"{OrderDate:dd/mm/yyyy}\"]);]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [           ][column.Add(c =\> c.Freight).HeaderText([\"Freight\"]);           ][]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [                })               ]                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [      .Render(); ]                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [   [}]]                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: This is of the type: [GridBuilder]\<T\> Grid\<T\>([this] [HtmlHelper] html, [string] id) where T: [class]


It is important that the **ID** used in the **FlatGrid.cshtml** file and in the **HomeController.cs** file should match in order to ensure binding of the properties to the control.

 

4.   Add two methods in **HomeController** (one for loading the view and one for handling the grid paging/sorting actions).

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [///][ ][\<summary\>][]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [///][ Used to bind the Grid.][]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [///][ ][\</summary\>][]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [///][ ][\<returns\>][View page, displays the Grid][\</returns\>][]          |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [public][ [ActionResult] Index()]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [{]                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [var data=new NorthwindDataContext().Orders.Take(200);]                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [return][ View(data);]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [///][ ][\<summary\>][]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [///][ Paging/sorting requests are mapped to this method. This method invokes the ][]                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [///][ HtmlActionResult from the grid. The required response is generated.][]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [///][ ][\</summary\>][]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [///][ ][\<param name=\"args\"\>][Contains paging properties ][\</param\>][] |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [///][ ][\<returns\>][]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [///][ HtmlActionResult returns the data displayed on the grid.][]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [///][ ][\</returns\>][]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [\[[AcceptVerbs]([HttpVerbs].Post)\]]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [public][ [ActionResult] Index([PagingParams] args)]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [{]                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [IEnumerable][ data = [new] [NorthwindDataContext]().Orders.Take(200);]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [return][ data.GridActions\<[Order]\>();]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

5.   Run the application.

 

 

{border="0"}

Figure 57: Grid Control Added to the Application

[]{#related-topics}

