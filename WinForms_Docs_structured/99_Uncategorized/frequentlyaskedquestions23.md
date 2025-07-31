---
title: frequentlyaskedquestions23.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\frequentlyaskedquestions23.md
created_at: 2025-07-03
---






##### Frequently Asked Questions {#frequently-asked-questions style="tab-stops: 0pt"}

[] 

This section illustrates the solutions for various task-based queries about the control.

###### []{#p265}3.3.2.3.5.1 How to customize the calculator display text area to use NumberGroupSeparator? {#how-to-customize-the-calculator-display-text-area-to-use-numbergroupseparator style="tab-stops: 0pt"}

[] 

The calculator control by default does not allow the use of NumberGroupSeparator like in DoubleTextBox.

[] 

{border="0"}

[] 

Figure 203: DoubleTextBox

[] 

So to achieve this we need to derive the CalculatorControl and override the **CreateCalculatorDisplayBox()** method.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                              |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                             |
| [private][ [CalculatorAdv] calculatorControl1;]                                                                                   |
|                                                                                                                                                                                                                                             |
| [this][.calculatorControl1 = [new] [CalculatorAdv]();]                                                       |
|                                                                                                                                                                                                                                             |
| [public][ [class] [CalculatorAdv] : Syncfusion.Windows.Forms.Tools.[CalculatorControl]] |
|                                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| [    [public] CalculatorAdv()]                                                                                                                                                     |
|                                                                                                                                                                                                                                             |
| [    {]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                             |
| [    }]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                             |
| [    [protected] [override] [void] CreateCalculatorDisplayBox()]                                                                         |
|                                                                                                                                                                                                                                             |
| [    {]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                             |
| [        Syncfusion.Windows.Forms.Tools.[DoubleTextBox] dtb = [new] Syncfusion.Windows.Forms.Tools.[DoubleTextBox]();]                   |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [        dtb.NumberGroupSeparator = [\",\"];]                                                                                                                                    |
|                                                                                                                                                                                                                                             |
| [        [this].textCalculatorBox = dtb; [//Changing the TextBox to DoubleTextBox]]                                                                          |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                                             |
| [    }]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                   |
|                                                                                                                                                                                                      |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                      |
| [Private][ calculatorControl1 [As] CalculatorAdv]                                          |
|                                                                                                                                                                                                      |
| [Me.calculatorControl1 = New CalculatorAdv() ]                                                                                                                   |
|                                                                                                                                                                                                      |
| [Public][ [Class] CalculatorAdv]                                                           |
|                                                                                                                                                                                                      |
| [    [Inherits] Syncfusion.Windows.Forms.Tools.CalculatorControl]                                                                           |
|                                                                                                                                                                                                      |
| []                                                                                                                                                               |
|                                                                                                                                                                                                      |
| [    [Public] [Sub] [New]()]                                                                      |
|                                                                                                                                                                                                      |
| [    [End] [Sub]]                                                                                                      |
|                                                                                                                                                                                                      |
| [    [Protected] [Overloads] [Overrides] [Sub] CreateCalculatorDisplayBox()] |
|                                                                                                                                                                                                      |
| [        [Dim] dtb [As] [New] Syncfusion.Windows.Forms.Tools.DoubleTextBox()]                     |
|                                                                                                                                                                                                      |
| []                                                                                                                                                               |
|                                                                                                                                                                                                      |
| [        dtb.NumberGroupSeparator = [\",\"]]                                                                                              |
|                                                                                                                                                                                                      |
| [        [Me].textCalculatorBox = dtb]                                                                                                      |
|                                                                                                                                                                                                      |
| [        [\'Changing the TextBox to DoubleTextBox ]]                                                                                       |
|                                                                                                                                                                                                      |
| [    [End] [Sub]]                                                                                                      |
|                                                                                                                                                                                                      |
| [End][ [Class]]                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[  ]**[ ]**

{border="0"}

[] 

Figure 204: Calculator displaying NumberGroupSeparator with the help of DoubleTextBox

 

 

###### 3.3.2.3.5.2 How to Simulate a Particular button in the Calculator[]{#p266}? {#how-to-simulate-a-particular-button-in-the-calculator style="tab-stops: 0pt"}

[] 

We can use **Calculator.ButtonAction()** method for this. When the user clicks the button, the ButtonAction method of the Calculator control will  call back the action of the particular button (in this example it is \"=\" button) and displays the result in the textbox area, using CalcActions Enumerator. This enumerator has all the actions that can be assigned to the calculator buttons including digits and arithmetic operators also.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                          |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                |
|                                                                                                                                                                                                                         |
| [private][ [void] buttonAdv1_Click([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                         |
| [{]                                                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [    [//Performing the \"=\" button action]]                                                                                                                  |
|                                                                                                                                                                                                                         |
| [    [this].calculatorControl1.ButtonAction(Syncfusion.Windows.Forms.Tools.[CalcActions].CalcOperatorEquals);]                            |
|                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [Private Sub][ ][buttonAdv1_Click[(][ByVal][ sender][ As Object][, ][ByVal][ e ][As][ System.EventArgs) ]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [   \'Performing the \"=\" button action]                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [   ][Me][.calculatorControl1.ButtonAction(Syncfusion.Windows.Forms.Tools.CalcActions.CalcOperatorEquals) ]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [End Sub]                                                                                                                                                                                                                                                                                                                                                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

