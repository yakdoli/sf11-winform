---
title: watermarking.md
original_path: WinForms_Docs/99_Uncategorized/watermarking.md
created_at: 2025-08-05
---






#### Watermarking {#watermarking style="tab-stops: 0pt"}

Auto-complete textbox supports watermarking. A watermark text is a background text that appears in the text box without interfering with the text entry or readability of the text entered. It can be used to display a ready instruction or important information for the user. It appears as an auto text before the test is entered and disappears once the user starts entering the text.

 

Properties

+-------------+--------------------------------------------------------+--------------------------------------------------------------------------------------------------+------------------+-------------+
| Name        | Description                                            | Type of property                                                                                 | Value it accepts | Dependecy   |
+-------------+--------------------------------------------------------+--------------------------------------------------------------------------------------------------+------------------+-------------+
| WaterMark   | Sets the water mark text for the auto-complete textbox | [[string]]{.UGHyperlink} | Any string       | NA          |
|             |                                                        |                                                                                                  |                  |             |
|             |                                                        |                                                                                                  |                  |             |
+-------------+--------------------------------------------------------+--------------------------------------------------------------------------------------------------+------------------+-------------+

 

Using Builder

The following steps explain the setting of watermark text for an auto-complete textbox using Builder.

1.   In **View**, invoke the auto-complete textbox helper with the control ID as the first argument, followed by the **WaterMark** method with a desired string as argument.

 

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[aspx\]]**                                                                                                                                                                        |
|                                                                                                                                                                                                                               |
| [\<%][=][Html.AutocompleteTextBox([\"myAutocomplete\"])] |
|                                                                                                                                                                                                                               |
| [.RequestMapper([\"Home/GetData\"])]                                                                                                                              |
|                                                                                                                                                                                                                               |
| **[.WaterMark([\"Enter any keyword\"])]**[%\>]                                                            |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View\[cshtml\]]**                                                                                                                                                                      |
|                                                                                                                                                                                                                               |
| [\@{][ ][Html.AutocompleteTextBox([\"myAutocomplete\"])] |
|                                                                                                                                                                                                                               |
| [.RequestMapper([\"Home/GetData\"])]                                                                                                                              |
|                                                                                                                                                                                                                               |
| **[.WaterMark([\"Enter any keyword\"]).Render();]**[}]                                                    |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

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

3.   Build and run the application.

**[]** 

 

 

Using Properties Model

The following steps explain the setting of watermark text for an auto-complete textbox through the Properties model.

1.   In the Controller, create an instance of **AutoCompleteTextBoxModel**, define the **WaterMark** property and pass the instance through **View Specific Data** to **View** as shown below.

 

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
| [            myModel.WaterMark = [\"Enter any keyword\"];]                                                                          |
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

2.   In **View**, invoke the auto-complete textbox helper with the **View data** key as the control id.

 

 

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

[] 

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

3.   In the **Controller**, define the post action from which the auto-complete textbox requests the data source.

 

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

4.   Build and run the application.

The output is shown in the following screenshot.

 

{border="0"}

Figure 75: Auto-complete with watermark text

 

 

[]{#related-topics}

