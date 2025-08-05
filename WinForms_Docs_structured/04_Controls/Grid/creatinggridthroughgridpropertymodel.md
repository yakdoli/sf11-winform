---
title: creatinggridthroughgridpropertymodel.md
original_path: WinForms_Docs/04_Controls/Grid/creatinggridthroughgridpropertymodel.md
created_at: 2025-08-05
---








  









### Creating Grid through GridPropertyModel {#creating-grid-through-gridpropertymodel style="tab-stops: 0pt"}

 

1.   Create a model into application ([[Refer to ]]{.UGHyperlink}[Getting Started\>Adding a Model to the Application]{.UGHyperlink})

2.   Add the following code in the **Index.aspx** file, to create the Grid control in the view:

 

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                               |
| [\<%][=][Html.Syncfusion().Grid\<MvcSampleApplication.Models.[Order]\>([\"FlatGrid\"],[\"GridModel\"], ] |
|                                                                                                                                                                                                                                                                                                                               |
| [       column =\> {    ]                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                               |
| [                    column.Add(c =\> c.OrderID).HeaderText([\"Order ID\"]);]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                               |
| [                    column.Add(c =\> c.CustomerID).HeaderText([\"Customer ID\"]);]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                               |
| [                    column.Add(c =\> c.EmployeeID).HeaderText([\"Employee ID\"]);]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                               |
| [                    column.Add(c =\> c.OrderDate).HeaderText([\"Order Date\"]).Format([\"{OrderDate:dd/mm/yyyy}\"]);]                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                               |
| [                    column.Add(c =\> c.Freight).HeaderText([\"Freight\"]);  ]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                               |
| [                    })]                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                               |
| [       [%\>]]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


{border="0"}Note: This is of the type: string HTMLHelper.Grid\<T\>(string control_id, GridPropertiesModel gridModel, Action\<IRootGridColumnBuilder\<T\>\>columns); where T: class.


It is important that the **control_id** used in the **Index.aspx** file and in the **HomeController.cs** file should match to ensure the binding of the properties to the control.

3.   Double-click the **HomeController.cs** from the **Controller/Home** folder.

The HomeController.cs page is displayed in the main window.

 

{border="0"}

Figure 48: HomeController.cs Page

[] 

4.   Edit the **Index** method as shown below:

 

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                          |
| [///][ ][\<summary\>][]                                          |
|                                                                                                                                                                                                                                                          |
| [        [///][ Used to bind the Grid.]]                                                                                                                                  |
|                                                                                                                                                                                                                                                          |
| [        [///][ ][\</summary\>]]                                                                                                                     |
|                                                                                                                                                                                                                                                          |
| [        [///][ ][\<returns\>][Veiw page, it displays the Grid][\</returns\>]]                            |
|                                                                                                                                                                                                                                                          |
| [        [public] [ActionResult] Index()]                                                                                                                               |
|                                                                                                                                                                                                                                                          |
| [        {]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                          |
| [            [GridPropertiesModel]\<[Order]\> model = [new] [GridPropertiesModel]\<[Order]\>()] |
|                                                                                                                                                                                                                                                          |
| [            {]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                          |
| [                DataSource = [new] [NorthwindDataContext]().Orders.Take(200),]                                                                                         |
|                                                                                                                                                                                                                                                          |
| [                AllowPaging = [true],]                                                                                                                                                         |
|                                                                                                                                                                                                                                                          |
| [                AllowSorting = [true]]                                                                                                                                                         |
|                                                                                                                                                                                                                                                          |
| [            };]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                          |
| [            ViewData\[[\"GridModel\"]\] = model;]                                                                                                                                           |
|                                                                                                                                                                                                                                                          |
| [            [return] View();]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                          |
| [        }]                                                                                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

Code details:

[] 

a.  Objects created for **GridPropertiesModel** and the following grid properties are assigned to **model**

[·      ]**DataSource**---Gets or sets a data source for the Grid[ ]control

[·      ]**AllowPaging**---Gets or sets a value indicating whether the paging feature is enabled.

[·      ]**AllowSorting**---Gets or sets a value indicating whether the sorting feature is enabled.

b.  Pass the model to view using **ViewData**. This will pass the grid properties from the controller to the view.

Syntax:

ViewData\[\"model_id\"\] = object_name;

[] 

5.   In order to work with paging/sorting actions, create a post method for **Index** actions and update the following code in this method.

[       ]

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                      |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                                     |
| [///][ ][\<summary\>][]                     |
|                                                                                                                                                                                                                                     |
| [        [///][ Paging/sorting Requests are mapped to this method. This method invokes the HtmlActionResult]]                                        |
|                                                                                                                                                                                                                                     |
| [        [///][ from the grid. The required response is generated.]]                                                                                 |
|                                                                                                                                                                                                                                     |
| [        [///][ ][\</summary\>]]                                                                                                |
|                                                                                                                                                                                                                                     |
| [        [///][ ][\<param name=\"args\"\>][Contains paging properties ][\</param\>]] |
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
| [            [IEnumerable] data = [new] [NorthwindDataContext]().Orders.Take(200);]                                        |
|                                                                                                                                                                                                                                     |
| [            [return] data.GridActions\<[Order]\>();]                                                                                              |
|                                                                                                                                                                                                                                     |
| [        }]                                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: Essential Grid is fully AJAX enabled. For paging/sorting/filtering/editing actions the entire page will not be refreshed. The grid contents alone refresh using AJAX calls. The methods above are necessary to achieve the grid actions.


[] 

Code details:

a.  Get the data source and store it in an **IEnumeable** collection.

b.  Call the **GridAction** helper with the **Type** of **Model**, which invokes the custom action result. This will process the data source and return the required response while calling paging and sorting actions.

[] 

6.   Run the application.

 

{border="0"}

Figure 49**:** Grid Control Added to the Application

 

A sample which demonstrates a basic Grid control can be downloaded from the following link.

[[http://help.syncfusion.com/Support/grid_mvc/v8.3.0.20/UG/MvcGridSample.zip]{.UGHyperlink}](http://help.syncfusion.com/Support/grid_mvc/v8.3.0.20/UG/MvcGridSample.zip)[]{.UGHyperlink}

[] 


{border="0"}Note: The version number for the assemblies has been set to 8.3.0.20 in the Web.config file of the attached sample. Please change the version number to the appropriate version in the Web-2008.config or Web-2010.config files (available in root directory) and those will automatically be updated in the Web.config file.

 


[]{#related-topics}

