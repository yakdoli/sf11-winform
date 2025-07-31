---
title: chartdata5.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Chart\chartdata5.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






   


## Chart Data {#chart-data style="tab-stops: 0pt"}

Built-in support for data binding

Essential Chart has built-in support for binding to IEnumerable.

The ChartSeries,data points and the axis labels are the ones that can be databound.

 

Series properties

  -------- ------------------------------------------------------------------------------------------------------------------- ---------------------- ------------------ ------------
  Name     Description                                                                                                         Type of the property   Value it accepts   Dependency
  BindTo   This property allows you to get or set the data source of the series and fields that are used to render the axes.   ChartAdvDataBind       ChartAdvDataBind   NA
  -------- ------------------------------------------------------------------------------------------------------------------- ---------------------- ------------------ ------------

 

ChartAdvDataBind Properties

+-------------+-----------------------------------------------------------------------+----------------------+------------------+------------------------------------------------------------------------------------------------------+
| Name        | Description                                                           | Type of the property | Value it accepts | Dependency                                                                                           |
+-------------+-----------------------------------------------------------------------+----------------------+------------------+------------------------------------------------------------------------------------------------------+
| DataSource  | This property allows you to get or set the data source of the series. | IEnumerable          | IEnumerable      | NA                                                                                                   |
+-------------+-----------------------------------------------------------------------+----------------------+------------------+------------------------------------------------------------------------------------------------------+
| XName       | Allows you to get or set the field name of the X axis.                | String               | Any string value | Depends on DataSource---                                                                             |
|             |                                                                       |                      |                  |                                                                                                      |
|             |                                                                       |                      |                  | DataSource should be set and the field name should be the same as any entry in the IEnumerable list. |
+-------------+-----------------------------------------------------------------------+----------------------+------------------+------------------------------------------------------------------------------------------------------+
| YNames      | Allows you to get or set the field names of the Y axis.               | String\[\]           | Any string array | Depends on DataSource\--\                                                                            |
|             |                                                                       |                      |                  | DataSource should be set and the field name should be the same as any entry in the IEnumerable list. |
+-------------+-----------------------------------------------------------------------+----------------------+------------------+------------------------------------------------------------------------------------------------------+

 

More:





