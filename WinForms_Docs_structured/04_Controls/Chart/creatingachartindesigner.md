---
title: creatingachartindesigner.md
original_path: WinForms_Docs/04_Controls/Chart/creatingachartindesigner.md
created_at: 2025-08-05
---








  









## Creating a Chart in Designer {#creating-a-chart-in-designer style="tab-stops: 0pt"}

Users can create a simple chart through designer with Syncfusion WPF Chart control, by using the following steps.

[] 

Creating a Simple Chart

[] 

1.   Create a new WPF application in VS2010.

2.   Drag the Chart control from the **Toolbox** to the window.

[] 

{border="0"}

Figure 5: ToolBox


{border="0"}Note: the following output displays.


[] 

{border="0"}

Figure 6: Chart With Default Series

 

[] 


{border="0"}Note: The following code is auto generated in XAML window[.]


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [     ][\<][syncfusion][:][Chart][ HorizontalAlignment][=\"Left\"][ Margin][=\"46,25,0,0\"][ Name][=\"chart1\"][ ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [VerticalAlignment][=\"Top\"][ Width][=\"355\"][ Height][=\"250\"\>]                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [            ][\<][syncfusion][:][ChartArea][\>]                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [                ][\<][syncfusion][:][ChartSeries][ Data][=\"1,1,2,2,3,3,4,4,5,5,6,6\"][ ]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [LegendIcon][=\"Circle\" /\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [                ][\<][syncfusion][:][ChartSeries][ Data][=\"1,2,2,3,3,4,4,5,5,3,6,2\"][ ]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [LegendIcon][=\"Circle\" /\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [            ][\</][syncfusion][:][ChartArea][\>]                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [        ][\</][syncfusion][:][Chart][\>]                                                                                                                                                                                                                                                                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: Chart control displays the default series when it is dragged.


The default series can be deleted.

[] 

{border="0"}

Figure 7: Default Series Deleted

[] 

3.   Click the char area.


{border="0"}Note: An expand button displays.


[] 

4.   Click the expand button.


{border="0"}Note: Chart Area smart tag displays.


[] 

{border="0"}[]

Figure 8: Chart Area smart tag

[] 

[] 

5.   Click **Add chart Series** link to add new series to the chart area.

6.   The XAML Page gets updated as illustrated below.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [    ][\<][Grid][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [        ][\<][syncfusion][:][Chart][ HorizontalAlignment][=\"Left\"][ Margin][=\"46,96,0,0\"][ Name][=\"chart1\"][ ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [VerticalAlignment][=\"Top\"\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [            ][\<][syncfusion][:][ChartArea][\>]                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [               ][\<][syncfusion][:][ChartSeries][ /\>]                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [            ][\</][syncfusion][:][ChartArea][\>]                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [        ][\</][syncfusion][:][Chart][\>]                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [    ][\</][Grid][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

7.   Add the X and Y values using the **Data** property in the chart series.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [  ][\<][syncfusion][:][Chart][\>]                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [            ][\<][syncfusion][:][ChartArea][\>]                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [               ][\<][syncfusion][:][ChartSeries][ Data][=\"1,1,2,2,3,3,4,4,5,5,6,6\"/\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [            ][\</][syncfusion][:][ChartArea][\>]                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [  ][\</][syncfusion][:][Chart][\>]                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

8.   When the code runs, the following output displays.

 

{border="0"}

Figure 9: Simple Chart

***[]*** 

Customizing Chart[ ]

[] 

Adding Title to the Chart Area

1.   Select the property grid.

2.   Enter the title of the Chart in the Header field.

 

{border="0"}[]

Figure 10: Header Property

[] 

Title for the chart area is added.

[] 

{border="0"}

Figure 11: Chart Area with Title

***[]*** 

3.   To set the axis header, In the chart area properties

[] 

Click the Primary Axis drop down and enter the title in the Header field.

[] 

{border="0"}[]

Figure 12: Header Field[]

[] 

Click Secondary Axis drop down and enter the title in the Header field.

{border="0"}[]

Figure 13: Secondary Axis Header Added[]

[] 

Displaying AdormnetInfo

[] 

1.   To display the **AdornmentInfo**, set the **AdormnetInfo** property of Chart Series in Property grid.

[] 

{border="0"}

Figure 14: AdormnetInfo property

***[]*** 

2.   Select the **Visible** property.

3.   Set **SymbolWidth** and **SymbolHeight** values.

4.   Select the **Symbol Combo box** and select any one of the Symbol which has to be displayed in the info.

5.   To set the interior of the symbol, Select the **SymbolInterior** property.

6.   Users can display the content of the info based on the **SegmentLabelContent** Path property.


{border="0"}Note: Default value is LabelContentPath


[] 

The following output displays.

{border="0"}[]

Figure 15: Chart with

 

Adding Chart Area Legend

 

1.   Click Chart Area Legend.


{border="0"}Note: an expand button displays.


2.   Click the expand button. 


{border="0"}Note: Chart area smart tag displays.


3.   Click on the Add Chart Area Legend in the Chart area smart tag.

 

{border="0"}

Figure 16: Chart Area Smart Tag

 

The following output displays.

{border="0"}

Figure 17: Chart with Legend

[] 

Setting Icon Text of the Chart Legend

Set the Label property of the chart series, to set the icon text of the chart legend.

[] 

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [\<][syncfusion][:][ChartSeries][ Label][=\"FirstSeries\"][ ][ Data][=\"1,1,2,2,3,3,4,4,5,5,6,6\"\>]
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 

When the code runs, the following output displays.

 

{border="0"}

Figure 18: Chart with Icon Text For Legend

 

Consolidate Code

Consolidate Code of the above mentioned step

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<][syncfusion][:][Chart][ HorizontalAlignment][=\"Left\"][ Margin][=\"24,25,0,0\"][ Name][=\"chart1\"][ ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [VerticalAlignment][=\"Top\"][ Width][=\"371\"][ Height][=\"253\"][ Grid.Column][=\"2\"\>]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [            ][\<][syncfusion][:][ChartArea][ IsContextMenuEnabled][=\"True\"][ Header][=\"My First Chart ]                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [Control\"\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [                ][\<][syncfusion][:][ChartArea.Legend][\>]                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [                    ][\<][syncfusion][:][ChartLegend][ /\>]                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [                ][\</][syncfusion][:][ChartArea.Legend][\>]                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [                ][\<][syncfusion][:][ChartArea.SecondaryAxis][\>]                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [                    ][\<][syncfusion][:][ChartAxis][ Header][=\"Secondary Axis\" /\>]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [                ][\</][syncfusion][:][ChartArea.SecondaryAxis][\>]                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [                ][\<][syncfusion][:][ChartArea.PrimaryAxis][\>]                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [                    ][\<][syncfusion][:][ChartAxis][ Header][=\"Primary Axis\" /\>]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [                ][\</][syncfusion][:][ChartArea.PrimaryAxis][\>]                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [                ][\<][syncfusion][:][ChartSeries][ Label][=\"FirstSeries\"][ [ ]]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [Data][=\"1,1,2,2,3,3,4,4,5,5,6,6\"\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [                    ][\<][syncfusion][:][ChartSeries.AdornmentsInfo][\>]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [                        ][\<][syncfusion][:][ChartAdornmentInfo][ Visible][=\"True\"][ ]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [Symbol][=\"Hexagon\"][ SymbolWidth][=\"10\"][ SymbolHeight][=\"10\"][ ]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [LabelContentPath][=\"DataPoint.Values\[0\]\"][ SegmentShowLine][=\"False\"][                          ]                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [SegmentLabelContent][=\"LabelContentPath\"][ ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [SymbolInterior][=\"#FFE28915\"\>\</][syncfusion][:][ChartAdornmentInfo][\>]                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [                    ][\</][syncfusion][:][ChartSeries.AdornmentsInfo][\>]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [                ][\</][syncfusion][:][ChartSeries][\>]                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [            ][\</][syncfusion][:][ChartArea][\>]                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [        ][\</][syncfusion][:][Chart][\>]                                                                                                                                                                                                                                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

When the code runs, the following output displays

{border="0"}[]

Figure 19: Custimized Chart

 

[] 

[]{#related-topics}

