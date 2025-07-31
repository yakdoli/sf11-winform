---
title: documentsettings.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\documentsettings.md
created_at: 2025-07-03
---






#### Document Settings {#document-settings style="tab-stops: 0pt"}

 

The Document settings help in storing information about the document. Extensible Metadata Platform (XMP) is a technology that enables to embed metadata.

 

{border="0"} Metadata is the data that describes a file into the file itself.

 

It uses XML as the syntax for metadata description. XMP is provided with the following schemas:

 

[·      ]Basic Schema

[·      ]Dublin Core Schema

[·      ]Rights Management Schema

[·      ]Basic Job Ticket Schema

[·      ]Paged-Text Schema

[·      ]PDF Schema

 

The document properties of Adobe are set by using either the **XMP\'s PDF** schema or the **DocumentInformation** method of the PdfDocument. The properties that can be set are as follows.

 

[·      ]Author

[·      ]CreationDate

[·      ]Keywords

[·      ]Producer

[·      ]Subject

[·      ]Title

 

The following code snippet illustrates setting the document properties such as **Title**, **Author** and **Keywords**.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                               |
|                                                                                                                                                              |
| []                                                                                                         |
|                                                                                                                                                              |
| [// Setting various Document Properties.]                                                                  |
|                                                                                                                                                              |
| [pdfDoc.DocumentInformation.Title = [\"Document Properties Information\"];]                       |
|                                                                                                                                                              |
| [pdfDoc.DocumentInformation.Author = [\"Syncfusion\"];]                                           |
|                                                                                                                                                              |
| [pdfDoc.DocumentInformation.Keywords = [\"PDF\"];]                                                |
|                                                                                                                                                              |
| []                                                                                                                       |
|                                                                                                                                                              |
| [// XMP Basic Schema.]                                                                                     |
|                                                                                                                                                              |
| [BasicSchema][ basic = xmp.BasicSchema;]                                |
|                                                                                                                                                              |
| [basic.Advisory.Add([\"advisory\"]);]                                                             |
|                                                                                                                                                              |
| [basic.BaseURL = [new] [Uri]([\"http://google.com\"]);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][VB.NET[\]]]**                                              |
|                                                                                                                                                                               |
| []                                                                                                                          |
|                                                                                                                                                                               |
| [\' Setting various Document Properties.]                                                                                   |
|                                                                                                                                                                               |
| [pdfDoc.DocumentInformation.Title = [\"Document Properties Information\"]]                                         |
|                                                                                                                                                                               |
| [pdfDoc.DocumentInformation.Author = [\"Syncfusion\"]]                                                             |
|                                                                                                                                                                               |
| [pdfDoc.DocumentInformation.Keywords = [\"PDF\"]]                                                                  |
|                                                                                                                                                                               |
| []                                                                                                                         |
|                                                                                                                                                                               |
| [\' XMP Basic Schema.]                                                                                                      |
|                                                                                                                                                                               |
| [Dim][ basic [As] Syncfusion.Pdf.Xmp.BasicSchema = xmp.BasicSchema] |
|                                                                                                                                                                               |
| [basic.Advisory.Add([\"advisory\"])]                                                                               |
|                                                                                                                                                                               |
| [basic.BaseURL = [New] Uri([\"http://google.com\"])]                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 32: Document Properties

 

 

 

[]{#related-topics}

