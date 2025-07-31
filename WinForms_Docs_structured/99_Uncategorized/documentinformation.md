---
title: documentinformation.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\documentinformation.md
created_at: 2025-07-03
---








  









### Document Information {#document-information style="tab-stops: 0pt"}

 

Essential PDF enables the user to access the following information of the existing document with the help of the **PdfDocumentInformation** class.

 

[·      ]Author

[·      ]Creator

[·      ]Keywords

[·      ]Producer

[·      ]Subject

[·      ]Title and so on

 

The following code example illustrates how to access the document information.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                |
|                                                                                                                                                                                                 |
| []                                                                                                                                          |
|                                                                                                                                                                                                 |
| [PdfLoadedDocument][ doc = [new] [PdfLoadedDocument](filename);] |
|                                                                                                                                                                                                 |
| []                                                                                                                                            |
|                                                                                                                                                                                                 |
| [// Accessing document information           ]                                                                                                |
|                                                                                                                                                                                                 |
| [authorBox.Text = doc.DocumentInformation.Author;]                                                                                                          |
|                                                                                                                                                                                                 |
| [titleBox.Text = doc.DocumentInformation.Title;]                                                                                                            |
|                                                                                                                                                                                                 |
| [subjectBox.Text = doc.DocumentInformation.Subject;]                                                                                                        |
|                                                                                                                                                                                                 |
| [kwBox.Text = doc.DocumentInformation.Keywords;]                                                                                                            |
|                                                                                                                                                                                                 |
| [creatorBox.Text = doc.DocumentInformation.Creator;]                                                                                                        |
|                                                                                                                                                                                                 |
| [prodBox.Text = doc.DocumentInformation.Producer;]                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                  |
|                                                                                                                                                                                                       |
| []                                                                                                                                                |
|                                                                                                                                                                                                       |
| [Dim][ doc [As] PdfLoadedDocument = [New] PdfLoadedDocument(filename)] |
|                                                                                                                                                                                                       |
| []                                                                                                                                                  |
|                                                                                                                                                                                                       |
| [\' Accessing document information           ]                                                                                                      |
|                                                                                                                                                                                                       |
| [authorBox.Text = doc.DocumentInformation.Author]                                                                                                                 |
|                                                                                                                                                                                                       |
| [titleBox.Text = doc.DocumentInformation.Title]                                                                                                                   |
|                                                                                                                                                                                                       |
| [subjectBox.Text = doc.DocumentInformation.Subject]                                                                                                               |
|                                                                                                                                                                                                       |
| [kwBox.Text = doc.DocumentInformation.Keywords]                                                                                                                   |
|                                                                                                                                                                                                       |
| [creatorBox.Text = doc.DocumentInformation.Creator]                                                                                                               |
|                                                                                                                                                                                                       |
| [prodBox.Text = doc.DocumentInformation.Producer]                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

{border="0"}Note: You can write the document information with the newly created document, but you cannot overwrite the existing meta data information.


 

 

[]{#related-topics}

