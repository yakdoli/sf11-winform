---
title: dynamicdatabinding.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\dynamicdatabinding.md
created_at: 2025-07-03
---








  









### Dynamic Data Binding {#dynamic-data-binding style="tab-stops: 0pt"}

 

The dynamic data binding feature does not need any parameters to define the grid. This feature will be useful to dynamically define the **ModelType** of the grid. According to the data source the grid will render the columns internally.

 

Use Case Scenarios

 

Dynamic data binding can be used for:

1.  Automatically generating columns without mapping to column names. (Auto-generated column support)

2.  Dynamically binding data sources to the Grid control. (Dynamic data binding support)

 

Dynamically Bind Data to Grid

 

Through GridBuilder

 

To dynamically bind data to the grid through **GridBuilder**:

1.   Create a model in the application (Refer to [[[Getting Started\>Adding a Model to the Application]]{.underline}](http://help.syncfusion.com/ug_91/User%20Interface/ASP.NET%20MVC/Grid/Documents/addingamodeltotheapplication.htm)).

2.  Create the Grid control in the view of type **object** and configure its properties.

 


+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                             |
|                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                          |
|                                                                                                                                                                                                                     |
| [    [\<%][ =]Html.Grid\<[object]\>([\"Grid1\"])] |
|                                                                                                                                                                                                                     |
| [                        .Datasource(([IEnumerable])ViewData\[[\"data\"]\])]                    |
|                                                                                                                                                                                                                     |
| [                        .Caption([\"Dynamic DataSource\"])                         ]                                   |
|                                                                                                                                                                                                                     |
| [                        .AutoFormat([Skins].Almond)]                                                                   |
|                                                                                                                                                                                                                     |
| [    [%\>] ]                                                                                                        |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 


+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[][cshtml][\]]**                                         |
|                                                                                                                                                                                                  |
| [   [\@{] Html.Grid\<[object]\>([\"Grid1\"])]       |
|                                                                                                                                                                                                  |
| [                        .Datasource(([IEnumerable])ViewData\[[\"data\"]\])] |
|                                                                                                                                                                                                  |
| [                        .Caption(ViewData\[[\"datatype\"]\].ToString())]                            |
|                                                                                                                                                                                                  |
| [                        .AutoFormat([Skins].Almond)]                                                |
|                                                                                                                                                                                                  |
| [                .Render();]                                                                                                 |
|                                                                                                                                                                                                  |
| [    [}]]                                                                                        |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

3.  Set its data source in the corresponding **ViewData** and render the view.

 


+---------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                            |
|                                                                                                                                             |
|         [public] [ActionResult] Index()\                                                       |
| \                                                                                                                                           |
|                                                                                                                                             |
|         {\                                                                                                                                  |
| \                                                                                                                                           |
|                                                                                                                                             |
|             [var] data = [new] [NorthwindDataContext]().Orders;           |
|                                                                                                                                             |
| [              ViewData\[[\"data\"]\] = data;]\ |
| \                                                                                                                                           |
|                                                                                                                                             |
|             [return] View();\                                                                                          |
| \                                                                                                                                           |
|                                                                                                                                             |
|         }                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------+


 

4.  Run the application, the grid will appear as shown below:

 

{border="0"}

Figure 101: Grid Bound to Dynamic Data Source through GridBuilder

[   ]

 

Through GridPropertiesModel

To dynamically bind data to the grid through **GridPropertiesModel**:

1.   Create a model in the application (Refer to [[[Getting Started\>Adding a Model to the Application]]{.underline}](http://help.syncfusion.com/ug_91/User%20Interface/ASP.NET%20MVC/Grid/Documents/addingamodeltotheapplication.htm)).

2.  Add the following code in the **Index.aspx** file to create the Grid control in the view.

 


+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [    [\<%][=] Html.Syncfusion().Grid\<[object]\>([\"Grid1\"],] |
|                                                                                                                                                                                                                                  |
| [    ([GridPropertiesModel]\<[object]\>)ViewData\[[\"GridModel\"]\] ]                   |
|                                                                                                                                                                                                                                  |
| [    [%\>]]                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 


+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[][cshtml][\]]**                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [@(][new][ [HtmlString](Html.Syncfusion().Grid\<[object]\>([\"Grid1\"], ([GridPropertiesModel]\<[object]\>)ViewData\[[\"GridModel\"]\]).ToString())[)]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

 

3.  Create a **GridPropertiesModel** of type **object** in the **Index** method.

 


+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                     |
| [    [public] [ActionResult] Index()\                                                                                                                                                                                                  |
|     {]\                                                                                                                                                                                                                                              |
| [       [GridPropertiesModel]\<[object]\> gridModel = [new] [GridPropertiesModel]\<[object]\>()] |
|                                                                                                                                                                                                                                                                                     |
| [       {]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                     |
| [               DataSource = [new] [NorthwindDataContext]().Orders,]                                                                                               |
|                                                                                                                                                                                                                                                                                     |
| [               Caption = [\"Orders\"],]                                                                                                                                                |
|                                                                                                                                                                                                                                                                                     |
| [       };]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| [       ViewData\[[\"GridModel\"]\] = gridModel;]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                     |
| [       [return] View();]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                     |
| \                                                                                                                                                                                                                                                                                   |
|         }[]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                     |
| [   ]                                                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

4.  Run the application. The grid will appear as shown below:

 

{border="0"}

Figure 102: Grid Bound to Dynamic Data Source through GridPropertiesModel

 

Tables for Methods (Properties and Events Not Applicable)

 

Methods

 


  Method    Description                                   Parameters   Type   Return type
  --------- --------------------------------------------- ------------ ------ -------------------------
  UnBound   Gets or sets the column to be bound or not.   IsUnBound    bool   IGridColumnBuilder\<T\>


 

 

How to Add Columns

 

Through GridBuilder

To add columns in a dynamically bound grid through **GridBuilder**:

1.   Create a model in the application (Refer to [[[Getting Started\>Adding a Model to the Application]]{.underline}](http://help.syncfusion.com/ug_91/User%20Interface/ASP.NET%20MVC/Grid/Documents/addingamodeltotheapplication.htm)).

2.   Create the Grid control in the view of type **object** and configure its properties.

3.   Add columns using the following code snippet:


+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                             |
|                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                          |
|                                                                                                                                                                                                                     |
| [    [\<%][ =]Html.Grid\<[object]\>([\"Grid1\"])] |
|                                                                                                                                                                                                                     |
| [                        .Datasource(([IEnumerable])ViewData\[[\"data\"]\])]                    |
|                                                                                                                                                                                                                     |
| [                        .Column(col=\>{]                                                                                                       |
|                                                                                                                                                                                                                     |
| [                            col.Add([\"OrderId\"]).UnBound([false]);]                             |
|                                                                                                                                                                                                                     |
| [                            col.Add([\"OrderDate\"]).UnBound([false]);]                           |
|                                                                                                                                                                                                                     |
| [                            col.Add([\"CustomerID\"]).UnBound([false]);]                          |
|                                                                                                                                                                                                                     |
| [                            col.Add([\"ShippedDate\"]).UnBound([false]);]                         |
|                                                                                                                                                                                                                     |
| [                            col.Add([\"ShipAddress\"]).UnBound([false]);]                         |
|                                                                                                                                                                                                                     |
| [                        })]                                                                                                                    |
|                                                                                                                                                                                                                     |
| [                         .Caption([\"Dynamic DataSource\"])                         ]                                  |
|                                                                                                                                                                                                                     |
| [                         .AutoFormat([Skins].Almond)]                                                                  |
|                                                                                                                                                                                                                     |
| [    [%\>] ]                                                                                                        |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 


+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[][cshtml][\]]**                                         |
|                                                                                                                                                                                                  |
| **[]**                                                                                                                                                       |
|                                                                                                                                                                                                  |
| [   [\@{] Html.Grid\<[object]\>([\"Grid1\"])]       |
|                                                                                                                                                                                                  |
| [                        .Datasource(([IEnumerable])ViewData\[[\"data\"]\])] |
|                                                                                                                                                                                                  |
| [                        .Column(col=\>{]                                                                                    |
|                                                                                                                                                                                                  |
| [                            col.Add([\"OrderId\"]).UnBound([false]);]          |
|                                                                                                                                                                                                  |
| [                            col.Add([\"OrderDate\"]).UnBound([false]);]        |
|                                                                                                                                                                                                  |
| [                            col.Add([\"CustomerID\"]).UnBound([false]);]       |
|                                                                                                                                                                                                  |
| [                            col.Add([\"ShippedDate\"]).UnBound([false]);]      |
|                                                                                                                                                                                                  |
| [                            col.Add([\"ShipAddress\"]).UnBound([false]);]      |
|                                                                                                                                                                                                  |
| [                        })]                                                                                                 |
|                                                                                                                                                                                                  |
| [                        .Caption(ViewData\[[\"datatype\"]\].ToString())]                            |
|                                                                                                                                                                                                  |
| [                        .AutoFormat([Skins].Almond)]                                                |
|                                                                                                                                                                                                  |
| []                                                                                                                           |
|                                                                                                                                                                                                  |
| [          .Render();]                                                                                                       |
|                                                                                                                                                                                                  |
| [    [}] ]                                                                                       |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

4.   Set its data source in corresponding **ViewData** and render the view.

 


+---------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                            |
|                                                                                                                                             |
|         [public] [ActionResult] Index()\                                                       |
| \                                                                                                                                           |
|                                                                                                                                             |
|         {\                                                                                                                                  |
| \                                                                                                                                           |
|                                                                                                                                             |
|             [var] data = [new] [NorthwindDataContext]().Orders;           |
|                                                                                                                                             |
| [              ViewData\[[\"data\"]\] = data;]\ |
| \                                                                                                                                           |
|                                                                                                                                             |
|             [return] View();\                                                                                          |
| \                                                                                                                                           |
|                                                                                                                                             |
|         }                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------+


 

5.   Run the application. The grid will appear as shown below:

 

{border="0"}

Figure 103: Grid with Columns Added through GridBuilder

 

Through GridPropertiesModel

To add columns in a dynamically bound grid through **GridPropertiesModel**:

1.   Create a model in the application (Refer to [[[Getting Started\>Adding a Model to the Application]]{.underline}](http://help.syncfusion.com/ug_91/User%20Interface/ASP.NET%20MVC/Grid/Documents/addingamodeltotheapplication.htm)).

2.   Add the following code in the **Index.aspx** file to create the Grid control in the view.

3.   Add columns using the code shown below.

 


+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                            |
| [    [\<%][=] Html.Syncfusion().Grid\<[object]\>([\"Grid1\"],[\"GridModel\"],[\"GridModel\"], col =\> {] |
|                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                            |
| [                            col.Add([\"OrderId\"]).UnBound([false]);]                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                            |
| [                            col.Add([\"OrderDate\"]).UnBound([false]);]                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                            |
| [                            col.Add([\"CustomerID\"]).UnBound([false]);]                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                            |
| [                            col.Add([\"ShippedDate\"]).UnBound([false]);]                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                            |
| [                            col.Add([\"ShipAddress\"]).UnBound([false]);]                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                            |
| [       } ) [%\>]]                                                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

 


+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[][cshtml][\]]**                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [    [@(][new] [HtmlString](Html.Syncfusion().Grid\<[object]\>([\"Grid1\"],[\"GridModel\"],[\"GridModel\"], col =\> {] |
|                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [                            col.Add([\"OrderId\"]).UnBound([false]);]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [                            col.Add([\"OrderDate\"]).UnBound([false]);]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [                            col.Add([\"CustomerID\"]).UnBound([false]);]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [                            col.Add([\"ShippedDate\"]).UnBound([false]);]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [                            col.Add([\"ShipAddress\"]).UnBound([false]);]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [       } ).ToString())[)]]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

4.   Create a **GridPropertiesModel** of type **object** in the **Index** method.

 


+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                     |
| [    [public] [ActionResult] Index()\                                                                                                                                                                                                  |
|     {]\                                                                                                                                                                                                                                              |
| [       [GridPropertiesModel]\<[object]\> gridModel = [new] [GridPropertiesModel]\<[object]\>()] |
|                                                                                                                                                                                                                                                                                     |
| [       {]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                     |
| [               DataSource = [new] [NorthwindDataContext]().Orders,]                                                                                               |
|                                                                                                                                                                                                                                                                                     |
| [               Caption = [\"Orders\"],]                                                                                                                                                |
|                                                                                                                                                                                                                                                                                     |
| [       };]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| [       ViewData\[[\"GridModel\"]\] = gridModel;]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                     |
| [       [return] View();]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                     |
| \                                                                                                                                                                                                                                                                                   |
|         }[]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                     |
| [   ]                                                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

5.   Run the application. The Grid will appear as shown below:

{border="0"}

Figure 104: Grid with Columns Added through GridPropertiesModel

 

Sample Link

To view the samples, follow the steps below:

1.   Open the ASP.NET MVC sample browser from the dashboard.

2.   Navigate to the **Grid** samples.

3.   Select the **Data Binding** category and select the **Dynamic Data Binding** sample.

 

[]{#related-topics}

