---
title: attachments.md
original_path: WinForms_Docs/99_Uncategorized/attachments.md
created_at: 2025-08-05
---






#### Attachments {#attachments style="tab-stops: 0pt"}

 

PDF document can contain any number of attached files. They are displayed on the Attachments navigation panel. All the data of the attached file is embedded into the document. To add a new attachment to the document, you can use the **PdfAttachment** class.

 

The following code example illustrates how to add an attachment to the document.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [PdfAttachment][ attachment = [new] [PdfAttachment]([@\"..\\..\\Images\\jpg\\logo.jpg\"]);] |
|                                                                                                                                                                                                                                                   |
| [attachment.ModificationDate = [DateTime].Now;]                                                                                                                                          |
|                                                                                                                                                                                                                                                   |
| [attachment.Description = [\"Syncfusion Logo\"];]                                                                                                                                      |
|                                                                                                                                                                                                                                                   |
| [attachment.MimeType = [\"application/jpeg\"];]                                                                                                                                        |
|                                                                                                                                                                                                                                                   |
| [document.Attachments.Add(attachment);]                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                        |
| [Dim][ attachment [As] PdfAttachment = [New] PdfAttachment([\"..\\..\\Images\\jpg\\logo.jpg\"])] |
|                                                                                                                                                                                                                                                        |
| [attachment.ModificationDate = DateTime.Now ]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                        |
| [attachment.Description = [\"Syncfusion Logo\"] ]                                                                                                                                           |
|                                                                                                                                                                                                                                                        |
| [attachment.MimeType = [\"application/jpeg\"]]                                                                                                                                              |
|                                                                                                                                                                                                                                                        |
| [document.Attachments.Add( attachment )]                                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Be sure to add the attachment to the attachment collection of the document. You can specify some additional parameters such as CreationDate, ModificationDate, MimeType or Description for the attachment.

 

It is possible to create attachments from data contained in a stream or data array. In this case, the file name passed to the constructor will determine the title of the attachment displayed on the attachments panel.

 

The following code example illustrates how to attach stream data to the PDF document.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                |
| [using][ (FileStream fileStream = [new] FileStream([@\"..\\..\\Images\\jpg\\image.jpg\"], FileMode.Open))]    |
|                                                                                                                                                                                                                                                |
| [{]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                |
| [PdfAttachment][ streamAttachment = [new] [PdfAttachment]([\"mouse.jpg\"], fileStream);] |
|                                                                                                                                                                                                                                                |
| [streamAttachment.MimeType = [\"application/jpeg\"];]                                                                                                                               |
|                                                                                                                                                                                                                                                |
| [document.Attachments.Add(streamAttachment);]                                                                                                                                                              |
|                                                                                                                                                                                                                                                |
| [}]                                                                                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                            |
| [Dim][ fileStream [As] IO.FileStream = [New] IO.FileStream([\"..\\..\\Images\\jpg\\image.jpg\"], FileMode.Open)]                                     |
|                                                                                                                                                                                                                                                                                                            |
| [Dim][ streamAttachment [As] Syncfusion.Pdf.Interactive.PdfAttachment = [New] Syncfusion.Pdf.Interactive.PdfAttachment([\"mouse.jpg\"], fileStream)] |
|                                                                                                                                                                                                                                                                                                            |
| [streamAttachment.MimeType = [\"application/jpeg\"]]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                            |
| [document.Attachments.Add(streamAttachment)]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                            |
| [Dim][ disp [As] IDisposable = fileStream]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                            |
| [disp.Dispose()]                                                                                                                                                                                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

