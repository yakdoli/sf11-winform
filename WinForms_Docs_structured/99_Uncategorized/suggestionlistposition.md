---
title: suggestionlistposition.md
original_path: WinForms_Docs/99_Uncategorized/suggestionlistposition.md
created_at: 2025-08-05
---






#### Suggestion List Position {#suggestion-list-position style="tab-stops: 0pt"}

This feature gives support to change the suggestion list position by specifying X and Y values.

Use Case Scenarios

You can change the suggestion list position.

[] 

Properties

+-----------------+------------------------------------------------------+-----------------+-----------------+
| **Property**    | **Description**                                      | **Type**        | **Data Type**   |
+-----------------+------------------------------------------------------+-----------------+-----------------+
| ListPosition    | Displays the suggestion list in given X, Y Position. | Server side     | Point           |
|                 |                                                      |                 |                 |
|                 |                                                      |                 |                 |
+-----------------+------------------------------------------------------+-----------------+-----------------+

Sample Link

To view a sample:

1.   Open the Essential Tools sample browser from the dashboard. Refer to the Samples and Location chapter.

2.   Navigate to **Tools.MVC \> AutoComplete Textbox \> Customization**.[]

 

Adding List Position to an Application

Using AutocompleteTextBoxBuilder

To change the suggestion list position by using AutoCompleteBuilder:

1.   Create a **view**.

2.   In the **view**, invoke the **AutocompleteTextBox** helper with the control ID.

3.   Set the point values for **ListPosition.**


+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<%][=][Html.Syncfusion().AutocompleteTextBox([\"myAutocomplete\"]).RequestMapper([\"GetData\"]).ListPosition([new] System.Drawing.[Point](100,200))][%\>][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 


+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                    |
| [@][ ]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                    |
| [Html.Syncfusion().AutocompleteTextBox([\"myAutocomplete\"]).RequestMapper([\"GetData\"]).ListPosition([new] System.Drawing.[Point](100,200))][] |
|                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 


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

Figure 71: AutoComplete---ListPosition

 

Using AutocompleteTextBoxModel

To change the suggestion list position by using AutocompleteTextBoxModel:

1.   In the **controller**, create an object for the **AutocompleteTextBoxModel** class.

2.   Set the point values for **ListPosition**.

 


+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller][]**                                                                                                                   |
|                                                                                                                                                                                                              |
| [        [public] [ActionResult] Index()]                                                                      |
|                                                                                                                                                                                                              |
| [        {]                                                                                                                                                 |
|                                                                                                                                                                                                              |
| [            [AutocompleteTextBoxModel] myModel = [new] [AutocompleteTextBoxModel]();] |
|                                                                                                                                                                                                              |
| [            myModel.ListPosition = [new] System.Drawing.[Point](100,200); ]                                   |
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


 


+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                              |
|                                                                                                                                                                                                                                         |
| [@][Html.Syncfusion().AutocompleteTextBox([\"myAutocomplete\"])][] |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


[] 

6.   Build and run the application.

{border="0"}  

Figure 72: AutoComplete---ListPosition

 

[]{#related-topics}

