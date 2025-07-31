---
title: namedranges.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\namedranges.md
created_at: 2025-07-03
---






##### Named Ranges {#named-ranges style="tab-stops: 0pt"}

[] 

Essential Grid supports named ranges along with Grid Formula Engine. Named ranges let the users to set up names for expressions or ranges, and then use these names in formulas. For example, if you name the range, \"B4:B12\" as \"Expenses\", you can use formulas like =Sum(Expenses) instead of =Sum(B4:B12).

[] 

{border="0"}

[] 

*[Figure ][129][: Named Ranges in Grid Control]*

[] 

Example

[] 

The following example illustrates the creation and usage of named ranges in Grid controls.

 

You can call the **AddNamedRange** method by using an instance of Grid Formula Engine and pass two parameters-**Name** and **Value** to be set for the range.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                              |
|                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                             |
| [GridFormulaEngine][ engine;]                                                                                                                       |
|                                                                                                                                                                                                                                             |
| [this][.engine = (([GridFormulaCellModel])gridCashFlow.Model.CellModels\[[\"FormulaCell\"]\]).Engine;] |
|                                                                                                                                                                                                                                             |
| [this][.engine.AddNamedRange([\"Car\"], [\"300\"]);]                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                       |
|                                                                                                                                                                                                                                            |
| [Dim][ engine [As] GridFormulaEngine]                                                                                            |
|                                                                                                                                                                                                                                            |
| [Me][.engine = ([CType](gridCashFlow.Model.CellModels([\"FormulaCell\"]), GridFormulaCellModel)).Engine] |
|                                                                                                                                                                                                                                            |
| [Me][.engine.AddNamedRange([\"Car\"], [\"300\"])]                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

You can edit the named ranges by using the **NamedRange Collection Editor**. The following code uses the ShowNamedRangeDialog method to display the editor.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                          |
|                                                                                                                                                                                         |
| []                                                                                                                                                  |
|                                                                                                                                                                                         |
| [GridFormulaNamedRangesEditHelper][.ShowNamedRangesDialog([this].engine);] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                             |
|                                                                                                                                |
| []                                                                           |
|                                                                                                                                |
| [GridFormulaNamedRangesEditHelper.ShowNamedRangesDialog([Me].engine)] |
+--------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

*[Figure ][130][: NamedRange Collection Editor]*

[] 

In the above dialog box, you will notice the named ranges (Members) are displayed in the left pane and their corresponding properties to the right pane (Properties). You can select a Named Range and edit its value as follows.

[] 

{border="0"}

***[]*** 

*[Figure ][131][: Editing Named Ranges]*

[] 

You can also edit the title of this editor by handling the ShowingNamedRangesDialog event. The following code example illustrates this.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                     |
| [GridFormulaNamedRangesEditHelper][.ShowingNamedRangesDialog += [new] [ControlEventHandler](helper_ShowingNamedRangesDialog);] |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                     |
| [// Event handler to change the title of NamedRange Collection Editor dialog box.]                                                                                                                                |
|                                                                                                                                                                                                                                                                     |
| [private][ [void] helper_ShowingNamedRangesDialog([object] sender, [ControlEventArgs] e)]                    |
|                                                                                                                                                                                                                                                                     |
| [{]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                     |
| [      [Form] f = e.Control [as] [Form];]                                                                                                                  |
|                                                                                                                                                                                                                                                                     |
| [      [if](f != [null])]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                     |
| [      {]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                     |
| [            [// Set the title for the dialog box.]]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                     |
| [            f.Text = [\"CashFlow Inputs\"];]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                     |
| [      }     ]                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                     |
| [}]                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                     |
| [Private][ GridFormulaNamedRangesEditHelper.ShowingNamedRangesDialog += [New] ControlEventHandler([AddressOf] helper_ShowingNamedRangesDialog)]                                                      |
|                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                     |
| [\' Event handler to change the title of NamedRange Collection Editor dialog box.]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                     |
| [Private][ [Sub] helper_ShowingNamedRangesDialog([ByVal] sender [As] [Object], [ByVal] e [As] ControlEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                     |
| [Dim][ f [As] Form = [TryCast](e.Control, Form)]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                     |
| [If][ f [IsNot] [Nothing] [Then]]                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                     |
| [\' Set the title for the dialog box.]                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                     |
| [f.Text = [\"CashFlow Inputs\"]]                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                     |
| [End][ [If]]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                     |
| [End][ [Sub]]                                                                                                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Custom Title for the ShowNamedRange dialog is set to \"CashFlow Inputs\" by using the above code.

[] 

{border="0"}

***[]*** 

*[Figure ][132][: Custom Title set for the NamedRange Collection Editor]*

[] 


{border="0"}Note: The following sample illustrates the use of Cross Sheet References and Named Ranges with the Grid Formula Engine.


[] 

***\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Windows\\Samples\\2.0\\Formula Support\\Named Range For Formula Demo***

 

[]{#p280} 

 

[]{#related-topics}

