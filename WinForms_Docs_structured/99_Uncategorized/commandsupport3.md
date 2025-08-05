---
title: commandsupport3.md
original_path: WinForms_Docs/99_Uncategorized/commandsupport3.md
created_at: 2025-08-05
---








  









## Command Support {#command-support style="tab-stops: 0pt"}

The Spreadsheet control provides the build in commands to show case the features available in Spreadsheet. It can be executed in the Spreadsheet whenever it is bound to Command Property.

 

Table 2: Commands Table


+----------------------------------+-----------------------------------------------------------------+---------------------+-------------+-----------------+
| Property                         | Description                                                     | Type                | Data Type   | Reference links |
+----------------------------------+-----------------------------------------------------------------+---------------------+-------------+-----------------+
| BoldCommand                      | Command which will toggle bold.                                 | Dependency Property | CommandBase | NA              |
+----------------------------------+-----------------------------------------------------------------+---------------------+-------------+-----------------+
| ItalicCommand                    | Command which will toggle Italics.                              | Dependency Property | CommandBase | NA              |
+----------------------------------+-----------------------------------------------------------------+---------------------+-------------+-----------------+
| UnderlineCommand                 | Command to change the underline.                                | Dependency Property | CommandBase | NA              |
+----------------------------------+-----------------------------------------------------------------+---------------------+-------------+-----------------+
| CopyCommand                      | Command to copy the selected cells.                             | Dependency Property | CommandBase | NA              |
|                                  |                                                                 |                     |             |                 |
|                                  |                                                                 |                     |             |                 |
+----------------------------------+-----------------------------------------------------------------+---------------------+-------------+-----------------+
| CutCommand                       | Command to cut the selected cells.                              | Dependency Property | CommandBase | NA              |
|                                  |                                                                 |                     |             |                 |
|                                  |                                                                 |                     |             |                 |
+----------------------------------+-----------------------------------------------------------------+---------------------+-------------+-----------------+
| PasteCommand                     | Command to paste the cells from the clipboard.                  | Dependency Property | CommandBase | NA              |
+----------------------------------+-----------------------------------------------------------------+---------------------+-------------+-----------------+
| ColumnWidthCommand               | Command to customize the column width.                          | Dependency Property | CommandBase | NA              |
+----------------------------------+-----------------------------------------------------------------+---------------------+-------------+-----------------+
| ConditionalFormatCommand         | Command to apply conditional formatting for the selected cells. | Dependency Property | CommandBase | NA              |
+----------------------------------+-----------------------------------------------------------------+---------------------+-------------+-----------------+
| DataValidationCommand            | Command to apply data validation for the selected cells.        | Dependency Property | CommandBase | NA              |
+----------------------------------+-----------------------------------------------------------------+---------------------+-------------+-----------------+
| DeleteCommentCommand             | Command to delete the comment.                                  | Dependency Property | CommandBase | NA              |
+----------------------------------+-----------------------------------------------------------------+---------------------+-------------+-----------------+
| DeleteColumnCommand              | Command to delete column.                                       | Dependency Property | CommandBase | NA              |
+----------------------------------+-----------------------------------------------------------------+---------------------+-------------+-----------------+
| DeleteRowCommand                 | Command to delete row.                                          | Dependency Property | CommandBase | NA              |
+----------------------------------+-----------------------------------------------------------------+---------------------+-------------+-----------------+
| DeleteCurrentSheetCommand        | Command to delete current sheet.                                | Dependency Property | CommandBase | NA              |
+----------------------------------+-----------------------------------------------------------------+---------------------+-------------+-----------------+
| EncryptCommand                   | Command to encrypt the workbook.                                | Dependency Property | CommandBase | NA              |
+----------------------------------+-----------------------------------------------------------------+---------------------+-------------+-----------------+
| ExportToExcelCommand             | Command to save the workbook as Excel.                          | Dependency Property | CommandBase | NA              |
+----------------------------------+-----------------------------------------------------------------+---------------------+-------------+-----------------+
| FormatAsTableCommand             | Command to format as table.                                     | Dependency Property | CommandBase | NA              |
+----------------------------------+-----------------------------------------------------------------+---------------------+-------------+-----------------+
| HyperlinkCommand                 | Command to insert hyperlink.                                    | Dependency Property | CommandBase | NA              |
+----------------------------------+-----------------------------------------------------------------+---------------------+-------------+-----------------+
| ImportFromExcelCommand           | Command to import the Excel document to Spreadsheet.            | Dependency Property | CommandBase | NA              |
+----------------------------------+-----------------------------------------------------------------+---------------------+-------------+-----------------+
| InsertCommentCommand             | Command to insert comment.                                      | Dependency Property | CommandBase | NA              |
+----------------------------------+-----------------------------------------------------------------+---------------------+-------------+-----------------+
| InsertPictureCommand             | Command to insert picture.                                      | Dependency Property | CommandBase | NA              |
+----------------------------------+-----------------------------------------------------------------+---------------------+-------------+-----------------+
| InsertRowCommand                 | Command to insert row.                                          | Dependency Property | CommandBase | NA              |
+----------------------------------+-----------------------------------------------------------------+---------------------+-------------+-----------------+
| InsertSheetCommand               | Command to insert worksheet.                                    | Dependency Property | CommandBase | NA              |
+----------------------------------+-----------------------------------------------------------------+---------------------+-------------+-----------------+
| ProtectCurrentSheetCommand       | Command to protect current worksheet.                           | Dependency Property | CommandBase | NA              |
+----------------------------------+-----------------------------------------------------------------+---------------------+-------------+-----------------+
| ProtectWorkbookCommand           | Command to protect workbook.                                    | Dependency Property | CommandBase | NA              |
+----------------------------------+-----------------------------------------------------------------+---------------------+-------------+-----------------+
| RowHeightCommand                 | Command to customize row height.                                | Dependency Property | CommandBase | NA              |
+----------------------------------+-----------------------------------------------------------------+---------------------+-------------+-----------------+
| ShowGridLinesCommand             | Command to show or hide gridlines.                              | Dependency Property | CommandBase | NA              |
+----------------------------------+-----------------------------------------------------------------+---------------------+-------------+-----------------+
| RowColumnHeadersVisiblityCommand | Command to show or hide row and column header.                  | Dependency Property | CommandBase | NA              |
+----------------------------------+-----------------------------------------------------------------+---------------------+-------------+-----------------+


