---
title: databindingsupport2.md
original_path: WinForms_Docs/03_Data_Binding/databindingsupport2.md
created_at: 2025-08-05
---






##### Data Binding Support {#data-binding-support style="tab-stops: 0pt"}

The Data Binding feature has generated common DataModel based on the user bind underlying objects. You can use this DataModel to perform sorting and grouping operations. This can be done by using the **DataModel.View** property of ChartSeries control.  You can also bind **ObservableCollection, List, IList, CollectionViewSource, DataTable, LINQ** **results, ITypedList**, **IBindingList, BindingList** and XML data into the Chart.

[] 

The View is internally generated automatically based on the object collection bind on the **DataSource** property of ChartSeries.  You can also bind the external collection view objects into the Chart. The external collection view, SortDescription and GroupDescription are internally listened by Chart DataModel and the internal View.

[] 

This Data Binding engine improves the performance of chart with effectively handling the chart data.  The following are some of the useful tips to improve the chart performance.

[] 

[·      ]Instead of using built-in IsSortData and IsIndexed feature, you can sort the underlying business object in application level and then initialize it to **DataSource** property of ChartSeries control.

[·      ]Use **BeginInit** and **EndInit** method when you add, delete and replace multiple objects at a same time in ChartSeries control.  It helps to improve the performance.

[·      ]Disable Auto Range and Interval feature. You can manually initialize the Range and Interval to ChartAxis to get better performance.

[] 

Use Case Scenarios

In Stock market, data gets updated in a timely manner.  Initial data can be bind to chart and later you can update the underlying object.  Based on that new stock information added in your underlying object, the DataModel and the Chart Visual can refresh automatically.

 

Adding Data Binding to an Application

You can bind chart data into the **DataSource** property of ChartSeries control.  The View is generated internally for the user bound data and the chart can render in visual.  The **BindingPathX** and **BindingPathsY** properties are used to initialize the property name of the binded data.  This property values is used as coordinate values for X and Y direction in the ChartAxis control.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<][syncfusion][:][ChartSeries][ DataSource][=\"{][StaticResource][ data][}\"][ BindingPathX][=\"ProductID\"][ BindingPathsY][=\"Price\" /\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[.]

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                  |
| [            ][ProductDetails][ data = [this].Resources\[[\"data\"]\] [as] [ProductDetails];] |
|                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                  |
| [            [//Initialize the business object into the ChartSeries.]]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                  |
| [            series.DataSource = data;]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                  |
| [            series.BindingPathX = [\"ProductID\"];]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                  |
| [            series.BindingPathsY = [new] [string]\[\] { [\"Price\"] };]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                  |
| [            [//To add the SortDescription in DataModel View.]]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                  |
| [            [SortDescription] desc = [new] [SortDescription]([\"Price\"], [ListSortDirection].Descending);]                                                            |
|                                                                                                                                                                                                                                                                                                                                  |
| [            chart.Areas\[0\].Series\[0\].DataModel.View.SortDescriptions.Add(desc);]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[.]

Table 7: DataModel Table


  ----------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------ ---------------- -----------------
  Property    Description                                                                                                                                                         Type   Data Type        Reference links
  DataModel   This DataModel has internally initialized based on the user bind data on DataSource property of ChartSeries control.  It generates View for user bind DataSource.   CLR.   ChartDataModel   NA
  ----------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------ ---------------- -----------------


[] 

Table 2: ChartDataModel Table


  ---------- ------------------------------------------------------------------------------------------------------------------------------------------------------------ ------ -------------------- -----------------
  Property   Description                                                                                                                                                  Type   Data Type            Reference links
  View       This property helps to add SortDescription and GroupDescription features.  This property initializes the common view for all Collection objects initially.   CLR.   ICollectionViewAdv   NA
  ---------- ------------------------------------------------------------------------------------------------------------------------------------------------------------ ------ -------------------- -----------------


 

[]{#related-topics}

