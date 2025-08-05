---
title: performingocrforacom.md
original_path: WinForms_Docs/99_Uncategorized/performingocrforacom.md
created_at: 2025-08-05
---






#### Performing OCR for a Complete PDF Document {#performing-ocr-for-a-complete-pdf-document style="tab-stops: 0pt"}

The following code example illustrates how to perform OCR for a complete PDF document.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                       |
|                                                                                                                                                                                                                                        |
| [//Initialize the OCR processor]                                                                                                                                                     |
|                                                                                                                                                                                                                                        |
| [using][ ([OCRProcessor] processor = [new] [OCRProcessor](ocrBinariesPath))] |
|                                                                                                                                                                                                                                        |
| [{]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                        |
| [//Load a PDF document ]                                                                                                                                                             |
|                                                                                                                                                                                                                                        |
| [PdfLoadedDocument][ lDoc = [new] [PdfLoadedDocument](fileName);]                                 |
|                                                                                                                                                                                                                                        |
| [//Set OCR language to process]                                                                                                                                                      |
|                                                                                                                                                                                                                                        |
| [processor.Settings.Language = [Languages].English;]                                                                                                                       |
|                                                                                                                                                                                                                                        |
| [//Process OCR by providing the PDF document, data dictionary and language]                                                                                                          |
|                                                                                                                                                                                                                                        |
| [processor.PerformOCR(lDoc, tessDataPath);]                                                                                                                                                        |
|                                                                                                                                                                                                                                        |
| [//Save the OCR processed PDF document in a disk]                                                                                                                                    |
|                                                                                                                                                                                                                                        |
| [lDoc.Save([\"Sample.pdf\"]));]                                                                                                                                            |
|                                                                                                                                                                                                                                        |
| [lDoc.Close([true]);]                                                                                                                                                         |
|                                                                                                                                                                                                                                        |
| [}]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                           |
|                                                                                                                                                                                            |
| []                                                                                                                                                     |
|                                                                                                                                                                                            |
| [\'Initialize the OCR processor][]                                                                   |
|                                                                                                                                                                                            |
| [ [Using] processor [As] [New] [OCRProcessor](ocrBinariesPath)] |
|                                                                                                                                                                                            |
| [\'Load a PDF document ][]                                                                           |
|                                                                                                                                                                                            |
| [ [Dim] lDoc [As] [New] [PdfLoadedDocument](fileName)]          |
|                                                                                                                                                                                            |
| [\'Set OCR language to process ][]                                                                   |
|                                                                                                                                                                                            |
| [ processor.Settings.Language = [Languages].English]                                                                           |
|                                                                                                                                                                                            |
| [\'Process OCR by providing the PDF document, data dictionary, and  language][]                      |
|                                                                                                                                                                                            |
| [ processor.PerformOCR(lDoc, tessDataPath)]                                                                                                            |
|                                                                                                                                                                                            |
| [\'Save the OCR processed PDF document in a disk][]                                                  |
|                                                                                                                                                                                            |
| [ lDoc.Save([\"Sample.pdf\"])]                                                                                                 |
|                                                                                                                                                                                            |
| [ lDoc.Close([True])]                                                                                                             |
|                                                                                                                                                                                            |
| [ [End] [Using]]                                                                                             |
|                                                                                                                                                                                            |
| []                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

