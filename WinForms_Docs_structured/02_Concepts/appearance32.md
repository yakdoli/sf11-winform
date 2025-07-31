---
title: appearance32.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\appearance32.md
created_at: 2025-07-03
---






#### Appearance {#appearance style="tab-stops: 0pt"}

 

The **tree-view** control supports eighteen predefined skins to enhance its look and feel.

**[]** 

**[Properties]**

 

+-------------+----------------------------------------------+------------------+--------------------------------+-------------+
| Name        | Description                                  | Type of property | Values it accepts              | Dependency  |
+=============+==============================================+==================+================================+=============+
| Skin        | Defines one of the fourteen built-in themes. | enum             | TreeViewSkin.Office2007Blue,   | NA          |
|             |                                              |                  |                                |             |
|             |                                              |                  | TreeViewSkin.Office2007Silver, |             |
|             |                                              |                  |                                |             |
|             |                                              |                  | TreeViewSkin.Office2007Black,  |             |
|             |                                              |                  |                                |             |
|             |                                              |                  | TreeViewSkin.Vista,            |             |
|             |                                              |                  |                                |             |
|             |                                              |                  | TreeViewSkin.Almond,           |             |
|             |                                              |                  |                                |             |
|             |                                              |                  | TreeViewSkin.Blueberry,        |             |
|             |                                              |                  |                                |             |
|             |                                              |                  | TreeViewSkin.Blend,            |             |
|             |                                              |                  |                                |             |
|             |                                              |                  | TreeViewSkin.Olive,            |             |
|             |                                              |                  |                                |             |
|             |                                              |                  | TreeViewSkin.Turquoise,        |             |
|             |                                              |                  |                                |             |
|             |                                              |                  | TreeViewSkin.Monochrome,       |             |
|             |                                              |                  |                                |             |
|             |                                              |                  | TreeViewSkin.Sandune,          |             |
|             |                                              |                  |                                |             |
|             |                                              |                  | TreeViewSkin.VS2010,           |             |
|             |                                              |                  |                                |             |
|             |                                              |                  | TreeViewSkin.Marble,           |             |
|             |                                              |                  |                                |             |
|             |                                              |                  | TreeViewSkin.Midnight,         |             |
|             |                                              |                  |                                |             |
|             |                                              |                  | TreeViewSkin.Default,          |             |
|             |                                              |                  |                                |             |
|             |                                              |                  | TreeViewSkin.MSDN,             |             |
|             |                                              |                  |                                |             |
|             |                                              |                  | TreeViewSkin.WindowsLive,      |             |
|             |                                              |                  |                                |             |
|             |                                              |                  | TreeViewSkin.WindowsXP         |             |
|             |                                              |                  |                                |             |
|             |                                              |                  |                                |             |
+-------------+----------------------------------------------+------------------+--------------------------------+-------------+

*[[]]{.underline}* 

Using Builder

The following steps explain how to define themes for a tree view through the builder.

1.   In **View**, create a *ul-li* hierarchy of tree-view nodes and invoke the tree-view helper with the control ID as first argument and the tree-view content ID as the second argument, followed by the **Skin** method with the desired theme as an option.

**[]** 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                  |
| [\<][ul][ [id][=\"treeViewContents\"] [style][=\"][visibility][: hidden\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                  |
| [    [\<][li] [id][=\"ASP.NET\"\>]]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                  |
| [        [\<][img] [src][=\'][\<%][=] Url.Content(\"\~/Images/asp.png\")[%\>][\'] [/\>]]         |
|                                                                                                                                                                                                                                                                                                                                                  |
| [  ][ASP.NET]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                  |
| [         [\<][ul][\>]]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                  |
| [            [\<][li] [id][=\"aspGrid\"\>]Essential Grid[\</][li][\>]]                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                  |
| [            [\<][li] [id][=\"aspSchedule\"\>]Essential Schedule[\</][li][\>]]                                                                         |
|                                                                                                                                                                                                                                                                                                                                                  |
| [            [\<][li] [id][=\"aspTools\"\>]Essential Tools[\</][li][\>]]                                                                               |
|                                                                                                                                                                                                                                                                                                                                                  |
| [         [\</][ul][\>]]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                  |
| [    [\</][li][\>]        ]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                  |
| [    [\<][li] [id][=\"Silverlight\"\>]]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                  |
| [        [\<][img] [src][=\'][\<%][=] Url.Content(\"\~/Images/silverlight.png\")[%\>][\'] [/\>\                                                           |
| ]        Silverlight]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                  |
| [        [\<][ul][\>]]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                  |
| [           [\<][li] [id][=\"silverGrid\"\>]Essential Tools [\</][li][\>]]                                                                             |
|                                                                                                                                                                                                                                                                                                                                                  |
| [           [\<][li] [id][=\"silverGauge\"\>]Essential Gauge [\</][li][\>]]                                                                            |
|                                                                                                                                                                                                                                                                                                                                                  |
| [           [\<][li] [id][=\"silverChart\"\>]Essential Chart [\</][li][\>]]                                                                            |
|                                                                                                                                                                                                                                                                                                                                                  |
| [        [\</][ul][\>]]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                  |
| [    [\</][li][\>]]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                  |
| [    [\<][li] [id][=\"WPF\"\>]]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                  |
| [        [\<][img] [src][=\'][\<%][=] Url.Content(\"\~/Images/wpf.png\")[%\>][\'] [/\>]WPF]      |
|                                                                                                                                                                                                                                                                                                                                                  |
| [        [\<][ul][\>]]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                  |
| [           [\<][li] [id][=\"wpfGrid\"\>]Essential Grid[\</][li][\>]]                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                  |
| [           [\<][li] [id][=\"wpfSchedule\"\>]Essential Schedule[\</][li][\>]]                                                                          |
|                                                                                                                                                                                                                                                                                                                                                  |
| [            [\<][li] [id][=\"wpfTools\"\>]Essential Tools[\</][li][\>]]                                                                               |
|                                                                                                                                                                                                                                                                                                                                                  |
| [        [\</][ul][\>]]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                  |
| [     [\</][li][\>]]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                  |
| [\</][ul][\>][]                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                  |
| [\<%][=][Html.Syncfusion().TreeView([\"myTreeView\"], [\"treeViewContents\"])]                                                                      |
|                                                                                                                                                                                                                                                                                                                                                  |
| [    **.Skin([TreeViewSkin].WindowsXP)**[%\>]]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**[]** 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                  |
| [\<][ul][ [id][=\"treeViewContents\"] [style][=\"][visibility][: hidden\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                  |
| [    [\<][li] [id][=\"ASP.NET\"\>]]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                  |
| [        [\<][img] [src][=\'][@]Url.Content(\"\~/Images/asp.png\")[\'] [/\>]]                                                                     |
|                                                                                                                                                                                                                                                                                                                                                  |
| [  ][ASP.NET]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                  |
| [         [\<][ul][\>]]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                  |
| [            [\<][li] [id][=\"aspGrid\"\>]Essential Grid[\</][li][\>]]                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                  |
| [            [\<][li] [id][=\"aspSchedule\"\>]Essential Schedule[\</][li][\>]]                                                                         |
|                                                                                                                                                                                                                                                                                                                                                  |
| [            [\<][li] [id][=\"aspTools\"\>]Essential Tools[\</][li][\>]]                                                                               |
|                                                                                                                                                                                                                                                                                                                                                  |
| [         [\</][ul][\>]]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                  |
| [    [\</][li][\>]        ]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                  |
| [    [\<][li] [id][=\"Silverlight\"\>]]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                  |
| [        [\<][img] [src][=\'][@]Url.Content(\"\~/Images/silverlight.png\")[\'] [/\>\                                                                                                                       |
| ]        Silverlight]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                  |
| [        [\<][ul][\>]]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                  |
| [           [\<][li] [id][=\"silverGrid\"\>]Essential Tools [\</][li][\>]]                                                                             |
|                                                                                                                                                                                                                                                                                                                                                  |
| [           [\<][li] [id][=\"silverGauge\"\>]Essential Gauge [\</][li][\>]]                                                                            |
|                                                                                                                                                                                                                                                                                                                                                  |
| [           [\<][li] [id][=\"silverChart\"\>]Essential Chart [\</][li][\>]]                                                                            |
|                                                                                                                                                                                                                                                                                                                                                  |
| [        [\</][ul][\>]]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                  |
| [    [\</][li][\>]]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                  |
| [    [\<][li] [id][=\"WPF\"\>]]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                  |
| [        [\<][img] [src][=\'][@]Url.Content(\"\~/Images/wpf.png\")[\'] [/\>]WPF]                                                                  |
|                                                                                                                                                                                                                                                                                                                                                  |
| [        [\<][ul][\>]]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                  |
| [           [\<][li] [id][=\"wpfGrid\"\>]Essential Grid[\</][li][\>]]                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                  |
| [           [\<][li] [id][=\"wpfSchedule\"\>]Essential Schedule[\</][li][\>]]                                                                          |
|                                                                                                                                                                                                                                                                                                                                                  |
| [            [\<][li] [id][=\"wpfTools\"\>]Essential Tools[\</][li][\>]]                                                                               |
|                                                                                                                                                                                                                                                                                                                                                  |
| [        [\</][ul][\>]]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                  |
| [     [\</][li][\>]]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                  |
| [\</][ul][\>][]                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                  |
| [\@{][ Html.Syncfusion().TreeView([\"myTreeView\"], [\"treeViewContents\"])]                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                  |
| [    **.Skin([TreeViewSkin].WindowsXP)**.Render();[}]]                                                                                                                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   Build and run the application

 

Using Properties Model

[] 

The following steps explain how to define themes for a tree view through the properties model.

1.   In the controller, create an instance of **TreeViewModel**.

2.   Define the **Skin** property and pass the instance through **view-specific data** to the **View**.

**[]** 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                  |
|                                                                                                                                                                           |
| [public][ [ActionResult] Index()]                            |
|                                                                                                                                                                           |
| [        {]                                                                                                                           |
|                                                                                                                                                                           |
| [            [TreeViewModel] myModel = [new] [TreeViewModel]();] |
|                                                                                                                                                                           |
| [            myModel.Skin = [TreeViewSkin].WindowsXP;]                                                        |
|                                                                                                                                                                           |
| []                                                                                                                                    |
|                                                                                                                                                                           |
| [            [//pass the model through view data to the view]]                                                  |
|                                                                                                                                                                           |
| [            ViewData\[[\"myTreeView\"]\] = myModel;]                                                         |
|                                                                                                                                                                           |
| [            [return] View();]                                                                                   |
|                                                                                                                                                                           |
| [        }]                                                                                                                           |
|                                                                                                                                                                           |
| []                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

**[]** 

3.   In **View**, create a *ul-li* hierarchy of tree-view nodes and invoke the tree-view helper by passing the view data key as the first argument and the tree-view content ID as the second argument.

**[]** 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                  |
| [\<][ul][ [id][=\"treeViewContents\"] [style][=\"][visibility][: hidden\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                  |
| [    [\<][li] [id][=\"ASP.NET\"\>]]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                  |
| [        [\<][img] [src][=\'][\<%][=] Url.Content(\"\~/Images/asp.png\")[%\>][\'] [/\>]]         |
|                                                                                                                                                                                                                                                                                                                                                  |
| [  ][ASP.NET]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                  |
| [         [\<][ul][\>]]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                  |
| [            [\<][li] [id][=\"aspGrid\"\>]Essential Grid[\</][li][\>]]                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                  |
| [            [\<][li] [id][=\"aspSchedule\"\>]Essential Schedule[\</][li][\>]]                                                                         |
|                                                                                                                                                                                                                                                                                                                                                  |
| [            [\<][li] [id][=\"aspTools\"\>]Essential Tools[\</][li][\>]]                                                                               |
|                                                                                                                                                                                                                                                                                                                                                  |
| [         [\</][ul][\>]]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                  |
| [    [\</][li][\>]        ]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                  |
| [    [\<][li] [id][=\"Silverlight\"\>]]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                  |
| [        [\<][img] [src][=\'][\<%][=] Url.Content(\"\~/Images/silverlight.png\")[%\>][\'] [/\>\                                                           |
| ]        Silverlight]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                  |
| [        [\<][ul][\>]]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                  |
| [           [\<][li] [id][=\"silverGrid\"\>]Essential Tools [\</][li][\>]]                                                                             |
|                                                                                                                                                                                                                                                                                                                                                  |
| [           [\<][li] [id][=\"silverGauge\"\>]Essential Gauge [\</][li][\>]]                                                                            |
|                                                                                                                                                                                                                                                                                                                                                  |
| [           [\<][li] [id][=\"silverChart\"\>]Essential Chart [\</][li][\>]]                                                                            |
|                                                                                                                                                                                                                                                                                                                                                  |
| [        [\</][ul][\>]]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                  |
| [    [\</][li][\>]]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                  |
| [    [\<][li] [id][=\"WPF\"\>]]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                  |
| [        [\<][img] [src][=\'][\<%][=] Url.Content(\"\~/Images/wpf.png\")[%\>][\'] [/\>]WPF]      |
|                                                                                                                                                                                                                                                                                                                                                  |
| [        [\<][ul][\>]]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                  |
| [           [\<][li] [id][=\"wpfGrid\"\>]Essential Grid[\</][li][\>]]                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                  |
| [           [\<][li] [id][=\"wpfSchedule\"\>]Essential Schedule[\</][li][\>]]                                                                          |
|                                                                                                                                                                                                                                                                                                                                                  |
| [            [\<][li] [id][=\"wpfTools\"\>]Essential Tools[\</][li][\>]]                                                                               |
|                                                                                                                                                                                                                                                                                                                                                  |
| [        [\</][ul][\>]]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                  |
| [     [\</][li][\>]]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                  |
| [\</][ul][\>][]                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                  |
| [\<%][=][Html.Syncfusion().TreeView([\"myTreeView\"], [\"treeViewContents\"])[%\>]]                                     |
|                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                  |
| [\<][ul][ [id][=\"treeViewContents\"] [style][=\"][visibility][: hidden\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                  |
| [    [\<][li] [id][=\"ASP.NET\"\>]]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                  |
| [        [\<][img] [src][=\'][@]Url.Content(\"\~/Images/asp.png\")[\'] [/\>]]                                                                     |
|                                                                                                                                                                                                                                                                                                                                                  |
| [  ][ASP.NET]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                  |
| [         [\<][ul][\>]]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                  |
| [            [\<][li] [id][=\"aspGrid\"\>]Essential Grid[\</][li][\>]]                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                  |
| [            [\<][li] [id][=\"aspSchedule\"\>]Essential Schedule[\</][li][\>]]                                                                         |
|                                                                                                                                                                                                                                                                                                                                                  |
| [            [\<][li] [id][=\"aspTools\"\>]Essential Tools[\</][li][\>]]                                                                               |
|                                                                                                                                                                                                                                                                                                                                                  |
| [         [\</][ul][\>]]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                  |
| [    [\</][li][\>]        ]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                  |
| [    [\<][li] [id][=\"Silverlight\"\>]]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                  |
| [        [\<][img] [src][=\'][@]Url.Content(\"\~/Images/silverlight.png\")[\'] [/\>\                                                                                                                       |
| ]        Silverlight]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                  |
| [        [\<][ul][\>]]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                  |
| [           [\<][li] [id][=\"silverGrid\"\>]Essential Tools [\</][li][\>]]                                                                             |
|                                                                                                                                                                                                                                                                                                                                                  |
| [           [\<][li] [id][=\"silverGauge\"\>]Essential Gauge [\</][li][\>]]                                                                            |
|                                                                                                                                                                                                                                                                                                                                                  |
| [           [\<][li] [id][=\"silverChart\"\>]Essential Chart [\</][li][\>]]                                                                            |
|                                                                                                                                                                                                                                                                                                                                                  |
| [        [\</][ul][\>]]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                  |
| [    [\</][li][\>]]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                  |
| [    [\<][li] [id][=\"WPF\"\>]]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                  |
| [        [\<][img] [src][=\'][@]Url.Content(\"\~/Images/wpf.png\")[\'] [/\>]WPF]                                                                  |
|                                                                                                                                                                                                                                                                                                                                                  |
| [        [\<][ul][\>]]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                  |
| [           [\<][li] [id][=\"wpfGrid\"\>]Essential Grid[\</][li][\>]]                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                  |
| [           [\<][li] [id][=\"wpfSchedule\"\>]Essential Schedule[\</][li][\>]]                                                                          |
|                                                                                                                                                                                                                                                                                                                                                  |
| [            [\<][li] [id][=\"wpfTools\"\>]Essential Tools[\</][li][\>]]                                                                               |
|                                                                                                                                                                                                                                                                                                                                                  |
| [        [\</][ul][\>]]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                  |
| [     [\</][li][\>]]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                  |
| [\</][ul][\>][]                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                  |
| [\@{][ Html.Syncfusion().TreeView([\"myTreeView\"], [\"treeViewContents\"]).Render();[}]]                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.   Build and run the application.

The following figure shows the tree-view control with a defined theme.

{border="0"}

Figure 325: Tree View with a Set Theme

[]{#related-topics}