[] 

[] 

[] 

[] 

Table 3: Parameterized Commands


  ------------------------------ ----------------------------------------------------------------------------------------------------- --------------------- ------------- --------------- ----------------------------
  Property                       Description                                                                                           Type                  Data Type     Parameter       Reference links
  BorderCommand                  Command to customize the cell border.                                                                 Dependency Property   CommandBase   String          NA
  FreezePaneCommand              Command to freeze rows and column.                                                                    Dependency Property   CommandBase   Freeze          NA
  HideColumnCommand              Command to hide the column.                                                                           Dependency Property   CommandBase                   NA
  HideRowCommand                 Command to hide the row.                                                                              Dependency Property   CommandBase   Boolean         NA
  HideCurrentSheetCommand        Command to hide the current sheet.                                                                    Dependency Property   CommandBase   Boolean         NA
  VerticalAlignmentCommand       Command to align[ ]the cells vertically. []   Dependency Property   CommandBase   String          NA
  MergeCommand                   Command to merge the cells.                                                                           Dependency Property   CommandBase   String          NA
  NewCommand                     Command to add new workbook.                                                                          Dependency Property   CommandBase   Int             Creating an Excel Document
  NumberFormatCommand            Command to apply number formatting.                                                                   Dependency Property   CommandBase   String          NA
  IncreaseDecimalCommand         Command to increase decimal places.                                                                   Dependency Property   CommandBase   Boolean         NA
  IncreaseIndentCommand          Command to increase text margin.                                                                      Dependency Property   CommandBase   Boolean         NA
  InsertColumnCommand            Command to insert column.                                                                             Dependency Property   CommandBase   Boolean         NA
  HorizontalAlignmentCommand     Command to align the cells horizontally.                                                              Dependency Property   CommandBase   String          NA
  CellStyleCommand               Command to apply cell style.                                                                          Dependency Property   CommandBase   BuiltInStyles   NA
  FontFamilyCommand              Command to specify the font family.                                                                   Dependency Property   CommandBase   String          NA
  FontSizeCommand                Command to specify the font size.                                                                     Dependency Property   CommandBase   Double          NA
  ------------------------------ ----------------------------------------------------------------------------------------------------- --------------------- ------------- --------------- ----------------------------


 

[]{#related-topics}

