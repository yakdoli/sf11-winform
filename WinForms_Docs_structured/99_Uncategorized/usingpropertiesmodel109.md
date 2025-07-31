---
title: usingpropertiesmodel109.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingpropertiesmodel109.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

The following steps, explains the appearance of Toolbar Control using the Properties model:

1.   In the **Controller**, create an instance for the **MobToolbarModel** and pass the instance through **ViewData** to **View** as given below.**

*[[ [] ]]{.underline}*  

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                   |
| [ [public][ActionResult] Appearance()]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                   |
| [ {]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                   |
| [   [MobToolbarModel] model = [new][MobToolbarModel]()]                                                                                                                  |
|                                                                                                                                                                                                                                                                                   |
| [   {]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                   |
| [     AutoFormat = [MobSkins].DarkNight,]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                   |
| [     Items = [new][List]\<[ToolbarItem]\>()]                                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| [     {]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                   |
| [      [new][ToolbarItem]() { Value=[\"New\"], Text=[\"New\"], ImageUrl=[\"\~/Content/Toolbar/Images/new.png\"]},]       |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| [      [new][ToolbarItem]() { Value=[\"Open\"], Text=[\"Open\"], ImageUrl=[\"\~/Content/Toolbar/Images/open.png\"]},]    |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| [      [new][ToolbarItem]() { Value=[\"Save\"], Text=[\"Save\"], ImageUrl=[\"\~/Content/Toolbar/Images/save.png\"]},]    |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| [      [new][ToolbarItem]() { Value=[\"Print\"], Text=[\"Print\"], ImageUrl=[\"\~/Content/Toolbar/Images/print.png\"]},] |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| [      [new][ToolbarItem]() { IsSeparator=[true] },]                                                                                                                        |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| [      [new][ToolbarItem]() { Value=[\"Cut\"], Text=[\"Cut\"], ImageUrl=[\"\~/Content/Toolbar/Images/Cut.png\"]}]        |
|                                                                                                                                                                                                                                                                                   |
| [      }]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                   |
| [    };]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                   |
| [    ViewData\[[\"ApperanceToolbar\"]\] = model;]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                   |
| [    [return] View();]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                   |
| [ }]                                                                                                                                                                                                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In **View**, invoke the Toolbar helper with the ViewData key as the first argument.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                        |
| **[]**                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                        |
| [\<%] [=] [Html.MobSyncfusion().Toolbar([\"ApperanceToolbar\"])[%\>]] |
|                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                        |
|                                                                                                                            |
| **[]**                                                                                 |
|                                                                                                                            |
| [  [\@{]]                                                  |
|                                                                                                                            |
| [        Html.MobSyncfusion().Toolbar([\"ApperanceToolbar\"])] |
|                                                                                                                            |
| [            .Render();]                                                               |
|                                                                                                                            |
| [   [}]] []                    |
+----------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Build and run the application.

 

The output is shown in the following screenshot:[]

{border="0"}

Figure 172: Toolbar Control with DarkNight Theme

[]{#related-topics}

