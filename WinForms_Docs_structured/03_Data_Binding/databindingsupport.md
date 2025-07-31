---
title: databindingsupport.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\databindingsupport.md
created_at: 2025-07-03
---








  









### Data Binding support {#data-binding-support style="tab-stops: 0pt"}

The Data Binding feature has generated a common DataModel class based on the user bind underlying objects. You can use this Data Model to perform sorting and grouping operations. This can be done by using the DataModel.View property of ChartSeries control.  You can also bind ObservableCollection, List, IList, CollectionViewSource, LINQ results into the Chart.

 

The View is internally generated automatically based on the object collection bind on the DataSource property of ChartSeries.  You can also bind the external collection view objects into the Chart. The external collection view, SortDescription and GroupDescription are internally listened by Chart DataModel and the internal View.

**[]** 

Use Case Scenarios

In Stock market, data gets updated in a timely manner.  Initial data can be bind to Chart and later you can update the underlying object.  Based on that new stock information added in your underlying object, the DataModel and the Chart Visual can refresh automatically.

[] 

Adding Data Binding to an Application

You can bind chart data into the DataSource property of the ChartSeries control.  The View is generated internally for the user bound data and the chart can render in visual.  The BindingPathX and BindingPathsY properties are used to initialize the property name of the binded data.  This property values is used as co-ordinate values for X and Y direction in the ChartAxis control.

**[]** 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[XAML\]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<][syncfusion][:][ChartSeries][ DataSource][=\"{][StaticResource][ data][}\"][ BindingPathX][=\"ProductID\"][ BindingPathsY][=\"Price\" /\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[.]

**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                  |
| [            ][ProductDetails][ data = [this].Resources\[[\"data\"]\] [as] [ProductDetails];] |
|                                                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                  |
| [            [//Initialize the business object into the ChartSeries.]]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                  |
| [            series.DataSource = data;]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                  |
| [            series.BindingPathX = [\"ProductID\"];]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                  |
| [            series.BindingPathsY = [new] [string]\[\] { [\"Price\"] };]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                                                                       |
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

Properties

Table 1: DataModel Table

  ------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------
  Property                                                                              Description                                                                                                                                                                                                                                  Type                                                                           Data Type                                                                                  Reference links
  [[DataModel ]]{.18}   [[This DataModel has internally initialized based on the user bind data on DataSource property of ChartSeries control.  It generates View for user bind DataSource.]]{.18}   [[CLR]]{.18}   [[ChartDataModel ]]{.18}   [[NA ]]{.18}
  ------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------ ------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------

**[]** 

Table 2: ChartDataModel Table

  -------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------
  Property                                                                         Description                                                                                                                                                                                                                          Type                                                                           Data Type                                                                                      Reference links
  [[View ]]{.18}   [[This property helps to add SortDescription and GroupDescription features.  This property initializes the common view for all Collection objects initially]]{.18}   [[CLR]]{.18}   [[ICollectionViewAdv ]]{.18}   [[NA ]]{.18}
  -------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------

 

 

[]{#related-topics}

