---
title: stronglytypedhtmlhelpers1.md
original_path: WinForms_Docs/99_Uncategorized/stronglytypedhtmlhelpers1.md
created_at: 2025-08-05
---






#### Strongly Typed HTML Helpers {#strongly-typed-html-helpers style="tab-stops: 0pt"}

The numeric text box control supports strongly typed HTML helpers, which use lambda expressions to reference models or view models passed to a view template. These helpers allow you to define the name and value of the numeric text box from the model.

The following steps explain how to use the strongly typed helpers to create a numeric text box.

1.   In the controller, pass the model to the View.

 

+------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[Controller\]**                                                                                                                             |
|                                                                                                                                                |
|                                                                                                                                                |
|                                                                                                                                                |
| [public][ [ActionResult] Index()] |
|                                                                                                                                                |
| [        {]                                                                                                |
|                                                                                                                                                |
| [            [Northwind] data = SqlCE;]                                            |
|                                                                                                                                                |
| [            ]                                                                                             |
|                                                                                                                                                |
| [            [//pass the model to the view]]                                         |
|                                                                                                                                                |
| [            [return] View(data.Employees);]                                          |
|                                                                                                                                                |
| [  }]                                                                                                      |
|                                                                                                                                                |
|                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Create a strongly typed view. Please refer to the [Creating a Strongly Typed View]{.UGHyperlink} section for more details.

3.   In **View**, invoke the strongly typed numeric text box helper with the lambda expression to set the default value.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<%][=][Html.Syncfusion().NumericTextBoxFor(model=\>model.][EmployeeID][)[%\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [@(][new][ [HtmlString](][Html.Syncfusion().NumericTextBoxFor(model=\>model.][EmployeeID][)][.ToString())[)]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

4.   Build and run the application.

 

In the output, you will be able to observe the numeric text box created with the ID "EmployeeID" as well as the value of the employee ID.

[]{#related-topics}

