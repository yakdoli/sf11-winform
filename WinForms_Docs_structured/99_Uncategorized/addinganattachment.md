---
title: addinganattachment.md
original_path: WinForms_Docs/99_Uncategorized/addinganattachment.md
created_at: 2025-08-05
---






#### Adding an Attachment {#adding-an-attachment style="tab-stops: 0pt"}

 

An attachment can be easily added to a PDF document using the **PdfAttachment** class. The following code example illustrates this.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                       |
| [PdfLoadedDocument][ doc1 = [new] [PdfLoadedDocument]([@\"..\\..\\Data\\Sample.pdf\"]);] |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [if][(doc1.Attachments == [null])]                                                                                                          |
|                                                                                                                                                                                                                                                       |
| [doc1.CreateAttachment();]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [PdfAttachment][ attachment = [new] [PdfAttachment]([@\"..\\..\\Data\\Manual.txt\"]);]   |
|                                                                                                                                                                                                                                                       |
| [attachment.ModificationDate = [DateTime].Now;]                                                                                                                                           |
|                                                                                                                                                                                                                                                       |
| [attachment.Description = [@\"..\\..\\Data\\Manual.txt\"];]                                                                                                                               |
|                                                                                                                                                                                                                                                       |
| [attachment.MimeType = [\"application/txt\"];]                                                                                                                                            |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [doc1.Attachments.Add(attachment);]                                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][VB.NET[\]]]**                                                                                                  |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                                   |
| [Dim][ doc1 [As] [New] PdfLoadedDocument([\"..\\..\\Data\\Sample.pdf\"])]   |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                   |
| [If][ doc1.Attachments [Is] [Nothing] [Then]]                                 |
|                                                                                                                                                                                                                                   |
| [    doc1.CreateAttachment()]                                                                                                                                                                 |
|                                                                                                                                                                                                                                   |
| [End][ [If]]                                                                                                            |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                                   |
| [Dim][ attachment [As] [New] PdfAttachment([\"..\\..\\Data\\Manual.txt\"])] |
|                                                                                                                                                                                                                                   |
| [attachment.ModificationDate = DateTime.Now]                                                                                                                                                  |
|                                                                                                                                                                                                                                   |
| [attachment.Description = [\"..\\..\\Data\\Manual.txt\"]]                                                                                                              |
|                                                                                                                                                                                                                                   |
| [attachment.MimeType = [\"application/txt\"]]                                                                                                                          |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                                   |
| [doc1.Attachments.Add(attachment)]                                                                                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 57: \"Manual.txt\" document attached to the PDF Document

***[]*** 

Manual.txt file is attached to the pdf document.

 

 

[]{#related-topics}

