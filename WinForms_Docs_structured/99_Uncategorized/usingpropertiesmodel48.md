---
title: usingpropertiesmodel48.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingpropertiesmodel48.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

The following steps explain the setting of the dimensions of the dialog using the Properties model:

1.   In the **Controller**, create an instance of **MobDialogModel**, define the **Height** and **Width** and pass the instance through **View Specific Data** to **View** as given below.**

*[[ [] ]]{.underline}*  

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                              |
|                                                                                                                                                                         |
| **[\[Controller\]]**                                                                                                                |
|                                                                                                                                                                         |
| **[]**                                                                                                                              |
|                                                                                                                                                                         |
| [        [public][ActionResult] Dialog()]                                              |
|                                                                                                                                                                         |
| [        {]                                                                                                                         |
|                                                                                                                                                                         |
| [            [//create an instance of MobDialogModel]]                                                        |
|                                                                                                                                                                         |
| [            [MobDialogModel] model = [new][MobDialogModel]()] |
|                                                                                                                                                                         |
| [            {]                                                                                                                     |
|                                                                                                                                                                         |
| [                Height = 100,]                                                                                                     |
|                                                                                                                                                                         |
| [                Width = 400,]                                                                                                      |
|                                                                                                                                                                         |
| [                Title = [\"Syncfusion Essential Studio\"],]                                                |
|                                                                                                                                                                         |
| [                DialogIconUrl = [\"\~/Content/Images/favicon.ico\"]]                                       |
|                                                                                                                                                                         |
| [            };]                                                                                                                    |
|                                                                                                                                                                         |
| [            ViewData\[[\"MobDialog\"]\] = model;]                                                          |
|                                                                                                                                                                         |
| [            [return] View();]                                                                                 |
|                                                                                                                                                                         |
| [        }]                                                                                                                         |
|                                                                                                                                                                         |
| []                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In **View**, create the dialog contents and invoke the dialog helper with the **View Data** key as the first argument.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                   |
|                                                                                                                                                                      |
| **[]**                                                                                                                           |
|                                                                                                                                                                      |
| [        [\<%]{]                                                                                     |
|                                                                                                                                                                      |
| [          Html.MobSyncfusion().Dialog([\"MobDialog\"])]                                                 |
|                                                                                                                                                                      |
| [              .Template(() =\>]                                                                                                 |
|                                                                                                                                                                      |
| [              {[%\>][\<][div][\>]] |
|                                                                                                                                                                      |
| [                  This is the Syncfusion Mobile Dialog control]                                                                 |
|                                                                                                                                                                      |
| [              [\</][div][\>]]                                  |
|                                                                                                                                                                      |
| [    [\<%]})]                                                                                        |
|                                                                                                                                                                      |
| [            .Render();]                                                                                                         |
|                                                                                                                                                                      |
| [      }[%\>]]                                                                                       |
|                                                                                                                                                                      |
| []                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                       |
|                                                                                                                                                                           |
| **[]**                                                                                                                                |
|                                                                                                                                                                           |
| [    [\@{]]                                                                                               |
|                                                                                                                                                                           |
| [        Html.MobSyncfusion().Dialog([\"MobDialog\"])]                                                        |
|                                                                                                                                                                           |
| [            .Template([@][\<][div][\>]] |
|                                                                                                                                                                           |
| [                This is the Syncfusion Mobile Dialog control]                                                                        |
|                                                                                                                                                                           |
| [            [\</][div][\>]]                                         |
|                                                                                                                                                                           |
| [).Render();]                                                                                                                         |
|                                                                                                                                                                           |
| [    [}]]                                                                                                 |
|                                                                                                                                                                           |
| []                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Build and run the application in emulator.

The output is displayed in the following screenshot.

[] 

{border="0"}

Figure 41: Dialog with customized dimensions

 

[]{#related-topics}

