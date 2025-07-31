---
title: alternatingbackground.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\alternatingbackground.md
created_at: 2025-07-03
---








  









### Alternating Background {#alternating-background style="tab-stops: 0pt"}

 

Essential Chart Silverlight is now enhanced with horizontal or vertical background in intervals of a chart area.

**[]** 

Properties

Alternating Background, Alternating Fill Mode, and Alternating Fill Direction properties in the class Chart Area are used to apply alternating backgrounds to the chart area.

The following tabular column contains the properties detail.

[] 


+-----------------------+----------------------------------------------------------------+----------------------+-----------------------------------------------+
| Name of the Property  | Description                                                    | Type of the Property | Value It Accepts                              |
+-----------------------+----------------------------------------------------------------+----------------------+-----------------------------------------------+
| AlternatingBackground | Determines whether to fill the grid with alternate Color.      | Dependency Property  | Bool                                          |
+-----------------------+----------------------------------------------------------------+----------------------+-----------------------------------------------+
| AlternatingFillMode   | Fills the color alternately in the odd/even grid as specified. | Dependency Property  | Odd or Even                                   |
+-----------------------+----------------------------------------------------------------+----------------------+-----------------------------------------------+
| AlternatingFillMode   | Set as Horizontal to fills the color in grid row.              | Dependency Property  | Enum from the type AlternatingFillDirection   |
|                       |                                                                |                      |                                               |
|                       | Set as Vertical to fills the color in grid column.             |                      |                                               |
+-----------------------+----------------------------------------------------------------+----------------------+-----------------------------------------------+


[] 

**[]** 

**[]** 

**[]** 

Applying Background in Intervals of a Chart Area

 Apply background in intervals of a chart area, by using the following code.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[Xaml\] ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<][syncfusion][:][ChartArea][ CornerRadius][=\"20\"][ AlternatingGridBackground][=\"AliceBlue\"][      ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [                             AlternatingFillDirection][=\"Horizontal\"][ AlternatingFillMode][=\"Odd\"\>]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [           . . . .]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [           . . . .]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [     ][\</][syncfusion][:][ChartArea][\>][ ]                                                                                                                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C# \]]                                                                                                                                                                            |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                          |
| [chart.Areas\[0\].AlternatingFillMode = ][AlternatingFillMode][.Odd;]          |
|                                                                                                                                                                                                                          |
| [     chart.Areas\[0\].AlternatingFillDirection = ][Orientation][.Horizontal;] |
|                                                                                                                                                                                                                          |
| [     chart.Areas\[0\].AlternatingGridBackground = [new] [SolidColorBrush]([Colors].Gray);]                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

When the code runs, the following output displays.

[] 

{border="0"}

Figure 61: Horizontal Back Ground

[] 

[]{#related-topics}

