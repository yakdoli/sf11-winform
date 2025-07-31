---
title: frequentlyaskedquestions33.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\frequentlyaskedquestions33.md
created_at: 2025-07-03
---






##### Frequently Asked Questions {#frequently-asked-questions style="tab-stops: 0pt"}

###### 3.3.8.1.4.1 How to Change the Calculator layout using CalcPopup property {#how-to-change-the-calculator-layout-using-calcpopup-property style="tab-stops: 0pt"}

Sometimes we may be in need of a calculator with Windows standard layout. By changing the **CalcPopup** property, we can do the same. Include this code fragment in the **FormLoad** event.[]

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                                                       |
|                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                     |
|                                                                                                                                                                                                                              |
| [// Changes the layout of the calculator.][]                                                                                                         |
|                                                                                                                                                                                                                              |
| [PopupCalculator pc=][new][ Popupcalculator();][] |
|                                                                                                                                                                                                                              |
| [pc.LayoutType=CalculatorLayoutTypes.WindowsStandard;][]                                                                                             |
|                                                                                                                                                                                                                              |
| [pc.ParentControl=currencyEdit1;][]                                                                                                                  |
|                                                                                                                                                                                                                              |
| [currencyEdit1.CalcPopup=pc][;][]                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**[]                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [\' Changes the layout of the calculator.][]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [Dim][ pc ][As][ PopupCalculator = ][New][ Popupcalculator()][] |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [pc.LayoutType=CalculatorLayoutTypes.WindowsStandard][]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [pc.ParentControl=currencyEdit1][]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                |
| [currencyEdit1.CalcPopup=pc][]                                                                                                                                                                                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

