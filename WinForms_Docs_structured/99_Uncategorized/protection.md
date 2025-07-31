---
title: protection.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\protection.md
created_at: 2025-07-03
---






##### Protection {#protection style="tab-stops: 0pt"}

[] 

Excel provides various options to protect worksheet and workbook elements. Protection prevents a user from accidentally or deliberately changing, moving, or deleting important data. There are various options to protect worksheets and workbooks.

 

 Refer to the  section for more details.

 

This section explains how cell protection can be applied in MS Excel by using XlsIO.

 

###### []{#p68}[]{#_Lock_Cells}4.1.3.3.4.1 Lock Cells {#lock-cells style="tab-stops: 0pt"}

 

Cell modification can be prevented by locking the cell, by using the **Protection** tab in the **Format** **Cells** dialog box.

 

{border="0"}

Figure 71: Format Cells dialog - Protection[]

[] 

[] 

This will prompt the following error message at run time, when a user tries to modify the cell.

[] 

{border="0"}

Figure 72: Error on modifying the protected cell[]

[] 

Locking and Unlocking in XlsIO

[] 

XlsIO supports locking and unlocking cells by using the cell\'s **Locked** property, which can be manipulated to make certain cells editable in a protected worksheet. Please note that locking/unlocking a cell in an unprotected worksheet has no effect. For protecting the worksheet, see .

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                       |
|                                                                                                                                                                                                        |
| **[]**                                                                                                                                                             |
|                                                                                                                                                                                                        |
| [// Opening the Existing (Protected) Worksheet from a Workbook]                                                                                      |
|                                                                                                                                                                                                        |
| [IWorkbook][ workbook = application.Workbooks.Open([\"CellProtectionTemplate.xls\"]);] |
|                                                                                                                                                                                                        |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                        |
| [// Unlocking the cell which, need to be edited.]                                                                                                    |
|                                                                                                                                                                                                        |
| [sheet.Range\[[\"A1\"]\].CellStyle.Locked = [false];]                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                                                      |
|                                                                                                                                                                                                                                 |
| [\' Opening the Existing (Protected) Worksheet from a Workbook]                                                                                                               |
|                                                                                                                                                                                                                                 |
| [Dim][ workbook [As] IWorkbook = application.Workbooks.Open([\"CellProtectionTemplate.xls\"])] |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [\' Unlocking the cells which, need to be edited.]                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [sheet.Range([\"A1\"]).CellStyle.Locked = [False]]                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

