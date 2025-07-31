---
title: creatingcomboboxbase.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\creatingcomboboxbase.md
created_at: 2025-07-03
---






##### Creating ComboBoxBase {#creating-comboboxbase style="tab-stops: 0pt"}

 

[]{#p410}ComboBoxBase can be created easily through designer, by just dragging and dropping the ComboBoxBase control from the Toolbox.

 

{border="0"}

***[]*** 

Figure 360: ComboBoxBase in Toolbox

[] 

[] 

{border="0"}

 

Figure 361**[: ComboBoxBase in Designer]**

**[]** 

To add data for the popup, add a listbox control to the form and select it in **ListControl** property.

[] 

{border="0"}

 

Figure 362: ListControl Property of ComboBoxBase

 

{border="0"}

***[]*** 

Figure 363: ComboBoxBase at Run Time

 

It can be created through code by following the below steps.

[] 

1.   Added Shared.Base to the reference folder through solution explorer and include the below namespace in the code.

[] 

+--------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                 |
|                                                                                                                                |
| []                                                                                                     |
|                                                                                                                                |
| [using ][Syncfusion.Windows.Forms.Tools;] |
+--------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                              |
|                                                                                                                                 |
| []                                                                                                      |
|                                                                                                                                 |
| [Imports][ Syncfusion.Windows.Forms.Tools] |
+---------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Create an instance of the ComboBoxBase control and ListBox.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                        |
|                                                                                                                                                                                       |
| []                                                                                                                                                            |
|                                                                                                                                                                                       |
| [private][ Syncfusion.Windows.Forms.Tools.ComboBoxBase comboBoxBase1;]                           |
|                                                                                                                                                                                       |
| [private][ System.Windows.Forms.ListBox listBox1;]                                               |
|                                                                                                                                                                                       |
| []                                                                                                                                                |
|                                                                                                                                                                                       |
| [this][.comboBoxBase1=[new] Syncfusion.Windows.Forms.Tools.ComboBoxBase();] |
|                                                                                                                                                                                       |
| [this][.listBox1=[new] ListBox();]                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                   |
|                                                                                                                                                                                      |
| []                                                                                                                                                           |
|                                                                                                                                                                                      |
| [Private][ comboBoxBase1 [As] Syncfusion.Windows.Forms.Tools.ComboBoxBase] |
|                                                                                                                                                                                      |
| [Private][ listBox1 [As] System.Windows.Forms.ListBox]                     |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [Me][.comboBoxBase1 = [New] Syncfusion.Windows.Forms.Tools.ComboBoxBase()] |
|                                                                                                                                                                                      |
| [Me][.listBox1 = [New] ListBox()]                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Set the ListControl that will be used in the dropdown portion of ComboBoxBase and specify the size of ComboBoxBase.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                |
|                                                                                                                                                               |
| []                                                                                                                                    |
|                                                                                                                                                               |
| [this][.comboBoxBase1.ListControl=[this].listBox1;] |
|                                                                                                                                                               |
| [this][.comboBoxBase1.Size=[new] Size(120,20);]     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                       |
|                                                                                                                                                          |
| []                                                                                                                               |
|                                                                                                                                                          |
| [Me][.comboBoxBase1.ListControl=[Me].listBox1] |
|                                                                                                                                                          |
| [Me][.comboBoxBase1.Size = [New] Size(120,20)] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Specify the datasource.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                             |
|                                                                                                                                                                                                            |
| **[]**                                                                                                                                                   |
|                                                                                                                                                                                                            |
| [// Sets the datasource.]                                                                                                                                |
|                                                                                                                                                                                                            |
| [ArrayList USStates = ][new][ ArrayList(); ]          |
|                                                                                                                                                                                                            |
| [\                                                                                                                                                                                                         |
| USStates.Add(][new][ USState(\"Washington\", \"WA\"));\                                                 |
| USStates.Add(][new][ USState(\"West Virginia\", \"WV\"));\                                              |
| USStates.Add(][new][ USState(\"Wisconsin\", \"WI\"));\                                                  |
| USStates.Add(][new][ USState(\"Wyoming\", \"WY\")); ] |
|                                                                                                                                                                                                            |
| [\                                                                                                                                                                                                         |
| ListBox1.DataSource = USStates; ]                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [\' Sets the datasource.]                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [Dim][ USStates ][As][ ArrayList = ][New][ ArrayList()] |
|                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [USStates.Add(][New][ USState(\"Washington\", \"WA\"))]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [USStates.Add(][New][ USState(\"West Virginia\", \"WV\"))]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [USStates.Add(][New][ USState(\"Wisconsin\", \"WI\"))]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [USStates.Add(][New][ USState(\"Wyoming\", \"WY\"))]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [ListBox1.DataSource = USStates]                                                                                                                                                                                                                                                                               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

5.   Finally add ComboBoxBase and Listbox to the Form.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                         |
|                                                                                                                                                        |
| []                                                                                                                             |
|                                                                                                                                                        |
| [this][.Controls.Add([this].listBox1);]      |
|                                                                                                                                                        |
| [this][.Controls.Add([this].comboBoxBase1);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                |
|                                                                                                                                                   |
| []                                                                                                                        |
|                                                                                                                                                   |
| [Me][.Controls.Add([Me].listBox1)]      |
|                                                                                                                                                   |
| [Me][.Controls.Add([Me].comboBoxBase1)] |
+---------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

***[]*** 

Figure 364: ComboBoxBase with External DataSource

**[]** 

**[]** 

Refer [Creating ListControl-Derived Controls] about ListControl-Derived controls in detail.

[]{#related-topics}

