---
title: querycellinfoaction.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\querycellinfoaction.md
created_at: 2025-07-03
---






#### QueryCellInfo Action {#querycellinfo-action style="tab-stops: 0pt"}

Grid formatting can be applied to different grid cell elements dynamically at run time. This can be achieved by proper handling of **QueryCellInfo** action. It provides the **Htmlattributes** object for a cell on demand.

**QueryCellInfo** is raised every time a request is made to access the style information for a cell. You can do any type of formatting cells with this event.

It accepts **GridTableCell\<T\>** as its parameter, which can be used to customize the cells of the grid control. For instance, you can apply styles for a given cellType by using the **TableCellType** property on the instances of **GridTableCell\<T\>**.

The following table describes the **GridTableCell\<T\>** properties:

 

Properties

[] 

 


+----------------+--------------------------------------------------------+------------------------------+------------------------------------------------+--------------------------------------------------+
| Property       | Description                                            | Type of property             | Value it accepts                               | Any other dependencies/sub-properties associated |
+================+========================================================+==============================+================================================+==================================================+
| Data           | Gets or sets data value of querycell.                  | Generic T                    | Any data                                       | NA                                               |
+----------------+--------------------------------------------------------+------------------------------+------------------------------------------------+--------------------------------------------------+
| Column         | Gets or sets the column type of the querycell.         | GridColumn\<T\>              | Any GridColumn\<T\>                            | NA                                               |
|                |                                                        |                              |                                                |                                                  |
|                |                                                        |                              |                                                |                                                  |
+----------------+--------------------------------------------------------+------------------------------+------------------------------------------------+--------------------------------------------------+
| HtmlAttributes | Gets or sets the Htmlattributes for customizing cells. | IDictionary\<string,object\> |                                                | NA                                               |
|                |                                                        |                              |                                                |                                                  |
|                |                                                        |                              |                                                |                                                  |
+----------------+--------------------------------------------------------+------------------------------+------------------------------------------------+--------------------------------------------------+
| Text           | Gets or sets the value renders in cell.                | object                       | Any object                                     | NA                                               |
+----------------+--------------------------------------------------------+------------------------------+------------------------------------------------+--------------------------------------------------+
| TableCellType  | Gets or sets the table cell type of the querycell.     | Enum                         | GridTableCellType.GroupCaptionCell             | NA                                               |
|                |                                                        |                              |                                                |                                                  |
|                |                                                        |                              | GridTableCellType.GroupHeaderIndentCell        |                                                  |
|                |                                                        |                              |                                                |                                                  |
|                |                                                        |                              | GridTableCellType.SummaryFieldCell             |                                                  |
|                |                                                        |                              |                                                |                                                  |
|                |                                                        |                              | GridTableCellType.IndentCell                   |                                                  |
|                |                                                        |                              |                                                |                                                  |
|                |                                                        |                              | GridTableCellType.TopLeftHeaderCell            |                                                  |
|                |                                                        |                              |                                                |                                                  |
|                |                                                        |                              | GridTableCellType.RowHeaderCell                |                                                  |
|                |                                                        |                              |                                                |                                                  |
|                |                                                        |                              | GridTableCellType.ColumnHeaderCell             |                                                  |
|                |                                                        |                              |                                                |                                                  |
|                |                                                        |                              | GridTableCellType.RecordPlusMinusCell          |                                                  |
|                |                                                        |                              |                                                |                                                  |
|                |                                                        |                              | GridTableCellType.RecordFieldCell              |                                                  |
|                |                                                        |                              |                                                |                                                  |
|                |                                                        |                              | GridTableCellType.AlternateRecordFieldCell     |                                                  |
|                |                                                        |                              |                                                |                                                  |
|                |                                                        |                              | GridTableCellType.AlternateRecordRowHeaderCell |                                                  |
|                |                                                        |                              |                                                |                                                  |
|                |                                                        |                              | GridTableCellType.EmptyCell                    |                                                  |
|                |                                                        |                              |                                                |                                                  |
|                |                                                        |                              | GridTableCellType.CaptionCell                  |                                                  |
|                |                                                        |                              |                                                |                                                  |
|                |                                                        |                              |                                                |                                                  |
+----------------+--------------------------------------------------------+------------------------------+------------------------------------------------+--------------------------------------------------+


More:







