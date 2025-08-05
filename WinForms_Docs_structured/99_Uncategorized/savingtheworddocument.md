---
title: savingtheworddocument.md
original_path: WinForms_Docs/99_Uncategorized/savingtheworddocument.md
created_at: 2025-08-05
---








  









## Saving the Word Document {#saving-the-word-document style="tab-stops: 0pt"}

 

This topic illustrates how to save the Word document created in an application.

 

Essential DocIO provides support to save the Word document to the following formats:

 

[·      ]Doc

[·      ]Docx

[·      ]Dot

[·      ]Rtf

[·      ]Html

[·      ]Text

[·      ]Xml

[·      ]Docm

[·      ]Dotm

[·      ]Dotx

 

Saving the Word document in Windows Forms and WPF Applications

 

To use DocIO in Windows Forms and WPF applications, you must save the created document to disk. The following code example illustrates this.

 

+-------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                      |
|                                                                                                                                     |
| []                                                                                |
|                                                                                                                                     |
| [// Saving the document to disk.]                                                 |
|                                                                                                                                     |
| [doc.Save([\"Sample.doc\"], [FormatType].Doc);] |
+-------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\] ]**                                                                |
|                                                                                                                                    |
| []                                                                               |
|                                                                                                                                    |
| [\' Saving the document to disk.]                                                |
|                                                                                                                                    |
| [doc.Save([\"Sample.doc\"], [FormatType].Doc)] |
+------------------------------------------------------------------------------------------------------------------------------------+

 


!


 

Saving the Word document in ASP.NET Application

 

Essential DocIO is a Non-UI component that is used in Web applications. To use DocIO in an ASP.NET application, you must stream the created document to the client browser.

[] 

The following code example illustrates how to stream the document to the browser.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\] ]**                                                                                        |
|                                                                                                                                                        |
| **[]**                                                                                               |
|                                                                                                                                                        |
| [// Streaming the document to the Browser.]                                                          |
|                                                                                                                                                        |
| [doc.Save([\"Sample.doc\"], FormatType.Doc, Response, HttpContentDisposition.InBrowser);]   |
|                                                                                                                                                        |
| []                                                                                                                 |
|                                                                                                                                                        |
| [// Streaming the document to the Browser.]                                                          |
|                                                                                                                                                        |
| [doc.Save([\"Sample.docx\"], FormatType.Docx, Response, HttpContentDisposition.InBrowser);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                    |
|                                                                                                                                                       |
| []                                                                                                  |
|                                                                                                                                                       |
| [\' Streaming the document to the Browser.]                                                         |
|                                                                                                                                                       |
| [doc.Save([\"Sample.doc\"], FormatType.Doc, Response, HttpContentDisposition.InBrowser)]   |
|                                                                                                                                                       |
| []                                                                                                                |
|                                                                                                                                                       |
| [\' For .docx format]                                                                               |
|                                                                                                                                                       |
| [doc.Save([\"Sample.docx\"], FormatType.Docx, Response, HttpContentDisposition.InBrowser)] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Saving the Word document in Silverlight Application

 

To use DocIO in a Silverlight application, you must save the created document to the disk. The following code example illustrates how to do this.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                         |
|                                                                                                                                                                                        |
| []                                                                                                                                   |
|                                                                                                                                                                                        |
| [SaveFileDialog][ sfd = [new] [SaveFileDialog]()] |
|                                                                                                                                                                                        |
| [{]                                                                                                                                                |
|                                                                                                                                                                                        |
| [    DefaultExt = [\"doc\"],]                                                                                              |
|                                                                                                                                                                                        |
| [    FilterIndex = 1]                                                                                                                              |
|                                                                                                                                                                                        |
| [};]                                                                                                                                               |
|                                                                                                                                                                                        |
| [if][ (sfd.ShowDialog() == [true])]                                          |
|                                                                                                                                                                                        |
| [{]                                                                                                                                                |
|                                                                                                                                                                                        |
| [    [using] (Stream stream = sfd.OpenFile())]                                                                                |
|                                                                                                                                                                                        |
| [    {]                                                                                                                                            |
|                                                                                                                                                                                        |
| [        document.Save(stream, FormatType.Doc);]                                                                                                   |
|                                                                                                                                                                                        |
| [    }]                                                                                                                                            |
|                                                                                                                                                                                        |
| [}]                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\] ]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                        |
| [Dim][ sfd [As] [New] SaveFileDialog() [With] {.DefaultExt = [\"doc\"], .FilterIndex = 1}] |
|                                                                                                                                                                                                                                                                        |
| [If][ sfd.ShowDialog() = [True] [Then]]                                                                                                 |
|                                                                                                                                                                                                                                                                        |
| [      [Using] stream [As] Stream = sfd.OpenFile()]                                                                                                                                      |
|                                                                                                                                                                                                                                                                        |
| [            document.Save(stream, FormatType.Doc)]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                        |
| [      [End] [Using]]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                        |
| [End][ [If]]                                                                                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

