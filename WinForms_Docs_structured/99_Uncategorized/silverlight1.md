---
title: silverlight1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\silverlight1.md
created_at: 2025-07-03
---








  









### Silverlight {#silverlight style="tab-stops: 0pt"}

 

Now, you have created a Silverlight application (refer ). This section covers the following:

 

[·      ]Deploying Essential DocIO in a Silverlight Application

[·      ]Creating a Word Document

 

Essential DocIO has native support for creating and manipulating Word documents in a Silverlight application.

 


{border="0"}Note: DocIO provides support to create documents only in the .doc and .dot formats. It does not support the Word 2007 format.


 

Deploying Essential DocIO in a Silverlight Application

 

The following steps will guide you to deploy Essential DocIO:

 

1.   Open the MainPage.xaml of the application in the designer.

[] 

2.   Add the **Syncfusion.DocIO.Silverlight.dll** assembly as a reference to the application.

 

Essential DocIO is now deployed in your Silverlight application.

 

Creating a Word Document

 

Essential DocIO for Silverlight has support for creation and manipulation of richly formatted Word \[97-2003\] format documents. Advanced features like Mail merge, Search and replace can also be used in this approach.

 

Following steps will guide you to create a simple Word document with \"Hello World\" written on the first paragraph of the first section.

 

1.   Add reference to the following assemblies in your Silverlight application.

 

[·      ]Syncfusion.Compression.Silverlight.dll

[·      ]Syncfusion.DocIO.Silverlight.dll

 

2.   The next step is to add references to the following namespaces.

 

[·      ]**Syncfusion.DocIO.DLS** (using Syncfusion.DocIO.DLS)

[·      ]**Syncfusion.DocIO** (using Syncfusion.DocIO)

 

3.   Instantiate the **WordDocument** class. This class represents the Word document that will be created in the memory. This is the memory representation of the Word document that will be written to the disk.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                           |
|                                                                                                                                                                                          |
| **[]**                                                                                                                                 |
|                                                                                                                                                                                          |
| [// Create a new Word document. ]                                                                                                      |
|                                                                                                                                                                                          |
| [// This document has no section and no paragraph by default. ]                                                                        |
|                                                                                                                                                                                          |
| [WordDocument][ document = [new] [WordDocument]();] |
|                                                                                                                                                                                          |
| []                                                                                                                                                   |
|                                                                                                                                                                                          |
| [// Add a new section to the document.]                                                                                                |
|                                                                                                                                                                                          |
| [IWSection][ section = document.AddSection();]                                                   |
|                                                                                                                                                                                          |
| []                                                                                                                                                   |
|                                                                                                                                                                                          |
| [// Adding a new paragraph to the section.]                                                                                            |
|                                                                                                                                                                                          |
| [IWParagraph][ paragraph = section.AddParagraph();]                                              |
|                                                                                                                                                                                          |
| []                                                                                                                                                   |
|                                                                                                                                                                                          |
| [// Insert Text into the paragraph]                                                                                                    |
|                                                                                                                                                                                          |
| [paragraph.AppendText([\"Hello World!\"]);]                                                                                  |
|                                                                                                                                                                                          |
| []                                                                                                                                                   |
|                                                                                                                                                                                          |
| [// Save the file to stream.]                                                                                                          |
|                                                                                                                                                                                          |
| [SaveFileDialog sfd = [new] SaveFileDialog();]                                                                                  |
|                                                                                                                                                                                          |
| [sfd.DefaultExt = [\".xls\"];]                                                                                               |
|                                                                                                                                                                                          |
| [sfd.Filter = [\"Files(\*.xls)\|\*.xls\"];]                                                                                  |
|                                                                                                                                                                                          |
| [if][ (sfd.ShowDialog() == [true])]                                            |
|                                                                                                                                                                                          |
| [{]                                                                                                                                                  |
|                                                                                                                                                                                          |
| [using][ (Stream stream = sfd.OpenFile())]                                                          |
|                                                                                                                                                                                          |
| [{]                                                                                                                                                  |
|                                                                                                                                                                                          |
| [    document.Save(stream, FormatType.Doc);]                                                                                                         |
|                                                                                                                                                                                          |
| [}]                                                                                                                                                  |
|                                                                                                                                                                                          |
| [}]                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                       |
|                                                                                                                                                                                          |
| **[]**                                                                                                                                 |
|                                                                                                                                                                                          |
| [\' Create a new Word document. ]                                                                                                      |
|                                                                                                                                                                                          |
| [\' This document has no section and no paragraph by default. ]                                                                        |
|                                                                                                                                                                                          |
| [Dim][ document [As] WordDocument = [New] WordDocument()] |
|                                                                                                                                                                                          |
| []                                                                                                                                                   |
|                                                                                                                                                                                          |
| [\' Add a new section to the document.]                                                                                                |
|                                                                                                                                                                                          |
| [Dim][ section [As] IWSection = document.AddSection()]                         |
|                                                                                                                                                                                          |
| []                                                                                                                                                   |
|                                                                                                                                                                                          |
| [\' Adding a new paragraph to the section.]                                                                                            |
|                                                                                                                                                                                          |
| [Dim][ paragraph [As] IWParagraph = section.AddParagraph()]                    |
|                                                                                                                                                                                          |
| []                                                                                                                                                   |
|                                                                                                                                                                                          |
| [\' Insert Text into the paragraph]                                                                                                    |
|                                                                                                                                                                                          |
| [paragraph.AppendText([\"Hello World!\"])]                                                                                   |
|                                                                                                                                                                                          |
| []                                                                                                                                                   |
|                                                                                                                                                                                          |
| [\' Save the file to stream.]                                                                                                          |
|                                                                                                                                                                                          |
| [Dim][ sfd [As] [New] SaveFileDialog()]                   |
|                                                                                                                                                                                          |
| [sfd.DefaultExt = [\".xls\"]]                                                                                                |
|                                                                                                                                                                                          |
| [sfd.Filter = [\"Files(\*.xls)\|\*.xls\"]]                                                                                   |
|                                                                                                                                                                                          |
| [If][ sfd.ShowDialog() = [True] [Then]]                   |
|                                                                                                                                                                                          |
| [Using][ stream [As] Stream = sfd.OpenFile()]                                  |
|                                                                                                                                                                                          |
| [document.Save(stream, FormatType.Doc)]                                                                                                              |
|                                                                                                                                                                                          |
| [End][ [Using]]                                                                |
|                                                                                                                                                                                          |
| [End][ [If]][        ]                     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 


{border="0"}Note: Here, initially Word document has no section and no paragraph. You should add sections and paragraphs to write text on it. Save method of the WordDocument is used to save the created document to disk or stream to browser.


 

The following screen shot shows the Word document that is generated.

 

{border="0"}

Figure 20: Word Document

**** 

A Word document is created in the Silverlight application.

 

 

[]{#related-topics}

