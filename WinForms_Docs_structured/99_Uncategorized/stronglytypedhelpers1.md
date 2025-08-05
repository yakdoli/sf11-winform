---
title: stronglytypedhelpers1.md
original_path: WinForms_Docs/99_Uncategorized/stronglytypedhelpers1.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Strongly Typed helpers {#strongly-typed-helpers style="tab-stops: 0pt"}

The Numeric textbox control supports strongly typed HTML helpers, which uses lambda expressions in reference models or view models passed to a view template. These helpers allow you to define the name and value of the Numeric text box from the model.

1.   In the Controller, pass the model to the View.

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

3.   In View, invoke the strongly typed numeric text box helper with the lambda expression to set the default value.

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                    |
| [  ] [\<%] []                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                    |
| [ Html.MobSyncfusion().NumericTextBoxFor(x =\> x.EmployeeID).Render(); [%\>]]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                    |
| **[\[Razor\]]**                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                    |
| [    ] [\@{] [Html.MobSyncfusion().NumericTextBoxFor(x =\> x.EmployeeID).Render();        [}]] [] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.   Build and run the application.

[]{#related-topics}

