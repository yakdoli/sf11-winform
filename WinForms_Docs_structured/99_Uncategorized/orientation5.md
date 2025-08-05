---
title: orientation5.md
original_path: WinForms_Docs/99_Uncategorized/orientation5.md
created_at: 2025-08-05
---






#### Orientation {#orientation style="tab-stops: 0pt"}

 

The toolbar control supports both vertical and horizontal orientations, allowing it to fit into any scenario.

**[]** 

Properties

 

+-------------+----------------------------------------------------------------+------------------+--------------------------------+-------------+
| Name        | Description                                                    | Type of property | Value it accepts               | Dependency  |
+-------------+----------------------------------------------------------------+------------------+--------------------------------+-------------+
| Orientation | Defines the orientation by which the control will be rendered. | enum             | ToolbarOrientation.Horizontal, | NA          |
|             |                                                                |                  |                                |             |
|             |                                                                |                  | ToolbarOrientation.Vertical    |             |
+-------------+----------------------------------------------------------------+------------------+--------------------------------+-------------+

*[[]]{.underline}* 

Using Builder

The following steps explain how to set orientation for the toolbar using Builder.

1.   In **View**, create a *ul-li* list of toolbar items and invoke the toolbar helper.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][div][ [id][=\"toolbarItems\"] [style][=\"][visibility][:hidden\"\>]]                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [     [\<][ul][\>]]                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [         [\<][li] [id][=\"New\"] [title][=\"New \[Ctrl + N\]\"\>]]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [             [\<][img] [src][=\'][\<%][=] Url.Content(\"\~/Content/new.gif\")[%\>][\'] [/\>\</][li][\>]          ]          |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [          [\<][li] [id][=\"Open\"] [title][=\"Open file\]\"\>]]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [               [\<][img] [src][=\'][\<%][=] Url.Content(\"\~/Content/openremote.gif\")[%\>][\'] [/\>\</][li][\>]          ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [          [\<][li] [id][=\"Save\"] [title][=\"Save \[Ctrl + S\]\"\>]]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [               [\<][img] [src][=\'][\<%][=] Url.Content(\"\~/Content/savelocal.gif\")[%\>][\'] [/\>\</][li][\>]]            |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [      \</][ul][\>][       ]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [       [\<][ul][\>]]                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [          [\<][li] [id][=\"Bold\"] [tilte][=\"Bold \[Ctrl + B\]\"\>]]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [              [\<][img] [src][=\'][\<%][=] Url.Content(\"\~/Content/bold.gif\")[%\>][\'] [/\>\</][li][\>          ]]        |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [          [\<][li] [id][=\"Italic\"] [tilte][=\"Bold \[Ctrl + I\]\"\>]]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [              [\<][img] [src][=\'][\<%][=] Url.Content(\"\~/Content/italic.gif\")[%\>][\'] [/\>\</][li][\>          ]]      |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [          [\<][li] [id][=\"Underline\"] [tilte][=\"Bold \[Ctrl + U\]\"\>]]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [              [\<][img] [src][=\'][\<%][=] Url.Content(\"\~/Content/underline.gif\")[%\>][\'] [/\>\</][li][\>]]             |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [       [\</][ul][\>]]                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [   [\</][div][\>]]                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [    [\<%][=]Html.Syncfusion().Toolbar([\"myToolbar\"])]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [       .TargetId([\"toolbarItems\"])]                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **[.Orientation([ToolbarOrientation].Vertical)]**[%\>]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                         |
| [\<][div][ [id][=\"toolbarItems\"] [style][=\"][visibility][:hidden\"\>]]            |
|                                                                                                                                                                                                                                                                                                                                                         |
| [     [\<][ul][\>]]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                         |
| [         [\<][li] [id][=\"New\"] [title][=\"New \[Ctrl + N\]\"\>]]                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                         |
| [             [\<][img] [src][=\'][@]Url.Content(\"\~/Content/new.gif\")[\'] [/\>\</][li][\>]          ]     |
|                                                                                                                                                                                                                                                                                                                                                         |
| [          [\<][li] [id][=\"Open\"] [title][=\"Open file\]\"\>]]                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                         |
| [        [\<][img] [src][=\'][@]Url.Content(\"\~/Content/openremote.gif\")[\'] [/\>\</][li][\>]          ]   |
|                                                                                                                                                                                                                                                                                                                                                         |
| [        [\<][li] [id][=\"Save\"] [title][=\"Save \[Ctrl + S\]\"\>]]                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                         |
| [       [\<][img] [src][=\'][@]Url.Content(\"\~/Content/savelocal.gif\")[\'] [/\>\</][li][\>]]               |
|                                                                                                                                                                                                                                                                                                                                                         |
| [      \</][ul][\>][ [\<][ul][\>]]                                                            |
|                                                                                                                                                                                                                                                                                                                                                         |
| [          [\<][li] [id][=\"Bold\"] [tilte][=\"Bold \[Ctrl + B\]\"\>]]                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                         |
| [              [\<][img] [src][=\'][@]Url.Content(\"\~/Content/bold.gif\")[\'] [/\>\</][li][\>          ]]   |
|                                                                                                                                                                                                                                                                                                                                                         |
| [          [\<][li] [id][=\"Italic\"] [tilte][=\"Bold \[Ctrl + I\]\"\>]]                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                         |
| [              [\<][img] [src][=\'][@]Url.Content(\"\~/Content/italic.gif\")[\'] [/\>\</][li][\>          ]] |
|                                                                                                                                                                                                                                                                                                                                                         |
| [          [\<][li] [id][=\"Underline\"] [tilte][=\"Bold \[Ctrl + U\]\"\>]]                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                         |
| [              [\<][img] [src][=\'][@]Url.Content(\"\~/Content/underline.gif\")[\'] [/\>\</][li][\>]]        |
|                                                                                                                                                                                                                                                                                                                                                         |
| [       [\</][ul][\>] [\</][div][\>]]                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                         |
| [    [\@{] Html.Syncfusion().Toolbar([\"myToolbar\"])]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                         |
| [       .TargetId([\"toolbarItems\"])]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                         |
| **[.Orientation([ToolbarOrientation].Vertical)]**[.Render();][}]**[]**                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

2.   Build and run the application.**

*[[]]{.underline}* 

Using Properties Model

The following steps explain how to set orientation using the Builder.

1.   In the controller, create an instance of **ToolbarModel**.

2.   Define the **Orientation** property and pass the instance through the view-specific data to the view.[]

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                |
|                                                                                                                                                                         |
| [public][ [ActionResult] Index()]                          |
|                                                                                                                                                                         |
| [        {]                                                                                                                         |
|                                                                                                                                                                         |
| [            [ToolbarModel] myModel = [new] [ToolbarModel]();] |
|                                                                                                                                                                         |
| [            myModel.TargetId = [\"toolbarItems\"];]                                                        |
|                                                                                                                                                                         |
| [            **myModel.Orientation = [ToolbarOrientation].Vertical;**]                                      |
|                                                                                                                                                                         |
| []                                                                                                                                  |
|                                                                                                                                                                         |
| [            [//pass the instance through View Data]]                                                         |
|                                                                                                                                                                         |
| [            ViewData\[[\"myToolbar\"]\] = myModel;]                                                        |
|                                                                                                                                                                         |
| [            [return] View();]                                                                                 |
|                                                                                                                                                                         |
| [        }]                                                                                                                         |
|                                                                                                                                                                         |
| []                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   In **View**, create a *ul-li* list of of toolbar items and invoke the toolbar helper.

**[]** 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][div][ [id][=\"toolbarItems\"] [style][=\"][visibility][:hidden\"\>]]                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [     [\<][ul][\>]]                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [         [\<][li] [id][=\"New\"] [title][=\"New \[Ctrl + N\]\"\>]]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [             [\<][img] [src][=\'][\<%][=] Url.Content(\"\~/Content/new.gif\")[%\>][\'] [/\>\</][li][\>]          ]          |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [          [\<][li] [id][=\"Open\"] [title][=\"Open file\]\"\>]]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [               [\<][img] [src][=\'][\<%][=] Url.Content(\"\~/Content/openremote.gif\")[%\>][\'] [/\>\</][li][\>]          ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [          [\<][li] [id][=\"Save\"] [title][=\"Save \[Ctrl + S\]\"\>]]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [               [\<][img] [src][=\'][\<%][=] Url.Content(\"\~/Content/savelocal.gif\")[%\>][\'] [/\>\</][li][\>]]            |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [      \</][ul][\>][       ]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [       [\<][ul][\>]]                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [          [\<][li] [id][=\"Bold\"] [tilte][=\"Bold \[Ctrl + B\]\"\>]]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [              [\<][img] [src][=\'][\<%][=] Url.Content(\"\~/Content/bold.gif\")[%\>][\'] [/\>\</][li][\>          ]]        |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [          [\<][li] [id][=\"Italic\"] [tilte][=\"Bold \[Ctrl + I\]\"\>]]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [              [\<][img] [src][=\'][\<%][=] Url.Content(\"\~/Content/italic.gif\")[%\>][\'] [/\>\</][li][\>          ]]      |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [          [\<][li] [id][=\"Underline\"] [tilte][=\"Bold \[Ctrl + U\]\"\>]]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [              [\<][img] [src][=\'][\<%][=] Url.Content(\"\~/Content/underline.gif\")[%\>][\'] [/\>\</][li][\>]]             |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [       [\</][ul][\>]]                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [   [\</][div][\>]]                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [    [\<%][=]Html.Syncfusion().Toolbar([\"myToolbar\"])[%\>]]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                         |
| [\<][div][ [id][=\"toolbarItems\"] [style][=\"][visibility][:hidden\"\>]]            |
|                                                                                                                                                                                                                                                                                                                                                         |
| [     [\<][ul][\>]]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                         |
| [         [\<][li] [id][=\"New\"] [title][=\"New \[Ctrl + N\]\"\>]]                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                         |
| [             [\<][img] [src][=\'][@]Url.Content(\"\~/Content/new.gif\")[\'] [/\>\</][li][\>]          ]     |
|                                                                                                                                                                                                                                                                                                                                                         |
| [          [\<][li] [id][=\"Open\"] [title][=\"Open file\]\"\>]]                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                         |
| [        [\<][img] [src][=\'][@]Url.Content(\"\~/Content/openremote.gif\")[\'] [/\>\</][li][\>]          ]   |
|                                                                                                                                                                                                                                                                                                                                                         |
| [        [\<][li] [id][=\"Save\"] [title][=\"Save \[Ctrl + S\]\"\>]]                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                         |
| [       [\<][img] [src][=\'][@]Url.Content(\"\~/Content/savelocal.gif\")[\'] [/\>\</][li][\>]]               |
|                                                                                                                                                                                                                                                                                                                                                         |
| [      \</][ul][\>][ [\<][ul][\>]]                                                            |
|                                                                                                                                                                                                                                                                                                                                                         |
| [          [\<][li] [id][=\"Bold\"] [tilte][=\"Bold \[Ctrl + B\]\"\>]]                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                         |
| [              [\<][img] [src][=\'][@]Url.Content(\"\~/Content/bold.gif\")[\'] [/\>\</][li][\>          ]]   |
|                                                                                                                                                                                                                                                                                                                                                         |
| [          [\<][li] [id][=\"Italic\"] [tilte][=\"Bold \[Ctrl + I\]\"\>]]                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                         |
| [              [\<][img] [src][=\'][@]Url.Content(\"\~/Content/italic.gif\")[\'] [/\>\</][li][\>          ]] |
|                                                                                                                                                                                                                                                                                                                                                         |
| [          [\<][li] [id][=\"Underline\"] [tilte][=\"Bold \[Ctrl + U\]\"\>]]                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                         |
| [              [\<][img] [src][=\'][@]Url.Content(\"\~/Content/underline.gif\")[\'] [/\>\</][li][\>]]        |
|                                                                                                                                                                                                                                                                                                                                                         |
| [       [\</][ul][\>] [\</][div][\>]]                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                         |
| [    [\@{] Html.Syncfusion().Toolbar([\"myToolbar\"]).Render();[}]]**[]**                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Build and run the application.

The following screenshot shows the toolbar output with a vertical orientation.

 

{border="0"}

Figure 306: Toolbar with Vertical Orientation

 

[]{#related-topics}

