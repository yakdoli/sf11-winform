---
title: clientsidemethods18.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clientsidemethods18.md
created_at: 2025-07-03
---






#### Client-Side Methods {#client-side-methods style="tab-stops: 0pt"}

The client-side methods are used to do appropriate function on the client side. The **Enable** and **Disable** methods allow you to disable and enable the AutocompleteTextBox control.

Use Case Scenarios

You can able to disable the Autocomplete text box as well as the drop-down support.[]

 

Methods

  **[Method ]**[]   **[Description ]**[]    **[Parameters ]**[]   **[Type ]**[]   **[Return Type ]**[]
  ------------------------------------------------------------- ------------------------------------------------------------------- ----------------------------------------------------------------- ----------------------------------------------------------- ------------------------------------------------------------------
  Enable[]                              This method will Enable the AutoComplete Textbox if it is Disable   \-                                                                Client Side                                                 void
  Disable                                                       This method will Disable the AutoComplete Textbox if it is Enable   \-                                                                Client Side                                                 void

 

Sample Link

To view a sample:

3.   Open the Essential Tools sample browser from the dashboard. (Refer to the Samples and Location chapter).

4.   Navigate to **Tools.MVC** \> **AutoComplete Textbox** \> **Customization**.[]

 

Adding Client-Side Methods to an Application

To disable and enable AutoComplete TextBox by using AutoCompleteBuilder:

5.   Create a **view**.

6.   In the **view**, invoke the **AutocompleteTextBox** helper with the control ID.

7.   Use the methods in the **ButtonClick** event**.**

 


+------------------------------------------------------------------------------------------------------------------------------------+
| **[\[script\]]**                                                                               |
|                                                                                                                                    |
| **[]**                                                                                         |
|                                                                                                                                    |
| [    [function] Button1Click() {]                            |
|                                                                                                                                    |
| [        \$([\"#myAutocomplete\"])\[0\].control.Disable()] |
|                                                                                                                                    |
| [    }]                                                                           |
|                                                                                                                                    |
| **[]**                                                                                         |
|                                                                                                                                    |
| [    [function] Button1Click() {]                            |
|                                                                                                                                    |
| [        \$([\"#myAutocomplete\"])\[0\].control.Enable()]  |
|                                                                                                                                    |
| [    }]                                                                           |
|                                                                                                                                    |
| **[]**                                                                                         |
|                                                                                                                                    |
| []                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------+


 


+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<%][=][Html.Syncfusion().AutocompleteTextBox([\"myAutocomplete\"])][.][RequestMapper][([\"GetData\"])][%\>][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 


+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                              |
| [@][Html.Syncfusion().AutocompleteTextBox([\"myAutocomplete\"]).RequestMapper([\"GetData\"])][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 


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


 

 

8.   Build and run the application.

{border="0"}

Figure 80: AutoComplete---Disable

[]{#related-topics}

