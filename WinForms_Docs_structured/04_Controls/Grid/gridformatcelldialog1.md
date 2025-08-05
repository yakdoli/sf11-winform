---
title: gridformatcelldialog1.md
original_path: WinForms_Docs/04_Controls/Grid/gridformatcelldialog1.md
created_at: 2025-08-05
---








  









### Grid Format Cell Dialog {#grid-format-cell-dialog style="tab-stops: 0pt"}

[] 

The **Grid Format Cell Dialog**, similar to the Excel-like Format Cell Dialog, enables users to format the cells dynamically. It provides options to customize the cell font family, font color, font size, font style, font effects, background, alignment, text format, and so on. You can instantiate the Grid Format Cell Dialog by using the following code.

[] 

1.   Using C#

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                                           |
| [GridFormatCellDialog][ f = [new] [GridFormatCellDialog]([this].gridControl1);] |
|                                                                                                                                                                                                                                           |
| [f.ShowDialog();]                                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                               |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                             |
|                                                                                                                                                                                                                  |
| [Dim][ f [As] [New] GridFormatCellDialog([Me].gridControl1)] |
|                                                                                                                                                                                                                  |
| [f.ShowDialog()]                                                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Following screen shot illustrates the Format Cell Dialog of the Grid control.

[] 

{border="0"}

[] 

*[Figure ][470][: Grid control with Format Cell Dialog]*

 

[]{#p538} 

 

[]{#related-topics}

