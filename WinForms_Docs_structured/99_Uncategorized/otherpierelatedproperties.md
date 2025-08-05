---
title: otherpierelatedproperties.md
original_path: WinForms_Docs/99_Uncategorized/otherpierelatedproperties.md
created_at: 2025-08-05
---






##### Other Pie Related Properties {#other-pie-related-properties style="tab-stops: 0pt"}

[]{#_Insideradius}The properties that come under the other Pie related properties are the following:

[·      ]InsideRadius

[·      ]OptimizePiePointPositions

[·      ]PieWithSameRadius

[·      ]ShowTicks

[·      ]VisibleAllPies

###### []{#_Insideradius_1}5.2.1.2.9.1 Insideradius {#insideradius style="tab-stops: 0pt"}

Insideradius gets or sets the radius of the doughnut hole of the Pie chart as a fraction of the radius of the pie.


+------------------------------+---------------------------+
| Details                                                  |
+------------------------------+---------------------------+
| Possible values              | Ranges from 0.0f to 1.0f. |
+------------------------------+---------------------------+
| Default value                | None                      |
+------------------------------+---------------------------+
| 2D/3D limitations            | No                        |
+------------------------------+---------------------------+
| Application to chart element | All series                |
+------------------------------+---------------------------+
| Application to chart types   | Pie chart                 |
+------------------------------+---------------------------+


[                ]

[                                ]

{border="0"}

Figure 180: Pie chart with Insideradius 0.5f

###### []{#_OptimizePiePointPositions}5.2.1.2.9.2 OptimizePiePointPositions {#optimizepiepointpositions style="tab-stops: 0pt"}

OptimizePiePointPositions specifies if the data points with smaller values are grouped together and ordered. By default, they are ordered in the order in which the points are added to the series.


+-------------------------------------+-------------------------------------+
| Details                                                                   |
+-------------------------------------+-------------------------------------+
| Possible values                     | True - Enables optimization.        |
|                                     |                                     |
|                                     | False - Disables optimization.      |
+-------------------------------------+-------------------------------------+
| Default value                       | True                                |
+-------------------------------------+-------------------------------------+
| 2D/3D limitations                   | No                                  |
+-------------------------------------+-------------------------------------+
| Application to chart element        | Any series                          |
+-------------------------------------+-------------------------------------+
| Application to chart types          | Pie chart                           |
+-------------------------------------+-------------------------------------+


[                ]

{border="0"}

Figure 181: OptimizePiePointsPosition as false in the Pie chart

[] 

###### []{#_PieWithSameradius}5.2.1.2.9.3 PieWithSameradius {#piewithsameradius style="tab-stops: 0pt"}

PieWithSameradius gets or sets whether the Pie chart is rendered in the same radius when the LabelStyle is set to Outside or OutsideInColumn.

 


+------------------------------+-------------------------------+
| Details                                                      |
+------------------------------+-------------------------------+
| Possible values              | True or False                 |
+------------------------------+-------------------------------+
| Default value                | False                         |
+------------------------------+-------------------------------+
| 2D/3D limitations            | No                            |
+------------------------------+-------------------------------+
| Application to chart element | Any Pie series.               |
+------------------------------+-------------------------------+
| Application to chart types   | Pie chart and Doughnut chart. |
+------------------------------+-------------------------------+


[] 

[]{#_ShowTicks}Setting this property to true will allow you to display the Pie chart with the same size in the **divided area**.

[] 

{border="0"}

Figure 182: OptimizePiePointPositions as true in the Pie chart

[] 

###### []{#_ShowTicks_1}5.2.1.2.9.4 ShowTicks {#showticks style="tab-stops: 0pt"}

ShowTicks indicates whether ticks should be shown or not.


+-------------------------------------+-------------------------------------+
| Details                                                                   |
+-------------------------------------+-------------------------------------+
| Possible values                     | True - Displays ticks.              |
|                                     |                                     |
|                                     | False - Hides ticks.                |
+-------------------------------------+-------------------------------------+
| Default value                       | True                                |
+-------------------------------------+-------------------------------------+
| 2D/3D limitations                   | No                                  |
+-------------------------------------+-------------------------------------+
| Application to chart element        | Any series                          |
+-------------------------------------+-------------------------------------+
| Application to chart types          | Pie chart                           |
+-------------------------------------+-------------------------------------+


[] 

{border="0"}

Figure 183: Pie chart with ShowTicks as False

[] 

{border="0"}

Figure 184: Pie chart with ShowTicks

###### []{#_VisibleAllPies}5.2.1.2.9.5 VisibleAllPies {#visibleallpies style="tab-stops: 0pt"}

VisibleAllPies specifies whether the legend is to be displayed with one legend item for each slice in the pie.

 


+-------------------------------------+----------------------------------------------------------------------+
| Details                                                                                                    |
+-------------------------------------+----------------------------------------------------------------------+
| Possible values                     | True - Indicates only one legend item for all the slices in the pie. |
|                                     |                                                                      |
|                                     | False - Indicates one legend item for each slice in the pie.         |
+-------------------------------------+----------------------------------------------------------------------+
| Default value                       | False                                                                |
+-------------------------------------+----------------------------------------------------------------------+
| 2D/3D limitations                   | No                                                                   |
+-------------------------------------+----------------------------------------------------------------------+
| Application to chart element        | Any series                                                           |
+-------------------------------------+----------------------------------------------------------------------+
| Application to chart types          | Pie chart                                                            |
+-------------------------------------+----------------------------------------------------------------------+


[] 

{border="0"}

Figure 185: Pie chart with VisibleAllPies property

 

{border="0"}

Figure 186: Pie chart with VisibleAllPies as false

[] 

###### 5.2.1.2.9.6 Creation of Pie Chart with the Other Pie Related Properties {#creation-of-pie-chart-with-the-other-pie-related-properties style="tab-stops: 0pt"}

[] 

Pie chart with the other Pie related properties can be created in two ways:

[·      ]Builder

[·    ]ChartModel[]

[] 

5.2.1.2.9.6.1      Builder

To create a Pie chart and set its other Pie related properties through Builder:

1.   In Controller, return view to the corresponding View page.

2.   In the View page, invoke the ChartBuilder by using the control ID as the first argument.

3.   Add the **Series** to the ChartModel and [set the Chart Type to **Pie**], and add the **Points** to the series and set the style.

4.   Set the ChartModel and ChartArea properties.

5.   Set the Pie related properties, as specified in the code snippets displayed below.

[] 


\[C#\]

[        [public] [ActionResult] SimpleChart()]

[        {            ]

[            [return] View();]

[        }]


[] 


View \[ASPX\]

[    ][\<%][=][Html.Chart([\"chart_Model\"]).Text([\"Project Cost Analysis\"]).Series(series =\>]

[        {]

[            series.Add()]

[                  .Name([\"Market\"])]

[                  .Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Pie)]

[            [//\-\-\-\-\-\-\-\-\-\-\-\-\-- Add the remaining points to the series and set some stylings you want, to the series \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]]

**[                 .ExplodedIndex(2)]**

**[                  .InSideRadius(0.2f)]**

**[                  .OptimizePiePointPositions([true])]**

**[                  .ShowTicks([false])                  ]**

**[                  .ConfigItems(configItems =\> {]**

**[                      configItems.PieItem(item =\> {]**

**[                          item.PieWithSameRadius([true]);                     ]**

**[                      });]**

**[                  });]**

[        ]

[        })]

[ **             .ChartArea(area =\>{**]

**[                  area.VisibleAllPies([false]);]**

**[              })]**

[    //\-\-\-\-\-\-\-\-\-\-\-\-- Set the required properties to chartmodel to set skin, size, legend visibility and so on  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--][    ]

[    [%\>]]

[] 


[] 

[] 


View \[cshtml\]

[    ][\@{][ Html.Chart([\"chart_Model\"]).Text([\"Project Cost Analysis\"]).Series(series =\>]

[        {]

[            series.Add()]

[                  .Name([\"Market\"])]

[                  .Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Pie)]

[            [//\-\-\-\-\-\-\-\-\-\-\-\-\-- Add the remaining points to the series and set some stylings you want, to the series \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]]

**[                 .ExplodedIndex(2)]**

**[                  .InSideRadius(0.2f)]**

**[                  .OptimizePiePointPositions([true])]**

**[                  .ShowTicks([false])                  ]**

**[                  .ConfigItems(configItems =\> {]**

**[                      configItems.PieItem(item =\> {]**

**[                          item.PieWithSameRadius([true]);                     ]**

**[                      });]**

**[                  });]**

[        ]

[        })]

[ **             .ChartArea(area =\>{**]

**[                  area.VisibleAllPies([false]);]**

**[              })]**

[    //\-\-\-\-\-\-\-\-\-\-\-\-- Set the required properties to chartmodel to set skin, size, legend visibility and so on  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--][    ]

[    [}]]

[] 


[] 

[] 

[6.   ]Run the code, to get the following output:[]

[] 

{border="0"}

Figure 187: Pie chart with VisibleAllPies = false, ShowTicks = False, PieWithSameRadius = true, InSideRadius = 0.2f, and OptimizePiePointPositions = true

[] 

5.2.1.2.9.6.2      ChartModel

 

To create a Pie chart and set its other Pie related properties through ChartModel:

 

1.   In Controller, create an instance of **MVCChartModel**.

2.   Create an instance of **ChartSeries**, and set the Chart Type to **Pie**.

3.   Set the ChartSeries, ChartArea, and ChartModel properties.

4.   Set the Pie related properties, as specified in the code displayed below.

[] 


[            series1.Style.DisplayText = [true];]

[] 

[            series1.ConfigItems.PieItem.PieWithSameRadius = [true];]

[            series1.OptimizePiePointPositions = [true];]

[            series1.ShowTicks = [false];]

[            series1.InSideRadius = 0.2f;]

[] 

[            ]

[            chartModel.Series.Add(series1);]

[           chartModel.ChartArea.VisibleAllPies = [false];]

[] 


**[]** 

5.   Return view to the corresponding View page after setting the ChartModel to the ViewData.

6.   Refer to the following code snippets.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [        [public] [ActionResult] SimpleChart()]                                                                                                                                          |
|                                                                                                                                                                                                                                                                           |
| [        {            ]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                           |
| [           [MVCChartModel] chartModel = [new] [MVCChartModel]();]                                                                                               |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [            [// Create chart series and add data points to it.]]                                                                                                                                               |
|                                                                                                                                                                                                                                                                           |
| [            [ChartSeries] series1 = [new] [ChartSeries]([\"Market\"]);]                                                                 |
|                                                                                                                                                                                                                                                                           |
| [            series1.Type = [ChartSeriesType].Pie;]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                           |
| [            series1.Points.Add(0, 20);        ]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                           |
| [    //\-\-\-\-\-\-\-\-\-\-\-\-\-- Add the remaining points to the series and set some stylings you want to the series \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--]                                                             |
|                                                                                                                                                                                                                                                                           |
| **[            series1.Style.DisplayText = [true];]**                                                                                                                                                            |
|                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                           |
| **[            series1.ConfigItems.PieItem.PieWithSameRadius = [true];]**                                                                                                                                        |
|                                                                                                                                                                                                                                                                           |
| **[            series1.OptimizePiePointPositions = [true];]**                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| **[            series1.ShowTicks = [false];]**                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                           |
| **[            series1.InSideRadius = 0.2f;]**                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                           |
| **[            ]**                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| **[            chartModel.Series.Add(series1);]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                           |
| **[           chartModel.ChartArea.VisibleAllPies = [false];]**                                                                                                                                                  |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [           []]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                           |
| [          //\-\-\-\-\-\-\-\-\-\-\-\-- Set the required properties to chartmodel to set skin, size, legend visibility and so on  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--][] |
|                                                                                                                                                                                                                                                                           |
| [            ]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                           |
| [            ViewData.Model = chartModel;]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [            [return] View();]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                           |
| [}]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

7.   In the View page, invoke the ChartBuilder by using the control ID as the first argument, and convert the ViewData to **MVCChartModel** and set it as the second argument.

[] 

 


View \[ASPX\]

 

[\<%][=][ Html.Chart([\"SimpleChart\"],([MVCChartModel])ViewData.Model) [%\>]]


[] 

 


View \[cshtml\]

 

[@(][ ][new][ [HtmlString]][(][Html.Chart([\"SimpleChart\"],([MVCChartModel])ViewData.Model)][.ToString())][)][]

[] 


[8.   ]Run the code, to get the following output:[]

[] 

{border="0"}

Figure 188: Pie chart with VisibleAllPies = false, ShowTicks = False, PieWithSameRadius = true, InSideRadius = 0.2f, and OptimizePiePointPositions = true

 

See Also

[PieChart]

[] 

[]{#related-topics}

