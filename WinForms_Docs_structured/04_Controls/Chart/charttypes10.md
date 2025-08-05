---
title: charttypes10.md
original_path: WinForms_Docs/04_Controls/Chart/charttypes10.md
created_at: 2025-08-05
---








  









## Chart Types {#chart-types style="tab-stops: 0pt"}

Essential BI OLAP Chart for Silverlight supports the following chart types, each of which has a unique way of displaying data.

Use Case Scenarios

The user can choose any type of chart to visualize data among the available chart types. There are 20 chart types available for selectionfor example, when doing a comparison analysis  several charts can be displayed in Sales and Marketing dashboards.

Specifying the Chart Type for Chart in an Application

There are 20 chart types available andyou can use the OlapChartType property to set the expected chart type. Previously, this property was a ChartType. However, the ChartType property will exist but it will be obsolete. The main advantage of the new OlapChartType property is that you no longer need to call DataBind method after changing from one chart type to another. The following code snippets and images illustrate this in detail.

[] 

For more information refer:

[]{.UGHyperlink}

[] 

 

Table 14: OlapChartType Property

 


+---------------+--------------------------------------------------+---------------------+------------------+-----------------+
| Property      | Description                                      | Type                | Data Type        | Reference links |
+===============+==================================================+=====================+==================+=================+
| OlapChartType | Is used for selecting the particular chart type. | Dependency Property | OlapChartType,   |                 |
|               |                                                  |                     |                  |                 |
|               |                                                  |                     |                  |                 |
|               |                                                  |                     |                  |                 |
|               |                                                  |                     | Column           |                 |
|               |                                                  |                     |                  |                 |
|               |                                                  |                     | Bar              |                 |
|               |                                                  |                     |                  |                 |
|               |                                                  |                     | Area             |                 |
|               |                                                  |                     |                  |                 |
|               |                                                  |                     | Line             |                 |
|               |                                                  |                     |                  |                 |
|               |                                                  |                     | Spline           |                 |
|               |                                                  |                     |                  |                 |
|               |                                                  |                     | Scatter          |                 |
|               |                                                  |                     |                  |                 |
|               |                                                  |                     | Pie              |                 |
|               |                                                  |                     |                  |                 |
|               |                                                  |                     | StackingColumn   |                 |
|               |                                                  |                     |                  |                 |
|               |                                                  |                     | StackingCoIum100 |                 |
|               |                                                  |                     |                  |                 |
|               |                                                  |                     | StackingBar      |                 |
|               |                                                  |                     |                  |                 |
|               |                                                  |                     | StackingBarl00   |                 |
|               |                                                  |                     |                  |                 |
|               |                                                  |                     | StackingArea     |                 |
|               |                                                  |                     |                  |                 |
|               |                                                  |                     | StepArea         |                 |
|               |                                                  |                     |                  |                 |
|               |                                                  |                     | SplineArea       |                 |
|               |                                                  |                     |                  |                 |
|               |                                                  |                     | StepLine         |                 |
|               |                                                  |                     |                  |                 |
|               |                                                  |                     | RotatedSpline    |                 |
|               |                                                  |                     |                  |                 |
|               |                                                  |                     | Radar            |                 |
|               |                                                  |                     |                  |                 |
|               |                                                  |                     | Polar            |                 |
|               |                                                  |                     |                  |                 |
|               |                                                  |                     | Funnel           |                 |
|               |                                                  |                     |                  |                 |
|               |                                                  |                     | Pyramid          |                 |
+---------------+--------------------------------------------------+---------------------+------------------+-----------------+


[] 

Sample Link

To view the sample, go the sample installed location.

1.   Run the sample. Or run the BI Silverlight samples, by clicking the "Run locally installed samples" from the drop-down in the **Silverlight** ComboBox-button found in the  DashBoard under the **BI Tab**.

2\. **..\\..\\Syncfusion\\BI\\Silverlight\\Syncfusion.OlapChart.Silverlight.Samples\\Syncfusion.OlapChart.Silverlight.Samples\\Samples**

3.   Now, navigate to **OlapChart** tab in the sample browser.

 

Now, select the **Chart Gallery Demo** sample

More:











































