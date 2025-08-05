---
title: throughdiagrambuilder1.md
original_path: WinForms_Docs/04_Controls/Diagram/throughdiagrambuilder1.md
created_at: 2025-08-05
---






#### Through Diagram Builder {#through-diagram-builder style="tab-stops: 0pt"}

1.  [Create a model in the application (Refer to ][[Getting Started \> Examining the MVC Project \> Adding a Model to the Application]](http://help.syncfusion.com/ug_94/User%20Interface/ASP.NET%20MVC/Diagram/default.htm?turl=Documents%2Faddingamodeltotheapplication.htm)[).]

2.  [In the **controller**, pass the data to the **view** page.]


+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller][]**                                                                             |
|                                                                                                                                                                        |
| []                                                                                                    |
|                                                                                                                                                                        |
| [Northwind][ context = [null];] |
|                                                                                                                                                                        |
| [        [public] [ActionResult] Index()]                                |
|                                                                                                                                                                        |
| [        {]                                                                                                           |
|                                                                                                                                                                        |
| [            context = SqlCE;]                                                                                        |
|                                                                                                                                                                        |
| [            [return] View(context.DiagramDataBinding);]                                         |
|                                                                                                                                                                        |
| [        }]                                                                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

[3.   ]Create a strongly typed view (Refer to [How to \> Strongly Typed View](http://help.syncfusion.com/ug_94/User%20Interface/ASP.NET%20MVC/Diagram/default.htm?turl=Documents%2Fcreateastronglytypedview.htm)).[]

[4.   ]In the **view**, invoke the **Diagram** helper with the control ID, and you can use its **Model** property in **Datasource()** in order to bind the data source.[ ]

[] 

+-------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                  |
|                                                                                                                                     |
| [\<%][{]      |
|                                                                                                                                     |
| [      Html.Syncfusion().Diagram([\"LinqToSql\"])]         |
|                                                                                                                                     |
| [        .DataSource(Model)]                                                       |
|                                                                                                                                     |
| [        .BindTo(bind =\>]                                                         |
|                                                                                                                                     |
| [            bind.NodeId([\"NodeId\"])]                    |
|                                                                                                                                     |
| [            .ParentNodeId([\"ParentNodeId\"])]            |
|                                                                                                                                     |
| [            .NodeText([\"NodeText\"])]                    |
|                                                                                                                                     |
| [            .NodeShape([\"Shape\"]))]                     |
|                                                                                                                                     |
| [        .DiagramMode([DiagramMode].SVG)]                  |
|                                                                                                                                     |
| [        .LayoutType([LayoutType].HierarchicalTreeLayout)] |
|                                                                                                                                     |
| [        .Orientation([TreeOrientation].TopBottom)]        |
|                                                                                                                                     |
| [        .Width(750)]                                                              |
|                                                                                                                                     |
| [        .Height(450)]                                                             |
|                                                                                                                                     |
| [        .Render();]                                                               |
|                                                                                                                                     |
| [  }[%\>]]                                             |
|                                                                                                                                     |
| []                                                             |
|                                                                                                                                     |
| **[\[Razor\]]**                                                                                 |
|                                                                                                                                     |
| [\@{][]       |
|                                                                                                                                     |
| [    Html.Syncfusion().Diagram([\"LinqToSql\"])]           |
|                                                                                                                                     |
| [      .DataSource(Model)]                                                         |
|                                                                                                                                     |
| [      .BindTo(bind =\>]                                                           |
|                                                                                                                                     |
| [          bind.NodeId([\"NodeId\"])]                      |
|                                                                                                                                     |
| [          .ParentNodeId([\"ParentNodeId\"])]              |
|                                                                                                                                     |
| [          .NodeText([\"NodeText\"])]                      |
|                                                                                                                                     |
| [          .NodeShape([\"Shape\"]))]                       |
|                                                                                                                                     |
| [      .DiagramMode([DiagramMode].SVG)]                    |
|                                                                                                                                     |
| [      .LayoutType([LayoutType].HierarchicalTreeLayout)]   |
|                                                                                                                                     |
| [      .Orientation([TreeOrientation].TopBottom)]          |
|                                                                                                                                     |
| [      .Width(750)]                                                                |
|                                                                                                                                     |
| [      .Height(450)]                                                               |
|                                                                                                                                     |
| [      .Render();]                                                                 |
|                                                                                                                                     |
| [}][]         |
+-------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.  [Build and run the application. The diagram will appear as shown below.]

 

{border="0"}

Figure 123: LINQ to SQL Diagram

[]{#related-topics}

