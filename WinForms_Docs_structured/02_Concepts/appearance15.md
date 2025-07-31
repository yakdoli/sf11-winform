---
title: appearance15.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\appearance15.md
created_at: 2025-07-03
---






#### Appearance {#appearance style="tab-stops: 0pt"}

Auto-complete textbox supports fourteen pre-defined skins to enhance the look and feel.

Properties

 

+-------------+--------------------------------------+------------------+---------------------------------------------------+-------------+
| Name        | Description                          | Type of property | Value it accepts                                  | Dependency  |
+-------------+--------------------------------------+------------------+---------------------------------------------------+-------------+
| AutoFormat  | Used to define the syncfusion themes | enum             | [Skins].Office2007Blue,   | NA          |
|             |                                      |                  |                                                   |             |
|             |                                      |                  | [Skins].Office2007Silver, |             |
|             |                                      |                  |                                                   |             |
|             |                                      |                  | [Skins].Office2007Black,  |             |
|             |                                      |                  |                                                   |             |
|             |                                      |                  | [Skins].Vista,            |             |
|             |                                      |                  |                                                   |             |
|             |                                      |                  | [Skins].Almond,           |             |
|             |                                      |                  |                                                   |             |
|             |                                      |                  | [Skins].Blueberry,        |             |
|             |                                      |                  |                                                   |             |
|             |                                      |                  | [Skins].Blend,            |             |
|             |                                      |                  |                                                   |             |
|             |                                      |                  | [Skins].Olive,            |             |
|             |                                      |                  |                                                   |             |
|             |                                      |                  | [Skins].Turquoise,        |             |
|             |                                      |                  |                                                   |             |
|             |                                      |                  | [Skins].Monochrome,       |             |
|             |                                      |                  |                                                   |             |
|             |                                      |                  | [Skins].Sandune,          |             |
|             |                                      |                  |                                                   |             |
|             |                                      |                  | [Skins].VS2010,           |             |
|             |                                      |                  |                                                   |             |
|             |                                      |                  | [Skins].Marble,           |             |
|             |                                      |                  |                                                   |             |
|             |                                      |                  | [Skins].Midnight          |             |
+-------------+--------------------------------------+------------------+---------------------------------------------------+-------------+

 

Using Builder

The following steps explain the setting of the Syncfusion theme for an auto-complete textbox using Builder.

1.   In **View**, invoke the auto-complete textbox helper with the control id as first argument, followed by the **AutoFormat** method with a desired theme as argument.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                            |
| [\<%][=][Html.Syncfusion().AutocompleteTextBox([\"myAutocomplete\"])] |
|                                                                                                                                                                                                                                            |
| [.RequestMapper([\"Home/GetData\"])]                                                                                                                                           |
|                                                                                                                                                                                                                                            |
| [.DropDown([true])]                                                                                                                                                               |
|                                                                                                                                                                                                                                            |
| **[.AutoFormat([Skins].Vista)]**[%\>]                                                                                  |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                            |
| [\@{][ ][Html.Syncfusion().AutocompleteTextBox([\"myAutocomplete\"])] |
|                                                                                                                                                                                                                                            |
| [.RequestMapper([\"Home/GetData\"])]                                                                                                                                           |
|                                                                                                                                                                                                                                            |
| [.DropDown([true])]                                                                                                                                                               |
|                                                                                                                                                                                                                                            |
| **[.AutoFormat([Skins].Vista).Render();]**[}]                                                                          |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In the Controller, define the post action from which the auto-complete textbox requests the data source.

 

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[Controller\]**                                                                                                                                                                        |
|                                                                                                                                                                                           |
| [\[[AcceptVerbs]([HttpVerbs].Post)\]]                                                    |
|                                                                                                                                                                                           |
| [        [public] [ActionResult] GetData([string] QueryString)]        |
|                                                                                                                                                                                           |
| [        {]                                                                                                                              |
|                                                                                                                                                                                           |
| [            [Northwind] context = SqlCE;]                                                                       |
|                                                                                                                                                                                           |
| [            [//Get the data source]]                                                                              |
|                                                                                                                                                                                           |
| [            [var] dataSource = [from] suggestion [in] context.Customers] |
|                                                                                                                                                                                           |
| [                             [select] suggestion.CustomerID;]                                                      |
|                                                                                                                                                                                           |
| []                                                                                                                                       |
|                                                                                                                                                                                           |
| [            [//invoke the AutoCompleteActionResut]]                                                               |
|                                                                                                                                                                                           |
| [            [return] dataSource.AutocompleteActionResult();]                                                       |
|                                                                                                                                                                                           |
| [        }]                                                                                                                              |
|                                                                                                                                                                                           |
| []                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

3.   Build and run the application.

 

**Using Properties Model**

The following steps explain the setting of the Syncfusion theme for an auto-complete textbox using Properties model.

1.   In the Controller, create an instance of **AutoCompleteTextBoxModel**, define the **AutoFormat** property and pass the instance through **view specific data** to View as given below.

 

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
| [            myModel.RequestMapper = [\"Home/GetTemplate\"];]                                                                       |
|                                                                                                                                                                                                 |
| [            myModel.DropDown = [true];]                                                                                               |
|                                                                                                                                                                                                 |
| [            **myModel.AutoFormat = [Skins].Vista;**]                                                                               |
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

2.   In **View**, invoke the auto-complete textbox helper with the view data key as the Control ID.

 

 

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

[] 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                            |
| [\@{][ ][Html.Syncfusion().AutocompleteTextBox([\"myAutocomplete\"])] |
|                                                                                                                                                                                                                                            |
| [.RequestMapper([\"Home/GetData\"])]                                                                                                                                           |
|                                                                                                                                                                                                                                            |
| [.DropDown([true])]                                                                                                                                                               |
|                                                                                                                                                                                                                                            |
| **[.AutoFormat([Skins].Vista).Render();]**                                                                                                                                     |
|                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

3.   In the **Controller**, define the post action to which the auto-complete textbox requests the data source.

 

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
| [                             [select] suggestion.CustomerID;]                                                      |
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

4.   Build and run the application.

The output is shown in the following screenshot.

 

{border="0"}

Figure 79: Auto-complete textbox---Theme

 

 

[]{#related-topics}

