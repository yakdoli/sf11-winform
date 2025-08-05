---
title: enablingcaching.md
original_path: WinForms_Docs/99_Uncategorized/enablingcaching.md
created_at: 2025-08-05
---






#### Enabling Caching {#enabling-caching style="tab-stops: 0pt"}

Auto-complete textbox supports caching. Cache is a temporary storage area, which stores frequently accessed data. It provides rapid access to data by retrieving the cached copy rather than re-fetching it from the main data source every time, thereby reducing time and load. It can be used with Autocomplete TextBox in web browsers to access frequently used websites.

 

Properties

+-------------+-------------------------------------------------------------------------------------------------------------------------+----------------------+------------------+-------------------------------+
| Name        | Description                                                                                                             | Type of the property | Value it accepts | Dependecy                     |
+-------------+-------------------------------------------------------------------------------------------------------------------------+----------------------+------------------+-------------------------------+
| DropDown    | When set, renders a drop-down button, which when clicked, renders the un-filtered list.                                 | bool                 | true/false       | NA                            |
|             |                                                                                                                         |                      |                  |                               |
|             |                                                                                                                         |                      |                  |                               |
+-------------+-------------------------------------------------------------------------------------------------------------------------+----------------------+------------------+-------------------------------+
| AllowCache  | When set, allows cache therebypreventing further requests (after the first request) to the server on *drop-down* click. | bool                 | true/false       | Requires DropDown set to true |
|             |                                                                                                                         |                      |                  |                               |
|             |                                                                                                                         |                      |                  |                               |
+-------------+-------------------------------------------------------------------------------------------------------------------------+----------------------+------------------+-------------------------------+

*[[]]{.underline}* 

Using Builder

The following steps explain enabling caching for an auto-complete textbox using builder.

1.   In **View**, invoke the auto-complete textbox helper with the control id as the first argument, followed by the **DropDown** and **AllowCache** methods with arguments set to 'true'.

 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                            |
| [\<%][=][Html.Syncfusion().AutocompleteTextBox([\"myAutocomplete\"])] |
|                                                                                                                                                                                                                                            |
| [.RequestMapper([\"Home/GetData\"])]                                                                                                                                           |
|                                                                                                                                                                                                                                            |
| **[.DropDown([true])]**                                                                                                                                                           |
|                                                                                                                                                                                                                                            |
| **[.AllowCache([true])]**                                                                                                                                                         |
|                                                                                                                                                                                                                                            |
| **[%\>]**[]                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                            |
| [\@{][ ][Html.Syncfusion().AutocompleteTextBox([\"myAutocomplete\"])] |
|                                                                                                                                                                                                                                            |
| [.RequestMapper([\"Home/GetData\"])]                                                                                                                                           |
|                                                                                                                                                                                                                                            |
| **[.DropDown([true])]**                                                                                                                                                           |
|                                                                                                                                                                                                                                            |
| **[.AllowCache([true]).Render();]**                                                                                                                                               |
|                                                                                                                                                                                                                                            |
| **[}]**[]                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

[] 

**[]** 

2.   In the Controller, define the post action from which the auto-complete textbox requests the data source.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                     |
|                                                                                                                                                                              |
| [\[[AcceptVerbs]([HttpVerbs].Post)\]]                                                    |
|                                                                                                                                                                              |
| [        [public] [ActionResult] GetData([string] QueryString)]        |
|                                                                                                                                                                              |
| [        {]                                                                                                                              |
|                                                                                                                                                                              |
| [            [Northwind] context = SqlCE;]                                                                       |
|                                                                                                                                                                              |
| [            [//Get the data source]]                                                                              |
|                                                                                                                                                                              |
| [            [var] dataSource = [from] suggestion [in] context.Customers] |
|                                                                                                                                                                              |
| [                             [select] suggestion.CustomerID;]                                                      |
|                                                                                                                                                                              |
| []                                                                                                                                       |
|                                                                                                                                                                              |
| [            [//invoke the AutoCompleteActionResut]]                                                               |
|                                                                                                                                                                              |
| [            [return] dataSource.AutocompleteActionResult();]                                                       |
|                                                                                                                                                                              |
| [        }\                                                                                                                                                                  |
| \                                                                                                                                                                            |
| []]                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

\
\

[] 

3.   Build and run the application

**[]** 

[] 

Using Properties Model

The following steps explain you how to configure the filtering conditions for an auto-complete textbox through properties model.

*[[[]]]{.underline}* 

1.   In the Controller, create an instance of **AutoCompleteTextBoxModel**, set the **DropDown** and **AllowCache** properties and pass the instance through view specific data to the view as below.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                                        |
|                                                                                                                                                                                                 |
| [public][ [ActionResult] Index()]                                                  |
|                                                                                                                                                                                                 |
| [        {]                                                                                                                                                 |
|                                                                                                                                                                                                 |
| [            [//create and instance of AutocompleteTextBoxModel]]                                                                     |
|                                                                                                                                                                                                 |
| [            [AutocompleteTextBoxModel] myModel = [new] [AutocompleteTextBoxModel]();] |
|                                                                                                                                                                                                 |
| [            myModel.RequestMapper = [\"Home/GetData\"];]                                                                           |
|                                                                                                                                                                                                 |
| [            **myModel.DropDown = [true];**]                                                                                           |
|                                                                                                                                                                                                 |
| **[            myModel.AllowCache = [true];]**                                                                                         |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
|                                                                                                                                                                                                 |
| [            [//pass the instance through view data to the view]]                                                                     |
|                                                                                                                                                                                                 |
| [            ViewData\[[\"myAutocomplete\"]\] = myModel;]                                                                           |
|                                                                                                                                                                                                 |
| [            [return] View();]                                                                                                         |
|                                                                                                                                                                                                 |
| [        }]                                                                                                                                                 |
|                                                                                                                                                                                                 |
| []                                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**[]** 

[] 

2.   In the **View**, invoke the auto-complete textbox helper with the view data key as the control id.

 

**[]** 

**[]** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                             |
| [\<%][=][Html.Syncfusion().AutocompleteTextBox([\"myAutocomplete\"])[%\>]] |
|                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**[]** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                     |
| [\@{][ ][Html.Syncfusion().AutocompleteTextBox([\"myAutocomplete\"]).Render();[}]] |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

3.   In the Controller, define the post action to which the auto-complete textbox requests the data source.

 

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**                                                                                                                     |
|                                                                                                                                                                              |
| **[]**                                                                                                                                   |
|                                                                                                                                                                              |
| [\[[AcceptVerbs]([HttpVerbs].Post)\]]                                                    |
|                                                                                                                                                                              |
| [        [public] [ActionResult] GetData([string] QueryString)]        |
|                                                                                                                                                                              |
| [        {]                                                                                                                              |
|                                                                                                                                                                              |
| [            [Northwind] context = SqlCE;]                                                                       |
|                                                                                                                                                                              |
| [            [//Get the data source]]                                                                              |
|                                                                                                                                                                              |
| [            [var] dataSource = [from] suggestion [in] context.Customers] |
|                                                                                                                                                                              |
| [                             [select] suggestion.CustomerID;]                                                      |
|                                                                                                                                                                              |
| []                                                                                                                                       |
|                                                                                                                                                                              |
| [            [//invoke the AutoCompleteActionResut]]                                                               |
|                                                                                                                                                                              |
| [            [return] dataSource.AutocompleteActionResult();]                                                       |
|                                                                                                                                                                              |
| [        }]                                                                                                                              |
|                                                                                                                                                                              |
| []                                                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**[]** 

[] 

4.   Build and run the application.

The output is shown in the following screen shot.

{border="0"}

Figure 76: Auto-complete with drop-down

[] 

[]{#related-topics}

