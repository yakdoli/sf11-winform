---
title: howtoreadconformancelevelfrompdf.md
original_path: WinForms_Docs/99_Uncategorized/howtoreadconformancelevelfrompdf.md
created_at: 2025-08-05
---








  









### How To Read Conformance Level From PDF? {#how-to-read-conformance-level-from-pdf style="tab-stops: 0pt"}

 

You can read conformance level applied to a PDF file using **PdfLoadedDocument.Conformance** property. This property will return the levels supported by PdfConformanceLevel enum.

 


{border="0"}Note: It will return none when the PDF file is not applied with any levels.


 

Following is the code snippet to read conformance level from PDF.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                 |
|                                                                                                                                                                                                                  |
| [PdfLoadedDocument][ loadedDocument = [new] [PdfLoadedDocument](fileName);] |
|                                                                                                                                                                                                                  |
| [PdfConformanceLevel][ appliedConformance = loadedDocument.Conformance;]                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                         |
|                                                                                                                                                                                              |
| [Dim][ loadedDocument [As] [New] PdfLoadedDocument(fileName)] |
|                                                                                                                                                                                              |
| [Dim][ appliedConformance [As] PdfConformanceLevel = loadedDocument.Conformance]   |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

