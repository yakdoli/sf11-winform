---
title: chartdatabindingwithienumerables.md
original_path: WinForms_Docs/04_Controls/Chart/chartdatabindingwithienumerables.md
created_at: 2025-08-05
---








  









### Chart Data Binding with IEnumerables {#chart-data-binding-with-ienumerables style="tab-stops: 0pt"}

[] 

Syncfusion chart provides an option of binding the Chart with IEnumerables, like ArrayList for Indexed or Non Indexed model data through ChartDataBindModel implementation.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                       |
|                                                                                                                                                                      |
| **[]**                                                                                                             |
|                                                                                                                                                                      |
| [class][ PopulationData]                                                        |
|                                                                                                                                                                      |
| [{]                                                                                                                              |
|                                                                                                                                                                      |
| []                                                                                                                               |
|                                                                                                                                                                      |
| [    [private] [string] city;]                                                         |
|                                                                                                                                                                      |
| []                                                                                                                               |
|                                                                                                                                                                      |
| [    [public] [string] City]                                                           |
|                                                                                                                                                                      |
| [    {]                                                                                                                          |
|                                                                                                                                                                      |
| []                                                                                                                               |
|                                                                                                                                                                      |
| [        [get] { [return] city; }]                                                     |
|                                                                                                                                                                      |
| []                                                                                                                               |
|                                                                                                                                                                      |
| [        [set] { city = [value]; }]                                                    |
|                                                                                                                                                                      |
| [    }]                                                                                                                          |
|                                                                                                                                                                      |
| []                                                                                                                               |
|                                                                                                                                                                      |
| [    [private] [double] population;]                                                   |
|                                                                                                                                                                      |
| []                                                                                                                               |
|                                                                                                                                                                      |
| [    [public] [double] Population]                                                     |
|                                                                                                                                                                      |
| [    {]                                                                                                                          |
|                                                                                                                                                                      |
| []                                                                                                                               |
|                                                                                                                                                                      |
| [        [get] { [return] population; }]                                               |
|                                                                                                                                                                      |
| []                                                                                                                               |
|                                                                                                                                                                      |
| [        [set] { population = [value]; }]                                              |
|                                                                                                                                                                      |
| []                                                                                                                               |
|                                                                                                                                                                      |
| [    }]                                                                                                                          |
|                                                                                                                                                                      |
| []                                                                                                                               |
|                                                                                                                                                                      |
| [    [public] PopulationData([string] city, [double] population)] |
|                                                                                                                                                                      |
| [    {]                                                                                                                          |
|                                                                                                                                                                      |
| [        [this].city = city;]                                                                               |
|                                                                                                                                                                      |
| [        [this].population = population;]                                                                   |
|                                                                                                                                                                      |
| [    }]                                                                                                                          |
|                                                                                                                                                                      |
| []                                                                                                                               |
|                                                                                                                                                                      |
| [}]                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                           |
|                                                                                                                                                                              |
| **[]**                                                                                                                     |
|                                                                                                                                                                              |
| [Class][ PopulationData]                                                                |
|                                                                                                                                                                              |
| []                                                                                                                                       |
|                                                                                                                                                                              |
| [    [Private] m_city [As] [String]]                                      |
|                                                                                                                                                                              |
| []                                                                                                                          |
|                                                                                                                                                                              |
| [    [Public] [Property] City() [As] [String]]       |
|                                                                                                                                                                              |
| []                                                                                                                          |
|                                                                                                                                                                              |
| [        [Get]]                                                                                                     |
|                                                                                                                                                                              |
| [            [Return] m_city]                                                                                       |
|                                                                                                                                                                              |
| [        [End] [Get]]                                                                          |
|                                                                                                                                                                              |
| []                                                                                                                          |
|                                                                                                                                                                              |
| [        [Set]([ByVal] value [As] [String])]         |
|                                                                                                                                                                              |
| [            m_city = value]                                                                                                             |
|                                                                                                                                                                              |
| [        [End] [Set]]                                                                          |
|                                                                                                                                                                              |
| [    [End] [Property]]                                                                         |
|                                                                                                                                                                              |
| []                                                                                                                          |
|                                                                                                                                                                              |
| [    [Private] m_population [As] [Double]]                                |
|                                                                                                                                                                              |
| []                                                                                                                          |
|                                                                                                                                                                              |
| [    [Public] [Property] Population() [As] [Double]] |
|                                                                                                                                                                              |
| []                                                                                                                          |
|                                                                                                                                                                              |
| [        [Get]]                                                                                                     |
|                                                                                                                                                                              |
| [            [Return] m_population]                                                                                 |
|                                                                                                                                                                              |
| [        [End] [Get]]                                                                          |
|                                                                                                                                                                              |
| []                                                                                                                          |
|                                                                                                                                                                              |
| [        [Set]([ByVal] value [As] [Double])]         |
|                                                                                                                                                                              |
| [            m_population = value]                                                                                                       |
|                                                                                                                                                                              |
| [        [End] [Set]]                                                                          |
|                                                                                                                                                                              |
| [    [End] [Property]]                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

If you have a class like above, you will have a collection of this class instances, in an ArrayList. To bind with the Chart, you need to create a ChartDataBindModel instance, by supplying the instance of data source(In our case, ArrayList is the data source).

[] 

In this example, we are binding with a Non Indexed data, with YNames alone and the chart will not be rendered with x-axis values. We need to assign the x-axis values through **ChartDataBindAxisLabelModel** class. ChartDataBindAxisLabelModel class provides a facility to bind the axis label values through the data source like ChartDataBindModel.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                          |
| [ArrayList][ populations = [new] [ArrayList]();]                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                          |
| [populations.Add([new] PopulationData([\"New York\"], 13));]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                          |
| [populations.Add([new] PopulationData([\"Houston\"], 6));]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                          |
| [populations.Add([new] PopulationData([\"Tokyo\"], 17));]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                          |
| [populations.Add([new] PopulationData([\"London\"], 15));]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                          |
| [populations.Add([new] PopulationData([\"Los Angels\"], 11));]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                          |
| [ChartSeries][ series = [new] [ChartSeries]([\"Populations\"]);]                                                                                                   |
|                                                                                                                                                                                                                                                                                                                          |
| [ChartDataBindModel][ dataSeriesModel = [new] [ChartDataBindModel](populations);]                                                                                                         |
|                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                          |
| [// If ChartDataBindModel.XName is empty or null, X value is index of point.]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                          |
| [//Here I have assigned the property name Population as Y axis name and ChartDataBindModel automatically detects the Population property and will bind the data from it.]                                                                                              |
|                                                                                                                                                                                                                                                                                                                          |
| [dataSeriesModel.YNames = [new] [string]\[\] { [\"Population\"] };]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                          |
| [//Binding the ChartDataBindModel with the Series. This is the best practise for binding with the large amount of data since it will reduce the performance issue of Chart rendering and manipulating data.]                                                           |
|                                                                                                                                                                                                                                                                                                                          |
| [series.SeriesModel = dataSeriesModel;]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                          |
| [//Since we have specified YNames only for the DataBind model, it will take the data source is non indexed model and it will ignore the X axis values. We need to assign the X axis values what we need to show on X axis by ChartDataBindAxisLableModel separately. ] |
|                                                                                                                                                                                                                                                                                                                          |
| [ChartDataBindAxisLabelModel][ dataLabelsModel = [new] [ChartDataBindAxisLabelModel](populations);]                                                                                       |
|                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                          |
| [dataLabelsModel.LabelName = [\"City\"];]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                          |
| [ChartWebControl1.Series.Add(series);]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                          |
| [ChartWebControl1.PrimaryXAxis.LabelsImpl = dataLabelsModel; ]                                                                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                          |
| [Dim][ populations [As] [New] ArrayList()]                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                          |
| [populations.Add([New] PopulationData([\"New York\"], 13)) ]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                          |
| [populations.Add([New] PopulationData([\"Houston\"], 6)) ]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                          |
| [populations.Add([New] PopulationData([\"Tokyo\"], 17)) ]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                          |
| [populations.Add([New] PopulationData([\"London\"], 15)) ]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                          |
| [populations.Add([New] PopulationData([\"Los Angels\"], 11)) ]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                          |
| [Dim][ series [As] [New] ChartSeries([\"Populations\"])]                                                                                                           |
|                                                                                                                                                                                                                                                                                                                          |
| [Dim][ dataSeriesModel [As] [New] ChartDataBindModel(populations)]                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                          |
| [\' If ChartDataBindModel.XName is empty or null, X value is index of point. ]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                          |
| [\'Here I have assigned the property name Population as Y axis name and ChartDataBindModel automatically detects the Population property and will bind the data from it. ]                                                                                             |
|                                                                                                                                                                                                                                                                                                                          |
| [dataSeriesModel.YNames = [New] [String]() {[\"Population\"]} ]                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                          |
| [\'Binding the ChartDataBindModel with the Series. This is the best practise for binding with the large amount of data since it will reduce the performance issue of Chart rendering and manipulating data. ]                                                          |
|                                                                                                                                                                                                                                                                                                                          |
| [series.SeriesModel = dataSeriesModel ]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                          |
| [\'Since we have specified YNames only for the DataBind model, it will take the data source is non indexed model and it will ignore the X axis values. We need to assign the X axis values what we need to show on X axis by ChartDataBindAxisLableModel separately. ] |
|                                                                                                                                                                                                                                                                                                                          |
| [Dim][ dataLabelsModel [As] [New] ChartDataBindAxisLabelModel(populations)]                                                                                                               |
|                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                          |
| [dataLabelsModel.LabelName = [\"City\"] ]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                          |
| [ChartWebControl1.Series.Add(series) ]                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                          |
| [ChartWebControl1.PrimaryXAxis.LabelsImpl = dataLabelsModel ]                                                                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

**[]** 

Figure 38: Chart bound with IEnumerables

[]{#p27} 

[]{#related-topics}

