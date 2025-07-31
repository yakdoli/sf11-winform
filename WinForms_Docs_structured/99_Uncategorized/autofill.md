---
title: autofill.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\autofill.md
created_at: 2025-07-03
---






#### AutoFill {#autofill style="tab-stops: 0pt"}

The AutocompleteTextBox control offers an AutoFill option. This feature can be used to automatically fill the item when text is entered. The first Item in the suggestion list will automatically display in an AutoComplete text box. The search text will be selected in the AutoComplete text box for identification.

Use Case Scenarios

This feature allows you to fill the first item in an AutoComplete text box.

This feature reduces the need to type the entire text.

Properties

+------------------------------------+------------------------------------------------------------------+----------------------------------------+----------------------------------------------+
| **Property**                       | **Description**                                                  | **Type**                               | **Data Type**                                |
+------------------------------------+------------------------------------------------------------------+----------------------------------------+----------------------------------------------+
| AutoFill[] | Gives the functionality to auto select the first suggested item. | Server-side [] | Binary, true/false[] |
|                                    |                                                                  |                                        |                                              |
|                                    | By default the value is false.[]         |                                        |                                              |
+------------------------------------+------------------------------------------------------------------+----------------------------------------+----------------------------------------------+

[] 

Sample Link

To view a sample:

1.   Open the Essential Tools sample browser from the dashboard. Refer to the Samples and Location chapter.

2.   Navigate to **Tools.MVC** \> **AutoComplete Textbox** \> **Customization**[]

 

Adding AutoFill to an Application

Using AutocompleteTextBoxBuilder

Add the AutoFill option to an AutoComplete text box by using AutocompleteTextBoxBuilder:

1.   Create a **view**.

2.   In the **view**, invoke the **AutocompleteTextBox** helper with the control ID.

3.   Set **AutoFill** to **true**.


