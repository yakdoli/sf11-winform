---
title: howtoformatatable.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoformatatable.md
created_at: 2025-07-03
---








  









## How to format a Table? {#how-to-format-a-table style="tab-stops: 0pt"}

 

You can format a table in two ways.

 

**Method 1**

 

You can use the **TableFormat** property of the table object.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                             |
|                                                                                                                                                                                            |
| **[]**                                                                                                                                                               |
|                                                                                                                                                                                            |
| [WTable][ table= doc.LastSection.AddTable() [as] [WTable];] |
|                                                                                                                                                                                            |
| [table.ResetCells(4, 4);]                                                                                                                              |
|                                                                                                                                                                                            |
| [table.TableFormat.Borders.BorderType = Syncfusion.DocIO.DLS.[BorderStyle].Double;]                                               |
|                                                                                                                                                                                            |
| [table.TableFormat.LeftIndent=20;  ]                                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                             |
|                                                                                                                                                            |
| []                                                                                                                                   |
|                                                                                                                                                            |
| [Dim][ table [As] IWTable = sec.body.AddTable()] |
|                                                                                                                                                            |
| [table.ResetCells(4, 4)]                                                                                               |
|                                                                                                                                                            |
| [table.TableFormat.Borders.BorderType = Syncfusion.DocIO.DLS.BorderStyle.Double]                                       |
|                                                                                                                                                            |
| [table.TableFormat.LeftIndent = 20]                                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**Method 2**

 

You can use the **ResetCell** method of the table object to format the cell. The following code illustrates this.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                             |
|                                                                                                                                                                                            |
| **[]**                                                                                                                                                               |
|                                                                                                                                                                                            |
| [WTable][ table= doc.LastSection.AddTable() [as] [WTable];] |
|                                                                                                                                                                                            |
| [RowFormat][ rowFormat=[new] [RowFormat](); ]               |
|                                                                                                                                                                                            |
| [rowFormat.Borders.BorderType = Syncfusion.DocIO.DLS.[BorderStyle].Double;]                                                       |
|                                                                                                                                                                                            |
| [rowFormat.LeftIndent=20;  ]                                                                                                                           |
|                                                                                                                                                                                            |
| [table.ResetCells(3,3,rowFormat,100); ]                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                             |
|                                                                                                                                                            |
| []                                                                                                                                   |
|                                                                                                                                                            |
| [Dim][ table [As] IWTable = sec.body.AddTable()] |
|                                                                                                                                                            |
| [Dim rowFormat As New RowFormat()]                                                                                     |
|                                                                                                                                                            |
| [rowFormat.BackColor = Color.Purple]                                                                                   |
|                                                                                                                                                            |
| [rowFormat.Borders.BorderType = Syncfusion.DocIO.DLS.BorderStyle.\[Double\]]                                           |
|                                                                                                                                                            |
| [rowFormat.LeftIndent = 20]                                                                                            |
|                                                                                                                                                            |
| [table.ResetCells(3, 3, rowFormat, 100)]                                                                               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

