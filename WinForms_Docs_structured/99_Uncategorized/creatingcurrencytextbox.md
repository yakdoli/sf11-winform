---
title: creatingcurrencytextbox.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\creatingcurrencytextbox.md
created_at: 2025-07-03
---






##### Creating CurrencyTextBox {#creating-currencytextbox style="tab-stops: 0pt"}

 

This section illustrates how to create the CurrencyTextBox control through designer and programmatically.

 

###### []{#_Through_Designer_1}5.1.2.1.1.1 Through Designer {#through-designer style="tab-stops: 0pt"}

[] 

You can create a CurrencyTextBox in the designer as follows.

[] 

1.   Create a new ASP.NET Web application. For details, see [Creating ASP.NET Web Application]{.UGHyperlink}.

2.   Drag the CurrencyTextBox control onto your page from the controls toolbox.

3.   Customize the look and feel settings and the behavior and culture settings of the control as required. For details, see [Concepts and Features]{.UGHyperlink}.

4.      

[] 

{border="0"}

[] 

Figure 35: CurrencyTextBox control in Toolbox

[] 

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][ssw][:][CurrencyTextBox][ [ID][=\"CurrencyTextBox1\"] [runat][=\"server\"] [/\>]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The figure below shows CurrencyTextBox in design mode.

[] 

{border="0"}

[] 

Figure 36: CurrencyTextBox in Designer View

[] 

See Also

[] 

[Through Code]{.UGHyperlink}[]{.UGHyperlink}

 

###### []{#_Through_Code_1}5.1.2.1.1.2 Through Code {#through-code style="tab-stops: 0pt"}

[] 

This tutorial shows how to create CurrencyTextBox entirely with code.

To create a CurrencyTextBox in ASP.NET code, follow the below given steps.

[] 

1.   Add a new **Web Form** to your project.

2.   In .cs file, include the following directives.

3.      

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                    |
|                                                                                                                                                                     |
| **[]**                                                                                                          |
|                                                                                                                                                                     |
| [using][ Syncfusion.Web.UI.WebControls.Tools;] |
|                                                                                                                                                                     |
| [using][ Syncfusion.Web.UI;]                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                     |
|                                                                                                                                                                      |
| **[]**                                                                                                           |
|                                                                                                                                                                      |
| [Imports][ Syncfusion.Web.UI.WebControls.Tools] |
|                                                                                                                                                                      |
| [Imports][ Syncfusion.Web.UI]                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   In code view, the control has to be instantiated and created as follows.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\] ]**                                                                                                                                                  |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                              |
|                                                                                                                                                                                                                                  |
| [protected][ Syncfusion.Web.UI.WebControls.Tools.CurrencyTextBox Currencytextbox1;]                         |
|                                                                                                                                                                                                                                  |
| [        ]                                                                                                                                                                   |
|                                                                                                                                                                                                                                  |
| [private][ [void] Page_Init([object] sender, System.EventArgs e)] |
|                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [   BuildCurrencyTextbox();]                                                                                                                                                 |
|                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [                ]                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [public][ [void] BuildCurrencyTextbox()]                                               |
|                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [   //Create an instance of the CurrencyTextBox]                                                                                                             |
|                                                                                                                                                                                                                                  |
| [   Currencytextbox1 = [new] CurrencyTextBox();]                                                                                                        |
|                                                                                                                                                                                                                                  |
| [   //ID of the Currency TextBox]                                                                                                                            |
|                                                                                                                                                                                                                                  |
| [   Currencytextbox1.ID = \"CurrencyTextBox1\";]                                                                                                                             |
|                                                                                                                                                                                                                                  |
| [   [form1].Controls.Add(Currencytextbox1);]                                                                                                            |
|                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Private][ Currencytextbox1 [As] Syncfusion.Web.UI.WebControls.Tools.CurrencyTextBox]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Private][ [Sub] Page_Init([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs) [Handles] [MyBase].Load] |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [    [\'Put user code to initialize the page here]]                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [    BuildCurrencyTextbox()]                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [End][ [Sub]]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Public][ [Sub] BuildCurrencyTextbox()]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [    [\'Create an instance of the CurrencyTextBox]]                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [    Currencytextbox1 = [New] CurrencyTextBox()]                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [    [\'ID of the Currency TextBox]]                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [    Currencytextbox1.ID = [\"CurrencyTextBox1\"]]                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [    form1.Controls.Add(Currencytextbox1)]                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [End][ [Sub]]                                                                                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Build and run the project to view the output.

[] 

See Also

[[Through Designer]{.UGHyperlink}]()[]{.UGHyperlink}

 

[]{#related-topics}

