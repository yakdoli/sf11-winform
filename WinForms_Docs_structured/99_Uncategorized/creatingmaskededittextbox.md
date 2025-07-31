---
title: creatingmaskededittextbox.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\creatingmaskededittextbox.md
created_at: 2025-07-03
---






##### Creating MaskedEditTextBox {#creating-maskededittextbox style="tab-stops: 0pt"}

 

The MaskedEditTextBox control can be created at design time and can be created programmatically, which has been discussed in the following topics.

 

###### 5.1.2.4.1.1 Through Designer {#through-designer style="tab-stops: 0pt"}

[] 

You can create the MaskedEditTextBox using the designer as follows.

[] 

1.   Create a new ASP.NET Web application. For details, see [Creating ASP.NET Web Application]{.UGHyperlink}[.]{.UGHyperlink}

2.   Drag the **MaskedEditTextBox** control onto your page from the controls toolbox.

3\.

[] 

{border="0"}

***[]*** 

Figure 59: MaskedEditTextBox Control in Toolbox

[] 

4.   Customize the look and feel settings, the behavior and culture settings of the control as required. For details, see [Concepts and Features]{.UGHyperlink}.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\<][ssw][:][MaskedEditTextBox][ [ID][=\"MaskedEditTextBox1\"] [runat][=\"server\"] [/\>]] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The figure below shows MaskedEditTextBox in design view.

[] 

{border="0"}

 

Figure 60: MaskedEditTextBox created Through Designer

 

###### []{#_Through_Code}5.1.2.4.1.2 Through Code {#through-code style="tab-stops: 0pt"}

[] 

This tutorial shows how to create MaskedEditTextBox entirely with code.

To create MaskedEditTextBox in ASP.NET code, follow the below given steps.

[] 

1.   Add a new Web Form to your project.

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

3.   In code view, the control has to instantiated and added as follows.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                   |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                             |
|                                                                                                                                                                                                                                  |
| [private][ Syncfusion.Web.UI.WebControls.Tools.MaskedEditTextBox maskededittextbox1;]                       |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [private][ [void] Page_Init([object] sender, System.EventArgs e)] |
|                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [    buildMaskedTextbox();]                                                                                                                                                  |
|                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [                ]                                                                                                                                                           |
|                                                                                                                                                                                                                                  |
| [public][ [void] buildMaskedTextbox()]                                                 |
|                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [                        ]                                                                                                                                                   |
|                                                                                                                                                                                                                                  |
| [    //Create an instance of the MaskedEditTextBox control.]                                                                                                   |
|                                                                                                                                                                                                                                  |
| [    maskededittextbox1=[new] MaskedEditTextBox();]                                                                                                     |
|                                                                                                                                                                                                                                  |
| [    form1.Controls.Add(maskededittextbox1);]                                                                                                                                |
|                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Private][ maskededittextbox1 [As] Syncfusion.Web.UI.WebControls.Tools.MaskedEditTextBox]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Private][ [Sub] Page_Init([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs) [Handles] [MyBase].Load] |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [End][ [Sub]]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Public][ [Sub] buildMaskedTextbox()]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [    [\'Create an instance of the MaskedEditTextBox control.]]                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [    maskededittextbox1 = [New] MaskedEditTextBox()]                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [    form1.Controls.Add(maskededittextbox1)]                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [End][ [Sub]]                                                                                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Build the project and view **MaskedEditTextBox** in the browser.

 

[]{#related-topics}

