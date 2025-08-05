---
title: logarithmicscale2.md
original_path: WinForms_Docs/99_Uncategorized/logarithmicscale2.md
created_at: 2025-08-05
---






##### Logarithmic Scale {#logarithmic-scale style="tab-stops: 0pt"}

Essential Circular gauge for WPF supports logarithmic label ticks. To enable this set **IsLogarithmic** property to **true**, and specifying a valid **LogBase** value. The value of the **LabelTick** is calculated based on the **LogBase**.

[] 

Set the logarithmic scale for a Circular gauge, by using the following code.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][syncfusion][:][CircularLabelTick][ DistanceFromScale][=\"5\"][ FontSize][=\"11\"][ Name][=\"labelTick\"][ ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [  TickPlacement][=\"Inside\"][ TickStyle][=\"MajorTick\"][ [IsLogarithmic][=\"True\"][ LogBase][=\"10\"\>]]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\</][syncfusion][:][CircularLabelTick][\>]                                                                                                                                                                                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                          |
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
| [labeltick.IsLogarithmic = [true];]                                                                                                   |
|                                                                                                                                                                                           |
| [labeltick.LogBase = 10;]                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Run the code. Figure 1 illustrates the output.

{border="0"}

Figure 32: Logarthmic Scale with logbase-2

[]{#p29} 

[]{#related-topics}

