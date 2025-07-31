---
title: highlighttext.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\highlighttext.md
created_at: 2025-07-03
---






#### Highlight Text {#highlight-text style="tab-stops: 0pt"}

This feature allows us to highlight the search text in an AutoComplete suggestion list. It will highlight all the search text contained in the suggestion list.

 

Use Case Scenarios

This feature allows you to highlight the search text in an AutoComplete suggestion list.

The suggestion list will appear with the search text it contains highlighted. You can customize the highlighted text CSS using the **HighlightTextCss** property.

Properties

  ---------------------- -------------------------------------------------------- ------------- -------------------- ----------------------
  **Property**           **Description**                                          **Type**      **Data Type**        **Reference links**
  HighlightTypedString   This will highlight the typed text in suggestion list.   Server side   Binary, true/false   NA
  HighlightTextCss       The CssClass applied to HighlightTypedString.            Server side   String               HighlightTypedString
  ---------------------- -------------------------------------------------------- ------------- -------------------- ----------------------

[] 

Sample Link

To view a sample:

1.   Open the Essential Tools sample browser from the dashboard. Refer to the Samples and Location chapter.

2.   Navigate to **Tools.MVC** \> **AutoComplete Textbox** \> **Customization**[]

[] 

Adding Highlight to an Application

Using AutocompleteTextBoxBuilder

To highlight the searched text in the AutoComplete suggestion list using AutoCompleteBuilder:

1.   Create a **view**.

2.   In the **view**, invoke the **AutocompleteTextBox** helper with the control ID.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Style]**                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                |
| [\<][style][\>][] |
|                                                                                                                                                                                                                                                                |
| [.CustomHighlightQueryText][]                                                                                                                 |
|                                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                |
| [    [background-color]:[Yellow];]                                                                                                                                   |
|                                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                |
| [\</][style][\>]                                                   |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

3.   Set **HighlightTypedString** to **true** and **HighlightTextCss** to the CSS class name**.**

 

 


+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<%][=][Html.Syncfusion().AutocompleteTextBox([\"myAutocomplete\"]).RequestMapper([\"GetData\"]).HighlightTypedString([true]).HighlightTextCss([\"CustomHighlightQueryText\"])] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [%\>][]                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 


+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [@][Html.Syncfusion().AutocompleteTextBox([\"myAutocomplete\"]).RequestMapper([\"GetData\"]).HighlightTypedString([true]). HighlightTextCss([\"CustomHighlightQueryText\"])][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 


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

Figure 67: AutoComplete---Highlighted Search Text

 

Using AutocompleteTextBoxModel

To highlight the search text in the AutoComplete suggestion list by using AutocompleteTextBoxModel:

1.  In the **controller**, create an object for the **AutocompleteTextBoxModel** class.

2.   Set the **HighlightTypedString** as **true** and the **HighlightTextCss** to the CSS class name**.**


+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller][]**                                                                                                                   |
|                                                                                                                                                                                                              |
| [        [public] [ActionResult] Index()]                                                                      |
|                                                                                                                                                                                                              |
| [        {]                                                                                                                                                 |
|                                                                                                                                                                                                              |
| [            [AutocompleteTextBoxModel] myModel = [new] [AutocompleteTextBoxModel]();] |
|                                                                                                                                                                                                              |
| [            myModel.HighlightTypedString = [true]; ]                                                                                  |
|                                                                                                                                                                                                              |
| [            myModel.RequestMapper = [\"GetData\"];]                                                                                |
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
| []                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


**[]** 

3.   Create a **view**.

4.   In the **view**, invoke the **AutocompleteTextBox** helper with the control ID.

5.   From the **ViewData**, assign the **AutocompleteTextBoxModel** class to the **AutocompleteTextBox** helper.


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

6.   Build and run the application.

{border="0"}  

Figure 68: AutoComplete---Highlighted Search Text

 

[]{#related-topics}

