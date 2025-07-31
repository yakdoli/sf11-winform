---
title: howtostoreandretrieveapdfdocumentfromthedatabase.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\howtostoreandretrieveapdfdocumentfromthedatabase.md
created_at: 2025-07-03
---








  









### How To Store And Retrieve a PDF Document From the Database? {#how-to-store-and-retrieve-a-pdf-document-from-the-database style="tab-stops: 0pt"}

 

Essential PDF provides support for reading and writing PDF documents from / to the System.IO.Stream. You can store a PDF document stream as a binary object in the database. The following code example illustrates this.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [// Store the PDF document in Database.]                                                                                                                                                        |
|                                                                                                                                                                                                                                                   |
| [// Initialize a stream.]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                   |
| [MemoryStream stream = [new] MemoryStream();]                                                                                                                                            |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [// Save the document to stream.]                                                                                                                                                               |
|                                                                                                                                                                                                                                                   |
| [doc.Save(stream);]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [// Retrieve and display the stream in PDFformat.]                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [OleDbDataReader Reader = command.ExecuteReader();]                                                                                                                                                           |
|                                                                                                                                                                                                                                                   |
| [byte][\[\] PdfFile = ([byte]\[\])Reader\[1\];]                                                                                         |
|                                                                                                                                                                                                                                                   |
| [Stream strm = [new] MemoryStream(PdfFile);]                                                                                                                                             |
|                                                                                                                                                                                                                                                   |
| [using][ (FileStream fstream = [new] FileStream([\"sample.pdf\"], FileMode.OpenOrCreate, FileAccess.ReadWrite))] |
|                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                   |
| [fstream.Write(PdfFile, 0, PdfFile.Length);]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                           |
| [\' Store the PDF document in Database.]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                           |
| [\' Initialize a stream.]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                           |
| [Dim][ stream [As] MemoryStream = [New] MemoryStream()]                                                                                    |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                           |
| [\' Save the document to stream.]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                           |
| [doc.Save(stream)]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                           |
| [\' Retrieve and display the stream in PDFformat.]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                           |
| [Dim][ Reader [As] OleDbDataReader = Command.ExecuteReader()]                                                                                                   |
|                                                                                                                                                                                                                                                                           |
| [Dim][ PdfFile [As] [Byte]() = [CType](Reader(1), [Byte]())]                                     |
|                                                                                                                                                                                                                                                                           |
| [Dim][ strm [As] Stream = [New] MemoryStream(PdfFile)]                                                                                     |
|                                                                                                                                                                                                                                                                           |
| [Using][ fstream [As] FileStream = [New] FileStream([\"sample.pdf\"], FileMode.OpenOrCreate, FileAccess.ReadWrite)] |
|                                                                                                                                                                                                                                                                           |
| [fstream.Write(PdfFile, 0, PdfFile.Length)]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                           |
| [End][ [Using]]                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

