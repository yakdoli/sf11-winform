---
title: configuringthefilterconditions.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\configuringthefilterconditions.md
created_at: 2025-07-03
---






#### Configuring the Filter Conditions {#configuring-the-filter-conditions style="tab-stops: 0pt"}

The Auto-complete textbox supports a wide range of filtering conditions.

 

Properties

+---------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+-------------+
| Name          | Description                                                                | Type of the property                                                                           | Value it accepts                                                                                             | Dependecy   |
+---------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+-------------+
| MinCharacter  | Sets the minimum number of characters that are required to start filtering | [[int]]{.UGHyperlink}  | 0 to [[int ]]{.UGHyperlink}.MaxValue | NA          |
|               |                                                                            |                                                                                                |                                                                                                              |             |
|               |                                                                            |                                                                                                |                                                                                                              |             |
+---------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+-------------+
| Delimiter     | When set, allows continuous filtering separated by the specified delimiter | [[char]]{.UGHyperlink} | Any character                                                                                                | NA          |
|               |                                                                            |                                                                                                |                                                                                                              |             |
|               |                                                                            |                                                                                                |                                                                                                              |             |
+---------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+-------------+
| CaseSensitive | When set, allows case sensitive filtering.                                 | [[bool]]{.UGHyperlink} | [[true/false]]{.UGHyperlink}         | NA          |
|               |                                                                            |                                                                                                |                                                                                                              |             |
|               |                                                                            |                                                                                                |                                                                                                              |             |
+---------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+-------------+

*[[]]{.underline}* 

Through Builder

Using Builder

The following steps explain the configuration of the filtering conditions for an auto-complete textbox using Builder.

 

1.   In **View**, invoke the auto-complete textbox helper with the control id as the first argument, followed by the **MinCharacter, Delimiter** and **CaseSensitive** methods with the desired options as arguments.

 

**[]** 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                            |
| [\<%][=][Html.Syncfusion().AutocompleteTextBox([\"myAutocomplete\"])] |
|                                                                                                                                                                                                                                            |
| [.**RequestMapper([\"Home/GetData\"])**]                                                                                                                                       |
|                                                                                                                                                                                                                                            |
| **[.MinCharacter(2)]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                            |
| **[.Delimiter([\';\'])]**                                                                                                                                                      |
|                                                                                                                                                                                                                                            |
| **[.CaseSensitive([true])]**[%\>]                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

**[]** 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                            |
| [\@{][ ][Html.Syncfusion().AutocompleteTextBox([\"myAutocomplete\"])] |
|                                                                                                                                                                                                                                            |
| [.**RequestMapper([\"Home/GetData\"])**]                                                                                                                                       |
|                                                                                                                                                                                                                                            |
| **[.MinCharacter(2)]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                            |
| **[.Delimiter([\';\'])]**                                                                                                                                                      |
|                                                                                                                                                                                                                                            |
| **[.CaseSensitive([true]).Render();]**[}]                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

**[]** 

[] 

2.   In the Controller, define the post action to which the auto-complete textbox requests the data source.

 

 

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

 

[] 

[] 

3.   Build and run the application.

 

Using Properties Model

The following steps explain the configuration of the filtering conditions for an auto-complete textbox using the Properties model.

1.   In the Controller, create an instance of **AutoCompleteTextBoxModel**, define the **MinCharacter, Delimiter** and **CaseSensitive** properties and pass the instance through **View Specific Data** to the view as given below.

 

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
| [            **myModel.RequestMapper = [\"Home/GetData\"];**]                                                                       |
|                                                                                                                                                                                                 |
| **[            myModel.MinCharacter = 2;]**                                                                                                                 |
|                                                                                                                                                                                                 |
| **[            myModel.Delimiter = [\';\'];]**                                                                                      |
|                                                                                                                                                                                                 |
| **[            myModel.CaseSensitive = [true];]**                                                                                      |
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

 

[] 

2.   In **View**, invoke the auto-complete textbox helper with the view data key as the Control ID.

[] 

[] 

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

[] 

The output is shown in the following screenshot.

[] 

{border="0"} 

Figure 62: Auto-complete textbox with filter conditons

[]{#related-topics}

