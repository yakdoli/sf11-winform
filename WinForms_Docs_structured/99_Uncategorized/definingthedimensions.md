---
title: definingthedimensions.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\definingthedimensions.md
created_at: 2025-07-03
---






#### Defining the Dimensions {#defining-the-dimensions style="tab-stops: 0pt"}

Auto-complete textbox supports customizing its dimensions.

+-------------+-----------------------------------------------------------------------------------+-------------------------------+------------------------------------------+-------------+
| Width       | Sets the width of the auto-complete textbox in pixels                             | [struct] | Members of Unit                          | NA          |
|             |                                                                                   |                               |                                          |             |
|             |                                                                                   |                               |                                          |             |
+-------------+-----------------------------------------------------------------------------------+-------------------------------+------------------------------------------+-------------+
| ListHeight  | Sets the maximum height of the suggestion list in pixels.                         | [struct] | Members of Unit[]   | NA          |
|             |                                                                                   |                               |                                          |             |
|             |                                                                                   |                               |                                          |             |
+-------------+-----------------------------------------------------------------------------------+-------------------------------+------------------------------------------+-------------+
| ListWidth   | Sets the width of the suggestion list in pixels.                                  | [struct] | Members of Unit[]   | NA          |
|             |                                                                                   |                               |                                          |             |
|             |                                                                                   |                               |                                          |             |
+-------------+-----------------------------------------------------------------------------------+-------------------------------+------------------------------------------+-------------+
| ListSize    | Sets the maximum number of suggetsions to be displayed within the suggestion list | [int]    | 0 to [int.]MaxValue | NA          |
|             |                                                                                   |                               |                                          |             |
|             |                                                                                   |                               | []                  |             |
+-------------+-----------------------------------------------------------------------------------+-------------------------------+------------------------------------------+-------------+

 

Using Builder

The following steps explain the setting of dimensions for an auto-complete textbox using Builder.

1.   In **View**, invoke the auto-complete textbox helper with the control id as the first argument, followed by the **Width, ListHeight, ListWidth** and **ListSize** methods with the desired dimensions as arguments.

 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                            |
| [\<%][=][Html.Syncfusion().AutocompleteTextBox([\"myAutocomplete\"])] |
|                                                                                                                                                                                                                                            |
| [.RequestMapper([\"Home/GetData\"])]                                                                                                                                           |
|                                                                                                                                                                                                                                            |
| [            .**Width(150)**]                                                                                                                                                                          |
|                                                                                                                                                                                                                                            |
| **[            .ListHeight(300)]**                                                                                                                                                                     |
|                                                                                                                                                                                                                                            |
| **[.ListWidth(200)]**                                                                                                                                                                                  |
|                                                                                                                                                                                                                                            |
| **[.ListSize(5)[%\>]]**                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                            |
| [\@{][ ][Html.Syncfusion().AutocompleteTextBox([\"myAutocomplete\"])] |
|                                                                                                                                                                                                                                            |
| [.RequestMapper([\"Home/GetData\"])]                                                                                                                                           |
|                                                                                                                                                                                                                                            |
| [            .**Width(150)**]                                                                                                                                                                          |
|                                                                                                                                                                                                                                            |
| **[            .ListHeight(300)]**                                                                                                                                                                     |
|                                                                                                                                                                                                                                            |
| **[.ListWidth(200)]**                                                                                                                                                                                  |
|                                                                                                                                                                                                                                            |
| **[.ListSize(5).Render();]**                                                                                                                                                                           |
|                                                                                                                                                                                                                                            |
| **[}]**                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

**[]** 

2.   In the Controller, define the post action to which the auto-complete textbox requests the data source.

 

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
| [        }]                                                                                                                              |
|                                                                                                                                                                              |
| []                                                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Build and run the application.

**[]** 

Using Properties Model

The following steps explain the setting of the dimensions for an auto-complete textbox through Properties model.

1.   In the Controller, create an instance of AutoCompleteTextBoxModel, define the **Width, ListHeight, ListWidth** and **ListSize** properties and pass the instance through *View Specific Data* to View as given below.

 

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
| [            **myModel.Width = 150;**]                                                                                                                      |
|                                                                                                                                                                                                 |
| **[            myModel.ListHeight = 300;]**                                                                                                                 |
|                                                                                                                                                                                                 |
| **[            myModel.ListWidth = 200;]**                                                                                                                  |
|                                                                                                                                                                                                 |
| **[            myModel.ListSize = 5;]**                                                                                                                     |
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

**[]** 

[] 

2.   In **View**, invoke the auto-complete textbox helper with the view data key as the Control ID.

 

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                             |
| [\<%][=][Html.Syncfusion().AutocompleteTextBox([\"myAutocomplete\"])[%\>]] |
|                                                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                       |
| [\@{][ ][Html.Syncfusion().AutocompleteTextBox([\"myAutocomplete\"]).Render();**[}]**[]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

3.   In the Controller, define the post action to which the auto-complete textbox requests the data source.

 

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
| [        }]                                                                                                                              |
|                                                                                                                                                                              |
| **[]**                                                                                                               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

4.   Build and run the application.

The output is shown in the following screen shot.

 

{border="0"}

Figure 61: Auto-complete textbox with customized dimensions

 

 

[]{#related-topics}

