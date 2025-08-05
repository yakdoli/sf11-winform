---
title: formatting.md
original_path: WinForms_Docs/99_Uncategorized/formatting.md
created_at: 2025-08-05
---








  









## Formatting {#formatting style="tab-stops: 0pt"}

 

Essential Grid allows  you to format grid cells. You can achieve this formatting by three methods. They are:

[·      ]Using column formatting

[·      ]Using custom actions

[·      ]Using conditional formatting

 

Properties

 

 


  -------------------- --------------------------------------------------------------------------------------------- ---------------------------------------------------- --------------------------------------------------
  Property             Description                                                                                   Type of the property                                 Value it accepts
  ConditionalFormats   A collection from GridConditionalFormatDescritor that defines conditional formats for Grid.   ICollection\<GridConditionalFormatDescritor\<T\>\>   IEnumerable of GridConditionalFormatDescriptors.
  Format               Gets or sets format for the column.                                                           String                                               Any string
  CssClass             Used to CssClass for the  the Column.                                                         String                                               Any class name in string format
  -------------------- --------------------------------------------------------------------------------------------- ---------------------------------------------------- --------------------------------------------------


[] 

[] 

Methods

[] 

 


+-----------------------------------+----------------------+-------------------------+-------------------------------------------------------------------------+
| Method                            | Parameters           | Return type             | Descriptions                                                            |
+-----------------------------------+----------------------+-------------------------+-------------------------------------------------------------------------+
| QueryCellInfo(GridTableCell\<T\>) | GridTableCell\<T\>   | Void                    | Used to format the cell dynamically.                                    |
|                                   |                      |                         |                                                                         |
|                                   |                      |                         | Executed for every cell in the grid.                                    |
+-----------------------------------+----------------------+-------------------------+-------------------------------------------------------------------------+
| RowDataBound(GridTableRow\<T\>)   | GridTableRow\<T\>    | Void                    | Used to format the row dynamically. Executed for every row in the grid. |
+-----------------------------------+----------------------+-------------------------+-------------------------------------------------------------------------+
| Format(string)                    | Format string        | IGridColumnBuilder\<T\> | Used to set the format to the column.                                   |
+-----------------------------------+----------------------+-------------------------+-------------------------------------------------------------------------+
| CssClass(string)                  | Class name as string | IGridColumnBuilder\<T\> | Used to set the CssClass to the column.                                 |
+-----------------------------------+----------------------+-------------------------+-------------------------------------------------------------------------+


[] 

More:







