---
title: nodeediting.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\nodeediting.md
created_at: 2025-07-03
---






#### Node Editing {#node-editing style="tab-stops: 0pt"}

The tree-view control can permit the end-user to edit a node, or prevent him or her from editing. Double-clicking a node or selecting a node, and pressing the F2 key, will display an edit text box, allowing the node to be renamed.

[] 

{border="0"}

Figure 319: Tree View with Edit Text Box

 

3.   To save changes after making edits, press the ENTER key. Clicking anywhere outside the node will also save changes made to node text.

4.   To exit without saving any changes, press the ESC key.

 

Properties

 

 

  ----------- ---------------------------------------- ------------------ ------------------ -----------
  Name        Description                              Type of property   Value it accepts   Dependecy
  AllowEdit   Controls a nodes ability to be edited.   bool               True/False         NA
  ----------- ---------------------------------------- ------------------ ------------------ -----------

*[[]]{.underline}* 

**[]** 

Using Builder

The following steps explain how to restrict node editing through the builder.

1.   In **View**, create a *ul-li* hierarchy of tree-view nodes and invoke the tree-view helper with the control ID as the first argument and the tree-view content ID as the second argument followed by the **AllowEdit** method with False as an argument.

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
| []                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                  |
| [\<%][=][Html.Syncfusion().TreeView([\"myTreeView\"], [\"treeViewContents\"])]                                                                      |
|                                                                                                                                                                                                                                                                                                                                                  |
| **[.AllowEdit([false])]**[%\>]                                                                                                                                                                                                  |
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
| [\@{][ Html.Syncfusion().TreeView([\"myTreeView\"], [\"treeViewContents\"])]                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                  |
| **[.AllowEdit([false])]**[.Render();[}]]                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   Build and run the application.

**[]** 

Using Properties Model

The following steps explain how to restrict node editing through the properties model.

1.   In the controller, create an instance of **TreeViewModel**.

2.   Reset the **AllowEdit** property and pass the instance through the **view-specific data** to the **view**.

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
| [            myModel.AllowEdit = [false];]                                                                       |
|                                                                                                                                                                           |
| []                                                                                                                                    |
|                                                                                                                                                                           |
| [            [//Pass the model through the view data to the view.]]                                             |
|                                                                                                                                                                           |
| [            ViewData\[[\"myTreeView\"]\] = myModel;]                                                         |
|                                                                                                                                                                           |
| [            [return] View();]                                                                                   |
|                                                                                                                                                                           |
| [        }]                                                                                                                           |
|                                                                                                                                                                           |
| []                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   In **View**, create a *ul-li* hierarchy of tree-view nodes and invoke the tree-view helper by passing the view data key as the first argument and the tree-view content ID as the second argument.

**[]** 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                                                                                                                 |
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
| []                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                  |
| [\<%][=][Html.Syncfusion().TreeView([\"myTreeView\"], [\"treeViewContents\"])[%\>]]                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

**[]** 

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

[] 

 

4.   Build and run the application.

 

After performing the above steps, the end-user will not be able to edit the nodes of the tree view.  

 

[]{#related-topics}

