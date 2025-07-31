---
title: rowdataboundaction.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\rowdataboundaction.md
created_at: 2025-07-03
---






#### RowDataBound Action {#rowdatabound-action style="tab-stops: 0pt"}

 

Grid formatting can be applied to different grid row elements dynamically at run time. This can be achieved by **RowDataBound** action. It provides the **Htmlattributes** object for a cell on demand.

**RowDataBound** is raised every time a request is made to access the style information for a row. You can do any type of row formatting with this event.

It accepts **GridTableRow\<T\>** as its parameter which can be used to customize the rows of the Grid control.

The following table describes the **GridTableRow\<T\>** properties:

Properties

 

 


+----------------+--------------------------------------------------------+------------------------------+----------------------+--------------------------------------------------+
| Property       | Description                                            | Type of the property         | Value it accepts     | Any other dependencies/sub-properties associated |
+----------------+--------------------------------------------------------+------------------------------+----------------------+--------------------------------------------------+
| Data           | Gets or sets Data for the current row.                 | Generic T                    | Any data             | NA                                               |
+----------------+--------------------------------------------------------+------------------------------+----------------------+--------------------------------------------------+
| HtmlAttributes | Gets or sets the Htmlattributes for customizing cells. | IDictionary\<string,object\> | Any dictionary value | NA                                               |
|                |                                                        |                              |                      |                                                  |
|                |                                                        |                              |                      |                                                  |
+----------------+--------------------------------------------------------+------------------------------+----------------------+--------------------------------------------------+
| IsAlternate    | Indicates whether the record row is alternate.         | Boolean                      | True/False           | NA                                               |
|                |                                                        |                              |                      |                                                  |
|                |                                                        |                              |                      |                                                  |
+----------------+--------------------------------------------------------+------------------------------+----------------------+--------------------------------------------------+


 

More:







