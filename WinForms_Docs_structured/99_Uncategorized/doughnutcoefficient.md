---
title: doughnutcoefficient.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\doughnutcoefficient.md
created_at: 2025-07-03
---






##### Doughnut Co-Efficient {#doughnut-co-efficient style="tab-stops: 0pt"}

[] 

Doughnut Co-Efficient specifies the percentage of the overall radius of the chart that will be used for the Doughnut center hole. For example, if the doughnut hole is set to 0, then it will not exist, therefore, the chart will look like a Pie chart.

When the DoughnutCoeficient property is greater than zero then the Pie chart is also known as the **Doughnut chart**.

 


+------------------------------+-------------------------------+
| Details                                                      |
+------------------------------+-------------------------------+
| Possible values              | Ranges from 0.0 to 0.9.       |
+------------------------------+-------------------------------+
| Default value                | 0                             |
+------------------------------+-------------------------------+
| 2D/3D limitations            | No                            |
+------------------------------+-------------------------------+
| Application to chart element | All series                    |
+------------------------------+-------------------------------+
| Application to chart types   | Doughnut chart and Pie chart. |
+------------------------------+-------------------------------+


Pie charts with a DoughnutCoeficient specified will be rendered as doughnuts. By default, this value is set to 0.0 and hence the chart will be rendered as a full pie.

The DoughnutCoeficient property specifies the fraction of the radius occupied by the doughnut whole. Hence, the value can range from 0.0 to 0.9.

The following sample illustrates the Doughnutcoefficient property:

Pie chart with Doughnut Coefficient can be created through two ways:

[·      ]Builder

[·      ]ChartModel

 

See Also

[PieChart]

 

###### 5.2.1.2.2.1 Builder {#builder style="tab-stops: 0pt"}

[] 

To create a Pie chart and set its Doughnut Co-Efficient through Builder:

1.   In Controller, return view to the corresponding View page.

2.   In the View page, invoke the ChartBuilder by using the control ID as the first argument.

3.   Add the **Series** to the ChartModel and set the Chart Type to **Pie**, and add the **Points** to the series and set the style.

4.   Set the ChartModel and ChartArea properties.

5.   Set the Doughnut Co-Efficient, as specified in the code snippets displayed below.

[] 


\[C#\]

[        [public] [ActionResult] SimpleChart()]

[        {            ]

[            [return] View();]

[        }]


[] 


View \[ASPX\]

[     ][\<%][=][Html.Chart([\"chart_Model\"]).Text([\"Project Cost Analysis\"]).Series(series =\>]

[        {]

[            series.Add()]

[                  .Name([\"Market\"])]

[                  .Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Pie)]

[                  .Points(points =\>]

[                  {]

[                      points.Add(0, 20);]

[                      points.Add(1, 28);]

[                      points.Add(2, 23);]

[                      points.Add(3, 10);]

[                      points.Add(4, 12);]

[                      points.Add(5, 3);]

[                  })]

[                  .Style(style =\>]

[                  {]

[                      style.DisplayText([true]);]

[                  })]

[                  .Styles(styles =\> {]

[                      styles.Get(0)]

[                            .Text([\"Production\"])]

[                            .Interior([new] Syncfusion.Drawing.[BrushInfo](Syncfusion.Drawing.[GradientStyle].Horizontal, [new] System.Drawing.[Color]\[\] { System.Drawing.[Color].FromArgb(177, 140, 188), System.Drawing.[Color].FromArgb(229, 197, 221), System.Drawing.[Color].FromArgb(201, 163, 202) }));]

[                      styles.Get(1)]

[                            .Text([\"Labour\"])]

[                           .Interior([new] Syncfusion.Drawing.[BrushInfo](Syncfusion.Drawing.[GradientStyle].Horizontal, [new] System.Drawing.[Color]\[\] { System.Drawing.[Color].FromArgb(191, 62, 35), System.Drawing.[Color].FromArgb(226, 83, 37), System.Drawing.[Color].FromArgb(255, 195, 127) }));]

[                      styles.Get(2)]

[                            .Text([\"Facilities\"])]

[                           .Interior([new] Syncfusion.Drawing.[BrushInfo](Syncfusion.Drawing.[GradientStyle].Horizontal, [new] System.Drawing.[Color]\[\] { System.Drawing.[Color].FromArgb(139, 193, 58), System.Drawing.[Color].FromArgb(206, 222, 103), System.Drawing.[Color].FromArgb(227, 231, 135) }));]

[                      styles.Get(3)]

[                            .Text([\"Taxes\"])]

[                           .Interior([new] Syncfusion.Drawing.[BrushInfo](Syncfusion.Drawing.[GradientStyle].Horizontal, [new] System.Drawing.[Color]\[\] { System.Drawing.[Color].FromArgb(255, 244, 42), System.Drawing.[Color].FromArgb(253, 240, 38), System.Drawing.[Color].FromArgb(255, 216, 25) }));]

[                      styles.Get(4)]

[                            .Text([\"Insurance\"])]

[                           .Interior([new] Syncfusion.Drawing.[BrushInfo](Syncfusion.Drawing.[GradientStyle].Horizontal, [new] System.Drawing.[Color]\[\] { System.Drawing.[Color].FromArgb(112, 227, 220), System.Drawing.[Color].FromArgb(102, 175, 201), System.Drawing.[Color].FromArgb(104, 142, 191) }));]

[                      styles.Get(5)]

[                            .Text([\"Licenses\"])]

[                           .Interior([new] Syncfusion.Drawing.[BrushInfo](Syncfusion.Drawing.[GradientStyle].Horizontal, [new] System.Drawing.[Color]\[\] { System.Drawing.[Color].FromArgb(255, 141, 51), System.Drawing.[Color].FromArgb(248, 183, 56), System.Drawing.[Color].FromArgb(249, 228, 70) }));                                                                                                ]

[                                    ]

[                  })                 ]

**[                  .ConfigItems(configItems =\>]**

**[                  {]**

**[                      configItems.PieItem(item =\>]**

**[                      {]**

**[                          item.DoughnutCoeficient(0.5f);]**

**[                      });]**

**[                  });                      ]**

[        }).BorderAppearance(border =\>]

[        {]

[            border.SkinStyle(Syncfusion.Windows.Forms.Chart.[ChartBorderSkinStyle].Pinned);]

[        })    .Size([new] System.Drawing.[Size](500, 400))]

[              .Skins([ChartModelSkins].Office2007Blue)]

[              .Series3D([true])]

[              .ElementsSpacing(5) ]

[              .Font([new] System.Drawing.[Font]([\"Verdana\"], 12, System.Drawing.[FontStyle].Bold))           ]

[] 

[    ]

[    [%\>]]

[] 

[] 


[] 

[] 


View \[cshtml\]

[     ][\@{][ ][Html.Chart([\"chart_Model\"]).Text([\"Project Cost Analysis\"]).Series(series =\>]

[        {]

[            series.Add()]

[                  .Name([\"Market\"])]

[                  .Type(Syncfusion.Windows.Forms.Chart.[ChartSeriesType].Pie)]

[                  .Points(points =\>]

[                  {]

[                      points.Add(0, 20);]

[                      points.Add(1, 28);]

[                      points.Add(2, 23);]

[                      points.Add(3, 10);]

[                      points.Add(4, 12);]

[                      points.Add(5, 3);]

[                  })]

[                  .Style(style =\>]

[                  {]

[                      style.DisplayText([true]);]

[                  })]

[                  .Styles(styles =\> {]

[                      styles.Get(0)]

[                            .Text([\"Production\"])]

[                            .Interior([new] Syncfusion.Drawing.[BrushInfo](Syncfusion.Drawing.[GradientStyle].Horizontal, [new] System.Drawing.[Color]\[\] { System.Drawing.[Color].FromArgb(177, 140, 188), System.Drawing.[Color].FromArgb(229, 197, 221), System.Drawing.[Color].FromArgb(201, 163, 202) }));]

[                      styles.Get(1)]

[                            .Text([\"Labour\"])]

[                           .Interior([new] Syncfusion.Drawing.[BrushInfo](Syncfusion.Drawing.[GradientStyle].Horizontal, [new] System.Drawing.[Color]\[\] { System.Drawing.[Color].FromArgb(191, 62, 35), System.Drawing.[Color].FromArgb(226, 83, 37), System.Drawing.[Color].FromArgb(255, 195, 127) }));]

[                      styles.Get(2)]

[                            .Text([\"Facilities\"])]

[                           .Interior([new] Syncfusion.Drawing.[BrushInfo](Syncfusion.Drawing.[GradientStyle].Horizontal, [new] System.Drawing.[Color]\[\] { System.Drawing.[Color].FromArgb(139, 193, 58), System.Drawing.[Color].FromArgb(206, 222, 103), System.Drawing.[Color].FromArgb(227, 231, 135) }));]

[                      styles.Get(3)]

[                            .Text([\"Taxes\"])]

[                           .Interior([new] Syncfusion.Drawing.[BrushInfo](Syncfusion.Drawing.[GradientStyle].Horizontal, [new] System.Drawing.[Color]\[\] { System.Drawing.[Color].FromArgb(255, 244, 42), System.Drawing.[Color].FromArgb(253, 240, 38), System.Drawing.[Color].FromArgb(255, 216, 25) }));]

[                      styles.Get(4)]

[                            .Text([\"Insurance\"])]

[                           .Interior([new] Syncfusion.Drawing.[BrushInfo](Syncfusion.Drawing.[GradientStyle].Horizontal, [new] System.Drawing.[Color]\[\] { System.Drawing.[Color].FromArgb(112, 227, 220), System.Drawing.[Color].FromArgb(102, 175, 201), System.Drawing.[Color].FromArgb(104, 142, 191) }));]

[                      styles.Get(5)]

[                            .Text([\"Licenses\"])]

[                           .Interior([new] Syncfusion.Drawing.[BrushInfo](Syncfusion.Drawing.[GradientStyle].Horizontal, [new] System.Drawing.[Color]\[\] { System.Drawing.[Color].FromArgb(255, 141, 51), System.Drawing.[Color].FromArgb(248, 183, 56), System.Drawing.[Color].FromArgb(249, 228, 70) }));                                                                                                ]

[                                    ]

[                  })                 ]

**[                  .ConfigItems(configItems =\>]**

**[                  {]**

**[                      configItems.PieItem(item =\>]**

**[                      {]**

**[                          item.DoughnutCoeficient(0.5f);]**

**[                      });]**

**[                  });                      ]**

[        }).BorderAppearance(border =\>]

[        {]

[            border.SkinStyle(Syncfusion.Windows.Forms.Chart.[ChartBorderSkinStyle].Pinned);]

[        })    .Size([new] System.Drawing.[Size](500, 400))]

[              .Skins([ChartModelSkins].Office2007Blue)]

[              .Series3D([true])]

[              .ElementsSpacing(5) ]

[              .Font([new] System.Drawing.[Font]([\"Verdana\"], 12, System.Drawing.[FontStyle].Bold)).Render();           ]

[] 

[    ]

[    [}]]

[] 

[] 


[] 

6.   Build and run the code, to get the following output:

[] 

[] 

{border="0"}

Figure 157: Pie chart with Doughnut Coefficient 0.5f

[] 

[                ]

###### 5.2.1.2.2.2 ChartModel {#chartmodel style="tab-stops: 0pt"}

[] 

To create a Pie chart and set its Doughnut Co-Efficient through ChartModel:

1.   In Controller, create an instance of **MVCChartModel**.

2.   Create an instance of **ChartSeries**, and set the Chart Type to **Pie**.

3.   Set the ChartSeries, ChartArea, and ChartModel properties.

4.   Set the Doughnut Co-Efficient, as specified in the code displayed below.

series1.ConfigItems.PieItem.DoughnutCoeficient = 0.5f;

5.   Return view to the corresponding View page after setting the ChartModel to the ViewData.

6.   Refer to the below code snippets.


\[C#\]            

[        [public] [ActionResult] SimpleChart()]

[        {            ]

[            [MVCChartModel] chartModel = [new] [MVCChartModel]();]

[            [// Create chart series and add data points to it.]]

[] 

[            [ChartSeries] series1 = [new] [ChartSeries]([\"Market\"]);]

[            series1.Type = [ChartSeriesType].Pie;]

[            series1.Points.Add(0, 20);]

[            series1.Points.Add(1, 28);]

[            series1.Points.Add(2, 23);]

[            series1.Points.Add(3, 10);]

[            series1.Points.Add(4, 12);]

[            series1.Points.Add(5, 3);]

[] 

[            series1.Styles\[0\].Text = [\"Production\"];]

[            series1.Styles\[1\].Text = [\"Labour\"];]

[            series1.Styles\[2\].Text = [\"Facilities\"];]

[            series1.Styles\[3\].Text = [\"Taxes\"];]

[            series1.Styles\[4\].Text = [\"Insurance\"];]

[            series1.Styles\[5\].Text = [\"Licenses\"];]

[] 

[            series1.Style.DisplayText = [true];]

[] 

**[            series1.ConfigItems.PieItem.DoughnutCoeficient = 0.5f;]**

[] 

[            series1.Styles\[0\].Interior = [new] [BrushInfo]([GradientStyle].Horizontal, [new] [Color]\[\] { [Color].FromArgb(177, 140, 188), [Color].FromArgb(229, 197, 221), [Color].FromArgb(201, 163, 202) });]

[            series1.Styles\[1\].Interior = [new] [BrushInfo]([GradientStyle].Horizontal, [new] [Color]\[\] { [Color].FromArgb(191, 62, 35), [Color].FromArgb(226, 83, 37), [Color].FromArgb(255, 195, 127) });]

[            series1.Styles\[2\].Interior = [new] [BrushInfo]([GradientStyle].Horizontal, [new] [Color]\[\] { [Color].FromArgb(139, 193, 58), [Color].FromArgb(206, 222, 103), [Color].FromArgb(227, 231, 135) });]

[            series1.Styles\[3\].Interior = [new] [BrushInfo]([GradientStyle].Horizontal, [new] [Color]\[\] { [Color].FromArgb(255, 244, 42), [Color].FromArgb(253, 240, 38), [Color].FromArgb(255, 216, 25) });]

[            series1.Styles\[4\].Interior = [new] [BrushInfo]([GradientStyle].Horizontal, [new] [Color]\[\] { [Color].FromArgb(112, 227, 220), [Color].FromArgb(102, 175, 201), [Color].FromArgb(104, 142, 191) });]

[            series1.Styles\[5\].Interior = [new] [BrushInfo]([GradientStyle].Horizontal, [new] [Color]\[\] { [Color].FromArgb(255, 141, 51), [Color].FromArgb(248, 183, 56), [Color].FromArgb(249, 228, 70) });]

[] 

[] 

[            chartModel.Series.Add(series1);]

[] 

[] 

[            chartModel.Text = [\"Project Cost Analysis\"];]

[            chartModel.Font = [new] [Font]([\"Verdana\"], 12, [FontStyle].Bold);]

[] 

[            chartModel.Series3D = [true];]

[            chartModel.ElementsSpacing = 5;]

[            chartModel.Skins = [ChartModelSkins].Office2007Blue;]

[] 

[            chartModel.SmoothingMode = System.Drawing.Drawing2D.[SmoothingMode].AntiAlias;]

[            chartModel.BorderAppearance.SkinStyle = [ChartBorderSkinStyle].Pinned;]

[] 

[            chartModel.Size = [new] System.Drawing.[Size](500, 400);]

[            ViewData.Model = chartModel;]

[] 

[            [return] View();]

[}]

[] 


[] 

7.   In the View page, invoke the ChartBuilder by using the control ID as the first argument, and convert the ViewData to **MVCChartModel** and set it as the second argument.

[] 


View \[ASPX\]

 

[\<%][=][ Html.Chart([\"SimpleChart\"],([MVCChartModel])ViewData.Model) [%\>]][]


 

[] 


View \[cshtml\]

 

[@(][ ][new][ [HtmlString]][(Html.Chart([\"SimpleChart\"],([MVCChartModel])ViewData.Model).ToString())][)][]

 


 

 

8.   Build and run the code, to get the following output:

[] 

{border="0"}

Figure 158: Pie chart with Doughnut Coefficient 0.5f

[] 

[]{#related-topics}

