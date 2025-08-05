---
title: chartdata.md
original_path: WinForms_Docs/04_Controls/Chart/chartdata.md
created_at: 2025-08-05
---








  









## Chart Data {#chart-data style="tab-stops: 0pt"}

[] 

Built-in Support for data binding

**[]** 

Essential Chart has built-in support for binding to **DataTables**, **DataSets**, **DataViews** or any implementation of **IListSource**, **IBindingList** or **ITypedList**.

 

The **ChartSeries** data points and the axis labels are the ones that can be databound.

 

There is however no DESIGN TIME support for data binding. This has to be setup in code.

[] 

[]{.UGHyperlink}

[] 

Data binding via custom interfaces

[] 

There is also a more flexible support for implementing custom data models by implementing specific interfaces. Using this approach you can query and provide data for the chart much more flexibly and from any kind of data store.

[] 

[]{.UGHyperlink}

[] 


{border="0"}Note: One important reason you might want to use either of the above two approaches is to greatly enhance performance (speed and memory) especially while dealing with a large set of data points.


[] 

See Also

[] 

[]{.UGHyperlink}

[]{#p24} 

 

More:









