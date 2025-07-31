---
title: chartdata1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\chartdata1.md
created_at: 2025-07-03
---








  









## Chart Data {#chart-data style="tab-stops: 0pt"}

Built-in support for data binding

Essential Chart has built-in support for binding to DataTables, DataSets, and DataViews or any implementation of IListSource, IBindingList, or ITypedList.

The ChartSeries data points and the axis labels are the ones that can be databound.

[Binding a DataSet to the Chart]

Data binding by using custom interfaces

There is also a more flexible support for implementing custom data models by implementing specific interfaces. By using this approach you can query and provide data for the chart with much more flexibly and from any kind of data store.

[Implementing Custom Data Binding Interfaces]


{border="0"}Note: One important reason for which you might want to use either of the above two approaches is to greatly enhance performance (speed and memory), especially while dealing with a large set of data points.


 

See Also

[Chart Data Binding with IEnumerables]

More:











