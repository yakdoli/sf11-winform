---
title: howtocopyandpastethe1.md
original_path: WinForms_Docs/99_Uncategorized/howtocopyandpastethe1.md
created_at: 2025-08-05
---






#### How to Copy and Paste the Display Text {#how-to-copy-and-paste-the-display-text style="TEXT-ALIGN: justify; tab-stops: 0pt"}

By default, when you copy and paste the formula cell, the Spreadsheet control will copy and paste the formula from the particular cell. To copy and paste the display text you have to handle the **ClipboardCopy** event of the underling grid control. You can get all the Grid controls in the **WorkBookLoaded** event of the spreadsheet control.

The following code used to copy and paste only the display text.

+---------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                          |
|                                                                                                                           |
| ```                                                                                          |
| void spreadsheetControl_WorkBookLoaded(object sender, WorkbookLoadedEventArgs args)                                       |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
| {                                                                                                                         |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|     foreach (var grid in args.GridCollection)                                                                             |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|     {                                                                                                                     |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|         grid.Model.GridCopyPaste = null;                                                                                  |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|         grid.Model.ClipboardCopy += new GridCutPasteEventHandler(Model_ClipboardCopy);                                    |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|     }                                                                                                                     |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
| }                                                                                                                         |
| ```                                                                                                                       |
|                                                                                                                           |
| []                                                                                    |
|                                                                                                                           |
| ```                                                                                          |
| void Model_ClipboardCopy(object sender, GridCutPasteEventArgs e)                                                          |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
| {                                                                                                                         |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|     GridRangeInfoList rowRanges = e.RangeList.GetRowRanges(GridRangeInfoType.Cells | GridRangeInfoType.Rows);             |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|     GridRangeInfoList colRanges = e.RangeList.GetColRanges(GridRangeInfoType.Cells | GridRangeInfoType.Cols);             |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|     var sb = new StringBuilder();                                                                                         |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|     int nrowsdone = 0; int ncolsdone = 0;                                                                                 |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|     string tabDelim = "\t";                                                                                               |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|     for (int rowindex = 0; rowindex < rowRanges.Count; rowindex++)                                                        |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|     {                                                                                                                     |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|         for (int nrow = rowRanges[rowindex].Top; nrow <= rowRanges[rowindex].Bottom; nrow++)                              |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|         {                                                                                                                 |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|             if (nrowsdone > 0)                                                                                            |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|                 sb.Append(Environment.NewLine);                                                                           |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|             ncolsdone = 0;                                                                                                |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|             bool firstCol;                                                                                                |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|             firstCol = true;                                                                                              |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|             for (int colindex = 0; colindex < colRanges.Count; colindex++)                                                |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|             {                                                                                                             |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|                 for (int ncol = colRanges[colindex].Left; ncol <= colRanges[colindex].Right; ncol++)                      |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|                 {                                                                                                         |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|                     if (!firstCol)                                                                                        |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|                         sb.Append(tabDelim);                                                                              |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|                     string text = this.spreadsheetControl.GridProperties.CurrentExcelGridModel[nrow, ncol].FormattedText; |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|                     if (!e.RangeList.AnyRangeContains(GridRangeInfo.Cell(nrow, ncol)))                                    |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|                     {                                                                                                     |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|                         ncolsdone++;                                                                                      |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|                         continue;                                                                                         |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|                     }                                                                                                     |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|                     text = new StringBuilder(text).ToString().Trim();                                                     |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|                     // Append the Cell value to buffer text                                                               |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|                     sb.Append(text);                                                                                      |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|                     firstCol = false;                                                                                     |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|                     ncolsdone++;                                                                                          |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|                 }                                                                                                         |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|             }                                                                                                             |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|             nrowsdone++;                                                                                                  |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|         }                                                                                                                 |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|     }                                                                                                                     |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|     Clipboard.SetText(sb.ToString());                                                                                     |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|     e.DataObject = null;                                                                                                  |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
|     e.Handled = true;                                                                                                     |
| ```                                                                                                                       |
|                                                                                                                           |
| ```                                                                                          |
| }                                                                                                                         |
| ```                                                                                                                       |
|                                                                                                                           |
|                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

