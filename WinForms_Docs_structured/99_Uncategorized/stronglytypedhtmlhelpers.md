---
title: stronglytypedhtmlhelpers.md
original_path: WinForms_Docs/99_Uncategorized/stronglytypedhtmlhelpers.md
created_at: 2025-08-05
---






#### Strongly typed HTML Helpers {#strongly-typed-html-helpers style="tab-stops: 0pt"}

Mask Edit textbox supports strongly typed HTML helpers, which use lambda expressions to reference models or view models passed to a view template.The helper allows you to define the name and value of the mask edit text box from the Model.

The following steps explain the use of the strongly typed helpers to create mask edit textbox.

1.   In the Controller, pass model to the **View**.

**[]** 

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
| []                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   Create a strongly typed view. Refer [strongly typed view]{.UGHyperlink} for more details. In the Controller, pass model to the View.

[] 

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
| []                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------+

 

3.   Create a strongly typed view. Refer to [strongly typed view]{.UGHyperlink} for more details. In **View**, invoke the **mask edit** textbox with lambda expression to set the default value.

4. 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                             |
| [\<%][=][Html.Syncfusion().MaskEditTextBoxFor(model=\>model.HomePhone)] |
|                                                                                                                                                                                                                                                             |
| **[.Mask([\"(999)999-9999\"])]**[ [%\>]]                                                              |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                           |
| [\@{][ Html.Syncfusion().MaskEditTextBoxFor(model=\>model.HomePhone)]                                                               |
|                                                                                                                                                                                                                                                           |
| **[.Mask([\"(999)999-9999\"])]**[.Render();][ [}]] |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

5.   Build and run the application.

You can observe [that the mask edit textbox is created with the ID 'HomePhone' and value of the HomePhone. The output is shown in the]{.BodyText1Char} following screenshot.

 

{border="0"}

Figure 146: Mask edit textbox

***[]*** 

[]{#related-topics}

