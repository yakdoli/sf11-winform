---
title: chartaxisevents.md
original_path: WinForms_Docs/04_Controls/Chart/chartaxisevents.md
created_at: 2025-08-05
---






##### Chart Axis Events {#chart-axis-events style="tab-stops: 0pt"}

ChartAxis events that could be used to track the Axis changes are as follows.

Axis.Changed

This event is triggered whenever any properties of the axis are changed.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                               |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [Area.PrimaryAxis.Changed += [new] [EventHandler](PrimaryAxis_Changed);   ]                                   |
|                                                                                                                                                                                                |
| []                                                                                                                                                         |
|                                                                                                                                                                                                |
| [// PrimaryAxis.Changed Event]                                                                                                               |
|                                                                                                                                                                                                |
| [void][ PrimaryAxis_Changed([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                |
| [{]                                                                                                                                                        |
|                                                                                                                                                                                                |
| [   [MessageBox].Show(Area.PrimaryAxis.ToString());]                                                                               |
|                                                                                                                                                                                                |
| [}]                                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

Axis.RangeChanged

Both Primary and Secondary Axis comes with **Rangechanged** event. This event occurs when the Range of the axis is changed. We could get the old and new range from this event.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                              |
| [///\<summary\>]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                              |
| [///][Event triggered when Axis range is changed.]                                                                                                        |
|                                                                                                                                                                                                                                                              |
| [///\</summary\>]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                              |
| [///\<param name=\"sender\"\>][Sender Axis of event.][\</param\>]                                        |
|                                                                                                                                                                                                                                                              |
| [///\<param name=\"e\"\>][ChartAxisRangeArgument that will return old and new range values.][\</param\>] |
|                                                                                                                                                                                                                                                              |
| [        ]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                              |
| [void][ PrimaryAxis_RangeChanged([object] sender, [ChartAxisRangeArgs] e)]                                                 |
|                                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                              |
| [    [Console].WriteLine (e.OldValue.Start.ToString();]                                                                                                                                          |
|                                                                                                                                                                                                                                                              |
| [    [Console].WriteLine (e.OldValue.End.ToString();]                                                                                                                                            |
|                                                                                                                                                                                                                                                              |
| [    [Console].WriteLine (e.NewValue.Start.ToString();]                                                                                                                                          |
|                                                                                                                                                                                                                                                              |
| [    [Console].WriteLine (e.NewValue.End.ToString();]                                                                                                                                            |
|                                                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

See Also



[]{#p159} 

[]{#related-topics}

