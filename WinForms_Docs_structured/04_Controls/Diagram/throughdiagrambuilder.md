---
title: throughdiagrambuilder.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Diagram\throughdiagrambuilder.md
created_at: 2025-07-03
---






#### Through Diagram Builder {#through-diagram-builder style="tab-stops: 0pt"}

1.  [Create a model in the application (Refer to [[Getting Started \> Examining the MVC Project \> Adding a Model to the Application]]{.underline}).]

2.  [In the **controller**, pass the data to the **view** page.]


+----------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller][]**                                             |
|                                                                                                                                        |
| []                                                                    |
|                                                                                                                                        |
| [        [Northwind] context = [null];]  |
|                                                                                                                                        |
| [        [public] [ActionResult] CRUD()] |
|                                                                                                                                        |
| [        {]                                                                           |
|                                                                                                                                        |
| [            context = SqlCE;]                                                        |
|                                                                                                                                        |
| [            [return] View(context.Products);]                   |
|                                                                                                                                        |
| [        }]                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------+


 

[3.   ]Create a strongly typed view (Refer to [How to \> Strongly Typed View](http://help.syncfusion.com/ug_94/User%20Interface/ASP.NET%20MVC/Diagram/default.htm?turl=Documents%2Fcreateastronglytypedview.htm)).[]

[4.   ]In the **view**, invoke the **Diagram** helper with the control ID, and you can use its **Model** property in **DataSource** to bind the data source and set the **SaveAction** in **Mappers**.[ ]

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                 |
|                                                                                                                                                    |
| [\<%][{]                     |
|                                                                                                                                                    |
| [      Html.Syncfusion().Diagram([\"CRUD\"])]                             |
|                                                                                                                                                    |
| [        .DataSource(Model)]                                                                      |
|                                                                                                                                                    |
| [        .BindTo(bind =\>]                                                                        |
|                                                                                                                                                    |
| [            bind.NodeId([\"ProductCode\"])]                              |
|                                                                                                                                                    |
| [            .ParentNodeId([\"Parent\"])]                                 |
|                                                                                                                                                    |
| [            .NodeText([\"ProductName\"])]                                |
|                                                                                                                                                    |
| [            .NodeShape([\"Shape\"]))]                                    |
|                                                                                                                                                    |
| [        .DiagramMode([DiagramMode].SVG)]                                 |
|                                                                                                                                                    |
| [        .HorizontalSpacing(35)]                                                                  |
|                                                                                                                                                    |
| [        .LayoutType([LayoutType].HierarchicalTreeLayout)]                |
|                                                                                                                                                    |
| [        .Orientation([TreeOrientation].TopBottom)]                       |
|                                                                                                                                                    |
| **[        .Mappers(mappers =\> mappers.SaveAction([\"SaveDiagram\"]))]** |
|                                                                                                                                                    |
| [        .Width(1000)]                                                                            |
|                                                                                                                                                    |
| [        .Height(450)]                                                                            |
|                                                                                                                                                    |
| [        .Render();]                                                                              |
|                                                                                                                                                    |
| [  }[%\>]]                                                            |
|                                                                                                                                                    |
| []                                                                            |
|                                                                                                                                                    |
| **[\[Razor\]]**                                                                                                |
|                                                                                                                                                    |
| [\@{][]                      |
|                                                                                                                                                    |
| [    Html.Syncfusion().Diagram([\"CRUD\"])]                               |
|                                                                                                                                                    |
| [      .DataSource(Model)]                                                                        |
|                                                                                                                                                    |
| [      .BindTo(bind =\>]                                                                          |
|                                                                                                                                                    |
| [          bind.NodeId([\"ProductCode\"])]                                |
|                                                                                                                                                    |
| [            .ParentNodeId([\"Parent\"])]                                 |
|                                                                                                                                                    |
| [            .NodeText([\"ProductName\"])]                                |
|                                                                                                                                                    |
| [            .NodeShape([\"Shape\"]))]                                    |
|                                                                                                                                                    |
| [      .DiagramMode([DiagramMode].SVG)]                                   |
|                                                                                                                                                    |
| [      .HorizontalSpacing(35)]                                                                    |
|                                                                                                                                                    |
| [      .LayoutType([LayoutType].HierarchicalTreeLayout)]                  |
|                                                                                                                                                    |
| [      .Orientation([TreeOrientation].TopBottom)]                         |
|                                                                                                                                                    |
| **[      .Mappers(mappers =\> mappers.SaveAction([\"SaveDiagram\"]))]**   |
|                                                                                                                                                    |
| [      .Width(1000)]                                                                              |
|                                                                                                                                                    |
| [      .Height(450)]                                                                              |
|                                                                                                                                                    |
| [      .Render();]                                                                                |
|                                                                                                                                                    |
| [}][]                        |
|                                                                                                                                                    |
| []                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------+

 

5.  [In the controller, define the post action to save changes as displayed below. In this example, the repository method **SaveDiagram()** is used to update records to the data source. In the function below, we can get the list of updated nodes through the parameter **updatedNodes** using the bind prefix **updatedNodes**. In the same way we can get the list of added and deleted nodes and lines using the bind prefixes **addedNodes**, **deletedNodes**, **addedLines**, **updatedLines**, and **deletedLines** respectively.]

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [        \[[HttpPost]\]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [        [public] [ActionResult] SaveDiagram(\[[Bind](Prefix = [\"addedNodes\"])\][IEnumerable]\<[Node]\> addNodes, \[[Bind](Prefix = [\"updatedNodes\"])\][IEnumerable]\<[Node]\> updatedNodes,]                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [             \[[Bind](Prefix = [\"deletedNodes\"])\][IEnumerable]\<[Node]\> deletedNodes, \[[Bind](Prefix = [\"addedLines\"])\][IEnumerable]\<[LineConnector]\> addLines, \[[Bind](Prefix = [\"updatedLines\"])\][IEnumerable]\<[LineConnector]\> updatedLines,] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [               \[[Bind](Prefix = [\"deletedLines\"])\][IEnumerable]\<[LineConnector]\> deletedLines, [string] RequestType)]                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [        {]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [            context = SqlCE;]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [            [if] (addNodes != [null])]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [                [this].AddNodes(addNodes);]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [            [if] (updatedNodes != [null])]                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [                [this].UpdateNodes(updatedNodes);]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [            [if] (deletedNodes != [null])]                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [                [this].DeletedNodes(deletedNodes);]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [            [return] context.Products.DiagramAction([true]);]                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

6.  [To save the diagram, call the **saveDiagram** function on button click.]

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                                                                          |
|                                                                                                                                                                                   |
| [    \$([\"#btnSave\"]).bind([\"click\"], [function] (evt) {] |
|                                                                                                                                                                                   |
| [        diagram = \$find([\"CRUD\"]);]                                                                   |
|                                                                                                                                                                                   |
| [        diagram.saveDiagram();]                                                                                                 |
|                                                                                                                                                                                   |
| [    });]                                                                                                                        |
|                                                                                                                                                                                   |
| []                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

7.  [Build and run the application. Edit the diagram as displayed below.]

 

{border="0"}

Figure 121: Diagram with Editing

8.  [Click the **Save** button to save the changes in the data source. ]

[]{#related-topics}

