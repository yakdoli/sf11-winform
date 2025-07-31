---
title: printdiagrampageinuniformprintmodeusingframeworkprintdialog1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Diagram\printdiagrampageinuniformprintmodeusingframeworkprintdialog1.md
created_at: 2025-07-03
---








  









### Print DiagramPage in Uniform Print Mode Using Framework Print Dialog {#print-diagrampage-in-uniform-print-mode-using-framework-print-dialog style="tab-stops: 0pt"}

 

DiagramPage can also be printed using Framework PrintDialog instead of using syncfusion DiagramControl PrintPreview Dialog, as shown in the following code snippet.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                           |
| [     //Create Framwork Print Dialog.][]                                                                                                                                            |
|                                                                                                                                                                                                                                                                           |
| [            [PrintDialog] PrintDialog = [new] [PrintDialog]();]                                                                                                 |
|                                                                                                                                                                                                                                                                           |
| [            [//Open Print Dialog.]]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                           |
| [            [Nullable]\<[Boolean]\> printClicked = PrintDialog.ShowDialog();]                                                                                                        |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [            [//If Print is clicked.]]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                           |
| [            [if] (printClicked == [true])]                                                                                                                                                 |
|                                                                                                                                                                                                                                                                           |
| [            {]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                           |
| [                [//Print the Diagram Page.]]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                           |
| [                [//Get Printer Capabilities.]]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                           |
| [                [PrintCapabilities] printCapabilities = PrintDialog.PrintQueue.GetPrintCapabilities(PrintDialog.PrintTicket);]                                                                               |
|                                                                                                                                                                                                                                                                           |
| [                [Size] pageAreaSize = [new] [Size](printCapabilities.PageImageableArea.ExtentWidth, printCapabilities.PageImageableArea.ExtentHeight);]         |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [                [//Visual Brush for the DiagramPage to be printed.]]                                                                                                                                           |
|                                                                                                                                                                                                                                                                           |
| [                [VisualBrush] VisualBrush = [new] [VisualBrush](diagramView.Page);]                                                                             |
|                                                                                                                                                                                                                                                                           |
| [                VisualBrush.Stretch = [Stretch].Uniform;]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [                VisualBrush.ViewboxUnits = [BrushMappingMode].Absolute;]                                                                                                                                     |
|                                                                                                                                                                                                                                                                           |
| [                VisualBrush.Viewbox = [new] [Rect](0, 0, diagramView.Page.ActualWidth, diagramView.Page.ActualHeight);]                                                                 |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [                [//Rectangle to contain the VisualBrush. ]]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [                [Rectangle] rect = [new] [Rectangle]();]                                                                                                        |
|                                                                                                                                                                                                                                                                           |
| [                rect.Fill = VisualBrush;]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                           |
| [                rect.Arrange([new] [Rect]([new] [Point](0, 0), pageAreaSize));]                                                            |
|                                                                                                                                                                                                                                                                           |
| [                SetViewport(VisualBrush, [new] [Size](diagramView.Page.ActualWidth, diagramView.Page.ActualHeight));]                                                                   |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [                [//Print the Page.]]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                           |
| [                [XpsDocumentWriter] writer = [PrintQueue].CreateXpsDocumentWriter(PrintDialog.PrintQueue);]                                                                          |
|                                                                                                                                                                                                                                                                           |
| [                writer.Write(rect, PrintDialog.PrintTicket);]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                           |
| [            }]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [        //Paint the brush to fit uniformly.][]                                                                                                                                     |
|                                                                                                                                                                                                                                                                           |
| [        [private] [void] SetViewport([VisualBrush] brush, [Size] size)]                                                                    |
|                                                                                                                                                                                                                                                                           |
| [        {]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                           |
| [            [double] coefficientHeight = size.Height / brush.Viewbox.Height;]                                                                                                                                   |
|                                                                                                                                                                                                                                                                           |
| [            [double] coefficientWidth = size.Width / brush.Viewbox.Width;]                                                                                                                                      |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| [            [if] (coefficientHeight \< coefficientWidth)]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                           |
| [            {]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                           |
| [                [double] width = coefficientHeight \* brush.Viewbox.Width / size.Width;]                                                                                                                        |
|                                                                                                                                                                                                                                                                           |
| [                [double] x = (1 - width) / 2;]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                           |
| [                brush.Viewport = [new] [Rect]([new] [Point](x, 0), [new] [Size](width, 1));]  |
|                                                                                                                                                                                                                                                                           |
| [            }]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                           |
| [            [else] [if] (coefficientHeight \> coefficientWidth)]                                                                                                                           |
|                                                                                                                                                                                                                                                                           |
| [            {]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                           |
| [                [double] height = coefficientWidth \* brush.Viewbox.Height / size.Height;]                                                                                                                      |
|                                                                                                                                                                                                                                                                           |
| [                [double] y = (1 - height) / 2;]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                           |
| [                brush.Viewport = [new] [Rect]([new] [Point](0, y), [new] [Size](1, height));] |
|                                                                                                                                                                                                                                                                           |
| [            }]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                           |
| [        }]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                              |
| [     ][\'Create Framwork Print Dialog.][]                                                                                           |
|                                                                                                                                                                                                                                                                              |
| [        [Dim] PrintDialog [As] [New] [PrintDialog]()]                                                                                            |
|                                                                                                                                                                                                                                                                              |
| [        [\'Open Print Dialog.]]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                              |
| [        [Dim] printClicked [As] [Nullable]([Of] [Boolean]) = PrintDialog.ShowDialog()]                                      |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                              |
| [        [\'If Print is clicked.]]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                              |
| [                  [If] printClicked.GetValueOrDefault() = [True] [Then]]                                                                                                 |
|                                                                                                                                                                                                                                                                              |
| [        [\'Print the Diagram Page.]]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                              |
| [        [\'Get Printer Capabilities.]]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                              |
| [        [Dim] printCapabilities [As] [PrintCapabilities] = PrintDialog.PrintQueue.GetPrintCapabilities(PrintDialog.PrintTicket)]                                      |
|                                                                                                                                                                                                                                                                              |
| [        [Dim] pageAreaSize [As] [New] [Size](PrintCapabilities.PageImageableArea.ExtentWidth, PrintCapabilities.PageImageableArea.ExtentHeight)] |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                              |
| [        [\'Visual Brush for the DiagramPage to be printed.]]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                              |
| [        [Dim] VisualBrush [As] [New] [VisualBrush]([DiagramView].Page)]                                                  |
|                                                                                                                                                                                                                                                                              |
| [                        VisualBrush.Stretch = Stretch.Uniform]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                              |
| [                        VisualBrush.ViewboxUnits = BrushMappingMode.Absolute]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                              |
| [                        VisualBrush.Viewbox = [New] Rect(0, 0, diagramView.Page.ActualWidth, diagramView.Page.ActualHeight)]                                                                                       |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                              |
| [        [\'Rectangle to contain the VisualBrush. ]]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                              |
| [        [Dim] rect [As] [New] [Rectangle]()]                                                                                                     |
|                                                                                                                                                                                                                                                                              |
| [                        rect.Fill = VisualBrush]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                              |
| [                        rect.Arrange(New Rect(New Point(0, 0), pageAreaSize))]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                              |
| [                        SetViewport(VisualBrush, [New] Size(diagramView.Page.ActualWidth, diagramView.Page.ActualHeight))]                                                                                         |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                              |
| [        [\'Print the Page.]]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                              |
| [        [Dim] writer [As] [XpsDocumentWriter] = [PrintQueue].CreateXpsDocumentWriter(PrintDialog.PrintQueue)]                                 |
|                                                                                                                                                                                                                                                                              |
| [                        writer.Write(rect, PrintDialog.PrintTicket)]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                              |
| [                  [End] [If]]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                              |
| [        [\'Paint the brush to fit uniformly.]]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                              |
| [            [private] void SetViewport(VisualBrush brush, Size size)]                                                                                                                                              |
|                                                                                                                                                                                                                                                                              |
| [        [Dim] coefficientHeight [As] [Double] = [Size].Height / Brush.Viewbox.Height]                                                            |
|                                                                                                                                                                                                                                                                              |
| [        [Dim] coefficientWidth [As] [Double] = [Size].Width / Brush.Viewbox.Width]                                                               |
|                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                              |
| [                  [If] coefficientHeight \< coefficientWidth [Then]]                                                                                                                          |
|                                                                                                                                                                                                                                                                              |
| [        [Dim] width [As] [Double] = coefficientHeight \* Brush.Viewbox.Width / [Size].Width]                                                     |
|                                                                                                                                                                                                                                                                              |
| [        [Dim] x [As] [Double] = (1 - Width) / 2]                                                                                                                         |
|                                                                                                                                                                                                                                                                              |
| [                        brush.Viewport = [New] Rect(New Point(x, 0), [New] Size(width, 1))]                                                                                                   |
|                                                                                                                                                                                                                                                                              |
| [                  [ElseIf] coefficientHeight \> coefficientWidth [Then]]                                                                                                                      |
|                                                                                                                                                                                                                                                                              |
| [        [Dim] height [As] [Double] = coefficientWidth \* Brush.Viewbox.Height / [Size].Height]                                                   |
|                                                                                                                                                                                                                                                                              |
| [        [Dim] y [As] [Double] = (1 - Height) / 2]                                                                                                                        |
|                                                                                                                                                                                                                                                                              |
| [                        brush.Viewport = [New] Rect(New Point(0, y), [New] Size(1, height))]                                                                                                  |
|                                                                                                                                                                                                                                                                              |
| [                  [End] [If]][]                                                                                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

