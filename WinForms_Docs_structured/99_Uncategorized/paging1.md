---
title: paging1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\paging1.md
created_at: 2025-07-03
---








  









## Paging {#paging style="tab-stops: 0pt"}

Essential Grid offers complete navigation support to easily switch between the pages using the pager bar available at the bottom of the Grid control. It facilitates splitting up huge grid data and displays viewable sets of Grid rows on each page. By selecting the respective page numbers you can navigate to the other pages. You can also limit the number of pages.

The Grid control for MVC exposes the following properties and methods to enable and control the paging feature.

Properties

 


+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+------------------+--------------------------------------------------+
| Property    | Description                                                                                                                                                                                                | Type of property | Value it accepts | Any other dependencies/sub-properties associated |
+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+------------------+--------------------------------------------------+
| AllowPaging | Enables the paging feature.                                                                                                                                                                                | Boolean          | True/false       | NA                                               |
|             |                                                                                                                                                                                                            |                  |                  |                                                  |
|             |                                                                                                                                                                                                            |                  |                  |                                                  |
+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+------------------+--------------------------------------------------+
| PageSize    | Sets the number of records to be displayed in a single grid page. The same number of records will be available for the next page and you will be able to navigate between these pages using the pager bar. | Int              | +ve Integers     | Dependent on AllowPaging                         |
|             |                                                                                                                                                                                                            |                  |                  |                                                  |
|             | Default page size is 12.                                                                                                                                                                                   |                  |                  |                                                  |
+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+------------------+--------------------------------------------------+
| PageCount   | Sets the number of pages to be displayed in the pager bar. You can limit the number of pages to be displayed using this property.                                                                          | Int              | +ve Integers     | Dependent on AllowPaging                         |
|             |                                                                                                                                                                                                            |                  |                  |                                                  |
|             | Default page count is 10.                                                                                                                                                                                  |                  |                  |                                                  |
+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+------------------+--------------------------------------------------+
| CurrentPage | Set the current page to the Grid control.                                                                                                                                                                  | Int              | +ve Intergers    | Dependent on AllowPaging                         |
+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+------------------+--------------------------------------------------+


 

Methods

 


+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------+-------------------+
| Method             | Descriptions                                                                                                                                                                                            | Parameters                     | Return type       |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------+-------------------+
| EnablePaging()     | Used to enable the paging feature in the Grid control.                                                                                                                                                  | No parameter                   | IGridBuilder\<T\> |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------+-------------------+
| AllowPaging(bool)  | Used to enable/disable the paging feature.                                                                                                                                                              | Enable as bool                 | IPagerBuilder     |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------+-------------------+
| PageSize(Int32)    | Sets the number of records to be displayed in a single grid page. The same number of records will be available for the next page and you will be able to navigate between these pages using pager bars. | Page size as integer           | IPagerBuilder     |
|                    |                                                                                                                                                                                                         |                                |                   |
|                    |                                                                                                                                                                                                         |                                |                   |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------+-------------------+
| PageCount(Int32)   | Sets the number of pages to be displayed in the pager bar. You can limit the number of pages to be displayed using this property.                                                                       | Page count as integer          | IPagerBuilder     |
|                    |                                                                                                                                                                                                         |                                |                   |
|                    |                                                                                                                                                                                                         |                                |                   |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------+-------------------+
| CurrentPage(Int32) | Set the current page to the Grid control.                                                                                                                                                               | Current page number as integer | IPagerBuilder     |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------+-------------------+


More:









