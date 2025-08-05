---
title: clientsidemethods13.md
original_path: WinForms_Docs/99_Uncategorized/clientsidemethods13.md
created_at: 2025-08-05
---






#### Client-Side Methods {#client-side-methods style="tab-stops: 0pt"}

The toolbar control supports a rich set of client-side methods to control its behavior.

Methods

 


  -------------------------------------------------- ------------------------------------------------------ ------------- --------------------------------------------------
  Name                                               Parameters                                             Return type   Description
  [Disable_ToolbarItem]        index -- index of the toolbar item to be disabled.     \-            Disables the toolbar item of a specified index.
  [Disable_ToolbarItembyID]    id -- ID of the toolbar item to be disabled.           \-            Disables the toolbar item of a specified index.
  [Enable_ToolbarItem]         index -- index of the toolbar item to be enabled.      \-            Enables the toolbar item of a specified index.
  [Enable_ToolbarItembyID]     id -- ID of the toolbar item to be enabled.            \-            Enables the toolbar item of a specified index.
  [Select_ToolbarItem]         index -- index of the toolbar item to be selected.     \-            Selects a toolbar item of a specified index.
  [Select_ToolbarItembyID]     id -- ID of the toolbar item to be selected.           \-            Selects the toolbar item of a specified index.
  [Deselect_ToolbarItem]       index -- index of the toolbar item to be deselected.   \-            Deselects the toolbar item of a specified index.
  [Deselect_ToolbarItembyID]   id -- ID of the toolbar item to be deselected.         \-            Deselects the toolbar item of a specified index.
  [Show_Toolbar]               \-                                                     \-            Displays the toolbar.
  [Hide_Toolbar]               \-                                                     \-            Hides the toolbar.
  [Enable_All]                 \-                                                     \-            Enables all toolbar items.
  [Disable_All]                \-                                                     \-            Disables all toolbar items.
  -------------------------------------------------- ------------------------------------------------------ ------------- --------------------------------------------------


 

The following steps describe how to use the client-side methods.

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
| [      \</][ul][\>][]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [       ]                                                                                                                                                                                                                                                                                                                                                                            |
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
| [        .TargetId([\"toolbarItems\"])[%\>]]                                                                                                                                                                                                                                                                                     |
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
| [        .TargetId([\"toolbarItems\"])]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                         |
| **[      ]**[.Render();][}]**[]**                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

2.   In JavaScript, use the methods to enable, disable, select, and deselect a toolbar item.

**[]** 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [      ]**[\[JavaScript\]]**                                                                                                              |
|                                                                                                                                                                                                                                |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                |
| [        [function] DisableItem() {]                                                                                                                                  |
|                                                                                                                                                                                                                                |
| [            [//Code to create an instance of a toolbar client-side object]]                                                                                     |
|                                                                                                                                                                                                                                |
| [            [var] toolbarObj = \$find([\"myToolbar\"]);]                                                                                      |
|                                                                                                                                                                                                                                |
| [            [//Code to disable an item from passing its index]]                                                                                                 |
|                                                                                                                                                                                                                                |
| [            toolbarObj.Disable_ToolbarItem(3);]                                                                                                                                           |
|                                                                                                                                                                                                                                |
| [            [//Code to disable an item from passing its ID]]                                                                                                    |
|                                                                                                                                                                                                                                |
| [            toolbarObj.Disable_ToolbarItembyID([\"Print\"]);]                                                                                                      |
|                                                                                                                                                                                                                                |
| [            [//Code to disable all items]]                                                                                                                      |
|                                                                                                                                                                                                                                |
| [            toolbarObj.Disable_All();]                                                                                                                                                    |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| [        [function] EnableItem() {]                                                                                                                                   |
|                                                                                                                                                                                                                                |
| [            [//Code to create an instance of a toolbar client-side object]]                                                                                     |
|                                                                                                                                                                                                                                |
| [            [var] toolbarObj = \$find([\"myToolbar\"]);]                                                                                      |
|                                                                                                                                                                                                                                |
| [            [//Code to enable an item to pass its index]]                                                                                                       |
|                                                                                                                                                                                                                                |
| [            toolbarObj.Enable_ToolbarItem(3);]                                                                                                                                            |
|                                                                                                                                                                                                                                |
| [            [//Code to enable an item to pass its ID]]                                                                                                          |
|                                                                                                                                                                                                                                |
| [            toolbarObj.Enable_ToolbarItembyID([\"Print\"]);]                                                                                                       |
|                                                                                                                                                                                                                                |
| [            [//Code to enable all items]]                                                                                                                       |
|                                                                                                                                                                                                                                |
| [            toolbarObj.Enable_All();]                                                                                                                                                     |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [        [function] SelectItem() {]                                                                                                                                   |
|                                                                                                                                                                                                                                |
| [            [//Code to create an instance of a toolbar client-side object]]                                                                                     |
|                                                                                                                                                                                                                                |
| [            [var] toolbarObj = \$find([\"myToolbar\"]);]                                                                                      |
|                                                                                                                                                                                                                                |
| [            [//Code to select an item for passing its index]]                                                                                                   |
|                                                                                                                                                                                                                                |
| [            toolbarObj.Select_ToolbarItem(3);]                                                                                                                                            |
|                                                                                                                                                                                                                                |
| [            [//Code to select an item for passing its ID]]                                                                                                      |
|                                                                                                                                                                                                                                |
| [            toolbarObj.Select_ToolbarItembyID([\"Print\"]);]                                                                                                       |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [        [function] DeselectItem() {]                                                                                                                                 |
|                                                                                                                                                                                                                                |
| [            [//Code to create an instance of a toolbar client-side object]]                                                                                     |
|                                                                                                                                                                                                                                |
| [            [var] toolbarObj = \$find([\"myToolbar\"]);]                                                                                      |
|                                                                                                                                                                                                                                |
| [            [//Code to deselect an item passing its index]]                                                                                                     |
|                                                                                                                                                                                                                                |
| [            toolbarObj.Deselect_ToolbarItem(3);]                                                                                                                                          |
|                                                                                                                                                                                                                                |
| [            [//Code to deselect an item passing its ID]]                                                                                                        |
|                                                                                                                                                                                                                                |
| [            toolbarObj.Deselect_ToolbarItembyID([\"Print\"]);]                                                                                                     |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [        [function] ShowHide() {]                                                                                                                                     |
|                                                                                                                                                                                                                                |
| [            [//Code to create an instance of a toolbar client-side object]]                                                                                     |
|                                                                                                                                                                                                                                |
| [            [var] toolbarObj = \$find([\"myToolbar\"]);]                                                                                      |
|                                                                                                                                                                                                                                |
| [            [//Code to hide the toolbar]]                                                                                                                       |
|                                                                                                                                                                                                                                |
| [            toolbarObj.Hide_Toolbar();]                                                                                                                                                   |
|                                                                                                                                                                                                                                |
| [            [//Code to display the toolbar]]                                                                                                                    |
|                                                                                                                                                                                                                                |
| [            toolbarObj.Show_Toolbar();]                                                                                                                                                   |
|                                                                                                                                                                                                                                |
| [        }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                |
| **[      ]**[\</][script][\>]         |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Build and run the application.

**[]** 

[]{#related-topics}

