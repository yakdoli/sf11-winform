---
title: usingpropertiesmodel110.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingpropertiesmodel110.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Properties Model      {#using-properties-model style="tab-stops: 0pt"}

The following steps guide in handling client side events through the Properties model.

1.   In Controller, create an instance of MobToolbarModel, define the **ClientSideOnCreate**,and  **ClientSideOnClick** events and pass the instance through **ViewData** to **View** as given below.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                  |
| [ [public][ActionResult] ClientSideEvents()]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                  |
| [ {]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                  |
| [  [MobToolbarModel] model = [new][MobToolbarModel]()]                                                                                                                  |
|                                                                                                                                                                                                                                                                                  |
| [  {]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                  |
| [   ClientSideEvents = [new][ToolbarEvents]()]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                  |
| [   {]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                  |
| [     ClientSideOnClick = [\"onClick\"],]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                  |
| [     ClientSideOnCreate = [\"onCreate\"]]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                  |
| [   },]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                  |
| [   Items = [new][List]\<[ToolbarItem]\>()]                                                                                                                             |
|                                                                                                                                                                                                                                                                                  |
| [   {]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                  |
| [     [new][ToolbarItem]() { Value=[\"New\"], Text=[\"New\"], ImageUrl=[\"\~/Content/Toolbar/Images/new.png\"]},]       |
|                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                  |
| [     [new][ToolbarItem]() { Value=[\"Open\"], Text=[\"Open\"], ImageUrl=[\"\~/Content/Toolbar/Images/open.png\"]},]    |
|                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                  |
| [     [new][ToolbarItem]() { Value=[\"Save\"], Text=[\"Save\"], ImageUrl=[\"\~/Content/Toolbar/Images/save.png\"]},]    |
|                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                  |
| [     [new][ToolbarItem]() { Value=[\"Print\"], Text=[\"Print\"], ImageUrl=[\"\~/Content/Toolbar/Images/print.png\"]},] |
|                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                  |
| [     [new][ToolbarItem]() { IsSeparator=[true] },]                                                                                                                        |
|                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                  |
| [     [new][ToolbarItem]() { Value=[\"Cut\"], Text=[\"Cut\"], ImageUrl=[\"\~/Content/Toolbar/Images/Cut.png\"]}]        |
|                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                  |
| [   }]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                  |
| [  };]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                  |
| [  ViewData\[[\"[EventsToolbar]{#OLE_LINK1}\"]\] = model;]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                  |
| [  [return] View();]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                  |
| [ }]                                                                                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   In **View**, invoke the Toolbar helper with the ViewData key as the first argument.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                      |
| [ \<%] [=] [Html.MobSyncfusion().Toolbar([\"EventsToolbar\"])[%\>]] |
|                                                                                                                                                                                                                                                                      |
| [] []                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                |
|                                                                                                                    |
| **[]**                                                                         |
|                                                                                                                    |
| [\@{] []               |
|                                                                                                                    |
| [   Html.MobSyncfusion().Toolbar([\"EventsToolbar\"])] |
|                                                                                                                    |
| [   .Render();]                                                                |
|                                                                                                                    |
| [ [}]] **[]**  |
+--------------------------------------------------------------------------------------------------------------------+

 

3.   Define the call back methods in the script to handle the specified events.

**[]**  

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Javascript\]]**                                                                                                                  |
|                                                                                                                                                                           |
| [    [\<][script][type][=\"text/javascript\"\>]] |
|                                                                                                                                                                           |
| []                                                                                                                                    |
|                                                                                                                                                                           |
| [        [function] onCreate(inst) {]                                                                            |
|                                                                                                                                                                           |
| [            [//inst - Toolbar object]]                                                                     |
|                                                                                                                                                                           |
| [        }]                                                                                                                           |
|                                                                                                                                                                           |
| []                                                                                                                                    |
|                                                                                                                                                                           |
| [        [function] onClick(inst, args) {]                                                                       |
|                                                                                                                                                                           |
| [            [//inst - instance of Toolbar object]]                                                         |
|                                                                                                                                                                           |
| [            [//args :    args.element   - current Toolbar item ]]                                          |
|                                                                                                                                                                           |
| [            [//          args.value            - Toolbar id]]                                              |
|                                                                                                                                                                           |
| [            [//          args.text          - text of the current Toolbar item ]]                          |
|                                                                                                                                                                           |
| [        }]                                                                                                                           |
|                                                                                                                                                                           |
| []                                                                                                                                    |
|                                                                                                                                                                           |
| [    [\</][script][\>]]                                              |
|                                                                                                                                                                           |
| []                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]**  

4.   Run the application.

 

[]{#related-topics}