+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                              |
| [\<%][=][Html.Syncfusion().AutocompleteTextBox([\"myAutocomplete\"]).RequestMapper([\"GetData\"]).AutoFill([true])] |
|                                                                                                                                                                                                                                                                                                                                                                              |
| [%\>][]                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 


+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                        |
| [@][Html.Syncfusion().AutocompleteTextBox([\"myAutocomplete\"]).RequestMapper([\"GetData\"])] |
|                                                                                                                                                                                                                                                        |
| [.AutoFill([true])][           ]                                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 


+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                      |
|                                                                                                                                                                                           |
| [        [public] [ActionResult] Index()]                                                   |
|                                                                                                                                                                                           |
| [        {]                                                                                                                              |
|                                                                                                                                                                                           |
| [            [return] View();]                                                                                      |
|                                                                                                                                                                                           |
| [        }]                                                                                                                              |
|                                                                                                                                                                                           |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                            |
|                                                                                                                                                                                           |
| [        [public] [ActionResult] GetData([string] QueryString)]        |
|                                                                                                                                                                                           |
| [        {]                                                                                                                              |
|                                                                                                                                                                                           |
| [            [Northwind] context = SqlCE;]                                                                       |
|                                                                                                                                                                                           |
| [            [var] dataSource = [from] suggestion [in] context.Customers] |
|                                                                                                                                                                                           |
| [                             [select] suggestion.CustomerID;]                                                      |
|                                                                                                                                                                                           |
| []                                                                                                                                       |
|                                                                                                                                                                                           |
| []                                                                                                                                       |
|                                                                                                                                                                                           |
| [            [ActionResult] jsonResult = dataSource.AutocompleteActionResult();]                                 |
|                                                                                                                                                                                           |
| [            [return] jsonResult;]                                                                                  |
|                                                                                                                                                                                           |
| [        }]                                                                                                                              |
|                                                                                                                                                                                           |
| []                                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

 

4.   Build and run the application.

{border="0"}

Figure 63: AutoComplete---AutoFill

 

Using AutoCompleteModel

Add the AutoFill option in an AutoComplete text box by using AutocompleteTextBoxModel:

1.   In the **controller**, create an object for the **AutocompleteTextBoxModel** class.

2.   Set the **AutoFill** property as **True**.

3.   Pass the **AutocompleteTextBoxModel** class to the **ViewData**.

 


+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [      **\[Controller\]**]                                                                                                                                               |
|                                                                                                                                                                                                              |
| [        [public] [ActionResult] Index()]                                                                      |
|                                                                                                                                                                                                              |
| [        {]                                                                                                                                                 |
|                                                                                                                                                                                                              |
| [            [AutocompleteTextBoxModel] myModel = [new] [AutocompleteTextBoxModel]();] |
|                                                                                                                                                                                                              |
| [            myModel.AutoFill = [true]; ]                                                                                              |
|                                                                                                                                                                                                              |
| [            myModel. RequestMapper = [\"GetData\"];]                                                                               |
|                                                                                                                                                                                                              |
| [            ViewData\[[\"myAutocomplete\"]\] = myModel;]                                                                           |
|                                                                                                                                                                                                              |
| [            [return] View();]                                                                                                         |
|                                                                                                                                                                                                              |
| [        }]                                                                                                                                                 |
|                                                                                                                                                                                                              |
| []                                                                                                                                                          |
|                                                                                                                                                                                                              |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                                               |
|                                                                                                                                                                                                              |
| [        [public] [ActionResult] GetData([string] QueryString)]                           |
|                                                                                                                                                                                                              |
| [        {]                                                                                                                                                 |
|                                                                                                                                                                                                              |
| [            [Northwind] context = SqlCE;]                                                                                          |
|                                                                                                                                                                                                              |
| [            [var] dataSource = [from] suggestion [in] context.Customers]                    |
|                                                                                                                                                                                                              |
| [                             [select] suggestion.CustomerID;]                                                                         |
|                                                                                                                                                                                                              |
| []                                                                                                                                                          |
|                                                                                                                                                                                                              |
| []                                                                                                                                                          |
|                                                                                                                                                                                                              |
| [            [ActionResult] jsonResult = dataSource.AutocompleteActionResult();]                                                    |
|                                                                                                                                                                                                              |
| [            [return] jsonResult;]                                                                                                     |
|                                                                                                                                                                                                              |
| [        }]                                                                                                                                                 |
|                                                                                                                                                                                                              |
| []                                                                                                                                                          |
|                                                                                                                                                                                                              |
| []                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


**[]** 

4.   Create a **view**.

5.   In the **view**, invoke the **AutocompleteTextBox** helper with the control ID.

6.   From the **ViewData**, assign the **AutocompleteTextBoxModel** class to the **AutocompleteTextBox** helper.


+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<%][=][Html.Syncfusion().AutocompleteTextBox([\"myAutocomplete\"])][%\>][] |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 


+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                              |
|                                                                                                                                                                                                                                         |
| [@][Html.Syncfusion().AutocompleteTextBox([\"myAutocomplete\"])][] |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 


+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                              |
|                                                                                                                                                                                                   |
| [        [public] [ActionResult] Index([AutocompleteTextBoxModel] myModel)] |
|                                                                                                                                                                                                   |
| [        {]                                                                                                                                      |
|                                                                                                                                                                                                   |
| []                                                                                                                                               |
|                                                                                                                                                                                                   |
| [            myModel.RequestMapper = [\"GetData\"];]                                                                     |
|                                                                                                                                                                                                   |
| [            ViewData\[[\"myAutocomplete\"]\] = myModel;]                                                                |
|                                                                                                                                                                                                   |
| [            [return] View();]                                                                                              |
|                                                                                                                                                                                                   |
| [        }]                                                                                                                                      |
|                                                                                                                                                                                                   |
| [        \[[AcceptVerbs]([HttpVerbs].Post)\]]                                                    |
|                                                                                                                                                                                                   |
| [        [public] [ActionResult] GetData([string] QueryString)]                |
|                                                                                                                                                                                                   |
| [        {]                                                                                                                                      |
|                                                                                                                                                                                                   |
| [            [Northwind] context = SqlCE;]                                                                               |
|                                                                                                                                                                                                   |
| [            [var] dataSource = [from] suggestion [in] context.Customers]         |
|                                                                                                                                                                                                   |
| [                             [select] suggestion.CustomerID;]                                                              |
|                                                                                                                                                                                                   |
| []                                                                                                                                               |
|                                                                                                                                                                                                   |
| []                                                                                                                                               |
|                                                                                                                                                                                                   |
| [            [ActionResult] jsonResult = dataSource.AutocompleteActionResult();]                                         |
|                                                                                                                                                                                                   |
| [            [return] jsonResult;]                                                                                          |
|                                                                                                                                                                                                   |
| [        }]                                                                                                                                      |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

[] 

7.   Build and run the application.

{border="0"}  

Figure 64: AutoComplete---AutoFill

[]{#related-topics}

