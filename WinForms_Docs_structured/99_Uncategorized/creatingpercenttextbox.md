---
title: creatingpercenttextbox.md
original_path: WinForms_Docs/99_Uncategorized/creatingpercenttextbox.md
created_at: 2025-08-05
---






##### Creating PercentTextBox {#creating-percenttextbox style="tab-stops: 0pt"}

 

The PercentTextBox control can be created at design time and can be created programmatically. This has been discussed in the following topics.

 

###### 5.1.2.6.1.1 Through Designer {#through-designer style="tab-stops: 0pt"}

[] 

You can create PercentTextBox using the designer as follows:

[] 

1.   Create a new ASP.NET Web application. For details, see [Creating ASP.NET Web Application]{.UGHyperlink}.

2.   Drag the **PercentTextBox** control onto your page from the controls toolbox.

[] 

{border="0"}

[] 

Figure 69: PercentTextBox control in Toolbox

[] 

3.   Customize the look and feel settings and the behavior and culture settings of the control as required. For details, see [Concepts and Features]{.UGHyperlink}.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\<][ssw][:][PercentTextBox][ [ID][=\"PercentTextBox1\"] [runat][=\"server\"] [/\>]] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The figure below shows PercentTextBox in design mode.

[] 

{border="0"}

[] 

Figure 70: PercentTextBox created Through Designer

[]{#p106} 

###### 5.1.2.6.1.2 Through Code {#through-code style="tab-stops: 0pt"}

[] 

This tutorial shows how to create a PercentTextBox entirely with code.

[] 

To create a PercentTextBox in ASP.NET code:

[] 

1.   Add a new web form to your project.

2.   In .cs file, include the following directives.

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

3.   In code view, the control has to be instantiated and added as follows.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                 |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                              |
|                                                                                                                                                                                                                                  |
| [protected][ Syncfusion.Web.UI.WebControls.Tools.PercentTextBox percenttextbox1;]                           |
|                                                                                                                                                                                                                                  |
| [        ]                                                                                                                                                                   |
|                                                                                                                                                                                                                                  |
| [private][ [void] Page_Init([object] sender, System.EventArgs e)] |
|                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [      BuildPercentTextbox();]                                                                                                                                               |
|                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [              ]                                                                                                                                                             |
|                                                                                                                                                                                                                                  |
| [public][ [void] BuildPercentTextbox()]                                                |
|                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [    [PercentTextBox].RegisterResourceFiles([this].Page);]                                                                         |
|                                                                                                                                                                                                                                  |
| [     [//Create an instance of the PercentTextBox]]                                                                                                  |
|                                                                                                                                                                                                                                  |
| [    percenttextbox1 = [new] [PercentTextBox]();]                                                                                  |
|                                                                                                                                                                                                                                  |
| [     //ID of the Percent TextBox]                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [     percenttextbox1.ID = \"PercentTextBox1\";]                                                                                                                             |
|                                                                                                                                                                                                                                  |
| [    [form1].Controls.Add(percenttextbox1);]                                                                                                            |
|                                                                                                                                                                                                                                  |
| [}[  ]]                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Private][ percenttextbox1 [As] Syncfusion.Web.UI.WebControls.Tools.PercentTextBox]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Private][ [Sub] Page_Init([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs) [Handles] [MyBase].Load] |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [      \'Put user code to initialize the page here]                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [      BuildPercentTextbox()]                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [End][ [Sub]]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Public][ [Sub] BuildPercentTextbox()]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [    PercentTextBox.RegisterResourceFiles([Me].Page)]                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [    \'Create an instance of the PercentTextBox]                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [    [Private] percenttextbox1 [As] PercentTextBox = [New] PercentTextBox()]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [    \'ID of the Percent TextBox]                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [    percenttextbox1.ID = \"PercentTextBox1\"]                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [    form1.Controls.Add(percenttextbox1)]                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [End][ [Sub ]]                                                                                                                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Build the project and view PercentTextBox in the browser.

[] 


{border="0"}Note: Refer [Concepts and Features]{.UGHyperlink} to know about the various features of the control.


 

[]{#related-topics}

