---
title: addingpdfviewertoanapplication1.md
original_path: WinForms_Docs/99_Uncategorized/addingpdfviewertoanapplication1.md
created_at: 2025-08-05
---








  









## Adding PDF Viewer to an Application {#adding-pdf-viewer-to-an-application style="tab-stops: 0pt"}

To add a PDF Viewer control to your application:

[] 

1.   Open your form in the designer. Add the Syncfusion controls to your** **VS.NET toolbox if you haven\'t done so already (the install would have automatically done this unless you selected not to complete toolbox integration during installation).

[] 

{border="0"}[]

Figure 5*[: PDF Viewer control in Toolbox]*

*[]* 

2.   Drag a PDF Viewer control onto the form.

[] 

Appearance and behavior-related aspects of the PDF Viewer can be controlled by setting the appropriate properties through the properties grid.

*[]* 

{border="0"}*[]*

Figure 6*[: Properties]*

*[]* 

3.   Add Syncfusion.PdfViewer.Windows namespace.

*[]* 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                                  |
|                                                                                                                                                                                  |
| **C#:**                                                                                                                                                                          |
|                                                                                                                                                                                  |
|                                                                                                                                                                                  |
|                                                                                                                                                                                  |
| [using][ Syncfusion.PdfViewer.Windows;]                                                     |
|                                                                                                                                                                                  |
|                                                                                                                                                                                  |
|                                                                                                                                                                                  |
| [//Initializing the PDF Viewer]                                                                                                |
|                                                                                                                                                                                  |
| [PdfViewer][ viewer = [new] [PdfViewer]();] |
|                                                                                                                                                                                  |
| []                                                                                                                                           |
|                                                                                                                                                                                  |
| [//Loading the document in the PDF Viewer]                                                                                     |
|                                                                                                                                                                                  |
| [viewer.Load([@\"c:/documents/myPDF.pdf\"]);]                                                                        |
|                                                                                                                                                                                  |
| []                                                                                                                                           |
|                                                                                                                                                                                  |
| **[VB:]**                                                                                                                                    |
|                                                                                                                                                                                  |
| []                                                                                                                                           |
|                                                                                                                                                                                  |
| []                                                                                                                                           |
|                                                                                                                                                                                  |
| [Imports][ Syncfusion.PdfViewer.Windows]                                                    |
|                                                                                                                                                                                  |
| []                                                                                                                                           |
|                                                                                                                                                                                  |
| [\'Initializing the Pdf Viewer]                                                                                                |
|                                                                                                                                                                                  |
| [ [Dim] viewer [As] PdfViewer = [New] PdfViewer()]                            |
|                                                                                                                                                                                  |
| []                                                                                                                                           |
|                                                                                                                                                                                  |
| [\'Loading the document in the Pdf Viewer]                                                                                     |
|                                                                                                                                                                                  |
| [ viewer.Load([\"c:/documents/myPDF.pdf\"])]                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Refer to [ ]{.UGHyperlink}for more information.[[]]{.UGHyperlink}

[]{#related-topics}

