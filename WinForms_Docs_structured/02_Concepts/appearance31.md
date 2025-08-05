---
title: appearance31.md
original_path: WinForms_Docs/02_Concepts/appearance31.md
created_at: 2025-08-05
---






#### Appearance {#appearance style="tab-stops: 0pt"}

 

The toolbar control supports fourteen built-in skins and varied background layouts to enhance its look and feel.

**[]** 

Properties

 

+-------------+---------------------------------------------+----------------------------------+--------------------------------------------------------------------+-------------+
| Name        | Description                                 | Type of property                 | Value it accepts                                                   | Dependency  |
+=============+=============================================+==================================+====================================================================+=============+
| Skin        | Defines one of the fourteen in-built themes | [enum] | [·      ]ToolBarSkin.Office2007Blue   | NA          |
|             |                                             |                                  |                                                                    |             |
|             |                                             |                                  | [·      ]ToolBarSkin.Office2007Silver |             |
|             |                                             |                                  |                                                                    |             |
|             |                                             |                                  | [·      ]ToolBarSkin.Office2007Black  |             |
|             |                                             |                                  |                                                                    |             |
|             |                                             |                                  | [·      ]ToolBarSkin.Vista            |             |
|             |                                             |                                  |                                                                    |             |
|             |                                             |                                  | [·      ]ToolBarSkin.Almond           |             |
|             |                                             |                                  |                                                                    |             |
|             |                                             |                                  | [·      ]ToolBarSkin.Blueberry        |             |
|             |                                             |                                  |                                                                    |             |
|             |                                             |                                  | [·      ]ToolBarSkin.Blend            |             |
|             |                                             |                                  |                                                                    |             |
|             |                                             |                                  | [·      ]ToolBarSkin.Olive            |             |
|             |                                             |                                  |                                                                    |             |
|             |                                             |                                  | [·      ]ToolBarSkin.Turquoise        |             |
|             |                                             |                                  |                                                                    |             |
|             |                                             |                                  | [·      ]ToolBarSkin.Monochrome       |             |
|             |                                             |                                  |                                                                    |             |
|             |                                             |                                  | [·      ]ToolBarSkin.Sandune          |             |
|             |                                             |                                  |                                                                    |             |
|             |                                             |                                  | [·      ]ToolBarSkin.VS2010           |             |
|             |                                             |                                  |                                                                    |             |
|             |                                             |                                  | [·      ]ToolBarSkin.Marble           |             |
|             |                                             |                                  |                                                                    |             |
|             |                                             |                                  | [·      ]ToolBarSkin.Midnight         |             |
|             |                                             |                                  |                                                                    |             |
|             |                                             |                                  |                                                                    |             |
+-------------+---------------------------------------------+----------------------------------+--------------------------------------------------------------------+-------------+

*[[]]{.underline}* 

Using Builder

 

The following steps explain how to define a theme for the toolbar using Builder.

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
| **[.Skin([ToolBarSkin].Olive)]**[%\>]**[]**                                                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

 

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
| **[.Skin([ToolBarSkin].Olive)]**[.Render();][}]**[]**                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

2.   Build and run the application

 

Using Properties Model

 

The following steps explain how to define the theme for a toolbar using the Properties Model.

1.   In the controller, create an instance of **ToolbarModel**.

2.   Define the **Skin** property and pass the instance through the **view-specific data** to the **view**.[]

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
| [            **myModel.Skin = [ToolBarSkin].Olive;**]                                                       |
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

3.   In **View**, create a *ul-li* list of toolbar items and invoke the toolbar helper.

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
| [      [\<%][=]Html.Syncfusion().Toolbar([\"myToolbar\"])[%\>]]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                                                                                                                                                                                               |
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
| [    [\@{] Html.Syncfusion().Toolbar([\"myToolbar\"]).Render();[}]]**[]**                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Build and run the application

The following figure shows the output of the toolbar control with a set theme.

{border="0"}

Figure 307: Toolbar with Syncfusion Theme

[]{#related-topics}

