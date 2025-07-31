---
title: sorting2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\sorting2.md
created_at: 2025-07-03
---








  









## Sorting {#sorting style="tab-stops: 0pt"}

Sorting is defined as the process of arranging items/records in some ordered sequence. Essential Grid supports arranging table data in ascending ({border="0"}) or descending ({border="0"}) order based on the column header that is clicked. The order switches between ascending and descending each time you click a column header for sorting.

 

Multi-sorting is enabled by setting the **AllowMultiSorting** property to **True**. It can also be performed by holding CTRL and clicking the respective column headers.

The Grid control has the following properties and methods to enable sorting.

 

Properties

 


+----------------------+-------------------------------------------------------------------------------------------------------+-------------------------+------------------+--------------------------------------------------+
| Property             | Description                                                                                           | Type of property        | Value it accepts | Any other dependencies/sub-properties associated |
+----------------------+-------------------------------------------------------------------------------------------------------+-------------------------+------------------+--------------------------------------------------+
| AllowSorting         | Enables the sorting feature. Default value is False.                                                  | bool                    | True/False       | NA                                               |
+----------------------+-------------------------------------------------------------------------------------------------------+-------------------------+------------------+--------------------------------------------------+
| SortDescriptors      | Collection that is used to add sorted columns programmatically at initial load with sort directions.  | IList\<SortDescriptor\> |                  | Dependent on AllowSorting.                       |
|                      |                                                                                                       |                         |                  |                                                  |
|                      |                                                                                                       |                         |                  |                                                  |
+----------------------+-------------------------------------------------------------------------------------------------------+-------------------------+------------------+--------------------------------------------------+
| AllowMultiSorting    | Enables multicolumn sorting. Setting the value to true, will allow the user to sort multiple columns. | bool                    | True/False       | Dependent on AllowSorting.                       |
|                      |                                                                                                       |                         |                  |                                                  |
|                      | Default value is False.                                                                               |                         |                  |                                                  |
+----------------------+-------------------------------------------------------------------------------------------------------+-------------------------+------------------+--------------------------------------------------+
| DisableSortedColumns | Collection that is used to disable the sorting for individual columns.                                | List\<string\>          |                  | Dependent on AllowSorting.                       |
+----------------------+-------------------------------------------------------------------------------------------------------+-------------------------+------------------+--------------------------------------------------+


 


+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+-----------------+----------------------+
| Methods                                                  | Description                                                                                                  | Parameters      | Return type          |
+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+-----------------+----------------------+
| EnableSorting()                                          | Used to enable the sorting feature in Grid control.                                                          | No parameter    | IGridBuilder\<T\>    |
+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+-----------------+----------------------+
| AllowSorting(bool)                                       | Used to enable/disable the sorting feature.                                                                  | Enable as bool  | ISortingBuilder\<T\> |
+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+-----------------+----------------------+
| AllowMultiSorting (bool)                                 | Used to enable multicolumn sorting. Setting the value to true, will allow the user to sort multiple columns. | Enable as bool  | ISortingBuilder\<T\> |
+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+-----------------+----------------------+
| SortDescriptors(Action\<IGridSortingColumnBuilder\<T\>\> | Used to add sorted column collections programmatically at initial load with sort directions.                 | Action method   | ISortingBuilder\<T\> |
|                                                          |                                                                                                              |                 |                      |
|                                                          |                                                                                                              |                 |                      |
+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+-----------------+----------------------+


 

More:







