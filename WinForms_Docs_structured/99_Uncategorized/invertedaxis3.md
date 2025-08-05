---
title: invertedaxis3.md
original_path: WinForms_Docs/99_Uncategorized/invertedaxis3.md
created_at: 2025-08-05
---






##### Inverted Axis {#inverted-axis style="tab-stops: 0pt"}

Essential Chart provides support for inverting the values on the axis. Data on an inverted axis is plotted in the opposite direction - Top to Bottom for Y-axis and Right to Left for X-axis. To enable this behavior, set the **ChartAxis.IsInversed** property to **True**.

                                                                     

Table 135:\" ChartAxis Property


  -------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ChartAxis Property   Description
  IsInversed           Indicates whether the axis should be reversed. When reversed, the axis will render points from right to left if horizontal, top to bottom when vertical, and clockwise if radial.
  -------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][syncfusion][:][ChartArea][\>]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [ ][\<][syncfusion][:][ChartArea.PrimaryAxisAxis][\>]                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [         ][\<][syncfusion][:][ChartAxis][ IsInversed][=\"True\"\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [ ][\</][syncfusion][:][ChartArea.PrimaryAxisAxis][\>]                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [ ][\<][syncfusion][:][ChartArea.SecondaryAxis][\>]                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [    ][\<][syncfusion][:][ChartAxis][ IsInversed][=\"True\"\>]      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [          ][\</][syncfusion][:][ChartArea.SecondaryAxis][\>]                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\</][syncfusion][:][ChartArea][\>][                    ][    ]                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                |
|                                                                                                                                                                 |
| []                                                                                                                          |
|                                                                                                                                                                 |
| [// Sets the Axis as inversed.]                                                                               |
|                                                                                                                                                                 |
| [chart.Areas\[0\].PrimaryAxis.IsInversed = [true];]                                                    |
|                                                                                                                                                                 |
| [chart.Areas\[0\].SecondaryAxis.IsInversed = [true];[                   ]    ] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following image illustrates Chart with an Inversed Axis.

[] 

{border="0"}

Figure 190: IsInversed property set for the Chart Control

[] 

See Also

, , 

[]{#p132} 

[]{#_Opposed_Axis} 

[]{#related-topics}

