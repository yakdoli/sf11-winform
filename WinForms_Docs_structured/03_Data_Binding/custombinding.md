---
title: custombinding.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\custombinding.md
created_at: 2025-07-03
---








  









### Custom Binding {#custom-binding style="tab-stops: 0pt"}

Essential Grid processes the data source by using the built-in LINQ expressions to perform paging, sorting, grouping, filtering, and editing actions. However, in some cases you may want to bypass the built-in data source processing and process the data manually. This is called "custom binding."****

Essential Grid supports custom binding to perform paging, sorting, and filtering actions.

 

Properties

 


+------------------+----------------------------------------------------------------+------------------+--------------------+--------------------------------------------------+
| Property         | Description                                                    | Type of property | Value it accepts   | Any other dependencies/sub-properties associated |
+------------------+----------------------------------------------------------------+------------------+--------------------+--------------------------------------------------+
| EnableOnDemand   | Gets or sets a value indicating whether OnDemand is enabled.   | Boolean          | True/false         | NA                                               |
+------------------+----------------------------------------------------------------+------------------+--------------------+--------------------------------------------------+
| TotalRecordCount | Gets or sets the total record count.                           | Long             | 0 to long.MaxValue |                                                  |
|                  |                                                                |                  |                    |                                                  |
|                  |                                                                |                  |                    |                                                  |
+------------------+----------------------------------------------------------------+------------------+--------------------+--------------------------------------------------+
| EnableOnDemand   | Gets or sets the value indicating whether OnDemand is enabled. | Boolean          | True/false         |                                                  |
+------------------+----------------------------------------------------------------+------------------+--------------------+--------------------------------------------------+


 

Methods

 

+-----------------------------------------+------------------------------------------------------------------------------------------+--------------------------+-------------------------------+
| Method                                  | Description                                                                              | Parameters               | Return type                   |
+-----------------------------------------+------------------------------------------------------------------------------------------+--------------------------+-------------------------------+
| EnableOnDemand()                        | Used to enable the custom binding mode to True.                                          | \-\--                    | IGridBuilder\<T\>             |
|                                         |                                                                                          |                          |                               |
|                                         |                                                                                          |                          |                               |
+-----------------------------------------+------------------------------------------------------------------------------------------+--------------------------+-------------------------------+
| TotalRecordCount()                      | Used to set the total record count.                                                      | Long                     | 0 to long.MaxValue            |
|                                         |                                                                                          |                          |                               |
|                                         |                                                                                          |                          |                               |
+-----------------------------------------+------------------------------------------------------------------------------------------+--------------------------+-------------------------------+
| Where(List\<FilterConditions\> filters) | **IQueryable** extension method is used to filter the record from the given data source. | List of FilterConditions | Filter conditions collections |
+-----------------------------------------+------------------------------------------------------------------------------------------+--------------------------+-------------------------------+
| GridActions\<T\>(Long totalrecordcount) | **GridActionResult** method is used to call the custom binding grid post actions.        | Total record count       | Action result                 |
+-----------------------------------------+------------------------------------------------------------------------------------------+--------------------------+-------------------------------+

 

You can work with the custom binding feature through two ways:

[·      ]GridBuilder

[·      ]GridPropertiesModel

More:







