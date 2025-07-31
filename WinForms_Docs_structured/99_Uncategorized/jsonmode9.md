---
title: jsonmode9.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\jsonmode9.md
created_at: 2025-07-03
---








  









### JSON Mode {#json-mode style="TEXT-ALIGN: justify; tab-stops: 0pt"}

Through GridBuilder

 

Perform the followings steps to implement a hierarchical grid through **GridBuilder** in JSON mode:

 

1.   Create a model in the application (Refer to [Getting Started\>Adding a Model to the Application](http://help.syncfusion.com/ug_91/User%20Interface/ASP.NET%20MVC/Grid/Documents/addingamodeltotheapplication.htm)).

2.   Create the grid control in the view and configure the properties.

3.   Use the **ChildGrid** method as shown in the following code.

4.   **ParentRelationKey** should contain the **Foreign Key**.

5.   It should end with the method **ToChildGridTemplate**.

 


+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                         |
|                                                                                                                                                                                                                                            |
| [           [\<%][=]Html.Syncfusion().Grid\<[EmployeeView]\>([\"GridSrc\"])                         ] |
|                                                                                                                                                                                                                                            |
| [                         .Caption([\"Employee Grid\"])]                                                                                                                       |
|                                                                                                                                                                                                                                            |
| [                         .AutoFormat([Skins].Almond)]                                                                                                                         |
|                                                                                                                                                                                                                                            |
| [                         .ActionMode([ActionMode].JSON)]                                                                                                                      |
|                                                                                                                                                                                                                                            |
| [                         .ChildGrid(child =\>]                                                                                                                                                        |
|                                                                                                                                                                                                                                            |
| [                         {]                                                                                                                                                                           |
|                                                                                                                                                                                                                                            |
| [       child.ChildGridTemplate(Html.Syncfusion().Grid\<[OrdersView]\>([\"ChildGrid\_\${EmployeeID}\"])]                                               |
|                                                                                                                                                                                                                                            |
| [                            .ParentRelationKey([new] [string]\[\] { [\"EmployeeID\"] })]                                            |
|                                                                                                                                                                                                                                            |
| [                            .ActionMode([ActionMode].JSON)]                                                                                                                   |
|                                                                                                                                                                                                                                            |
| [                            .ToChildGridTemplate());]                                                                                                                                                 |
|                                                                                                                                                                                                                                            |
| [                        })]                                                                                                                                                                           |
|                                                                                                                                                                                                                                            |
| [            [%\>]][ ][]                                                       |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

6.   For Razor, the code is given below:

 


+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[cshtml\]]**                                                                                                                                            |
|                                                                                                                                                                                                 |
| [          [\@{]]                                                                                                               |
|                                                                                                                                                                                                 |
| [              Html.Syncfusion().Grid\<[EmployeeView]\>([\"GridSrc\"])]                                     |
|                                                                                                                                                                                                 |
| [                         .Datasource(Model)]                                                                                                               |
|                                                                                                                                                                                                 |
| [                         .Caption([\"Employee Grid\"])]                                                                            |
|                                                                                                                                                                                                 |
| [                         .AutoFormat([Skins].Almond)]                                                                              |
|                                                                                                                                                                                                 |
| [                         .ActionMode([ActionMode].JSON)]                                                                           |
|                                                                                                                                                                                                 |
| [                         .ChildGrid(child =\>]                                                                                                             |
|                                                                                                                                                                                                 |
| [                         {]                                                                                                                                |
|                                                                                                                                                                                                 |
| [        child.ChildGridTemplate(Html.Syncfusion().Grid\<[OrdersView]\>([\"ChildGrid\_\${EmployeeID}\"]).]  |
|                                                                                                                                                                                                 |
| [                            .ParentRelationKey([new] [string]\[\] { [\"EmployeeID\"] })] |
|                                                                                                                                                                                                 |
| [                            .ActionMode([ActionMode].JSON)]                                                                        |
|                                                                                                                                                                                                 |
| [                            .ToChildGridTemplate());]                                                                                                      |
|                                                                                                                                                                                                 |
| [                        })]                                                                                                                                |
|                                                                                                                                                                                                 |
| [             .Render();]                                                                                                                                   |
|                                                                                                                                                                                                 |
| [             [}]    ]                                                                                                          |
|                                                                                                                                                                                                 |
| **[]**                                                                                                                                                      |
|                                                                                                                                                                                                 |
| []                                                                                                                                                               |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

7.   Set its data source and render the view.

 


+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                             |
|                                                                                                                                                                              |
| [        [public] ActionResult ][Index][()] |
|                                                                                                                                                                              |
| [        {            ]                                                                                                                  |
|                                                                                                                                                                              |
| [            [return] View();]                                                                                      |
|                                                                                                                                                                              |
| []                                                                                                                                       |
|                                                                                                                                                                              |
| [        }]                                                                                                                              |
|                                                                                                                                                                              |
| []                                                                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

8.   In order to work with paging actions, create a **Post** method for **Index** actions and bind the data source to the grid as given in the following code snippet.

 


+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                   |
| [        [///][ ][\<summary\>]]                                                                                                                               |
|                                                                                                                                                                                                                                                                   |
| [        [///][ Used to bind the grid. ]]                                                                                                                                          |
|                                                                                                                                                                                                                                                                   |
| [        [///][ ][\</summary\>]]                                                                                                                              |
|                                                                                                                                                                                                                                                                   |
| [        [///][ ][\<returns\>][View page; it displays the grid.][\</returns\>]]                                    |
|                                                                                                                                                                                                                                                                   |
| [        \[AcceptVerbs(HttpVerbs.Post)\]]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                   |
| [        [public] ActionResult ][Index][([PagingParams] args, [string] EmployeeID)] |
|                                                                                                                                                                                                                                                                   |
| [        {]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                   |
| [        [if] (args.ID.Contains([\"ChildGrid\"]))]                                                                                                                               |
|                                                                                                                                                                                                                                                                   |
| [            {                ]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                   |
| [                [IEnumerable] data = [new] [NorthwindDataContext]().OrdersViews.Where(c =\> c.EmployeeID == EmployeeID).ToList();]                      |
|                                                                                                                                                                                                                                                                   |
| [                [return] data.GridJSONActions\<[OrdersView]\>();                ]                                                                                               |
|                                                                                                                                                                                                                                                                   |
| [            }]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                   |
| [            [else]]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                   |
| [            {]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                   |
| [                [var] ordersData = [new] [NorthwindDataContext]().EmployeeViews.ToList();]                                                                 |
|                                                                                                                                                                                                                                                                   |
| [                [return] ordersData.GridJSONActions\<[EmployeeView]\>();]                                                                                                       |
|                                                                                                                                                                                                                                                                   |
| [            }]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                   |
| [        }][]                                                                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

 

9.   Run the application. The grid will appear as shown below:

 

[   ]{border="0"}

Figure 271: Hierarchical Grid in JSON Mode through GridBuilder

 

Tables for Properties, Methods, and Events

 

Properties

 

+-----------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------+--------------------------------+
| Property                                                                          | Description                                                                   | Type                                | Data type                      |
+-----------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------+--------------------------------+
| [ChildGrid]                                                 | Set the Child grid if you need the hierarchical grid.[] | [Server Side] | [String] |
+-----------------------------------------------------------------------------------+-------------------------------------------------------------------------------+-------------------------------------+--------------------------------+
| [ParentRelationKey] | Gets or sets the relation Key property, which relates to its parent Grid      | [Server Side] | String array                   |
|                                                                                   |                                                                               |                                     |                                |
| []                                                          |                                                                               |                                     |                                |
+===================================================================================+===============================================================================+=====================================+================================+

[] 

Methods

 

+------------------------------------------------------+--------------------------------------------------------------------------+-------------+-------------------------------------------------------------------------------------------+--------------------------+
| Method                                               | Description                                                              | Parameters  | Type                                                                                      | Return type              |
+------------------------------------------------------+--------------------------------------------------------------------------+-------------+-------------------------------------------------------------------------------------------+--------------------------+
| ChildGrid                                            | Set the Child grid if you need hierarchical grid.                        |             | string                                                                                    | IGridBuilder             |
|                                                      |                                                                          |             |                                                                                           |                          |
| []  |                                                                          |             |                                                                                           |                          |
+------------------------------------------------------+--------------------------------------------------------------------------+-------------+-------------------------------------------------------------------------------------------+--------------------------+
| ParentRelationKey                                    | Gets or sets the relation Key property, which relates to its parent Grid | String      | String array                                                                              | ChildGridTemplateBuilder |
|                                                      |                                                                          |             |                                                                                           |                          |
| []  |                                                                          |             |                                                                                           |                          |
+------------------------------------------------------+--------------------------------------------------------------------------+-------------+-------------------------------------------------------------------------------------------+--------------------------+
| ToChildGridTemplate                                  | Renders the Grid in ChildGrid template format                            |             | ChildGridTemplate (to render the Chidgrid, the  user has to render the grid as this type) | ChildGridTemplate        |
|                                                      |                                                                          |             |                                                                                           |                          |
|                                                      |                                                                          |             |                                                                                           |                          |
+======================================================+==========================================================================+=============+===========================================================================================+==========================+

[] 

Events

 

+--------------------+-------------------------------------------------------+-----------------+-----------------+
| Event              | Description                                           | Arguments       | Type            |
+--------------------+-------------------------------------------------------+-----------------+-----------------+
| OnRecordExpanded   | This event  rises in every Master row expanded event. | String handler  | Client-Side     |
|                    |                                                       |                 |                 |
|                    |                                                       |                 |                 |
+--------------------+-------------------------------------------------------+-----------------+-----------------+
| OnRecordCollapsed  | This event rises in every Master row Collapsed event. | String  handler | Client-Side     |
|                    |                                                       |                 |                 |
|                    |                                                       |                 |                 |
+--------------------+-------------------------------------------------------+-----------------+-----------------+
| OnRecordExpanding  | This event rises before every Master row Expand.      | String handler  | Client-Side     |
|                    |                                                       |                 |                 |
|                    |                                                       |                 |                 |
+--------------------+-------------------------------------------------------+-----------------+-----------------+
| OnRecordCollapsing | This event rises before every Master row Collapse.    | String handler  | Client-Side     |
|                    |                                                       |                 |                 |
|                    |                                                       |                 |                 |
+====================+=======================================================+=================+=================+

[] 

[] 

Using Client-Side Events

 

Using the **OnRecordCollapsing** event, we can avoid the **Collapse** event. Using the **OnRecordExpanding** event, we can avoid the **Expand** event.

 

The client-side events are used in ASPX as shown below in the server mode through **GridBuilder**.

 


+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [\<%][=][Html.Syncfusion().Grid\<][Order][\>(\"[GridSrc]\")] |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [                         .Datasource(Model)]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [                         .Caption(\"[Order Grid]\")]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [                         .AutoFormat(][Skins][.Almond)]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [                         .ClientSideEvents(eve =\>]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [                         {]                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [                            eve.OnRecordCollapsing(\"OnRecordCollapsing\");]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [                            eve.OnRecordExpanding(\"OnRecordExpanding\");]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [                            eve.OnRecordCollapsed(\"OnRecordCollapsed\");]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [                            eve.OnRecordExpanded(\"OnRecordExpanded\");]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [                         })][]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [                        ]                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [                         .ChildGrid(child =\>]                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [                         {                            child.ChildGridTemplate(Html.Syncfusion().Grid\<[Order_Detail]\>(\"[ChildGrid\_\${OrderID]}\")]                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [                            .Caption(\"[OrderDetails Grid]\")                            ]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [                            .ParentRelationKey(][new][ [string]][\[\] { \"[OrderID]\" })]                                   |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [                            .ToChildGridTemplate());]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [                         })                       ]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [%\>][     ][]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

For Razor, use the code shown below in server mode through **GridBuilder**.

 

 


+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[cshtml\]]**                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                |
| [\@{][]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                |
| [      Html.Syncfusion().Grid\<][Order][\>(\"[GridSrc]\")]                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                |
| [                         .Datasource(Model)]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                |
| [                         .Caption(\"[Order Grid]\")                      ]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                |
| [                         .AutoFormat(][Skins][.Almond)]                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                |
| [                         .ClientSideEvents(eve =\>]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                |
| [                        {]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                |
| [                            eve.OnRecordCollapsing(\"OnRecordCollapsing\");]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                |
| [                            eve.OnRecordExpanding(\"OnRecordExpanding\");]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                |
| [                            eve.OnRecordCollapsed(\"OnRecordCollapsed\");]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                |
| [                            eve.OnRecordExpanded(\"OnRecordExpanded\");]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                |
| [                        })][]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                |
| [                         .ChildGrid(child =\>]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                |
| [                         {]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                |
| [                            child.ChildGridTemplate(Html.Syncfusion().Grid\<][ Order_Detail][\>(\"[ChildGrid\_\${OrderID]}\")]                               |
|                                                                                                                                                                                                                                                                                                                                |
| [                            .Caption(\"[OrderDetails Grid]\")                                                       ]                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                |
| [                            .ParentRelationKey(][new][ [string]][\[\] { \"[OrderID]\" })] |
|                                                                                                                                                                                                                                                                                                                                |
| [                            .ToChildGridTemplate());]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                |
| [                         })]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                |
| [                         .Render();]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                |
| [    [}]    ]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                |
| [ ][      ]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

 

Appearance

{border="0"}

Figure 272: Hierarchical Grid

 

Sample Link

 

To view samples:

1.   Open the **ASP.NET MVC** **Sample Browser** from the dashboard (Refer to the Samples and Location chapter).

2.   Navigate to **Grid**\>**Hierarchy** to check out the different hierarchical grid demos.

[] 

[]{#related-topics}

