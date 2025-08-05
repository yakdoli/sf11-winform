---
title: exportdiagraminimageformat1.md
original_path: WinForms_Docs/04_Controls/Diagram/exportdiagraminimageformat1.md
created_at: 2025-08-05
---








  









### Export Diagram in Image Format {#export-diagram-in-image-format style="tab-stops: 0pt"}

The following code snippet illustrates how to export the diagram page as an image file.

6.  [In the **controller**, pass the data to the **View** page.]


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


 

7.  [In the **controller**, define the post action to export image.]


+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller][]**                                                            |
|                                                                                                                                                       |
| []                                                                                                   |
|                                                                                                                                                       |
| [\[[HttpPost]\]]                                                             |
|                                                                                                                                                       |
| [        [public] [ActionResult] ExportToImage()]       |
|                                                                                                                                                       |
| [        {]                                                                                          |
|                                                                                                                                                       |
| [            [string] FileName = [\"ExportFileName\"];] |
|                                                                                                                                                       |
| [            [return] FileName.DiagramExportActions();]                         |
|                                                                                                                                                       |
| [        }]                                                                                          |
|                                                                                                                                                       |
| []                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

[8.   Create a ][[Strongly Typed View]{.UGHyperlink}](http://help.syncfusion.com/ug_94/User%20Interface/ASP.NET%20MVC/Diagram/default.htm?turl=Documents%2Fcreateastronglytypedview.htm)[. ]

9.  [In the **view**, invoke the **Diagram** helper with the control ID, and set the **DataDource** and **BindTo** methods.]

 

+----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                 |
|                                                                                                                                                    |
| [\<%][{]                     |
|                                                                                                                                                    |
| [      Html.Syncfusion().Diagram([\"ExportDiagram\"])]                    |
|                                                                                                                                                    |
| [        .DataSource(Model)]                                                                      |
|                                                                                                                                                    |
| [        .BindTo(bind =\>]                                                                        |
|                                                                                                                                                    |
| [            bind.NodeId([\"NodeId\"])]                                   |
|                                                                                                                                                    |
| [            .ParentNodeId([\"ParentNodeId\"])]                           |
|                                                                                                                                                    |
| [            .NodeText([\"NodeText\"])]                                   |
|                                                                                                                                                    |
| [            .NodeShape([\"Shape\"]))]                                    |
|                                                                                                                                                    |
| [        .DiagramMode([DiagramMode].SVG)]                                 |
|                                                                                                                                                    |
| [        .LayoutType([LayoutType].HierarchicalTreeLayout)]                |
|                                                                                                                                                    |
| [        .Orientation([TreeOrientation].TopBottom)]                       |
|                                                                                                                                                    |
| [        .Mappers(mappers =\> mappers.ExportAction([\"ExportToImage\"]))] |
|                                                                                                                                                    |
| [        .Width(750)]                                                                             |
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
| [    Html.Syncfusion().Diagram([\"ExportDiagram\"])]                      |
|                                                                                                                                                    |
| [      .DataSource(Model)]                                                                        |
|                                                                                                                                                    |
| [      .BindTo(bind =\>]                                                                          |
|                                                                                                                                                    |
| [          bind.NodeId([\"NodeId\"])]                                     |
|                                                                                                                                                    |
| [          .ParentNodeId([\"ParentNodeId\"])]                             |
|                                                                                                                                                    |
| [          .NodeText([\"NodeText\"])]                                     |
|                                                                                                                                                    |
| [          .NodeShape([\"Shape\"]))]                                      |
|                                                                                                                                                    |
| [      .DiagramMode([DiagramMode].SVG)]                                   |
|                                                                                                                                                    |
| [      .LayoutType([LayoutType].HierarchicalTreeLayout)]                  |
|                                                                                                                                                    |
| [      .Orientation([TreeOrientation].TopBottom)]                         |
|                                                                                                                                                    |
| [      .Mappers(mappers =\> mappers.ExportAction([\"ExportToImage\"]))]   |
|                                                                                                                                                    |
| [      .Width(750)]                                                                               |
|                                                                                                                                                    |
| [      .Height(450)]                                                                              |
|                                                                                                                                                    |
| [      .Render();]                                                                                |
|                                                                                                                                                    |
| [}][]                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------+

 

10\. [Include the following JavaScript files in the **Site.Master** page.]

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [    [\<%][\-- Download the below javascript files from this location: http://code.google.com/p/canvg/\--][%\>]]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [    [\<][script] [src][=\"][\<%][=]Url.Content(\"\~/Scripts/canvg.js\") [%\>][\"] [type][=\"text/javascript\"\>\</][script][\>]]    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [    [\<][script] [src][=\"][\<%][=]Url.Content(\"\~/Scripts/rgbcolor.js\") [%\>][\"] [type][=\"text/javascript\"\>\</][script][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [    [\<%][\-- Download the below javascript file from this location: http://code.google.com/p/stringencoders/source/browse/trunk/javascript/base64.js\--][%\>]]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [    [\<][script] [src][=\"][\<%][=]Url.Content(\"\~/Scripts/base64.js\") [%\>][\"] [type][=\"text/javascript\"\>\</][script][\>]]   |
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
| [    [@\*][Download the below javascript file from this location: http://code.google.com/p/stringencoders/source/browse/trunk/javascript/base64.js][\*@]]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [    [\<][script] [src][=\"][@][Url.Content(][\"\~/Scripts/base64.js\"][)\>\"] [type][=\"text/javascript\"\>\</][script][\>]]            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

11\. [Call the **exportTo()** method with the image type as an argument.]

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                                                                            |
|                                                                                                                                                                                     |
| [    \$([\"#btnExport\"]).bind([\"click\"], [function] (evt) {] |
|                                                                                                                                                                                     |
| [        [var] diagram = \$find([\"ExportDiagram\"]);]                                 |
|                                                                                                                                                                                     |
| [        diagram.exportTo([\"png\"]);]                                                                      |
|                                                                                                                                                                                     |
| [    });]                                                                                                                          |
|                                                                                                                                                                                     |
| []                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

12\. [Build and run the application.]

 

{border="0"}

Figure 135: Export Diagram to Image with PNG Format

[]{#related-topics}

