---
title: usingbuilder140.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder140.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps guide in handling client side events through Builder:

1.   In **View**, invoke the Toolbar helper with Toolbar ID as the first argument and enable the **ClientSideOnCreate** and **ClientSideOnClick** with the respective handlers as:

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                        |
| [ [\<%][=]Html.MobSyncfusion().Toolbar([\"EventsToolbar\"])]                                                              |
|                                                                                                                                                                                                                                        |
| [    .ClientSideEvents(events =\> events]                                                                                                                                                          |
|                                                                                                                                                                                                                                        |
| [      .ClientSideOnCreate([\"onCreate\"])]                                                                                                                                |
|                                                                                                                                                                                                                                        |
| [      .ClientSideOnClick([\"onClick\"]))]                                                                                                                                 |
|                                                                                                                                                                                                                                        |
| [    .Items(items =\>]                                                                                                                                                                             |
|                                                                                                                                                                                                                                        |
| [    {]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                        |
| [                   items.Add().Value([\"New\"]).Text([\"New\"]).ImageUrl([\"\~/Content/Toolbar/Images/new.png\"]);]       |
|                                                                                                                                                                                                                                        |
| [                   items.Add().Value([\"Open\"]).Text([\"Open\"]).ImageUrl([\"\~/Content/Toolbar/Images/open.png\"]);]    |
|                                                                                                                                                                                                                                        |
| [                   items.Add().Value([\"Save\"]).Text([\"Save\"]).ImageUrl([\"\~/Content/Toolbar/Images/save.png\"]);]    |
|                                                                                                                                                                                                                                        |
| [                   items.Add().Value([\"Print\"]).Text([\"Print\"]).ImageUrl([\"\~/Content/Toolbar/Images/print.png\"]);] |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                        |
| [items.Add().IsSeparator([true]);]                                                                                                                                            |
|                                                                                                                                                                                                                                        |
| [                   items.Add().Value([\"Cut\"]).Text([\"Cut\"]).ImageUrl([\"\~/Content/Toolbar/Images/Cut.png\"]);]       |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                        |
| [    })[%\>]]                                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [ [\@{]]                                                                                                                                                            |
|                                                                                                                                                                                                                                     |
| [   Html.MobSyncfusion().Toolbar([\"EventsToolbar\"])]                                                                                                                  |
|                                                                                                                                                                                                                                     |
| [   .ClientSideEvents(events =\> events]                                                                                                                                                        |
|                                                                                                                                                                                                                                     |
| [     .ClientSideOnCreate([\"onCreate\"])]                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [     .ClientSideOnClick([\"onClick\"]))]                                                                                                                               |
|                                                                                                                                                                                                                                     |
| [   .Items(items =\>]                                                                                                                                                                           |
|                                                                                                                                                                                                                                     |
| [   {]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                     |
| [                items.Add().Value([\"New\"]).Text([\"New\"]).ImageUrl([\"\~/Content/Toolbar/Images/new.png\"]);]       |
|                                                                                                                                                                                                                                     |
| [                items.Add().Value([\"Open\"]).Text([\"Open\"]).ImageUrl([\"\~/Content/Toolbar/Images/open.png\"]);]    |
|                                                                                                                                                                                                                                     |
| [                items.Add().Value([\"Save\"]).Text([\"Save\"]).ImageUrl([\"\~/Content/Toolbar/Images/save.png\"]);]    |
|                                                                                                                                                                                                                                     |
| [                items.Add().Value([\"Print\"]).Text([\"Print\"]).ImageUrl([\"\~/Content/Toolbar/Images/print.png\"]);] |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [items.Add().IsSeparator([true]);]                                                                                                                                         |
|                                                                                                                                                                                                                                     |
| [                items.Add().Value([\"Cut\"]).Text([\"Cut\"]).ImageUrl([\"\~/Content/Toolbar/Images/Cut.png\"]);]       |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [   })]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                     |
| [   .Render();[}]] []                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   Define the call back methods in the script to handle the specified events.

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
| [        }]                                                                                                                           |
|                                                                                                                                                                           |
| []                                                                                                                                    |
|                                                                                                                                                                           |
| [    [\</][script][\>]]                                              |
|                                                                                                                                                                           |
| []                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]**  

3.   Run the application.

**[]**  

[]{#related-topics}

