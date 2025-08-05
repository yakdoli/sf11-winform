---
title: servermode4.md
original_path: WinForms_Docs/99_Uncategorized/servermode4.md
created_at: 2025-08-05
---








  









### Server Mode {#server-mode style="tab-stops: 0pt"}

Grouping is defined as the act or process of consolidating grid data into groups. Grouping allows the categorization of records based on specified columns. You can easily group by a particular column by simply dragging the column to the upper portion of the grid. The grid data is automatically grouped when you drop a particular column. You are also able to expand a grouped record by clicking the {border="0"} icon beside the grouped record.

The Grid control has the following properties and methods which enable and control the grouping feature.

Properties

 


+------------------+----------------------------------------------------------------------------------+------------------+------------------+--------------------------------------------------+
| Property         | Description                                                                      | Type of property | Value it accepts | Any other dependencies/sub-properties associated |
+------------------+----------------------------------------------------------------------------------+------------------+------------------+--------------------------------------------------+
| AllowGrouping    | Enables the grouping feature.                                                    | bool             | True/False       | NA                                               |
|                  |                                                                                  |                  |                  |                                                  |
|                  | Default value is False.                                                          |                  |                  |                                                  |
+------------------+----------------------------------------------------------------------------------+------------------+------------------+--------------------------------------------------+
| GroupDescriptors | Collection that is used to add grouped columns programmatically at initial load. | List\<string\>   |                  | Dependent on AllowGrouping.                      |
|                  |                                                                                  |                  |                  |                                                  |
|                  |                                                                                  |                  |                  |                                                  |
+------------------+----------------------------------------------------------------------------------+------------------+------------------+--------------------------------------------------+


 

Methods

 


  ---------------------------------------- --------------------------------- ----------------------- ------------------------------------------------------------------------------
  Method                                   Parameters                        Return type             Descriptions
  EnableGrouping()                         No parameter                      IGridBuilder\<T\>       Used to enable the grouping feature in the Grid control.
  AllowGrouping(bool)                      Enable as bool                    IGroupingBuilder\<T\>   Used to enable/disable the grouping feature.
  Groups (Action\<IGroupingBuilder\<T\>)   Action\<IGroupingBuilder\<T\>\>   IGroupingBuilder\<T\>   Used to add the grouped columns collection programmatically at initial load.
  ---------------------------------------- --------------------------------- ----------------------- ------------------------------------------------------------------------------


 

More:







