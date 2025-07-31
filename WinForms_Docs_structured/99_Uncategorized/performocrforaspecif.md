---
title: performocrforaspecif.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\performocrforaspecif.md
created_at: 2025-07-03
---






#### Perform OCR for a Specific Region of PDF Document {#perform-ocr-for-a-specific-region-of-pdf-document style="tab-stops: 0pt"}

The following code example explains how to perform OCR for a specific region of the PDF document.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                             |
| [//Initialize the OCR processor]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                             |
| [using][ ([OCRProcessor] processor = [new] [OCRProcessor](ocrBinariesPath))]                      |
|                                                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                             |
| [//Load a PDF document ]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                             |
| [PdfLoadedDocument][ lDoc = [new] [PdfLoadedDocument](fileName);]                                                      |
|                                                                                                                                                                                                                                                             |
| [//Set OCR language to process ]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                             |
| [processor.Settings.Language = [Languages].English;]                                                                                                                                            |
|                                                                                                                                                                                                                                                             |
| [RectangleF][ rect = [new] [RectangleF](0, 100, 950, 150);]                                                            |
|                                                                                                                                                                                                                                                             |
| [//Assign rectangles to the page]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                             |
| [PageRegion][ region = [new] [PageRegion]();]                                                                          |
|                                                                                                                                                                                                                                                             |
| [List][\<[PageRegion]\> pageRegions = [new] [List]\<[PageRegion]\>();] |
|                                                                                                                                                                                                                                                             |
| [region.PageIndex = 1;]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                             |
| [region.PageRegions = [new] [RectangleF]\[\] { rect };]                                                                                                                    |
|                                                                                                                                                                                                                                                             |
| [pageRegions.Add(region);]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                             |
| [processor.Settings.OCRPageRegion = pageRegions;]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                             |
| [//Process OCR by providing the PDF document, data dictionary, and language]                                                                                                                              |
|                                                                                                                                                                                                                                                             |
| [processor.PerformOCR(lDoc, tessDataPath);]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                             |
| [//Save the OCR processed PDF document in a disk]                                                                                                                                                         |
|                                                                                                                                                                                                                                                             |
| [lDoc.Save([\"Sample.pdf\"]);]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                             |
| [lDoc.Close([true]);]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                             |
| [}]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                |
| [Using][ processor [As] [New] [OCRProcessor](ocrBinariesPath)]                                          |
|                                                                                                                                                                                                                                                                |
| [\'Load a PDF document ][]                                                                                                                                               |
|                                                                                                                                                                                                                                                                |
| [Dim][ lDoc [As] [New] [PdfLoadedDocument](fileName)]                                                   |
|                                                                                                                                                                                                                                                                |
| [\'Set OCR language to process ][]                                                                                                                                       |
|                                                                                                                                                                                                                                                                |
| [processor.Settings.Language = [Languages].English]                                                                                                                                                |
|                                                                                                                                                                                                                                                                |
| [Dim][ rect [As] [New] [RectangleF](0, 100, 950, 150)]                                                  |
|                                                                                                                                                                                                                                                                |
| [\'Assign rectangles to the page][]                                                                                                                                      |
|                                                                                                                                                                                                                                                                |
| [Dim][ region [As] [New] [PageRegion]()]                                                                |
|                                                                                                                                                                                                                                                                |
| [Dim][ pageRegions [As] [New] [List]([Of] [PageRegion])()] |
|                                                                                                                                                                                                                                                                |
| [region.PageIndex = 1]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                |
| [region.PageRegions = [New] [RectangleF]() {rect}]                                                                                                                            |
|                                                                                                                                                                                                                                                                |
| [pageRegions.Add(region)]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                |
| [processor.Settings.OCRPageRegion = pageRegions]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                |
| [\'Process OCR by providing the PDF document, data dictionary, and language][]                                                                                           |
|                                                                                                                                                                                                                                                                |
| [processor.PerformOCR(lDoc, tessDataPath)]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                |
| [\'Save the OCR processed PDF document in a disk][]                                                                                                                      |
|                                                                                                                                                                                                                                                                |
| [lDoc.Save([\"Sample.pdf\"])]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                |
| [lDoc.Close([True])]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                |
| [End][ [Using]]                                                                                                                                      |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 


{border="0"}Note: The Tesseract binaries, namely SyncfusionTessaract.dll, liblept168.dll, and language pack (tessdata), will be available in the following location.


**\<\<Installation Location\>\>\\Syncfusion\\Essential Studio\\\<\<Version Number\>\>\\OCRProcessor**

 

[]{#related-topics}

