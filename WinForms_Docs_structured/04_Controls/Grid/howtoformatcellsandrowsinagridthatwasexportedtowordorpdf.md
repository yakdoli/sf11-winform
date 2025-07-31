---
title: howtoformatcellsandrowsinagridthatwasexportedtowordorpdf.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\howtoformatcellsandrowsinagridthatwasexportedtowordorpdf.md
created_at: 2025-07-03
---






#### How to format cells and rows in a Grid that was exported to Word or PDF? {#how-to-format-cells-and-rows-in-a-grid-that-was-exported-to-word-or-pdf style="tab-stops: 0pt"}

You can use C# or VB code as shown below to format cells and rows in an exported Grid.

For PDF

These events are used to format cells and rows in a grid that was exported to PDF:

**C# Code:**

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]][]                                                                                                            |
|                                                                                                                                                                                                                   |
| [pdf.pdfCellFormatHandler += [new] [GridCellExportHandler](pdf_pdfCellFormatHandler);]                                           |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                   |
| [void][ pdf_pdfCellFormatHandler([object] sender, [ExportingToPdfEventArgs] e)] |
|                                                                                                                                                                                                                   |
| [    {]                                                                                                                                                                       |
|                                                                                                                                                                                                                   |
| [        [if] (e.RowElement.Kind == [DisplayElementKind].Caption)]                                                               |
|                                                                                                                                                                                                                   |
| [        {]                                                                                                                                                                   |
|                                                                                                                                                                                                                   |
| [            e.PdfGridCell.Style.TextBrush = [new] [PdfSolidBrush]([Color].AliceBlue);]                  |
|                                                                                                                                                                                                                   |
| [        }]                                                                                                                                                                   |
|                                                                                                                                                                                                                   |
| [    }]                                                                                                                                                                       |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**VB Code:**

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[VB\]][]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                               |
| [AddHandler][ pdf.pdfCellFormatHandler, [AddressOf] pdf_pdfCellFormatHandler]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                               |
| [Private][ [Sub] pdf_pdfCellFormatHandler([ByVal] sender [As] [Object], [ByVal] e [As] [ExportingToPdfEventArgs])] |
|                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                               |
| [        [If] e.RowElement.Kind = [DisplayElementKind].Caption [Then]]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                               |
| [            e.PdfGridCell.Style.TextBrush = [New] [PdfSolidBrush]([Color].AliceBlue)]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                               |
| [        [End] [If]]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                               |
| [End][ [Sub]]                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

For Word

These events are used to format cells and rows in a grid that was exported to Word:

**C# Code:**

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]][]                                                                                                               |
|                                                                                                                                                                                                                      |
| [word.WordCellFormatHandler += [new] [ExportGridCellHandler](word_WordCellFormatHandler);]                                          |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [void][ word_WordCellFormatHandler([object] sender, [ExportingToWordEventArgs] e)] |
|                                                                                                                                                                                                                      |
| [    {]                                                                                                                                                                          |
|                                                                                                                                                                                                                      |
| [        [if] (e.RowElement.Kind == [DisplayElementKind].Caption)]                                                                  |
|                                                                                                                                                                                                                      |
| [        {]                                                                                                                                                                      |
|                                                                                                                                                                                                                      |
| [            e.WordCell.CellFormat.BackColor = [Color].AliceBlue;]                                                                                       |
|                                                                                                                                                                                                                      |
| [        }]                                                                                                                                                                      |
|                                                                                                                                                                                                                      |
| [    }]                                                                                                                                                                          |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**For VB**

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[VB\]][]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [AddHandler][ word.WordCellFormatHandler, [AddressOf] word_DrawFooter]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [Private][ [Sub] word_WordCellFormatHandler([ByVal] sender [As] [Object], [ByVal] e [As] [ExportingToWordEventArgs])] |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [        [If] e.RowElement.Kind = [DisplayElementKind].Caption [Then]]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [            e.WordCell.CellFormat.BackColor = [Color].AliceBlue]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [        [End] [If]]                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [End][ [Sub]]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

