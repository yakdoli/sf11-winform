---
title: splitpdf.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\splitpdf.md
created_at: 2025-07-03
---








  









### Split PDF {#split-pdf style="tab-stops: 0pt"}

 

Splitting operation is used to generate a set of PDF documents, each of which is made of one page from the base document. Each new document is saved with a unique name which is generated from the pattern specified.

 

The pattern should be in .NET format (for example: \"myfile{0:000}.pdf\") or just a pdf name. In the latter case, the unique name will have the number before \".pdf\".

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                          |
|                                                                                                                                                                                                           |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                           |
| [PdfLoadedDocument][ ldDoc = [new] [PdfLoadedDocument](defDocumentPath);]  |
|                                                                                                                                                                                                           |
| [const][ [string] destFilePattern = OutputPath + [\"split{0:00}.pdf\"];] |
|                                                                                                                                                                                                           |
| [ldDoc.Split(destFilePattern);]                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                           |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [Dim][ ldDoc [As] PdfLoadedDocument = [New] PdfLoadedDocument(defDocumentPath)] |
|                                                                                                                                                                                                                |
| [const][ [String] destFilePattern = OutputPath + [\"split{0:00}.pdf\"]]       |
|                                                                                                                                                                                                                |
| [ldDoc.Split(destFilePattern)]                                                                                                                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note:[ ]Splitting algorithm uses the [Import Page] methods. So the result would be similar to it.


 

Essential PDF also allows to split the pages as per the user\'s need. The following code example illustrates this.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                  |
|                                                                                                                                                                                                   |
| []                                                                                                                                              |
|                                                                                                                                                                                                   |
| [// To load an existing document which needs to be split.]                                                                                      |
|                                                                                                                                                                                                   |
| [PdfLoadedDocument][ ldDoc = [new] [PdfLoadedDocument](filename);] |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
|                                                                                                                                                                                                   |
| [// Create a pdf document.]                                                                                                                     |
|                                                                                                                                                                                                   |
| [PdfDocument][ doc1 = [new] [PdfDocument]();]                      |
|                                                                                                                                                                                                   |
| [PdfDocument][ doc2 = [new] [PdfDocument]();]                      |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
|                                                                                                                                                                                                   |
| [// To add page 9 into pdf document1.]                                                                                                          |
|                                                                                                                                                                                                   |
| [doc1.ImportPage(ldDoc, 9);]                                                                                                                                  |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
|                                                                                                                                                                                                   |
| [// To add page 10 into pdf document1.]                                                                                                         |
|                                                                                                                                                                                                   |
| [doc1.ImportPage(ldoc, 10);]                                                                                                                                  |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
|                                                                                                                                                                                                   |
| [// To add page 5 into pdf document2.]                                                                                                          |
|                                                                                                                                                                                                   |
| [doc2.ImportPage(ldoc, 5);]                                                                                                                                   |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
|                                                                                                                                                                                                   |
| [// To add page 6 into pdf document2.]                                                                                                          |
|                                                                                                                                                                                                   |
| [doc2.ImportPage(ldoc, 6);]                                                                                                                                   |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
|                                                                                                                                                                                                   |
| [// Save pdf document1.]                                                                                                                        |
|                                                                                                                                                                                                   |
| [doc1.Save([\"Document1.pdf\"]);]                                                                                                      |
|                                                                                                                                                                                                   |
| []                                                                                                                                                            |
|                                                                                                                                                                                                   |
| [// Save pdf document1.]                                                                                                                        |
|                                                                                                                                                                                                   |
| [doc2.Save([\"Document2.pdf\"]);]                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                    |
|                                                                                                                                                                                                         |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                         |
| [\' To load an existing document which needs to be split.]                                                                                            |
|                                                                                                                                                                                                         |
| [Dim][ ldDoc [As] PdfLoadedDocument = [New] PdfLoadedDocument(filename)] |
|                                                                                                                                                                                                         |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                         |
| [\' Create a pdf document.]                                                                                                                           |
|                                                                                                                                                                                                         |
| [Dim][ doc1 [As] PdfDocument = [New] PdfDocument()]                      |
|                                                                                                                                                                                                         |
| [Dim][ doc2 [As] PdfDocument = [New] PdfDocument()]                      |
|                                                                                                                                                                                                         |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                         |
| [\' To add page 9 into pdf document1.]                                                                                                                |
|                                                                                                                                                                                                         |
| [doc1.ImportPage(ldDoc, 9)]                                                                                                                                         |
|                                                                                                                                                                                                         |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                         |
| [\' To add page 10 into pdf document1.]                                                                                                               |
|                                                                                                                                                                                                         |
| [doc1.ImportPage(ldoc,10)]                                                                                                                                          |
|                                                                                                                                                                                                         |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                         |
| [\' To add page 5 into pdf document2.]                                                                                                                |
|                                                                                                                                                                                                         |
| [doc2.ImportPage(ldoc, 5 )]                                                                                                                                         |
|                                                                                                                                                                                                         |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                         |
| [\' To add page 6 into pdf document2.]                                                                                                                |
|                                                                                                                                                                                                         |
| [doc2.ImportPage(ldoc, 6 )]                                                                                                                                         |
|                                                                                                                                                                                                         |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                         |
| [\' Save pdf document1.]                                                                                                                              |
|                                                                                                                                                                                                         |
| [doc1.Save([\"Document1.pdf\"])]                                                                                                             |
|                                                                                                                                                                                                         |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                         |
| [\' Save pdf document1.]                                                                                                                              |
|                                                                                                                                                                                                         |
| [doc2.Save([\"Document2.pdf\"])]                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

