---
title: clientsideevents44.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clientsideevents44.md
created_at: 2025-07-03
---






#### Client-Side Events {#client-side-events style="tab-stops: 0pt"}

 

The toolbar control supports client-side event handling.

**[]** 

**[Events][]**

 

  **Name**                **Description**                                                         **Arguments**   **Reference Link**
  ----------------------- ----------------------------------------------------------------------- --------------- --------------------
  ClientSideOnLoded       This event is raised immediately when the toolbar is loaded.            inst            NA
  ClientSideOnClick       This event is raised when a toolbar item is clicked.                    inst,args       NA
  ClientSideOnMouseOver   This event is raised when the pointer moves over a toolbar item.        inst,args       NA
  ClientSideOnMouseOut    This event is raised when the pointer moves away from a toolbar item.   inst,args       NA

*[[]]{.underline}* 

**[]** 

Using Builder

The following steps explain how to handle client-side events raised by the toolbar.

1.   In **View**, create a *ul-li* list of toolbar items and invoke the toolbar helper.

 

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
| **[.ClientSideOnLoaded([\"OnLoaded\"])]**                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **[            .ClientSideClick([\"OnClick\"])]**                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **[            .ClientSideMouseOver([\"OnMouseOver\"])]**                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **[            .ClientSideMouseOut([\"OnMouseOut\"])]**[%\>]                                                                                                                                                                                                                                         |
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
| **[.ClientSideOnLoaded([\"OnLoaded\"])]**                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                         |
| **[            .ClientSideClick([\"OnClick\"])]**                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                         |
| **[            .ClientSideMouseOver([\"OnMouseOver\"])]**                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                         |
| **[      .ClientSideMouseOut([\"OnMouseOut\"])]**                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                         |
| **[      ]**[.Render();][}]**[]**                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Define the callback methods in the script to handle the specified events.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                                                                                                                       |
|                                                                                                                                                                                                                                |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [        [function] OnLoaded(inst) {]                                                                                                                                 |
|                                                                                                                                                                                                                                |
| [          [//inst - instance of a toolbar client-side object]]                                                                                                  |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [        [function] OnClick(inst, args) {]                                                                                                                            |
|                                                                                                                                                                                                                                |
| [          [//inst               - instance of a toolbar client-side object]]                                                                                    |
|                                                                                                                                                                                                                                |
| [          [//args:]]                                                                                                                                            |
|                                                                                                                                                                                                                                |
| [          [//   \_currentItem    - current toolbar item as a DOM element       ]]                                                                               |
|                                                                                                                                                                                                                                |
| [          [//   \_currentItemId  - ID of the current toolbar item]]                                                                                             |
|                                                                                                                                                                                                                                |
| [          [//   \_currentIndex   - index of the current toolbar item]]                                                                                          |
|                                                                                                                                                                                                                                |
| [          [//   \_selected       - true, if the current item is in selected state.]]                                                                            |
|                                                                                                                                                                                                                                |
| [          [//   \_disable        - true, if the current item is in selected state.]]                                                                            |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [        [function] OnMouseOver(inst, args) {]                                                                                                                        |
|                                                                                                                                                                                                                                |
| [          [//inst               - instance of a toolbar client-side object]]                                                                                    |
|                                                                                                                                                                                                                                |
| [          [//args:]]                                                                                                                                            |
|                                                                                                                                                                                                                                |
| [          [//   \_currentItem    - current toolbar item as a DOM element       ]]                                                                               |
|                                                                                                                                                                                                                                |
| [          [//   \_currentItemId  - ID of current toolbar item]]                                                                                                 |
|                                                                                                                                                                                                                                |
| [          [//   \_currentIndex   - index of the current toolbar item]]                                                                                          |
|                                                                                                                                                                                                                                |
| [          [//   \_selected       - true, if the current item is in selected state.]]                                                                            |
|                                                                                                                                                                                                                                |
| [          [//   \_disable        - true, if the current item is in selected state.]]                                                                            |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [        [function] OnMouseOut(inst, args) {]                                                                                                                         |
|                                                                                                                                                                                                                                |
| [          [//inst               - instance of a toolbar client-side object]]                                                                                    |
|                                                                                                                                                                                                                                |
| [          [//args:]]                                                                                                                                            |
|                                                                                                                                                                                                                                |
| [          [//   \_currentItem    - current toolbar item as a DOM element       ]]                                                                               |
|                                                                                                                                                                                                                                |
| [          [//   \_currentItemId  - ID of current toolbar item]]                                                                                                 |
|                                                                                                                                                                                                                                |
| [          [//   \_currentIndex   - index of the current toolbar item]]                                                                                          |
|                                                                                                                                                                                                                                |
| [          [//   \_selected       - true, if the current item is in selected state.]]                                                                            |
|                                                                                                                                                                                                                                |
| [          [//   \_disable        - true, if the current item is in selected state.]]                                                                            |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [\</][script][\>]                                                         |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Build and run the application.

 

**[Using Properties Model]**[]

The following steps explain how to handle client-side events raised by the toolbar through the properties model.

1.   In the controller, create an instance of **ToolbarModel**.

2.   Define the **Orientation** property and pass the instance through the **view-specific data** to the **view**.

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
| [            **myModel.ClientSideOnLoaded = [\"OnLoaded\"];**]                                              |
|                                                                                                                                                                         |
| **[            myModel.ClientSideClick = [\"OnClick\"];]**                                                  |
|                                                                                                                                                                         |
| **[            myModel.ClientSideMouseOver = [\"OnMouseOver\"];]**                                          |
|                                                                                                                                                                         |
| **[            myModel.ClientSideMouseOut = [\"OnMouseOut\"];]**                                            |
|                                                                                                                                                                         |
| []                                                                                                                                  |
|                                                                                                                                                                         |
| [            [//Pass the instance through ViewData]]                                                          |
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
| [    [\@{] Html.Syncfusion().Toolbar([\"myToolbar\"]).Render();[}]]**[]**                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

4.   Define the callback methods in the script to handle the specified events.[]

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                                                                                                                       |
|                                                                                                                                                                                                                                |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [        [function] OnLoaded(inst) {]                                                                                                                                 |
|                                                                                                                                                                                                                                |
| [          [//inst - instance of toolbar client side object]]                                                                                                    |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [        [function] OnClick(inst, args) {]                                                                                                                            |
|                                                                                                                                                                                                                                |
| [          [//inst               - instance of toolbar client side object]]                                                                                      |
|                                                                                                                                                                                                                                |
| [          [//args:]]                                                                                                                                            |
|                                                                                                                                                                                                                                |
| [          [//   \_currentItem    - current toolbar item as a DOM element       ]]                                                                               |
|                                                                                                                                                                                                                                |
| [          [//   \_currentItemId  - ID of current toolbar item]]                                                                                                 |
|                                                                                                                                                                                                                                |
| [          [//   \_currentIndex   - index of the current toolbar item]]                                                                                          |
|                                                                                                                                                                                                                                |
| [          [//   \_selected       - true, if the current item is in selected state.]]                                                                            |
|                                                                                                                                                                                                                                |
| [          [//   \_disable        - true, if the current item is in selected state.]]                                                                            |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [        [function] OnMouseOver(inst, args) {]                                                                                                                        |
|                                                                                                                                                                                                                                |
| [          [//inst               - instance of toolbar client side object]]                                                                                      |
|                                                                                                                                                                                                                                |
| [          [//args:]]                                                                                                                                            |
|                                                                                                                                                                                                                                |
| [          [//   \_currentItem    - current toolbar item as DOM element       ]]                                                                                 |
|                                                                                                                                                                                                                                |
| [          [//   \_currentItemId  - id of current toolbar item]]                                                                                                 |
|                                                                                                                                                                                                                                |
| [          [//   \_currentIndex   - index of the current toolbar item]]                                                                                          |
|                                                                                                                                                                                                                                |
| [          [//   \_selected       - true, if the current item is in selected state.]]                                                                            |
|                                                                                                                                                                                                                                |
| [          [//   \_disable        - true, if the current item is in selected state.]]                                                                            |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [        [function] OnMouseOut(inst, args) {]                                                                                                                         |
|                                                                                                                                                                                                                                |
| [          [//inst               - instance of a toolbar client-side object]]                                                                                    |
|                                                                                                                                                                                                                                |
| [          [//args:]]                                                                                                                                            |
|                                                                                                                                                                                                                                |
| [          [//   \_currentItem    - current toolbar item as a DOM element       ]]                                                                               |
|                                                                                                                                                                                                                                |
| [          [//   \_currentItemId  - ID of the current toolbar item]]                                                                                             |
|                                                                                                                                                                                                                                |
| [          [//   \_currentIndex   - index of the current toolbar item]]                                                                                          |
|                                                                                                                                                                                                                                |
| [          [//   \_selected       - true, if the current item is in selected state.]]                                                                            |
|                                                                                                                                                                                                                                |
| [          [//   \_disable        - true, if the current item is in selected state.]]                                                                            |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [\</][script][\>]                                                         |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Build and run the application.

After performing the above steps, you can observe the handlers being invoked when the corresponding events are triggered.

[] 

[]{#related-topics}

