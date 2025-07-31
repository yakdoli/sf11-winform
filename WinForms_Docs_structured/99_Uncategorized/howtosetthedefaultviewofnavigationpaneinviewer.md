---
title: howtosetthedefaultviewofnavigationpaneinviewer.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtosetthedefaultviewofnavigationpaneinviewer.md
created_at: 2025-07-03
---






#### How to set the default view of Navigation Pane in Viewer? {#how-to-set-the-default-view-of-navigation-pane-in-viewer style="tab-stops: 0pt"}

 

When a PDF document is opened in Adobe, by default, any one of the tabs in the Navigation pane can be expanded. It can be set using the PdfPageMode enumeration in Essential PDF. The following code snippet when executed, make Attachments as a default view.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                       |
|                                                                                                                                                                                        |
| [PdfDocument][ document = [new] [PdfDocument]();] |
|                                                                                                                                                                                        |
| [document.ViewerPreferences.PageMode = [PdfPageMode].UseAttachments;]                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                     |
|                                                                                                                                                                          |
| [Dim][ document [As] [New] PdfDocument()] |
|                                                                                                                                                                          |
| []                                                                                                                                   |
|                                                                                                                                                                          |
| [document.ViewerPreferences.PageMode = PdfPageMode.UseAttachments]                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 65: PDF with default view

 

[]{#related-topics}

