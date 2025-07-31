---
title: howtoswaprowsandcolumns.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoswaprowsandcolumns.md
created_at: 2025-07-03
---








  









### How to Swap Rows and Columns {#how-to-swap-rows-and-columns style="tab-stops: 0pt"}

[] 

Introduction

[] 

This can be done in the **GridControl** by handling the virtual events **QueryCellInfo**, **SaveCellInfo**, **QueryRowCount**, **QueryColCount**. Here the **GridControl.Data** property is used.

[] 

Example

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                               |
| [// In the QueryCellInfo handler.]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                               |
| [e.Style.ModifyStyle(][this][.gridControl1.Data\[e.ColIndex, e.RowIndex\], Syncfusion.Styles.StyleModifyType.Override);] |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                               |
| [// In the SaveCellInfo handler.]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                               |
| [this][.gridControl1.Data\[e.ColIndex, e.RowIndex\] = e.Style.Store;]                                                                                                      |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                               |
| [// In the QueryRowCount handler.]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                               |
| [e.Count = ][this][.gridControl1.Data.ColCount;]                                                                         |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                               |
| [// In the QueryColCount handler.]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                               |
| [e.Count = ][this][.gridControl1.Data.RowCount;]                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                          |
| [\' In the QueryCellInfo handler.]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                          |
| [e.Style.ModifyStyle(][Me][.gridControl1.Data(e.ColIndex, e.RowIndex), Syncfusion.Styles.StyleModifyType.Override)] |
|                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                          |
| [\' In the SaveCellInfo handler.]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                          |
| [Me][.gridControl1.Data(e.ColIndex, e.RowIndex) = e.Style.Store]                                                                                                      |
|                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                          |
| [\' In the QueryRowCount handler.]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                          |
| [e.Count = ][Me][.gridControl1.Data.ColCount]                                                                       |
|                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                          |
| [\' In the QueryColCount handler.]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                          |
| [e.Count = ][Me][.gridControl1.Data.RowCount]                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p574} 

 

[]{#related-topics}

