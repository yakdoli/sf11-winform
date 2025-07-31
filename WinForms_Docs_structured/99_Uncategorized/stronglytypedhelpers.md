---
title: stronglytypedhelpers.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\stronglytypedhelpers.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Strongly Typed helpers {#strongly-typed-helpers style="tab-stops: 0pt"}

MaskEdit textbox supports strongly typed HTML helpers, which uses lambda expressions in reference models or view models passed to a view template.The helper allows you to define the name and value of the MaskEdit text box from the model.

The following steps explain the use of the strongly typed helpers to create MaskEdit textbox:[]

1.   In the **Controller**, pass the model to the View.[]

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                            |
|                                                                                                                                                                                     |
| [public] [ [ActionResult] Index()]                                     |
|                                                                                                                                                                                     |
| [        {]                                                                                                                                     |
|                                                                                                                                                                                     |
| [            ] [Northwind] [ data = SqlCE;            ] |
|                                                                                                                                                                                     |
| [            [return] View(data.Employees);]                                                                               |
|                                                                                                                                                                                     |
| [        }]                                                                                                                                     |
|                                                                                                                                                                                     |
| []                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]**  

2.   Create a strongly typed view. (Please refer to the Creating a Strongly Typed View section for more details.)

3.   In View, invoke the strongly typed MaskEdit textbox helper with the lambda expression to set the default value.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                   |
| [  ] [\<%] [] [Html.MobSyncfusion().MaskEditTextBoxFor(model=\>model.HomePhone)] |
|                                                                                                                                                                                                                                                                   |
| **[.Mask([\"(999)999-9999\"])]** [ [%\>] ]                                                                                            |
|                                                                                                                                                                                                                                                                   |
| **[\[Razor\]]**                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                   |
| [    ] [\@{] [ Html.MobSyncfusion().MaskEditTextBoxFor(model=\>model.HomePhone)]                                                  |
|                                                                                                                                                                                                                                                                   |
| **[.Mask([\"(999)999-9999\"])]** [         [}]] []               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.   Build and run the application.

[]{#related-topics}

