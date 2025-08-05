---
title: annotation2.md
original_path: WinForms_Docs/99_Uncategorized/annotation2.md
created_at: 2025-08-05
---






#### Annotation {#annotation style="tab-stops: 0pt"}

 

An annotation associates an object such as a note, sound, or movie with a location on the page of a PDF document, or provides a way to interact with the user, by means of the mouse and keyboard.

 

An annotation is activated when you click the left mouse button.

 

[·      ]PdfSoundAnnotation plays sound file

[·      ]PdfAttachmentAnnotation opens attached file

[·      ]PdfUriAnnotation navigates to specified URI

[·      ]PdfActionAnnotation performs specified action

[·      ]PdfFileLinkAnnotation opens file with the specified path

[·      ]PdfDocumentLinkAnnotation navigates to specified destination within the document

[·      ]PdfPopupAnnotation displays the text in a pop-up window for entry and editing

[·      ]PdfLineAnnotation displays a single straight line on the page

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                   |
| [RectangleF][ popupAnnotationRectangle = [new] [RectangleF](0, 50, 50, 50);]                                                                       |
|                                                                                                                                                                                                                                                                                   |
| [PdfPopupAnnotation][ popupAnnotation = [new] [PdfPopupAnnotation](popupAnnotationRectangle, [\"Test popup annotation\"]);] |
|                                                                                                                                                                                                                                                                                   |
| [popupAnnotation.Border.Width = 4;]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                   |
| [popupAnnotation.Icon = PopupIcon.NewParagraph;]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                   |
| [page.Annotations.Add(popupAnnotation);]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| [RectangleF][ uriAnnotationRectangle = [new] [RectangleF](0, 100, 80, 20);]                                                                        |
|                                                                                                                                                                                                                                                                                   |
| [PdfUriAnnotation][ uriAnnotation = [new] [PdfUriAnnotation](uriAnnotationRectangle, [\"http://www.google.com\"]);]         |
|                                                                                                                                                                                                                                                                                   |
| [page.Annotations.Add(uriAnnotation);]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| [RectangleF][ docLinkAnnotationRectangle = [new] [RectangleF](0, 200, 80, 20);]                                                                    |
|                                                                                                                                                                                                                                                                                   |
| [PdfDocumentLinkAnnotation][ documentAnnotation = [new] [PdfDocumentLinkAnnotation](docLinkAnnotationRectangle);]                                  |
|                                                                                                                                                                                                                                                                                   |
| [documentAnnotation.Text = [\"Document link annotation\"];]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| [documentAnnotation.Color = [new] [PdfColor]([Color].Navy);]                                                                                                                   |
|                                                                                                                                                                                                                                                                                   |
| [documentAnnotation.Border.Width = 3;]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                   |
| [documentAnnotation.Border.HorizontalRadius = 25;]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| [documentAnnotation.AnnotationFlags = AnnotationFlags.NoRotate;]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                   |
| [PdfPage][ page2 = document.Pages.Add();]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                   |
| [documentAnnotation.Destination = [new] [PdfDestination](page2);]                                                                                                                                   |
|                                                                                                                                                                                                                                                                                   |
| [documentAnnotation.Destination.Location = [new] [Point](0, 0);]                                                                                                                                    |
|                                                                                                                                                                                                                                                                                   |
| [documentAnnotation.Destination.Zoom = 5;]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                   |
| [page.Annotations.Add(documentAnnotation);]                                                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                               |
| [Dim][ popupAnnotationRectangle [As] RectangleF = [New] RectangleF(0, 50, 50, 50)]                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                               |
| [Dim][ popupAnnotation [As] Syncfusion.Pdf.Interactive.PdfPopupAnnotation = [New] Syncfusion.Pdf.Interactive.PdfPopupAnnotation(popupAnnotationRectangle, [\"Test popup annotation\"])] |
|                                                                                                                                                                                                                                                                                                                                               |
| [popupAnnotation.Border.Width = 4]                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                               |
| [popupAnnotation.Icon = PopupIcon.NewParagraph]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                               |
| [page.Annotations.Add(popupAnnotation)]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                               |
| [Dim][ uriAnnotationRectangle [As] RectangleF = [New] RectangleF(0, 100, 80, 20)]                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                               |
| [Dim][ uriAnnotation [As] Syncfusion.Pdf.Interactive.PdfUriAnnotation = [New] Syncfusion.Pdf.Interactive.PdfUriAnnotation(uriAnnotationRectangle, [\"http://www.google.com\"])]         |
|                                                                                                                                                                                                                                                                                                                                               |
| [page.Annotations.Add(uriAnnotation)]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                               |
| [Dim][ docLinkAnnotationRectangle [As] RectangleF = [New] RectangleF(0, 200, 80, 20)]                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                               |
| [Dim][ documentAnnotation [As] Syncfusion.Pdf.Interactive.PdfDocumentLinkAnnotation = [New] Syncfusion.Pdf.Interactive.PdfDocumentLinkAnnotation(docLinkAnnotationRectangle)]                                  |
|                                                                                                                                                                                                                                                                                                                                               |
| [documentAnnotation.Text = [\"Document link annotation\"]]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                               |
| [documentAnnotation.Color = [New] PdfColor(Color.Navy)]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                               |
| [documentAnnotation.Border.Width = 3]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                               |
| [documentAnnotation.Border.HorizontalRadius = 25]                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                               |
| [documentAnnotation.AnnotationFlags = AnnotationFlags.NoRotate]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                               |
| [Dim][ page2 [As] Syncfusion.Pdf.PdfPage = document.Pages.Add()]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                               |
| [documentAnnotation.Destination = [New] PdfDestination(page2)]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                               |
| [documentAnnotation.Destination.Location = [New] Point(0, 0)]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                               |
| [documentAnnotation.Destination.Zoom = 5]                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                               |
| [page.Annotations.Add(documentAnnotation)]                                                                                                                                                                                                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Getting Annotation from existing PDF Document

 

Essential PDF now supports reading annotations from the existing PDF document. The following code example illustrates this.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                |
| [PdfLoadedDocument][ ldoc = [new] [PdfLoadedDocument]([\"Sample.pdf\"]);]         |
|                                                                                                                                                                                                                                                                                |
| [PdfPageBase][ lpage = ldoc.Pages\[1\];]                                                                                                               |
|                                                                                                                                                                                                                                                                                |
| [PdfLoadedAttachmentAnnotation][ attAnnot = lpage.Annotations\[0\] [as] [PdfLoadedAttachmentAnnotation];] |
|                                                                                                                                                                                                                                                                                |
| [attAnnot.Color = [new] [PdfColor]([Color].Red);]                                                                                                     |
|                                                                                                                                                                                                                                                                                |
| [attAnnot.Text = [\"New Annotation\"];]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                |
| [attAnnot.Icon = [PdfAttachmentIcon].PushPin;]                                                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                     |
| [Dim][ ldoc [As] PdfLoadedDocument = [New] PdfLoadedDocument([\"Sample.pdf\"])]               |
|                                                                                                                                                                                                                                                                                     |
| [Dim][ lpage [As] PdfPageBase = ldoc.Pages(1)]                                                                                            |
|                                                                                                                                                                                                                                                                                     |
| [Dim][ attAnnot [As] PdfLoadedAttachmentAnnotation = [TryCast](lpage.Annotations(0), PdfLoadedAttachmentAnnotation)] |
|                                                                                                                                                                                                                                                                                     |
| [attAnnot.Color = [New] PdfColor(Color.Red)]                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                     |
| [attAnnot.Text = [\"New Annotation\"]]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                     |
| [attAnnot.Icon = PdfAttachmentIcon.PushPin]                                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

More:









