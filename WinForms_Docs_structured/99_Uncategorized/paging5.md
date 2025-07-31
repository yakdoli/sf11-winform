---
title: paging5.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\paging5.md
created_at: 2025-07-03
---








  









## Paging {#paging style="tab-stops: 0pt"}

Essential Grid for Mobile MVC offers complete navigation support to easily switch between the pages through swipe-up and swipe-down actions on the grid content area. Also, a pager bar will be available at the bottom of the page and it will be visible only on swiping the grid content area. It facilitates splitting up huge grid data and displays viewable sets of grid rows on each page.

The Grid control for MVC exposes the following properties and methods to enable and control the paging feature.

Properties


+------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+----------------------+------------------------------------------------------+
| [ ]**Property** | **Description**                                                                                                                                                                                            | **Type of Property** | **Value it Accepts** | **Any Other Dependencies/Sub-Properties Associated** |
+------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+----------------------+------------------------------------------------------+
| AllowPaging                              | Enables the paging feature.                                                                                                                                                                                | Boolean              | True/false           | NA                                                   |
|                                          |                                                                                                                                                                                                            |                      |                      |                                                      |
|                                          |                                                                                                                                                                                                            |                      |                      |                                                      |
+------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+----------------------+------------------------------------------------------+
| PageSize                                 | Sets the number of records to be displayed in a single grid page. The same number of records will be available for the next page and you will be able to navigate between these pages using the pager bar. | Int                  | +ve Integers         | Dependent on AllowPaging                             |
+------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+----------------------+------------------------------------------------------+
| ShowPager(bool)                          | Sets whether the pager bar should be displayed at the bottom of the page or not.                                                                                                                           | bool                 | True/false           | Dependent on AllowPaging                             |
+------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+----------------------+------------------------------------------------------+
| CurrentPage                              | Set the current page to the Grid control.                                                                                                                                                                  | Int                  | +ve Intergers        | Dependent on AllowPaging                             |
+------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------+----------------------+------------------------------------------------------+


[] 

**[Methods]**


  -------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------- -------------------
  **Method**           **Descriptions**                                                                                                                                                                                          **Parameters**                   **Return type**
  EnablePaging()       Used to enable the paging feature in the Grid control.                                                                                                                                                    No parameter                     IGridBuilder\<T\>
  AllowPaging(bool)    Used to enable/disable the paging feature.                                                                                                                                                                Enable as bool                   PageBuilder
  PageSize(Int32)      Sets the number of records to be displayed in a single grid page. The same number of records will be available for the next page and you will be able to navigate between these pages using pager bars.   Page size as integer             PageBuilder 
  ShowPager(bool)      Sets whether the pager bar should be displayed at the bottom of the page or not.                                                                                                                          ShowPager  as bool               PageBuilder 
  CurrentPage(Int32)   Set the current page to the Grid control.                                                                                                                                                                 Current page number as integer   PageBuilder
  -------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------- -------------------


More:







