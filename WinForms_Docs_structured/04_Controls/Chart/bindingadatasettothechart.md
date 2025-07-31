---
title: bindingadatasettothechart.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\bindingadatasettothechart.md
created_at: 2025-07-03
---








  









### Binding a DataSet to the Chart {#binding-a-dataset-to-the-chart style="tab-stops: 0pt"}

[] 

The following sample code illustrates how a custom **DataSet** can be bound to a **ChartSeries** to provide data points and to a **ChartAxis** to provide label names. Note that the DataSet can easily be replaced with a **DataTable** or **DataView**.

[] 

{border="0"}

[] 

Figure 35: Access Table data that is about to get bound to Chart

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                  |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [ChartDataBindModel model = [null];]                                                                                                                                   |
|                                                                                                                                                                                                                                 |
| [ChartDataBindAxisLabelModel xAxisLabelModel = [null];]                                                                                                                |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [// A custom DataSet bound to the Demographics table]                                                                                                                         |
|                                                                                                                                                                                                                                 |
| [private][ ChartAccessDataBind.DataSet1 dataSet11;]                                                                                        |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [this][.oleDbDataAdapter1.Fill([this].dataSet11.Demographics);]                                                       |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [model = [new] ChartDataBindModel([this].dataSet11,\"Demographics\");]                                                                            |
|                                                                                                                                                                                                                                 |
| [// The column that contains the X values.]                                                                                                                                   |
|                                                                                                                                                                                                                                 |
| [model.XName = \"ID\";]                                                                                                                                                                     |
|                                                                                                                                                                                                                                 |
| [// The columns that contain the Y values.]                                                                                                                                   |
|                                                                                                                                                                                                                                 |
| [model.YNames = [new] [string]\[\]{\"Population\"};]                                                                                              |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [ChartSeries series = [this].ChartWebControl1.Model.NewSeries(\"Data Bound Series\");]                                                                                 |
|                                                                                                                                                                                                                                 |
| [series.Text = series.Name;]                                                                                                                                                                |
|                                                                                                                                                                                                                                 |
| [series.SeriesModelImpl = model;]                                                                                                                                                           |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [series.Style.TextColor = Color.White ;]                                                                                                                                                    |
|                                                                                                                                                                                                                                 |
| [series.Style.Font.Bold = [true];]                                                                                                                                     |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [this][.ChartWebControl1.Series.Add(series);]                                                                                              |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [this][.xAxisLabelModel = [new] ChartDataBindAxisLabelModel([this].dataSet11,\"Demographics\");] |
|                                                                                                                                                                                                                                 |
| [// The columns that has the label values for the corresponding X values.]                                                                                                    |
|                                                                                                                                                                                                                                 |
| [this][.xAxisLabelModel.LabelName = \"City\";]                                                                                             |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [this][.ChartWebControl1.PrimaryXAxis.LabelsImpl = [this].xAxisLabelModel;]                                           |
|                                                                                                                                                                                                                                 |
| [this][.ChartWebControl1.PrimaryXAxis.ValueType = ChartValueType.Custom;]                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                            |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                               |
| [Dim][ model [As] ChartDataBindModel =[ Nothing]]                                              |
|                                                                                                                                                                                                                               |
| [Dim][ xAxisLabelModel [As] ChartDataBindAxisLabelModel = [Nothing]]                           |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                               |
| [\' A custom DataSet bound to the Demographics table]                                                                                                                       |
|                                                                                                                                                                                                                               |
| [Private][ dataSet11 [As] ChartAccessDataBind.DataSet1]                                                             |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                               |
| [Me][.oleDbDataAdapter1.Fill([Me].dataSet11.Demographics)]                                                          |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                               |
| [model = [New] ChartDataBindModel([Me].dataSet11,\"Demographics\")]                                                                             |
|                                                                                                                                                                                                                               |
| [\' The column that contains the X values.]                                                                                                                                 |
|                                                                                                                                                                                                                               |
| [model.XName = \"ID\"]                                                                                                                                                                    |
|                                                                                                                                                                                                                               |
| [\' The columns that contain the Y values.]                                                                                                                                 |
|                                                                                                                                                                                                                               |
| [model.YNames = [New String](){\"Population\"}]                                                                                                                      |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                               |
| [Dim][ series [As] ChartSeries = [Me].ChartWebControl1.Model.NewSeries(\"Data Bound Series\")] |
|                                                                                                                                                                                                                               |
| [series.Text = series.Name]                                                                                                                                                               |
|                                                                                                                                                                                                                               |
| [series.SeriesModelImpl = model]                                                                                                                                                          |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                               |
| [series.Style.TextColor = Color.White]                                                                                                                                                    |
|                                                                                                                                                                                                                               |
| [series.Style.Font.Bold = [True]]                                                                                                                                    |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                               |
| [Me][.ChartWebControl1.Series.Add(series)]                                                                                               |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                               |
| [Me][.xAxisLabelModel = [New] ChartDataBindAxisLabelModel(Me.dataSet11,\"Demographics\")]                           |
|                                                                                                                                                                                                                               |
| [\' The columns that has the label values for the corresponding X values.]                                                                                                  |
|                                                                                                                                                                                                                               |
| [Me][.xAxisLabelModel.LabelName = \"City\"]                                                                                              |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                               |
| [Me][.ChartWebControl1.PrimaryXAxis.LabelsImpl = [Me].xAxisLabelModel]                                              |
|                                                                                                                                                                                                                               |
| [Me][.ChartWebControl1.PrimaryXAxis.ValueType = ChartValueType.Custom]                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 36: Demographics DataSet bounded to the Chart

[]{#p25} 

[]{#related-topics}

