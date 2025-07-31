---
title: seriescustomization1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\seriescustomization1.md
created_at: 2025-07-03
---








  









### Series Customization {#series-customization style="tab-stops: 0pt"}

 

Essential Chart offers numerous appearance and behavior customization capabilities at the series level and on individual points.

Some of these options are applicable only for the whole series while the rest could be applied on the specific data points. Similarly, some of these options are specific to certain chart types.

Note that styles set at the series level automatically propagate to the points in the series.

Interestingly the Chart control allows the user to edit the styles of a series by double-clicking it during run-time. This feature can be turned on by setting the AllowUserEditStyles property to true.

The table displayed below lists the customization options available in the Chart Series and their restrictions:

 


  Customization Option              Applies to Series or DataPoints\*   Applies to Chart Type
  --------------------------------- ----------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  AngleOffset                       Series                              Pie chart
  Border                            Series and points                   Pyramid chart, Funnel chart, Area chart, Bar chart, Bubble chart, Column chart, Candle chart, Renko chart, Three Line Break chart, Box and Whisker chart, Gantt chart, Histogram chart, Tornado chart, Polar chart, Radar chart, and Pie chart.
  BubbleType                        Series                              Bubble chart
  ColumnDrawMode                                                        Column chart, Column Range chart, Bar chart, Box and Whisker chart, and Gantt chart.
  ColumnWidthMode                   Series                              Column charts
  ColumnFixedWidth                  Series                              Column charts
  ColumnType                        Series                              Column charts
  ColorsMode                        Series                              Renko chart
  DarkLightPower                    Series                              Renko chart
  DisplayShadow                     Series and points                   Area chart, Bar chart, Bubble chart, Column chart, Stacking Column chart, Stacking Column100 chart, Line chart, Spline chart, Rotated Spline chart, Step Line chart, Candle chart, Kagi chart, Point and Figure chart, Renko chart, Three Line Break charts, Gantt chart, Histogram chart, Tornado chart, Combination chart, and Box and Whisker chart.
  DisplayText                       Series and points                   All chart types.
  DoughnutCoeficient                Series                              Pie chart
  DrawColumnSeparatingLines         Series                              Column chart
  DrawErrorBars                     Series                              Column chart, Line chart, and HiLo chart.
  DrawHistogramNormalDistribution   Series                              Histogram chart
  DrawSeriesNameInDepth             Series                              All chart types.
  ElementBorders                    Series and points                   Area charts, Bar charts, Bubble chart, Column charts, Line charts, Candle chart, Renko chart, Three Line Break chart, Box and Whisker chart, Gantt chart, Tornado chart, Polar chart, and Radar chart.
  EnablePhongStyle                  Series                              Bubble chart.
  ErrorBarsSymbolShape              Series                              Column chart, Line chart, and HiLo chart.
  ExplodedAll                       Series                              Pie chart and Doughnut chart.
  ExplodedIndex                     Series                              Pie chart
  ExplosionOffset                   Series                              Pie chart
  FancyToolTip                      Series                              All chart types.
  FigureBase                        Series                              Funnel chart and Pyramid chart.
  FillMode                          Series                              Pie chart
  FunnelMode                        Series                              Funnel chart and Pyramid chart.
  Font                              Series and points                   All chart types.
  GanttDrawMode                     Series                              Gantt chart
  GapRatio                          Series                              Funnel chart and Pyramid chart.
  Gradient                          Series                              Pie chart
  HeightBox                         Series                              Point and Figure chart
  HeightByAreaDepth                 Series                              Pie chart
  HeightCoeficient                  Series                              Pie chart
  HighlightInterior                 Series                              Bar charts, Pie chart, Funnel chart, Pyramid chart, Bubble chart, Column chart, Area chart, Stacking Area chart, StackingArea100 chart, Line charts, Box and Whisker chart, Gantt chart, and Tornado chart.
  HitTestRadius                     Series                              Line chart and Step Line chart.
  ImageIndex                        Series and points                   Area charts, Bar charts, Bubble chart, Column charts, Line charts, Candle chart, Renko chart, Three Line Break chart, Box and Whisker chart, Gantt chart, Tornado chart, Polar chart, and Radar chart.
  Images                            Series and points                   Area charts, Bar charts, Bubble chart, Column charts, Line charts, Candle chart, Renko chart, Three Line Break chart, Box and Whisker chart, Gantt chart, Tornado chart, Polar chart, and Radar chart.
  InSideRadius                      Series                              Pie chart
  Interior                          Series and points                   All chart types.
  LabelPlacement                    Series                              Funnel chart and Pyramid chart.
  LabelStyle                        Series                              Funnel chart, Pyramid chart, and Pie chart.
  LegendItem                        Series                              All chart types.
  LightAngle                        Series                              Scatter chart, Column charts, Bar charts, Box and Whisker chart, Gantt chart, Histogram chart, Tornado chart, Polar chart, and Radar chart.
  LightColor                        Series                              Scatter chart, Column charts, Bar charts, Box and Whisker chart, Gantt chart, Histogram chart, Tornado chart, Polar chart, and Radar chart.
  Name                              Series                              All chart types.
  NumberOfHistogramIntervals        Series                              Histogram chart
  OpenCloseDrawMode                 Series                              HiLoOpenClose chart
  OptimizePiePointPositions         Series                              Pie chart
  PhongAlpha                        Series                              Column chart
  PieType                           Series                              Pie chart
  PieWithSameRadius                 Series                              Pie chart and Doughnut chart.
  PointsToolTipFormat               Series                              All chart types.
  PointWidth                        Series and points                   Gantt chart.
  PriceDownColor                    Series                              Financial types
  PriceUpColor                      Series                              Financial types
  PyramidMode                       Series                              Pyramid chart
  Radar Type                        Series                              Polar chart and Radar chart.
  RadarStyle                        Series                              Polar chart and Radar chart.
  RelatedPoints                     Series and points                   Gantt chart
  ReversalAmount                    Series                              Kagi chart, Point and Figure chart, and Renko chart.
  Rotate                            Series                              Column charts, Bar charts, Area charts, Line chart, Spline chart, Step Line chart, Candle chart, HiLo chart, HiLoOpenClose chart, Kagi chart, Box and Whisker chart, Histogram chart, Polar chart, and Radar chart.
  ScatterConnectType                Series                              Scatter chart
  ScatterSplineTension              Series                              Scatter chart
  SeriesToolTipFormat               Series                              Area charts
  ShadingMode                       Series                              Column chart, Bar charts, Candle chart, HiLo chart, HiLoOpenClose chart, Tornado chart, Box and Whisker chart, Gantt chart, Histogram chart, Polar chart, and Radar chart.
  ShadowInterior                    Series and points                   Column charts, Bubble chart, Line charts, Bar charts, Candle chart, Kagi chart, Point and Figure chart, Renko chart, Three Line Break chart, Box and Whisker chart, Gantt chart, Histogram chart, Tornado chart, Pie chart, Polar chart, and Radar chart.
  ShadowOffset                      Series and points                   Column charts, Bubble chart, Line charts, Bar charts, Candle chart, Kagi chart, Point and Figure chart, Renko chart, Three Line Break chart, Box and Whisker chart, Gantt chart, Histogram chart, Tornado chart, Pie chart, Polar chart, and Radar chart.
  ShowDataBindLabels                Series                              Pie chart, Doughnut chart, Funnel chart, and Pyramid chart.
  ShowHistogramDataPoints           Series                              Histogram chart
  ShowTicks                         Series                              Pie chart
  SmartLabels                       Series                              All chart types.
  Spacing                           Series and Points.                  Column charts, Bar charts, Box and Whisker chart, Gantt chart, and Tornado chart.
  Spacing between Series            Series                              Area charts, Bar charts, Line charts, Bubble chart, Financial charts, Gantt chart, Histogram chart, Tornado chart, Combination chart, and Box and Whisker chart.
  SpacingBetweenPoints              Series Points                       Column chart, Bar chart, HiLo chart, HiLoOpenClose chart, Candle chart, Tornado chart, and Box and Whisker chart.
  StepItem.Inverted                 Series                              Step Area chart and Step Line chart.
  Summary                           Series                              All chart types.
  Symbol                            Series and points                   Column chart, Bar chart, Bubble chart, Financial chart, Line chart, Box and Whisker chart, Gantt chart, Tornado chart, and Radar chart.
  Text (Series)                     Series                              All chart types.
  Text (Style)                      Series and Points                   All chart types.
  TextColor                         Series and points                   All chart types.
  TextFormat                        Series and points                   All chart types.
  TextOffset                        Series and points                   All chart types.
  TextOrientation                   Series and points                   All chart types.
  ToolTip                           Series and points                   All chart types.
  ToolTipFormat                     Series and points                   All chart types.
  Visible                           Series                              All chart types.
  VisibleAllPies                    Series                              Pie chart
  XType                             Series                              All chart types.
  YType                             Series                              All chart types.
  ZOrder                            Series                              Gantt chart, Stacking Bar chart, StackingBar100 chart, Stacking Column chart, StackedColumn100 chart, Stacking Area chart, and StackingArea100 chart.


 

[\* ][Indicates whether the property affects ALL the points in the series or if the property can also be set on individual points.]{.BodyText1Char}[]

More:



























