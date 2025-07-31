---
title: highlightindexitem.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\highlightindexitem.md
created_at: 2025-07-03
---






#### Highlight Index Item {#highlight-index-item style="tab-stops: 0pt"}

This feature allows you to highlight an item in the suggestion list when it appears.

Use Case Scenarios

This highlighted text will appear in the AutoComplete text box.

You can use it in the case of selecting the first option.

Properties

  -------------------- -------------------------------------------------- ------------- ---------------
  **Property**         **Description**                                    **Type**      **Data Type**
  HighlightItemIndex   Highlights the given index in a suggestion list.   Server side   Int
  -------------------- -------------------------------------------------- ------------- ---------------

[] 

Sample Link

To view a sample:

1.   Open the Tools Sample Browser from the dashboard. Refer to the Samples and Location chapter.

2.   Navigate to **Tools.MVC \> AutoComplete Textbox \> Customization**.[]

[] 

Adding Highlight Index Item to an Application

Using AutocompleteTextBoxBuilder

To highlight an item in the AutoComplete suggestion list by using AutoCompleteBuilder:

1.   Create a **view**.

2.   In the **view**, invoke the **AutocompleteTextBox** helper with the control ID.

3.   Set the integer value to denote the list index for **HighlightItemIndex.**


+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                              |
| [\<%][=][Html.Syncfusion().AutocompleteTextBox([\"myAutocomplete\"]).RequestMapper([\"GetData\"]).HighlightItemIndex(2)] |
|                                                                                                                                                                                                                                                                                                                                                              |
| [%\>][]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 


+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                              |
| [@][Html.Syncfusion().AutocompleteTextBox([\"myAutocomplete\"]).RequestMapper([\"GetData\"]).HighlightItemIndex(2)] |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 


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
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

 

4.   Build and run the application.

{border="0"}

Figure 69: AutoComplete---Highlight Index Item

 

Using AutocompleteTextBoxModel

To highlight an item in the AutoComplete suggestion list by using AutocompleteTextBoxModel:

1.   In the **controller**, create an object for the **AutocompleteTextBoxModel** class. Set the integer value to denote the list index for **HighlightItemIndex.**

 


+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [      **\[Controller\]**]                                                                                                                                               |
|                                                                                                                                                                                                              |
| [        [public] [ActionResult] Index()]                                                                      |
|                                                                                                                                                                                                              |
| [        {]                                                                                                                                                 |
|                                                                                                                                                                                                              |
| [            [AutocompleteTextBoxModel] myModel = [new] [AutocompleteTextBoxModel]();] |
|                                                                                                                                                                                                              |
| [            myModel.HighlightItemIndex = 2; ]                                                                                                              |
|                                                                                                                                                                                                              |
| [            myModel.RequestMapper = [\"GetData\"];]                                                                                |
|                                                                                                                                                                                                              |
| [            ViewData\[[\"myAutocomplete\"]\] = myModel;]                                                                           |
|                                                                                                                                                                                                              |
| [            [return] View();]                                                                                                         |
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
| [                             [select] suggestion.CustomerID;]                                                                         |
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
| []                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


**[]** 

2.   Create a **view**.

3.   In the **view**, invoke the **AutocompleteTextBox** helper with the control ID.

4.   From the **ViewData**, assign the **AutocompleteTextBoxModel** class to the **AutocompleteTextBox** helper.


+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| [\<%][=][Html.Syncfusion().AutocompleteTextBox([\"myAutocomplete\"])][%\>][] |
|                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 


+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                                      |
|                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                               |
|                                                                                                                                                                                                                                          |
| [@][ Html.Syncfusion().AutocompleteTextBox([\"myAutocomplete\"])][] |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

5.   Build and run the application.

{border="0"}  

Figure 70: AutoComplete---Highlight Index Item

 

[]{#related-topics}

