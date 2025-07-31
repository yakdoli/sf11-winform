---
title: clientsidefiltering.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clientsidefiltering.md
created_at: 2025-07-03
---






#### Client-Side Filtering {#client-side-filtering style="tab-stops: 0pt"}

**Client data fetching** allows us to filter data without post actions. The AutoComplete filtering takes place on the client side; to achieve this functionality the data source should set to **AutocompleteTextBox**.

 

Use Case Scenarios

This feature will allow you to do client-side data fetching by giving the data to the AutoComplete text box on load.

This increases the performance without post actions.

Properties

+-------------------------------------+-------------------------------------------------------------+----------------------------------------+-----------------------------------------------------------------------------------+
| **Property**                        | **Description**                                             | **Type**                               | **Data Type**                                                                     |
+-------------------------------------+-------------------------------------------------------------+----------------------------------------+-----------------------------------------------------------------------------------+
| DataFetch[] | Specifies the client- or server-side data fetching.         | Server side [] | AutocompleteTextBoxModel. DataFetchList, Client/Server[ ] |
|                                     |                                                             |                                        |                                                                                   |
|                                     | The default value is server-side.[] |                                        |                                                                                   |
+-------------------------------------+-------------------------------------------------------------+----------------------------------------+-----------------------------------------------------------------------------------+
| DataSource                          | Specifies the IEnumerable data.                             | Server side                            | IEnumerable                                                                       |
|                                     |                                                             |                                        |                                                                                   |
|                                     |                                                             |                                        |                                                                                   |
+-------------------------------------+-------------------------------------------------------------+----------------------------------------+-----------------------------------------------------------------------------------+

[] 

Events

  **[Event ]**[]   **[Description ]**[]   **[Arguments ]**[]   **[Type ]**[]
  ------------------------------------------------------------ ------------------------------------------------------------------ ---------------------------------------------------------------- -----------------------------------------------------------
  ClientSideOnFiltering                                        This event will trigger on client-side data fetching.              String                                                           Client side

[][] 

Sample Link

To view a sample:

1.   Open the **Tools Sample Browser** from the dashboard. Refer to the Samples and Location chapter.

2.  Navigate to **Tools.MVC** \> **AutoComplete Textbox** \> **Client Side Data Filtering**.

 

Adding AutoComplete Client-Side Filtering to an Application

Using AutocompleteTextBoxBuilder

To fetch data on the client-side by using AutocompleteTextBoxBuilder:

1.   Create a strongly typed view.

2.   Set the **DataFetch** method with **DataFetchList** and the **DataSource** with **IEnumerable** data.

 


+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller][]**                                                                                                      |
|                                                                                                                                                                                                 |
| [        [public] [ActionResult] ClientDataFiltering()]                                           |
|                                                                                                                                                                                                 |
| [        {]                                                                                                                                    |
|                                                                                                                                                                                                 |
| [            [Northwind] context = SqlCE;]                                                                             |
|                                                                                                                                                                                                 |
| [            [IEnumerable] data =  [from] suggestion [in] context.Customers] |
|                                                                                                                                                                                                 |
| [                             [select] suggestion.CustomerID;]                                                            |
|                                                                                                                                                                                                 |
| []                                                                                                                                             |
|                                                                                                                                                                                                 |
| [            [return] View(data);]                                                                                        |
|                                                                                                                                                                                                 |
| [        }]                                                                                                                                    |
|                                                                                                                                                                                                 |
| []                                                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 


+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<%][=][Html.Syncfusion().AutocompleteTextBox([\"myAutocomplete\"]) .DataFetch([AutocompleteTextBoxModel].[DataFetchList].Client).DataSource(Model)] |
|                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [%\>][]                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 


+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [@][Html.Syncfusion().AutocompleteTextBox([\"myAutocomplete\"]) .DataFetch([AutocompleteTextBoxModel].[DataFetchList].Client).DataSource(Model)][ ] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

3.   Build and run the application.

{border="0"} 

Figure 65: AutoComplete---Client-side Data Fetching

 

Using AutocompleteTextBoxModel

To fetch data on the client-side by using AutocompleteTextBoxModel:

1.   In the **controller**, create an object for the **AutocompleteTextBoxModel** class.

2.   Set the **DataFetch** method with **DataFetchList** and the **DataSource** with **IEnumerable** data.

 


+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller][]**                                                                                                                   |
|                                                                                                                                                                                                              |
| [        [public] [ActionResult] ClientDataFiltering()]                                                        |
|                                                                                                                                                                                                              |
| [        {]                                                                                                                                                 |
|                                                                                                                                                                                                              |
| [            [AutocompleteTextBoxModel] myModel = [new] [AutocompleteTextBoxModel]();] |
|                                                                                                                                                                                                              |
| [            [Northwind] context = SqlCE;]                                                                                          |
|                                                                                                                                                                                                              |
| [            [var] dataSource = [from] suggestion [in] context.Customers]                    |
|                                                                                                                                                                                                              |
| [                             [select] suggestion.CustomerID;]                                                                         |
|                                                                                                                                                                                                              |
| [            myModel.DataFetch = [AutocompleteTextBoxModel].[DataFetchList].Client]                         |
|                                                                                                                                                                                                              |
| [            myModel.DataSource = dataSource;]                                                                                                              |
|                                                                                                                                                                                                              |
| [            ViewData\[[\"myAutocomplete\"]\] = myModel;]                                                                           |
|                                                                                                                                                                                                              |
| []                                                                                                                                                          |
|                                                                                                                                                                                                              |
| [            [return] View();]                                                                                                         |
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

Figure 66: AutoComplete TextBox---Client-Side Filtering

[]{#related-topics}

