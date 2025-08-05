---
title: mergepdf1.md
original_path: WinForms_Docs/99_Uncategorized/mergepdf1.md
created_at: 2025-08-05
---






#### Merge PDF {#merge-pdf style="tab-stops: 0pt"}

[] 

Essential PDF supports the merging of multiple PDF documents. It can merge multiple documents from stream as well as the files stored on the disk.

 

The following merging techniques are discussed in this section:

 

[·      ]Merging Multiple Documents from Disk

[·      ]Merging Multiple Documents from Stream

[·      ]Merging Two Files using Append method

[·      ]Merging pages of different Documents

 

Merging Multiple Documents from Disk

 

The following code example illustrates how to merge multiple documents.

 

+------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                   |
|                                                                                                                                    |
| []                                                                               |
|                                                                                                                                    |
| [// Create a string array of source files which are to be merged.]               |
|                                                                                                                                    |
| [string][\[\] source = { source1, source2 };] |
|                                                                                                                                    |
| []                                                                                             |
|                                                                                                                                    |
| [// Merge PDFDocument.]                                                          |
|                                                                                                                                    |
| [PdfDocument][.Merge(destination, source);]   |
+------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                 |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [\' Create a string array of source files which are to be merged.]                                                                 |
|                                                                                                                                                                                      |
| [Dim][ source [As] [String]() = { source1, source2 }] |
|                                                                                                                                                                                      |
| []                                                                                                                                 |
|                                                                                                                                                                                      |
| [\' Merge PDFDocument.]                                                                                                            |
|                                                                                                                                                                                      |
| [PdfDocument.Merge(destination, source)]                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[Merge Multiple Documents from Stream]

[] 

It is also possible to merge multiple PDF documents from stream. The following code example illustrates this.

[] 

+------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                   |
|                                                                                                                                    |
| []                                                                               |
|                                                                                                                                    |
| [Stream][\[\] streams = { stream1,stream2}; ] |
|                                                                                                                                    |
| [PdfDocumentBase][.Merge(doc, streams);]      |
|                                                                                                                                    |
| [doc.Save([\"sample.pdf\"]);]                                           |
+------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                         |
|                                                                                                                                                              |
| []                                                                                                                       |
|                                                                                                                                                              |
| [Dim][ streams As [Stream]() = {stream1, stream2}] |
|                                                                                                                                                              |
| [PdfDocumentBase][.Merge(doc, streams)]                                 |
|                                                                                                                                                              |
| [doc.Save(\"sample.pdf\")]                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Merging two Files using Append method

 

You can also merge two files, by appending one file after another. The following code example illustrates this.

 

+----------------------------------------------------------------------------+
| **[\[C#\]]**                           |
|                                                                            |
| [                  ]                   |
|                                                                            |
| [// Append PDFDocument.] |
|                                                                            |
| [doc1.Append(doc2);]                   |
+----------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------+
| **[\[VB.NET\]]**                       |
|                                                                            |
| []                                     |
|                                                                            |
| [\' Append PDFDocument.] |
|                                                                            |
| [doc1.Append(doc2)]                    |
+----------------------------------------------------------------------------+

 

Merging pages of different Documents

 

Yet another way of merging will be, to import all the pages from one document to another. The following code example illustrates this.

[] 

+------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                               |
|                                                                                                |
| [                 ]                                        |
|                                                                                                |
| [//Import all the pages to another document] |
|                                                                                                |
| [doc2.ImportPageRange(doc2, 0, doc.Pages.Count);]          |
+------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                           |
|                                                                                                |
| []                                                         |
|                                                                                                |
| [\'Import all the pages to another document] |
|                                                                                                |
| [doc2.ImportPageRange(doc2, 0, doc.Pages.Count)]           |
+------------------------------------------------------------------------------------------------+

 

 

 

[]{#related-topics}

