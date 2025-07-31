---
title: seriescustomization.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\seriescustomization.md
created_at: 2025-07-03
---








  









### Series Customization {#series-customization style="tab-stops: 0pt"}

**[]** 

Essential Chart offers numerous appearance and behavior customization capabilities at the series level and on individual points.

Some of these options are applicable only for the whole series while the rest could be applied on the specific data points. Similarly some of these options are specific to certain chart types.

Note that styles set at the series level automatically propagate to the points in the series.

Interestingly the Chart control lets the user to edit the styles of a series by double clicking on it during run-time. This feature can be turned on by setting the **AllowUserEditStyles** property to **true**.

The table below lists the customization options available in **ChartSeries** and their restrictions.

[] 


  Customization Option                                                                                                      Applies to Series or DataPoints\*   Applies to Chart Type
  ------------------------------------------------------------------------------------------------------------------------- ----------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  []{.UGHyperlink}                       Series                              Pie Chart
  []{.UGHyperlink}                            Series and points                   Pyramid, Funnel, Area, Bar, Bubble, Column Chart, Candle Chart, Renko chart, Three Line Break Chart, Box and Whisker Chart, Gantt Chart, Histogram Chart, Tornado Chart, Polar and Radar Chart and Pie Chart.
  []{.UGHyperlink}                        Series                              Bubble chart.
  []{.UGHyperlink}                                                        Column Chart, ColumnRange Chart,Bar Chart, BoxAndWhisker Chart, Gantt Chart.
  []{.UGHyperlink}                   Series                              Column charts
  []{.UGHyperlink}                  Series                              Column charts
  []{.UGHyperlink}                        Series                              Column
  []{.UGHyperlink}                        Series                              Renko chart.
  []{.UGHyperlink}                    Series                              Renko chart.
  []{.UGHyperlink}                     Series and points                   Area Chart, Bar Chart, Bubble Chart, Column Chart, Stacking Column Chart, Stacking Column100 Chart, Line Chart, Spline Chart, Rotated Spline chart, Stepline Chart, Candle Chart, Kagi Chart, Point and Figure Chart, Renko Chart, Threeline Break Charts, Gantt Chart, Histogram chart, Tornado Chart, Combination Chart, Box and Whisker Chart.
  []{.UGHyperlink}                       Series and points                   All Chart types.
  []{.UGHyperlink}                Series                              Pie Chart.
  []{.UGHyperlink}         Series                              Column Chart.
  []{.UGHyperlink}                     Series                              Column Chart, Line Chart and HiLo Chart.
  []{.UGHyperlink}   Series                              Histogram chart.
  []{.UGHyperlink}             Series                              All Chart types.
  []{.UGHyperlink}                    Series and points                   Area Charts, Bar Charts, Bubble Chart, Column Charts, Line  Charts, Candle Chart, Renko chart, Three Line Break Chart, Box and Whisker Chart, Gantt Chart, Tornado Chart, Polar and Radar Chart.
  []{.UGHyperlink}                  Series                              Bubble Chart.
  []{.UGHyperlink}              Series                              Column Chart, Line Chart and HiLo Chart.
  []{.UGHyperlink}                       Series                              Pie Chart, Doughnut Chart.
  []{.UGHyperlink}                     Series                              Pie Chart.
  []{.UGHyperlink}                   Series                              Pie Chart.
  []{.UGHyperlink}                      Series                              All Chart Types.
  []{.UGHyperlink}                        Series                              Funnel and Pyramid chart.
  []{.UGHyperlink}                          Series                              Pie Chart
  []{.UGHyperlink}                        Series                              Funnel and Pyramid chart.
  []{.UGHyperlink}                              Series and points                   All Chart types.
  []{.UGHyperlink}                     Series                              Gantt Chart.
  []{.UGHyperlink}                          Series                              Funnel and Pyramid chart.
  []{.UGHyperlink}                          Series                              Pie Chart.
  []{.UGHyperlink}                         Series                              Point And Figure Chart.
  []{.UGHyperlink}                 Series                              Pie Chart.
  []{.UGHyperlink}                  Series                              Pie Chart.
  []{.UGHyperlink}                 Series                              Bar Charts, Pie, Funnel, Pyramid,Bubble, Column, Area, Stacking Area, Stacking Area100, Line Charts, Box and Whisker, Gantt Chart and Tornado Chart.
  []{.UGHyperlink}                     Series                              Line Chart and Step Line Chart.
  []{.UGHyperlink}                        Series and points                   Area Charts, Bar Charts, Bubble Chart, Column Charts, Line  Charts, Candle Chart, Renko chart, Three Line Break Chart, Box and Whisker Chart, Gantt Chart, Tornado Chart, Polar and Radar Chart.
  []{.UGHyperlink}                            Series and points                   Area Charts, Bar Charts, Bubble Chart, Column Charts, Line  Charts, Candle Chart, Renko chart, Three Line Break Chart, Box and Whisker Chart, Gantt Chart, Tornado Chart, Polar and Radar Chart.
  []{.UGHyperlink}                      Series                              Pie Chart.
  []{.UGHyperlink}                          Series and points                   All Chart Types.
  []{.UGHyperlink}                    Series                              Funnel and Pyramid Charts.
  []{.UGHyperlink}                        Series                              Funnel and Pyramid, Pie
  []{.UGHyperlink}                        Series                              All Chart Types.
  []{.UGHyperlink}                        Series                              Scatter Chart, Column Charts , Bar Charts, Box and Whisker Chart, Gantt Chart, Histogram Chart, Tornado Chart, Polar and Radar Chart.
  []{.UGHyperlink}                        Series                              Scatter Chart, Column Charts , Bar Charts, Box and Whisker Chart, Gantt Chart, Histogram Chart, Tornado Chart, Polar and Radar Chart.
  []{.UGHyperlink}                              Series                              All chart types.
  []{.UGHyperlink}        Series                              Histogram Chart.
  []{.UGHyperlink}                 Series                              HiLo OpenClose chart.
  []{.UGHyperlink}         Series                              Pie chart
  []{.UGHyperlink}                        Series                              Column Chart.
  []{.UGHyperlink}                           Series                              Pie chart
  []{.UGHyperlink}                 Series                              Pie chart and Doughnut chart.
  []{.UGHyperlink}               Series                              All Chart Types.
  []{.UGHyperlink}                        Series and points                   Gantt Chart.
  []{.UGHyperlink}                    Series                              Financial types
  []{.UGHyperlink}                      Series                              Financial types
  []{.UGHyperlink}                       Series                              Pyramid
  []{.UGHyperlink}                        Series                              Polar and Radar Chart.
  []{.UGHyperlink}                        Series                              Polar and Radar Chart.
  []{.UGHyperlink}                     Series and points                   Gantt Chart.
  []{.UGHyperlink}                    Series                              Kagi, PointAndFigure, Renko
  []{.UGHyperlink}                            Series                              Column Charts, Bar Charts, Area charts, Line Chart, Spline Chart, Stepline Chart, Candle Chart, HiLo Chart, HiLo Open Chart, Kagi Chart, BoxandWhisker chart, Histogram chart, Polar and Radar Chart.
  []{.UGHyperlink}                Series                              Scatter Chart.
  []{.UGHyperlink}              Series                              Scatter Chart.
  []{.UGHyperlink}               Series                              Area Charts.
  []{.UGHyperlink}                       Series                              Column Chart, BarCharts, Candle Chart, HiLO Chart, HiLoOpenClose Chart, Tornado chart, BoxandWhisker chart, Gantt Chart, Histogram Chart, Polar and Radar Chart.
  []{.UGHyperlink}                    Series and points                   Column Charts, Bubble Chart, Line Charts, BarCharts, Candle Chart, Kagi Chart, Point and Figure Chart, Renko Chart, Three Line Break Chart, Box and Whisker Chart, Gantt Chart, Histogram Chart, Tornado Chart, Pie Chart, Polar and Radar Chart.
  []{.UGHyperlink}                      Series and points                   Column Charts, Bubble Chart, Line Charts, BarCharts, Candle Chart, Kagi Chart, Point and Figure Chart, Renko Chart, Three Line Break Chart, Box and Whisker Chart, Gantt Chart, Histogram Chart, Tornado Chart, Pie Chart, Polar and Radar Chart.
  []{.UGHyperlink}                Series                              Pie Chart, Doughnut Chart, Funnel and Pyramid charts.
  []{.UGHyperlink}           Series                              Histogram Chart
  []{.UGHyperlink}                         Series                              Pie Chart.
  []{.UGHyperlink}                       Series                              All Chart Types.
  []{.UGHyperlink}                           Series and Points.                  Column Charts, BarCharts, Box and Whisker Chart, Gantt Chart, Tornado Chart.
  []{.UGHyperlink}            Series                              Area Charts, BarCharts, Line Charts, Bubble Chart, Financial Charts, Gantt Chart, Histogram chart, Tornado Chart, Combination Chart, Box and Whisker Chart.
  []{.UGHyperlink}              Series Points                       Column Chart, Bar Chart, HiLo Chart, HiLo Open Close Chart, Candle Chart, Tornado Chart, Boxes and Whisker Chart.
  []{.UGHyperlink}                 Series                              StepAreaChart, StepLine Chart.
  []{.UGHyperlink}                           Series                              All Chart Types.
  []{.UGHyperlink}                            Series and points                   Column Chart, Bar Chart, Bubble Chart, Financial Chart, Line Chart, BoxandWhisker Chart, Gantt chart, Tornado chart, Radar Chart
  []{.UGHyperlink}                     Series                              All Chart Types.
  []{.UGHyperlink}                      Series and Points                   All Chart Types.
  []{.UGHyperlink}                         Series and points                   All Chart Types.
  []{.UGHyperlink}                        Series and points                   All Chart Types.
  []{.UGHyperlink}                        Series and points                   All Chart Types.
  []{.UGHyperlink}                   Series and points                   All Chart Types.
  []{.UGHyperlink}                           Series and points                   Scatter Chart.
  []{.UGHyperlink}                     Series and points                   Scatter Chart.
  []{.UGHyperlink}                           Series                              All Chart Types.
  []{.UGHyperlink}                    Series                              Pie Chart.
  []{.UGHyperlink}                             Series                              All Chart Types.
  []{.UGHyperlink}                             Series                              All Chart Types.
  []{.UGHyperlink}                            Series                              Gantt chart, StackingBar chart, StackingBar100 chart, StackingColumn chart, StackedColumn100 chart, StackingArea chart, StackingArea100 chart.


**[]** 

\* Indicates whether the property affects ALL the points in the series or if the property can be set on individual points as well.

[]{#p79} 

More:





























































































































































































