---
title: printdiagrampage.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Diagram\printdiagrampage.md
created_at: 2025-07-03
---








  









### Print Diagram Page {#print-diagram-page style="tab-stops: 0pt"}

The following code snippet illustrates how to print the diagram page.

1.  [In the **controller**, pass the data to the **view** page.]


+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller][]**                                                                             |
|                                                                                                                                                                        |
| []                                                                                                    |
|                                                                                                                                                                        |
| [Northwind][ context = [null];] |
|                                                                                                                                                                        |
| [        [public] [ActionResult] ExportDiagram()]                        |
|                                                                                                                                                                        |
| [        {]                                                                                                           |
|                                                                                                                                                                        |
| [            context = SqlCE;]                                                                                        |
|                                                                                                                                                                        |
| [            [return] View(context.DiagramDataBinding);]                                         |
|                                                                                                                                                                        |
| [        }]                                                                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

[2.   Create a ][[Strongly Typed View]{.UGHyperlink}](http://help.syncfusion.com/ug_94/User%20Interface/ASP.NET%20MVC/Diagram/default.htm?turl=Documents%2Fcreateastronglytypedview.htm)[. ]

3.  [In the **view**, invoke the **Diagram** helper with the control ID, and set the **DataDource**, **BindTo**, **DiagramMode**, and **Mapper** methods.]

 

+-------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                  |
|                                                                                                                                     |
| [\<%][{]      |
|                                                                                                                                     |
| [      Html.Syncfusion().Diagram([\"ExportDiagram\"])]     |
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
| [    Html.Syncfusion().Diagram([\"ExportDiagram\"])]       |
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

4.  [Include the following JavaScript files in the **Site.Master** page]

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [    [\<%][\-- Download the below javascript files from this location: http://code.google.com/p/canvg/\--][%\>]]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [    [\<][script] [src][=\"][\<%][=]Url.Content(\"\~/Scripts/canvg.js\") [%\>][\"] [type][=\"text/javascript\"\>\</][script][\>]]    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [    [\<][script] [src][=\"][\<%][=]Url.Content(\"\~/Scripts/rgbcolor.js\") [%\>][\"] [type][=\"text/javascript\"\>\</][script][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **[\[Razor\]]**                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [    [@\*][Download the below javascript files from this location: http://code.google.com/p/canvg/][\*@]]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [    [\<][script] [src][=\"][@][Url.Content(][\"\~/Scripts/canvg.js\"][)\"] [type][=\"text/javascript\"\>\</][script][\>]]               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [    [\<][script] [src][=\"][@][Url.Content(][\"\~/Scripts/rgbcolor.js\"][)\"] [type][=\"text/javascript\"\>\</][script][\>]]            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

5.  [Call the **print()** method with the optional argument as width and height.]

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                                                                           |
|                                                                                                                                                                                    |
| [    \$([\"#btnPrint\"]).bind([\"click\"], [function] (evt) {] |
|                                                                                                                                                                                    |
| [        [var] diagram = \$find([\"PrintDiagram\"]);]                                 |
|                                                                                                                                                                                    |
| [        diagram.print();]                                                                                                        |
|                                                                                                                                                                                    |
| [    });]                                                                                                                         |
|                                                                                                                                                                                    |
| []                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

6.  [Build and run the application.]

{border="0"}

Figure 136: Diagram with Print Dialog

[]{#related-topics}

