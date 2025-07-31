---
title: stackinggroup.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\stackinggroup.md
created_at: 2025-07-03
---






#### Stacking Group {#stacking-group style="tab-stops: 0pt"}

 

This section illustrates how to group the stacking series with another stacking series.

1.   In order to group the stacking series with another stacking series in chart control, you need to set a StackingGroup property of the chart series with the desired group name.

The below example demonstrates the code on setting the StackingGroup for the series in the Chart control.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                |
|                                                                                                                                                                                                                          |
| [ChartSeries][ ser1 = [new] [ChartSeries]([\"Series 1\"]);] |
|                                                                                                                                                                                                                          |
| [ser1.Type = [ChartSeriesType].StackingColumn;]                                                                                                              |
|                                                                                                                                                                                                                          |
| [// specifing group name .]                                                                                                                                            |
|                                                                                                                                                                                                                          |
| [ser1.StackingGroup = [\"FirstGroup\"];]                                                                                                                     |
|                                                                                                                                                                                                                          |
| [ChartSeries][ ser2 = [new] [ChartSeries]([\"Series 2\"]);] |
|                                                                                                                                                                                                                          |
| [ser2.Type = [ChartSeriesType].StackingColumn;]                                                                                                              |
|                                                                                                                                                                                                                          |
| [// specifing group name .]                                                                                                                                            |
|                                                                                                                                                                                                                          |
| [ser2.StackingGroup = [\"SecondGroup\"];]                                                                                                                    |
|                                                                                                                                                                                                                          |
| [ChartSeries][ ser3 = [new] [ChartSeries]([\"Series 3\"]);] |
|                                                                                                                                                                                                                          |
| [ser3.Type = [ChartSeriesType].StackingColumn;]                                                                                                              |
|                                                                                                                                                                                                                          |
| [// specifing group name .]                                                                                                                                            |
|                                                                                                                                                                                                                          |
| [ser3.StackingGroup = [\"FirstGroup\"];[]]                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[VB\]]                                                                                                                                  |
|                                                                                                                                                                                                            |
| [Dim][ ser1 [As] [New] ChartSeries([\"Series 1\"])] |
|                                                                                                                                                                                                            |
| [ser1.Type = ChartSeriesType.StackingColumn]                                                                                                                           |
|                                                                                                                                                                                                            |
| [\' specifing group name .]                                                                                                                              |
|                                                                                                                                                                                                            |
| [ser1.StackingGroup = [\"FirstGroup\"]]                                                                                                        |
|                                                                                                                                                                                                            |
| [Dim][ ser2 [As] [New] ChartSeries([\"Series 2\"])] |
|                                                                                                                                                                                                            |
| [ser2.Type = ChartSeriesType.StackingColumn]                                                                                                                           |
|                                                                                                                                                                                                            |
| [\' specifing group name .]                                                                                                                              |
|                                                                                                                                                                                                            |
| [ser2.StackingGroup = [\"SecondGroup\"]]                                                                                                       |
|                                                                                                                                                                                                            |
| [Dim][ ser3 [As] [New] ChartSeries([\"Series 3\"])] |
|                                                                                                                                                                                                            |
| [ser3.Type = ChartSeriesType.StackingColumn]                                                                                                                           |
|                                                                                                                                                                                                            |
| [\' specifing group name .]                                                                                                                              |
|                                                                                                                                                                                                            |
| [ser3.StackingGroup = [\"FirstGroup\"][]]                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

{border="0"}

Figure 209: Column chart with stacking group.[]

**** 

{border="0"}

Figure 210: Bar chart with Stacking group.**[]**

 

[]{#related-topics}

