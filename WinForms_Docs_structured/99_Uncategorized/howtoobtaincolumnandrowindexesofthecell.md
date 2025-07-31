---
title: howtoobtaincolumnandrowindexesofthecell.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoobtaincolumnandrowindexesofthecell.md
created_at: 2025-07-03
---








  









## How to Obtain Column and Row Indexes of the Cell? {#how-to-obtain-column-and-row-indexes-of-the-cell style="tab-stops: 0pt"}

 

The *PointToCellRowColumnIndexOutsideCells* method enables you to obtain column index and row index of a cell when the mouse pointer traverses over the GridDataControl. The following code example illustrates how to determine the column and row indexes of the cell.

 

+------------------------------------------------------------------------------+
| ```                                             |
| [C#]                                                                         |
| ```                                                                          |
|                                                                              |
| ```                                             |
|                                                                              |
| ```                                                                          |
|                                                                              |
| ```                                             |
| void GridDataControl1_MouseMove(object sender, MouseEventArgs e)             |
| ```                                                                          |
|                                                                              |
| ```                                             |
|         {                                                                    |
| ```                                                                          |
|                                                                              |
| ```                                             |
|             var RowColumnIndex = GridDataControl1.Model.Grid.PointToCellRowC |
| ```                                                                          |
|                                                                              |
| ```                                             |
| olumnIndexOutsideCells(Mouse.GetPosition(this), true);                       |
| ```                                                                          |
|                                                                              |
| ```                                             |
|             Console.WriteLine(RowColumnIndex);                               |
| ```                                                                          |
|                                                                              |
| ```                                             |
|         }                                                                    |
| ```                                                                          |
|                                                                              |
| []                                       |
+------------------------------------------------------------------------------+

 

The following screen shot shows the output for the above code in the GridDataControl.

 

{border="0"}

Figure 277: RowColumnPosition

[]{#related-topics}

