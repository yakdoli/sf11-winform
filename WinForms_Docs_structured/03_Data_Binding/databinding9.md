---
title: databinding9.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\databinding9.md
created_at: 2025-07-03
---








  









## Data Binding {#data-binding style="tab-stops: 0pt"}

 

This section explains how to bind a data source to the Grid control. It includes the following topics:

[·      ]LINQ to SQL data source

[·      ]ADO.NET Entity Model data source

[·      ]Generic collection

 

The following table contains some data binding properties and their corresponding descriptions:

Property

 


  ------------ ---------------------------------------------- ------------------ ----------------------- --------------------------------------------------
  Property     Description                                    Type of property   Value it accepts        Any other dependencies/sub-properties associated
  DataSource   Gets or sets DataSource for the Grid control   IEnumerable        Any IEnumerable data.   NA
  ------------ ---------------------------------------------- ------------------ ----------------------- --------------------------------------------------


 

Method

 

  ------------------------------- ------------------------ ------------------- ----------------------------------------------
  Method                          Parameters               Return type         Descriptions
  Datasource (IEnumerable\<T\>)   IEnumerable datasource   IGridBuilder\<T\>   Used to set data source to the Grid control.
  ------------------------------- ------------------------ ------------------- ----------------------------------------------

More:



















