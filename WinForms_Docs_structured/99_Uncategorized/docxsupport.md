---
title: docxsupport.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\docxsupport.md
created_at: 2025-07-03
---








  









### Docx Support {#docx-support style="tab-stops: 0pt"}

 

Essential DocIO provides support for creating Microsoft Word 2007 format and Microsoft Word 2010 format files from scratch by using the DocIO API. Word 2007 and Word 2010 format files are created with the same API as that of .doc files, except the format type in which they are saved and opened.

 

The following code illustrates how to create a Word 2007 format document.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                       |
| [WordDocument][ doc = [new] WordDocument();]                                                                                                |
|                                                                                                                                                                                                                                                       |
| [//Add a new section to the document.]                                                                                                                                                              |
|                                                                                                                                                                                                                                                       |
| [IWSection][ section = document.AddSection();]                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [//Adding a new paragraph to the section.]                                                                                                                                                          |
|                                                                                                                                                                                                                                                       |
| [IWParagraph][ paragraph = section.AddParagraph()]                                                                                                               |
|                                                                                                                                                                                                                                                       |
| [//Insert Text into the paragraph.]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                       |
| [paragraph.AppendText( \"Hello World!\" );]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                       |
| [//Saves the document in Word 2007 format type.]                                                                                                                                                    |
|                                                                                                                                                                                                                                                       |
| [doc.Save([\"OutDocument.docx\"], ][FormatType][.Word2007][);] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                      |
| [Dim][ doc [As] [New] WordDocument()]                                                                                 |
|                                                                                                                                                                                                                                                      |
| [\'Add a new section to the document.]                                                                                                                                                             |
|                                                                                                                                                                                                                                                      |
| [Dim section As IWSection = document.AddSection()]                                                                                                                                                               |
|                                                                                                                                                                                                                                                      |
| [\'Adding a new paragraph to the section.]                                                                                                                                                         |
|                                                                                                                                                                                                                                                      |
| [Dim paragraph As IWParagraph = section.AddParagraph()]                                                                                                                                                          |
|                                                                                                                                                                                                                                                      |
| [\'Insert Text into the paragraph.]                                                                                                                                                                |
|                                                                                                                                                                                                                                                      |
| [paragraph.AppendText(\"Hello World!\")]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                      |
| [\'Saves the document in Word 2007 format type.]                                                                                                                                                   |
|                                                                                                                                                                                                                                                      |
| [doc.Save([\"OutDocument.docx\"], ][FormatType][.Word2007][)] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 


Note: The format type option "Docx" specifies the Microsoft Word 2007 format and its usage is deprecated, we recommend you to make use of Word2007 or Word2010.


 

The following code illustrates how to open a Word 2010 format document and save it.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                  |
| [WordDocument][ doc = [new] WordDocument();]                                                                                           |
|                                                                                                                                                                                                                                                  |
| [//Opens the Word 2010 format document.]                                                                                                                                                       |
|                                                                                                                                                                                                                                                  |
| [document.Open(filename, [FormatType].Automatic);][]                                                                                             |
|                                                                                                                                                                                                                                                  |
| [//Adding a new paragraph to the last section.]                                                                                                                                                |
|                                                                                                                                                                                                                                                  |
| [IWParagraph][ paragraph = document.LastSection.AddParagraph()]                                                                                             |
|                                                                                                                                                                                                                                                  |
| [//Insert Text into the paragraph.]                                                                                                                                                            |
|                                                                                                                                                                                                                                                  |
| [paragraph.AppendText( \"Creating Word 2010 format document!\" );]                                                                                                                                           |
|                                                                                                                                                                                                                                                  |
| [//Saves the document in Word 2010 format type.]                                                                                                                                               |
|                                                                                                                                                                                                                                                  |
| [doc.Save([\"Sample.docx\"], ][FormatType][.Word2010][);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                              |
|                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                 |
| [Dim][ doc [As] [New] WordDocument()]                                                                            |
|                                                                                                                                                                                                                                                 |
| [\'][Opens the Word 2010 format document.]                                                                                                  |
|                                                                                                                                                                                                                                                 |
| [document.Open(filename, [FormatType].Automatic);][]                                                                                            |
|                                                                                                                                                                                                                                                 |
| [\'Adding a new paragraph to the last section.]                                                                                                                                               |
|                                                                                                                                                                                                                                                 |
| [Dim paragraph As IWParagraph = document.LastSection.AddParagraph()]                                                                                                                                        |
|                                                                                                                                                                                                                                                 |
| [\'Insert Text into the paragraph.]                                                                                                                                                           |
|                                                                                                                                                                                                                                                 |
| [paragraph.AppendText(\"Creating Word 2010 format document!\")]                                                                                                                                             |
|                                                                                                                                                                                                                                                 |
| [\'Saves the document in Word 2007 format type.]                                                                                                                                              |
|                                                                                                                                                                                                                                                 |
| [doc.Save([\"Sample.docx\"], ][FormatType][.Word2010][)] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

DocIO also has the ability to save the doc files into docx format (i.e, Microsoft Word 2007 format and Microsoft Word 2010 format files). All the elements supported by .Doc are supported in .Docx.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                        |
| [WordDocument][ doc = [new] [WordDocument]();]                                                                    |
|                                                                                                                                                                                                                                                        |
| [doc.Open([\"SourceDocument.doc\"], [FormatType].Doc);]                                                                                                            |
|                                                                                                                                                                                                                                                        |
| [doc.Save([\"OutDocument.docx\"], ][FormatType][.Word2007][);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                      |
| [Dim][ doc [As] [New] WordDocument()]                                                                                 |
|                                                                                                                                                                                                                                                      |
| [doc.Open([\"SourceDocument.doc\"], FormatType.Doc)]                                                                                                                                      |
|                                                                                                                                                                                                                                                      |
| [doc.Save([\"OutDocument.docx\"], ][FormatType][.Word2007][)] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Essential DocIO provides support for reading Word 2007 / Word 2010 files. Currently we do have only a limited support. Docx files can be read with same API as that of .doc files, except the format it is opened.

 

The following code illustrates how to read a Docx file.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\] ]**                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                          |
| [WordDocument doc = [new] WordDocument([\"C:\\\\sample.docx\"], ][FormatType][.Word2007][);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\] ]**                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                           |
| [Dim][ doc [As] [New] WordDocument([\"c:\\\\sample.docx\"], ][FormatType][.Word2007][)] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

More:





