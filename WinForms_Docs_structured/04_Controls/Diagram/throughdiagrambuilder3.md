---
title: throughdiagrambuilder3.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Diagram\throughdiagrambuilder3.md
created_at: 2025-07-03
---






#### Through Diagram Builder {#through-diagram-builder style="tab-stops: 0pt"}

1.  [Create a model in the application (Refer to ][[How to \> Creating the Generic Collection Model]](http://help.syncfusion.com/ug_94/User%20Interface/ASP.NET%20MVC/Grid/Documents/creatingthegenericcollectionmodel1.htm)[).]

2.  [In the **controller**, pass the data to the **view** page.]


+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller][]**                                                                 |
|                                                                                                                                                            |
| [        [CompanyDataContext] companyContext = [null];]      |
|                                                                                                                                                            |
| [        [public] [ActionResult] Index()]                    |
|                                                                                                                                                            |
| [        {]                                                                                               |
|                                                                                                                                                            |
| [            companyContext = [new] [CompanyDataContext]();] |
|                                                                                                                                                            |
| [            [return] View(companyContext.Company);]                                 |
|                                                                                                                                                            |
| [        }]                                                                                               |
|                                                                                                                                                            |
| []                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

[3.   ]Create a strongly typed view (Refer to [How to \> Strongly Typed View](http://help.syncfusion.com/ug_94/User%20Interface/ASP.NET%20MVC/Diagram/default.htm?turl=Documents%2Fcreateastronglytypedview.htm)).[]

[4.   ]In the **view**, invoke the **Diagram** helper with the control ID, and you can use its **Model** property in **DataSource()** to bind the data source.[ ]

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                             |
|                                                                                                                                                |
| [\<%][{]                 |
|                                                                                                                                                |
| [      Html.Syncfusion().Diagram([\"GenericList\"])]                  |
|                                                                                                                                                |
| [        .DataSource(Model)]                                                                  |
|                                                                                                                                                |
| [        .BindTo(bind =\>]                                                                    |
|                                                                                                                                                |
| [            bind.NodeId([\"DeptId\"])]                               |
|                                                                                                                                                |
| [            .ParentNodeId([\"HeadDept\"])]                           |
|                                                                                                                                                |
| [            .NodeText([\"DeptName\"])]                               |
|                                                                                                                                                |
| [            .NodeShape([\"Shape\"]))]                                |
|                                                                                                                                                |
| [        .DiagramMode([DiagramMode].SVG)]                             |
|                                                                                                                                                |
| [        .HorizontalSpacing(40)]                                                              |
|                                                                                                                                                |
| [        .LayoutType([LayoutType].HierarchicalTreeLayout)]            |
|                                                                                                                                                |
| [        .Orientation([TreeOrientation].TopBottom)]                   |
|                                                                                                                                                |
| [        .Mappers(mappers =\> mappers.SaveAction([\"SaveDiagram\"]))] |
|                                                                                                                                                |
| [        .Width(900)]                                                                         |
|                                                                                                                                                |
| [        .Height(500)]                                                                        |
|                                                                                                                                                |
| [        .Render();]                                                                          |
|                                                                                                                                                |
| [  }[%\>]]                                                        |
|                                                                                                                                                |
| **[]**                                                                                                     |
|                                                                                                                                                |
| **[\[Razor\]]**                                                                                            |
|                                                                                                                                                |
| [\@{][]                  |
|                                                                                                                                                |
| [    Html.Syncfusion().Diagram([\"GenericList\"])]                    |
|                                                                                                                                                |
| [         .DataSource(Model)]                                                                 |
|                                                                                                                                                |
| [        .BindTo(bind =\>]                                                                    |
|                                                                                                                                                |
| [            bind.NodeId([\"DeptId\"])]                               |
|                                                                                                                                                |
| [            .ParentNodeId([\"HeadDept\"])]                           |
|                                                                                                                                                |
| [            .NodeText([\"DeptName\"])]                               |
|                                                                                                                                                |
| [            .NodeShape([\"Shape\"]))]                                |
|                                                                                                                                                |
| [        .DiagramMode([DiagramMode].SVG)]                             |
|                                                                                                                                                |
| [        .HorizontalSpacing(40)]                                                              |
|                                                                                                                                                |
| [        .LayoutType([LayoutType].HierarchicalTreeLayout)]            |
|                                                                                                                                                |
| [        .Orientation([TreeOrientation].TopBottom)]                   |
|                                                                                                                                                |
| [        .Mappers(mappers =\> mappers.SaveAction([\"SaveDiagram\"]))] |
|                                                                                                                                                |
| [        .Width(900)]                                                                         |
|                                                                                                                                                |
| [        .Height(500)]                                                                        |
|                                                                                                                                                |
| [        .Render();]                                                                          |
|                                                                                                                                                |
| [}][]                    |
|                                                                                                                                                |
| []                                                                                            |
|                                                                                                                                                |
| []                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------+

 

5.  [Build and run the application. The diagram will appear as shown below.]

 

{border="0"}

Figure 127: Generic Collection Diagram

[]{#related-topics}

