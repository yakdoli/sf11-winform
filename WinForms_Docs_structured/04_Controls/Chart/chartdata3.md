---
title: chartdata3.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\chartdata3.md
created_at: 2025-07-03
---








  









## Chart Data {#chart-data style="tab-stops: 0pt"}

Built-in Support for Data Binding

Essential Chart has built-in support for binding to IEnumerable data sources.

The chart series, data points, and axis labels are the ones that can be data-bound.

 

Series properties

  -------- ----------------------------------------------------------------------------------------------------- ------------------ ------------------ ------------
  Name     Description                                                                                           Property Type      Value it Accepts   Dependency
  BindTo   Allows you to get or set the data source of the series and fields that are used to render the axes.   ChartAdvDataBind   ChartAdvDataBind   NA
  -------- ----------------------------------------------------------------------------------------------------- ------------------ ------------------ ------------

 

ChartAdvDataBind Properties

  ------------ --------------------------------------------------------- --------------- ------------------ ------------------------------------------------------------------------------------------------------------------------------
  Name         Description                                               Property Type   Value it Accepts   Dependency
  DataSource   Allows you to get or set the data source of the series.   IEnumerable     IEnumerable        NA
  XName        Allows you to get or set the field name of the x-axis.    String          Any string value   Depends on DataSource---DataSource should be set and the field name should be the same as any entry in the IEnumerable list.
  YNames       Allows you to get or set the field names of the y-axis.   String\[\]      Any string array   Depends on DataSource---DataSource should be set and the field name should be the same as any entry in the IEnumerable list.
  ------------ --------------------------------------------------------- --------------- ------------------ ------------------------------------------------------------------------------------------------------------------------------

 

More:





