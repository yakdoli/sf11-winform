---
title: howtocopyarangeofcellstotheclipboard.md
original_path: WinForms_Docs/99_Uncategorized/howtocopyarangeofcellstotheclipboard.md
created_at: 2025-08-05
---








  









### How to Copy a Range of Cells to the Clipboard {#how-to-copy-a-range-of-cells-to-the-clipboard style="tab-stops: 0pt"}

[] 

Introduction

[] 

You can use the **CopyTextToClipboard** method to copy the text from a selected range of cells to the clipboard.

[] 

Example

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [// To copy selected range of cells to clipboard in a GridControl.\                                                                                                                                                                                                                                                                                                                                                   |
| ][bool][ val = ][this][.gridControl1.CutPaste.CopyTextToClipboard(][this][.gridControl1.Selections.Ranges);\ |
| Console.WriteLine(\" Selected Range of cells(GridControl)are in Clipboard. This is\"+val);\                                                                                                                                                                                                                                                                                                                           |
| MessageBox.Show(\"Data copied\");]                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ][// To copy selected range of cells to clipboard in a GridDataBoundGrid.\                                                                                                                                                                                                                                                                                          |
| ][bool][ val = ][this][.gridDataBoundGrid1.Model.CutPaste.CopyTextToClipboard(this.gridDataBoundGrid1.Selections.Ranges);\                                                                                      |
| Console.WriteLine(\" Selected Range of cells(GridDataBoundGrid)are in Clipboard. This is\"+val);\                                                                                                                                                                                                                                                                                                                     |
| MessageBox.Show(\"Data copied\"); ]                                                                                                                                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\' To copy a selected range of cells to the clipboard in a GridControl.\                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ][Dim][ val][ As Boolean][ = ][Me][.gridControl1.CutPaste.CopyTextToClipboard(][Me][.gridControl1.Selections.Ranges)\                   |
| Console.WriteLine(\" Selected Range of cells(GridControl)are in Clipboard. This is\", val)\                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| MessageBox.Show(\"Data copied\")]                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\' To copy a selected range of cells to the clipboard in a GridDataBoundGrid.\                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ][Dim][ val ][As Boolean][ = ][Me][.gridDataBoundGrid1.Model.CutPaste.CopyTextToClipboard(][Me][.gridDataBoundGrid1.Selections.Ranges)\ |
| Console.WriteLine(\"Selected Range of cells(GridDataBoundGrid)are in Clipboard. This is\", val)\                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| MessageBox.Show(\"Data copied\")]                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p589} 

 

[]{#related-topics}

