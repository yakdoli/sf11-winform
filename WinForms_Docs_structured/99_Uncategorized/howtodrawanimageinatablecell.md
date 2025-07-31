---
title: howtodrawanimageinatablecell.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtodrawanimageinatablecell.md
created_at: 2025-07-03
---






#### How To Draw an Image In a Table Cell? {#how-to-draw-an-image-in-a-table-cell style="tab-stops: 0pt"}

 

You can draw an image in a particular table cell by using the **BeginCellLayout** event handler and its arguments. This is done by using the Graphics object in the event handler.

 

The following code example illustrates how to draw a borderless table.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                              |
| [// Adding the Event handler]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                              |
| [table.BeginCellLayout += [new] [BeginCellLayoutEventHandler](table_BeginCellLayout);]                                                                                                      |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                              |
| [// Drawing an image in a cell]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                              |
| [void][ table_BeginCellLayout([object] sender, [BeginCellLayoutEventArgs] args)]                                                           |
|                                                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                              |
| [if][ (args.RowIndex == 0 && args.CellIndex == 0)]                                                                                                                                      |
|                                                                                                                                                                                                                                                                              |
| [{]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                              |
| [PdfImage][ img = [new] [PdfBitmap]([Image].FromFile([@\"..\\..\\Data\\Image.png\"]));] |
|                                                                                                                                                                                                                                                                              |
| [args.Graphics.DrawImage(img,args.Bounds);]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                              |
| [// To dispose the image]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                              |
| [(img [as] [PdfBitmap]).Dispose();]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                              |
| [}]                                                                                                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                      |
| [\' Adding the Event handler]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                      |
| [Private][ table.BeginCellLayout += [New] BeginCellLayoutEventHandler([AddressOf] table_BeginCellLayout)]                                                                                             |
|                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                      |
| [\' Drawing an image in a cell]                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                      |
| [Private][ [Sub] table_BeginCellLayout([ByVal] sender [As] [Object], [ByVal] args [As] BeginCellLayoutEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                      |
| [If][ args.RowIndex = 0 [AndAlso] args.CellIndex = 0 [Then]]                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                      |
| [Dim][ img [As] PdfImage = [New] PdfBitmap(Image.FromFile([\"..\\..\\Data\\Image.png\"]))]                                                                                    |
|                                                                                                                                                                                                                                                                                                                                      |
| [args.Graphics.DrawImage(img, args.Bounds)]                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                      |
| [\' To dispose the image]                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                      |
| [([TryCast](img, PdfBitmap)).Dispose()]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                      |
| [End][ [If]]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                      |
| [End][ [Sub]]                                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

[]{#related-topics}

