---
title: chartmodel60.md
original_path: WinForms_Docs/04_Controls/Chart/chartmodel60.md
created_at: 2025-08-05
---








  









### ChartModel {#chartmodel style="tab-stops: 0pt"}

[] 

To export a chart through ChartModel:

[] 

Step 1:

View:

Add the code displayed below in the aspx file.

 


View \[ASPX\]

[] 

[    [\<%][\--Rendering the Chart COntrol\--][%\>]]

[] 

[     [\<%][=] Html.Chart([\"ChartModel\"],([MVCChartModel])ViewData\[[\"ChartModel\"]\]) [%\>]][]


 


View \[cshtml\]

[] 

[@\*][\--Rendering the Chart Control\--][\*@]

[] 

[@(][new][ [HtmlString]][  ][(][Html.Chart([\"ChartModel\"],([MVCChartModel])ViewData\[[\"ChartModel\"]\])][.ToString())[)]]

[] 


 

Step 2:

Controller:

Add the code displayed below in the Controller. By using the **ExportToImage** method, the chart can be exported to the server map path location. The filename and image format can be passed as a parameter to this method.

[] 


[public][ [ActionResult] Index()]

[        {]

[            [MVCChartModel] chartModel = [new] [MVCChartModel]();]

[            InitializeChart(chartModel);]

[            [//calling the ExportToImage method to export the chart in server side]]

[            chartModel.ExportToImage([\"Chart\"], [ChartImageFormat].Bmp);]

[            ViewData\[[\"ChartModel\"]\] = chartModel;]

[            [return] View();]

[] 

[        }[]]

[] 

[void][ InitializeChart([MVCChartModel] chartModel)]

[        {]

[] 

[            [ChartSeries] series;]

[            series = [new] [ChartSeries]([\"Saab\"], [ChartSeriesType].Column);]

[            series.Text = series.Name;]

[            series.Points.Add(1997, 437);]

[            series.Points.Add(1999, 311);]

[            series.Points.Add(2003, 466);]

[            chartModel.Series.Add(series);]

[            chartModel.BorderAppearance.SkinStyle = [ChartBorderSkinStyle].Emboss;]

[            chartModel.Skins = [ChartModelSkins].Office2007Blue;]

[            chartModel.ChartSeriesSkins = [ChartSeriesSkins].WarmCold;]

[        }][]


Step 3:

Run the code, to get the following output. Then the chart will be exported to the server map path location.

[] 

{border="0"}

Figure 346: Chart Export

[] 

[]{#related-topics}

