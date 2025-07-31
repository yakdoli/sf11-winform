---
title: creatingdatetimetextbox.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\creatingdatetimetextbox.md
created_at: 2025-07-03
---






##### Creating DateTimeTextBox {#creating-datetimetextbox style="tab-stops: 0pt"}

 

The DateTimeTextBox control can be created at design time and can be created programmatically, which has been discussed in the following topics.

 

###### 5.1.2.2.1.1 Through Designer {#through-designer style="tab-stops: 0pt"}

[] 

You can create the DateTimeTextBox using the designer as follows.

[] 

1.   Create a new ASP.NET Web application. For details, see [Creating ASP.NET Web Application]{.UGHyperlink}.

2.   Drag the **DateTimeTextBox** control onto your page from the toolbox.

[] 

{border="0"}

***[]*** 

Figure 42: DateTimeTextBox Control in ToolBox

**[]** 

3.   Customize the look and feel settings and the behavior and culture settings of the control as required. For details, see [Concepts and Features]{.UGHyperlink}.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\<][ssw][:][DateTimeTextBox][ [ID][=\"DateTimeTextBox1\"] [runat][=\"server\"/\>]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The figure below shows DateTimeTextBox in design view.

[] 

{border="0"}

***[]*** 

Figure 43: DateTimeTextBox created Through Designer

 

###### 5.1.2.2.1.2 Through Code {#through-code style="tab-stops: 0pt"}

[] 

This tutorial shows how to create DateTimeTextBox entirely with code. To create DateTimeTextBox in ASP.NET code, follow the below given steps.

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

3.   In code view, the control should be instantiated and created as follows.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                 |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                              |
|                                                                                                                                                                                                                                  |
| [private][ [void] Page_Load([object] sender, System.EventArgs e)] |
|                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [   CreateDateTimeTextBox();]                                                                                                                                                |
|                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                              |
|                                                                                                                                                                                                                                  |
| [public][ [void] CreateDateTimeTextBox()]                                              |
|                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [    [//Create an instance of DateTimeTextBox]]                                                                                                        |
|                                                                                                                                                                                                                                  |
| [    DateTimeTextBox1  =[new] Syncfusion.Web.UI.WebControls.Tools.DateTimeTextBox ();]                                                                  |
|                                                                                                                                                                                                                                  |
| [    [// Indicates ID of the Control]]                                                                                                                 |
|                                                                                                                                                                                                                                  |
| [    DateTimeTextBox1.ID = [\"DateTimeTextBox1\"];]                                                                                                   |
|                                                                                                                                                                                                                                  |
| [    DateTimeTextBox1.Value = System.DateTime.Today;]                                                                                                                        |
|                                                                                                                                                                                                                                  |
| [    [form1].Controls.Add(DateTimeTextBox1);]                                                                                                           |
|                                                                                                                                                                                                                                  |
| [}[ ]]                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\] ]**                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                               |
| [Private][ [Sub] Page_Load([ByVal] sender [As] [Object], [ByVal] e [As] System.EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                               |
| [    CreateDateTimeTextBox()]                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                               |
| [End][ [Sub]]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                               |
| [Public][ [Sub] CreateDateTimeTextBox()]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                               |
| [    [\'Create an instance of DateTimeTextBox]]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                               |
| [    DateTimeTextBox1 = [New] Syncfusion.Web.UI.WebControls.Tools.DateTimeTextBox()]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                               |
| [    [\' Indicates ID of the Control]]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                               |
| [    DateTimeTextBox1.ID = [\"DateTimeTextBox1\"]]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                               |
| [    DateTimeTextBox1.Value = System.DateTime.Today]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                               |
| [    form1.Controls.Add(DateTimeTextBox1)]                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                               |
| [End][ [Sub ]][ ]                                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Build the project and view the **DateTimeTextBox** in the browser.

 

[]{#related-topics}

