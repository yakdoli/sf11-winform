---
title: usingbuilder139.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingbuilder139.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps explain the appearance of Toolbar control using Builder.

1.   In **View**, invoke the Toolbar helper with the Control ID as first argument followed by the AutoFormat method with the desired theme as the argument.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                 |
| [\<%] [=] [Html.MobSyncfusion().Toolbar([\"ApperanceToolbar\"])[]] |
|                                                                                                                                                                                                                                                                 |
| [   .AutoFormat([MobSkins].DarkNight)]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                 |
| [   .Items(items =\>]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                 |
| [   {]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                 |
| [                   items.Add().Value([\"New\"]).Text([\"New\"]).ImageUrl([\"\~/Content/Toolbar/Images/new.png\"]);]                                |
|                                                                                                                                                                                                                                                                 |
| [                   items.Add().Value([\"Open\"]).Text([\"Open\"]).ImageUrl([\"\~/Content/Toolbar/Images/open.png\"]);]                             |
|                                                                                                                                                                                                                                                                 |
| [                   items.Add().Value([\"Save\"]).Text([\"Save\"]).ImageUrl([\"\~/Content/Toolbar/Images/save.png\"]);]                             |
|                                                                                                                                                                                                                                                                 |
| [                   items.Add().Value([\"Print\"]).Text([\"Print\"]).ImageUrl([\"\~/Content/Toolbar/Images/print.png\"]);]                          |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                 |
| [items.Add().IsSeparator([true]);]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                 |
| [                   items.Add().Value([\"Cut\"]).Text([\"Cut\"]).ImageUrl([\"\~/Content/Toolbar/Images/Cut.png\"]);]                                |
|                                                                                                                                                                                                                                                                 |
| [   })[%\>]]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                     |
| [ [\@{]]                                                                                                                                                            |
|                                                                                                                                                                                                                                     |
| [   Html.MobSyncfusion().Toolbar([\"ApperanceToolbar\"])]                                                                                                               |
|                                                                                                                                                                                                                                     |
| [   .AutoFormat([MobSkins].DarkNight)]                                                                                                                                  |
|                                                                                                                                                                                                                                     |
| [   .Items(items =\>]                                                                                                                                                                           |
|                                                                                                                                                                                                                                     |
| [   {]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                     |
| [items.Add().Value([\"New\"]).Text([\"New\"]).ImageUrl([\"\~/Content/Toolbar/Images/new.png\"]);]                       |
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
| [   })]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                     |
| [   .Render();[}]] **[]**                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

2.   Build and run the application.

**[]**  

[]{#related-topics}

