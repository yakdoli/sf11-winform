---
title: howtoprotectcertaincellsinaspreadsheet.md
original_path: WinForms_Docs/99_Uncategorized/howtoprotectcertaincellsinaspreadsheet.md
created_at: 2025-08-05
---








  









### How to protect certain cells in a spreadsheet? {#how-to-protect-certain-cells-in-a-spreadsheet style="tab-stops: 0pt"}

 

All the cells in an Excel spreadsheet have a Locked property, which determines if the cell will be editable when the worksheet is protected. All the cells are set to \"Locked\", by default. Hence when a worksheet is protected, all the cells in the worksheet get protected, by default.

 

However, there is often a need to protect only certain cells in a worksheet. In this scenario, you need to protect a worksheet, and set the IsLocked property to false for the cells that need to be made editable.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                 |
|                                                                                                                                                                  |
| []                                                                                                                           |
|                                                                                                                                                                  |
| [// Sample data]                                                                                               |
|                                                                                                                                                                  |
| [sheetOne.Range\[[\"A1:K20\"]\].Text = [\"Locked\"];]                          |
|                                                                                                                                                                  |
| []                                                                                                                           |
|                                                                                                                                                                  |
| [// A1:A10 will not be protected.]                                                                             |
|                                                                                                                                                                  |
| [sheetOne.Range\[[\"A1:A10\"]\].CellStyle.Locked = [false];]                     |
|                                                                                                                                                                  |
| [sheetOne.Range\[[\"A1:A10\"]\].Text = [\"UnLocked\"];]                        |
|                                                                                                                                                                  |
| [sheetOne.Protect([\"syncfusion\"], [ExcelSheetProtection].FormattingColumns); ] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                 |
|                                                                                                                                                                                                      |
| []                                                                                                                                                               |
|                                                                                                                                                                                                      |
| [\' Sample data  ]                                                                                                                                 |
|                                                                                                                                                                                                      |
| [Private][ sheetOne.Range([\"A1:K20\"]).Text = [\"Locked\"]]      |
|                                                                                                                                                                                                      |
| []                                                                                                                                                |
|                                                                                                                                                                                                      |
| [\' A1:A10 will not be protected. ]                                                                                                                |
|                                                                                                                                                                                                      |
| [Private][ sheetOne.Range([\"A1:A10\"]).CellStyle.Locked = [False]] |
|                                                                                                                                                                                                      |
| [Private][ sheetOne.Range([\"A1:A10\"]).Text = [\"UnLocked\"]]    |
|                                                                                                                                                                                                      |
| [sheetOne.Protect([\"syncfusion\"], ExcelSheetProtection.FormattingColumns)]                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: Locking/Unlocking cells in an unprotected worksheet has no effect.


 

[]{#related-topics}

