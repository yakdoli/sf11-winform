---
title: chartevents.md
original_path: WinForms_Docs/04_Controls/Chart/chartevents.md
created_at: 2025-08-05
---








  









## Chart Events {#chart-events style="tab-stops: 0pt"}

[]{#p112}AutoSetRangeChanged---This event is raised when the AutoSetRange is changed for Primary and secondary Axis.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                              |
|                                                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                               |
| [area.SecondaryAxis.AutoSetRangeChanged += [new] [PropertyChangedCallback](SecondaryAxis_AutoSetRangeChanged);]                                              |
|                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                               |
| [void][ SecondaryAxis_AutoSetRangeChanged([DependencyObject] d, [DependencyPropertyChangedEventArgs] e)] |
|                                                                                                                                                                                                                                               |
| [{]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                               |
| [    [MessageBox].Show(e.NewValue.ToString());]                                                                                                                                   |
|                                                                                                                                                                                                                                               |
| [}]                                                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

DesiredIntervalsCountChanged - This event is handled when DesiredIntervalCount value is changed. Note that to update this, IsAutoSetRange property must be *true*.

**[]** 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                      |
| [area.PrimaryAxis.DesiredIntervalsCountChanged += [new] [PropertyChangedCallback](PrimaryAxis_DesiredIntervalsCountChanged);]                                       |
|                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                      |
| [void][ PrimaryAxis_DesiredIntervalsCountChanged([DependencyObject] d, [DependencyPropertyChangedEventArgs] e)] |
|                                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                      |
| [   [MessageBox].Show(e.NewValue.ToString());]                                                                                                                                           |
|                                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

IntervalChanged - This event is raised when the interval value is changed for the X and Y axis.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                              |
|                                                                                                                                                                                                                                         |
| [area.PrimaryAxis.IntervalChanged += [new] [PropertyChangedCallback](PrimaryAxis_IntervalChanged);]                                                    |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [void][ PrimaryAxis_IntervalChanged([DependencyObject] d, [DependencyPropertyChangedEventArgs] e)] |
|                                                                                                                                                                                                                                         |
| [{]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                         |
| [    [MessageBox].Show(e.NewValue.ToString());]                                                                                                                             |
|                                                                                                                                                                                                                                         |
| [}]                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

LineStyleChanged - This event is raised when Line, GridLine property is changed.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                               |
|                                                                                                                                                                                                                                          |
| [area.PrimaryAxis.LineStyleChanged += [new] [PropertyChangedCallback](PrimaryAxis_LineStyleChanged);]                                                   |
|                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                          |
| [void][ PrimaryAxis_LineStyleChanged([DependencyObject] d, [DependencyPropertyChangedEventArgs] e)] |
|                                                                                                                                                                                                                                          |
| [{]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                          |
| [    [MessageBox].Show(e.NewValue.ToString());]                                                                                                                              |
|                                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

OpposedPositionChanged - This event is handled when OpposedPosition property is changed.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                  |
| [area.SecondaryAxis.OpposedPositionChanged += [new] [PropertyChangedCallback](SecondaryAxis_OpposedPositionChanged);]                                           |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                  |
| [void][ SecondaryAxis_OpposedPositionChanged([DependencyObject] d, [DependencyPropertyChangedEventArgs] e)] |
|                                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                  |
| [   [MessageBox].Show(e.NewValue.ToString());]                                                                                                                                       |
|                                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

RangeChanged - Both Primary and Secondary Axis comes with RangeChanged event. This event is handled when Range property is changed. We could get the old and new range from this event.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                                           |
|                                                                                                                                                                                                                                      |
| [area.PrimaryAxis.RangeChanged += [new] [PropertyChangedCallback](PrimaryAxis_RangeChanged);]                                                       |
|                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                      |
| [void][ PrimaryAxis_RangeChanged([DependencyObject] d, [DependencyPropertyChangedEventArgs] e)] |
|                                                                                                                                                                                                                                      |
| [{]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                      |
| [      [MessageBox].Show(e.NewValue.ToString());]                                                                                                                        |
|                                                                                                                                                                                                                                      |
| [}]                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

