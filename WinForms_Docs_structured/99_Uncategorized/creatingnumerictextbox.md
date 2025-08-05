---
title: creatingnumerictextbox.md
original_path: WinForms_Docs/99_Uncategorized/creatingnumerictextbox.md
created_at: 2025-08-05
---






##### Creating NumericTextBox {#creating-numerictextbox style="tab-stops: 0pt"}

 

The NumericTextBox control can be created at design time and can be created programmatically, which has been discussed in the following topics.

 

###### 5.1.2.5.1.1 Through Designer {#through-designer style="tab-stops: 0pt"}

[] 

You can create the NumericTextBox using the designer as follows.

[] 

1.   Create a new ASP.NET Web application. For details, see [Creating ASP.NET Web Application]{.UGHyperlink}.

2.   Drag the NumericTextBox control onto your page from the controls toolbox.

[] 

{border="0"}

***[]*** 

Figure 63: NumericTextBox control in Toolbox

**[]** 

3.   Customize the look and feel settings and the behavior and culture settings of the control as required. For details, see [Concepts and Features]{.UGHyperlink}.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\<][ssw][:][NumericTextBox][ [ID][=\"NumericTextBox1\"] [runat][=\"server\"] [/\>]] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The figure below shows NumericTextBox in design mode.

[] 

{border="0"}

***[]*** 

Figure 64: NumericTextBox created Through Designer

 

###### 5.1.2.5.1.2 Through Code {#through-code style="tab-stops: 0pt"}

[] 

This tutorial shows how to create NumericTextBox entirely with code.

To create NumericTextBox in ASP.NET code, follow the below given steps.

[] 

1.   In .cs file of the project, include the following directives.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                    |
|                                                                                                                                                                     |
| []                                                                                                 |
|                                                                                                                                                                     |
| [using][ Syncfusion.Web.UI.WebControls.Tools;] |
|                                                                                                                                                                     |
| [using][ Syncfusion.Web.UI;]                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                     |
|                                                                                                                                                                      |
| []                                                                                                  |
|                                                                                                                                                                      |
| [Imports][ Syncfusion.Web.UI.WebControls.Tools] |
|                                                                                                                                                                      |
| [Imports][ Syncfusion.Web.UI]                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In code view, the control has to instantiated and added as follows.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                   |
|                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                         |
|                                                                                                                                                                                                                                  |
| [private][ Syncfusion.Web.UI.WebControls.Tools.NumericTextBox numerictextbox1;]                             |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [private][ [void] Page_Init([object] sender, System.EventArgs e)] |
|                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [     BuildNumericTextbox();]                                                                                                                                                |
|                                                                                                                                                                                                                                  |
| [}        ]                                                                                                                                                                  |
|                                                                                                                                                                                                                                  |
| [public][ [void] BuildNumericTextbox()]                                                |
|                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [     //Create an instance of the Numeric TextBox control.]                                                                                                    |
|                                                                                                                                                                                                                                  |
| [     numerictextbox1 = [new] NumericTextBox();]                                                                                                        |
|                                                                                                                                                                                                                                  |
| [     numerictextbox1.ID=\"Numeric TextBox1\";]                                                                                                                              |
|                                                                                                                                                                                                                                  |
| [     numerictextbox1.Value=0.00;]                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [     [form1].Controls.Add(numerictextbox1);]                                                                                                           |
|                                                                                                                                                                                                                                  |
| [} ]                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\] ]**                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Private][ numerictextbox1 [As] Syncfusion.Web.UI.WebControls.Tools.NumericTextBox]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Private][ [Sub] Page_Init([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs) [Handles] [MyBase].Load] |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\'Put user code to initialize the page here]                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [BuildNumericTextbox()]                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [End][ [Sub]]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Public][ [Sub] BuildNumericTextbox()]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\'Create an instance of the Numeric TextBox control.]                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [numerictextbox1 = [New] NumericTextBox()]                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [numerictextbox1.ID=\"Numeric TextBox1\"]                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [numerictextbox1.Value=0.00]                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Me][.Controls.Add(numerictextbox1)]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [End][ [Sub]]                                                                                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Build the project and view **NumericTextBox** in the browser.

 

[]{#related-topics}

