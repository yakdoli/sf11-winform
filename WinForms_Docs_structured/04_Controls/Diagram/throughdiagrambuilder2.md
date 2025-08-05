---
title: throughdiagrambuilder2.md
original_path: WinForms_Docs/04_Controls/Diagram/throughdiagrambuilder2.md
created_at: 2025-08-05
---






#### Through Diagram Builder {#through-diagram-builder style="tab-stops: 0pt"}

1.  [Create an Entity model in an application (see ][[Creating the ADO.NET Entity Data Model]](http://help.syncfusion.com/ug_94/User%20Interface/ASP.NET%20MVC/Diagram/default.htm?turl=Documents%2F52createtheadonetentitydatamodel.htm)[).]

2.  [In the **controller**, pass the data to the **view** page.]


+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller][]**                                                          |
|                                                                                                                                                     |
| []                                                                                 |
|                                                                                                                                                     |
| [        [NorthwindEntities] entities = [null];]      |
|                                                                                                                                                     |
| [        [public] [ActionResult] Index()]             |
|                                                                                                                                                     |
| [        {]                                                                                        |
|                                                                                                                                                     |
| [            entities = [new] [NorthwindEntities]();] |
|                                                                                                                                                     |
| [            [return] View(entities.Employee);]                               |
|                                                                                                                                                     |
| [        }]                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+


 

[3.   ]Create a strongly typed view (Refer to [How to \> Strongly Typed View](http://help.syncfusion.com/ug_94/User%20Interface/ASP.NET%20MVC/Diagram/default.htm?turl=Documents%2Fcreateastronglytypedview.htm)).[]

[4.   ]In the **view**, invoke the **Diagram** helper with the control ID, and you can use its **Model** property in **DataSource()** to bind the data source.[ ]

[] 

+--------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                   |
|                                                                                                                                      |
| [\<%][{]       |
|                                                                                                                                      |
| [      Html.Syncfusion().Diagram([\"EntityDataModel\"])]    |
|                                                                                                                                      |
| [        .DataSource(Model)]                                                        |
|                                                                                                                                      |
| [        .BindTo(bind =\>]                                                          |
|                                                                                                                                      |
| [            bind.NodeId([\"Emp_Id\"])]                     |
|                                                                                                                                      |
| [            .ParentNodeId([\"Emp_Head\"])]                 |
|                                                                                                                                      |
| [            .NodeText([\"Emp_Name\"])]                     |
|                                                                                                                                      |
| [            .NodeShape([\"Shape\"]))]                      |
|                                                                                                                                      |
| [        .DiagramMode([DiagramMode].SVG)]                   |
|                                                                                                                                      |
| [        .HorizontalSpacing(40)]                                                    |
|                                                                                                                                      |
| [        .LayoutType([LayoutType].HierarchicalTreeLayout)]  |
|                                                                                                                                      |
| [        .Orientation([TreeOrientation].TopBottom)]         |
|                                                                                                                                      |
| [        .Width(900)]                                                               |
|                                                                                                                                      |
| [        .Height(450)]                                                              |
|                                                                                                                                      |
| [        .Render();]                                                                |
|                                                                                                                                      |
| [  }[%\>]]                                              |
|                                                                                                                                      |
| []                                                              |
|                                                                                                                                      |
| []                                                              |
|                                                                                                                                      |
| **[\[Razor\]]**                                                                                  |
|                                                                                                                                      |
| [\@{][]        |
|                                                                                                                                      |
| [    Html.Syncfusion().Diagram([\"EntityDataModel\"])]      |
|                                                                                                                                      |
| [         .DataSource(Model)]                                                       |
|                                                                                                                                      |
| [         .BindTo(bind =\>]                                                         |
|                                                                                                                                      |
| [             bind.NodeId([\"Emp_Id\"])]                    |
|                                                                                                                                      |
| [             .ParentNodeId([\"Emp_Head\"])]                |
|                                                                                                                                      |
| [             .NodeText([\"Emp_Name\"])]                    |
|                                                                                                                                      |
| [             .NodeShape([\"Shape\"]))]                     |
|                                                                                                                                      |
| [         .DiagramMode([DiagramMode].SVG)]                  |
|                                                                                                                                      |
| [         .HorizontalSpacing(40)]                                                   |
|                                                                                                                                      |
| [         .LayoutType([LayoutType].HierarchicalTreeLayout)] |
|                                                                                                                                      |
| [         .Orientation([TreeOrientation].TopBottom)]        |
|                                                                                                                                      |
| [         .Width(900)]                                                              |
|                                                                                                                                      |
| [         .Height(450)]                                                             |
|                                                                                                                                      |
| [         .Render();]                                                               |
|                                                                                                                                      |
| [}][]          |
+--------------------------------------------------------------------------------------------------------------------------------------+

 

5.  [Build and run the application. The diagram will appear as shown below.]

 

{border="0"}

Figure 125: Entity Model Diagram

[]{#related-topics}

