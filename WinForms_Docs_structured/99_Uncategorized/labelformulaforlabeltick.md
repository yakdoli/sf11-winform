---
title: labelformulaforlabeltick.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\labelformulaforlabeltick.md
created_at: 2025-07-03
---






##### LabelFormula for LabelTick {#labelformula-for-labeltick style="tab-stops: 0pt"}

Essential Gauge supports formula based label ticks. To enable this set **IsCalculateFormulaEnabled** property to **true**, and specifying a valid formula to the **CalculateFormula**. The value of the **LabelTick** is calculated based upon the formula that is specified.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][syncfusion][:][CircularLabelTick][ DistanceFromScale][=\"5\"][ FontSize][=\"11\"][ Name][=\"labelTick\"][ ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [  [TickPlacement][=\"Inside\"][ TickStyle][=\"MajorTick\"] [IsCalculateFormulaEnabled][=\"True\"][ ]]                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [  CalculateFormula][=\"!((x/10)\*10)\"\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\</][syncfusion][:][CircularLabelTick][\>]                                                                                                                                                                                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]][]**                                                                                   |
|                                                                                                                                                                                           |
| **[]**                                                                                                                                    |
|                                                                                                                                                                                           |
| [CircularLabelTick][ labeltick = [new] [CircularLabelTick]();] |
|                                                                                                                                                                                           |
| [labeltick.DistanceFromScale = 5;]                                                                                                                         |
|                                                                                                                                                                                           |
| [labeltick.FontSize = 11;]                                                                                                                                 |
|                                                                                                                                                                                           |
| [labeltick.TickPlacement = [ScalePlacement].Inside;]                                                                               |
|                                                                                                                                                                                           |
| [labeltick.TickStyle = [TickStyle].MajorTick;]                                                                                     |
|                                                                                                                                                                                           |
| [labeltick.IsCalculateFormulaEnabled = [true];]                                                                                       |
|                                                                                                                                                                                           |
| [labeltick.CalculateFormula = [\"!((x/10)\*10)\"];]                                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

When the code runs, the following output displays.

[] 

{border="0"}

Figure 33: Formula is Enabled

***[]*** 

 

[]{#related-topics}

