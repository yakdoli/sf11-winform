---
title: servermode9.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\servermode9.md
created_at: 2025-07-03
---








  









### Server Mode {#server-mode style="TEXT-ALIGN: justify; tab-stops: 0pt"}

Through GridBuilder

Perform the followings steps to implement a hierarchical grid through **GridBuilder** in server mode:

                                               

1.   Create a model in the application (Refer to [Getting Started\>Adding a Model to the Application](http://help.syncfusion.com/ug_91/User%20Interface/ASP.NET%20MVC/Grid/Documents/addingamodeltotheapplication.htm)).

2.   Create a strongly typed view (Refer to [How to\>Strongly Typed View](http://help.syncfusion.com/ug_91/User%20Interface/ASP.NET%20MVC/Grid/Documents/stronglytypedview.htm)).

3.   Create the grid control in the view and configure its properties.

4.   Use the **ChildGrid** method as shown below.

5.   **ParentRelationKey** should contain the **Foreign Key** to relate the **Parent**.

6.   It should end with the method **ToChildGridTemplate**.


+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [\<%][=][Html.Syncfusion().Grid\<][Order][\>(\"[GridSrc]\")] |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [                         .Datasource(Model)]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [                         .Caption(\"[Order Grid]\")]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [                         .AutoFormat(][Skins][.Almond)                        ]                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [                         .ChildGrid(child =\>]                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [                        {                            child.ChildGridTemplate(Html.Syncfusion().Grid\<[Order_Detail]\>(\"[ChildGrid\_\${OrderID]}\")]                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [                            .Caption(\"[OrderDetails Grid]\")                            ]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [                            .ParentRelationKey(][new][ [string]][\[\] { \"[OrderID]\" })]                                   |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [                            .ToChildGridTemplate());]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [                        })                       ]                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [%\>][     ]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


7.   For Razor, use the code shown below:

 


+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[cshtml\]]**                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                |
| [    [\@{]]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                |
| [      Html.Syncfusion().Grid\<][Order][\>(\"[GridSrc]\")]                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                |
| [                         .Datasource(Model)]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                |
| [                         .Caption(\"[Order Grid]\")                      ]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                |
| [                         .AutoFormat(][Skins][.Almond)]                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                |
| [                         .ChildGrid(child =\>]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                |
| [                         {]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                |
| [                            child.ChildGridTemplate(Html.Syncfusion().Grid\<][ Order_Detail][\>(\"[ChildGrid\_\${OrderID]}\")]                               |
|                                                                                                                                                                                                                                                                                                                                |
| [                            .Caption(\"[OrderDetails Grid]\")                                                       ]                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                |
| [                            .ParentRelationKey(][new][ [string]][\[\] { \"[OrderID]\" })] |
|                                                                                                                                                                                                                                                                                                                                |
| [                            .ToChildGridTemplate());]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                |
| [                         })]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                |
| [                         .Render();]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                |
| [    [}]    ][ ]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


8.   Set its data source and render the view.

 


+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                        |
|                                                                                                                                                                                                         |
| [        [public] ActionResult ][Index][()]  |
|                                                                                                                                                                                                         |
| [        {]                                                                                                                                            |
|                                                                                                                                                                                                         |
| [            [var] data = [new] [NorthwindDataContext]().Orders.Take(200).ToList();] |
|                                                                                                                                                                                                         |
| [            [return] View(data);]                                                                                                |
|                                                                                                                                                                                                         |
| []                                                                                                                                                     |
|                                                                                                                                                                                                         |
| [        }]                                                                                                                                            |
|                                                                                                                                                                                                         |
| [  ]                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


9.   In order to work with paging actions, create a **Post** method for **Index** actions and bind the data source to the grid as given in the following code:

 


+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [        [///][ ][\<summary\>]]                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [        [///][ Used to bind the grid.]]                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [        [///][ ][\</summary\>]]                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [        [///][ ][\<returns\>][View page; it displays the grid.][\</returns\>]]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [public][ ][ActionResult Index(][PagingParams][ ][args, ][int][? OrderID)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [        {]                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [        ][if][ (args.ID.Contains(\"][ChildGrid][\"))]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [            {]                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                ][IEnumerable][ ][data = new ][NorthwindDataContext][ ().Order_Details.Where(c =\> c.OrderID == OrderID).ToList();]                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                return data.GridActions\<][ Order_Detail][l\>();                ]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [            }]                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [            ][else][]                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [            {]                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                ][var][ ][ordersData = ][new][ NorthwindDataContext][ ().Orders.Take(60).ToList();]                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                return ordersData.GridActions\<][Order][\>();]                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [            }]                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [        }]                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

 

10.  Run the application. The grid will appear as shown below:

 

{border="0"}

Figure 270: Hierarchical Grid in Server Mode through GridBuilder

[   ]

[]{#related-topics}

