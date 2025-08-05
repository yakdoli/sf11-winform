---
title: hyperlinksforotherexternalfiles.md
original_path: WinForms_Docs/99_Uncategorized/hyperlinksforotherexternalfiles.md
created_at: 2025-08-05
---






##### Hyperlinks for other external files {#hyperlinks-for-other-external-files style="tab-stops: 0pt"}

 

External files can be hyperlinked in a pdf document using the Annotation feature. An annotation can associate objects such as note, sound or a movie by specifying the corresponding object location in the document.

 

**PdfFileLinkAnnotation** class of the Essential PDF can be used to associate an external file to the document as follows:

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [RectangleF][ flAnnotationRectangle = ][new][ ][RectangleF][(0, 100, 80, 20);]                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [//Create PdfFileLinkAnnotation to link external file]                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [PdfFileLinkAnnotation][ flAnnotation = ][new][ ][PdfFileLinkAnnotation][(flAnnotationRectangle, ][filename][);] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [//Add the Annotation to the page]                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [page.Annotations.Add(flAnnotation);]                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| [Dim][ flAnnotationRectangle ][As][ ][New][ RectangleF(0, 100, 80, 20)]                    |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\'Create PdfFileLinkAnnotation to link external file ]                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| [Dim][ flAnnotation ][As][ ][New][ PdfFileLinkAnnotation(flAnnotationRectangle, filename)] |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\'Add the Annotation to the page ]                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                     |
| [Page.Annotations.Add(flAnnotation)]                                                                                                                                                                                                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"} Where [filename] = A string value specifying the full path of the file to be embedded.

[] 

Example for the location of the external file

[] 

[PdfFileLinkAnnotation][ fileLinkAnnotation = [new] [PdfFileLinkAnnotation](fileLinkAnnotationRectangle,]

[    [@\"..\\..\\..\\Common\\Images\\PDF\\logo.png\"]);]

[] 

Sample Location

 

A sample which illustrates this feature is available in the following sample installation location:

 

***\<Install Location\>\\Windows\\Pdf.Windows\\Samples\\2.0\\User Interaction\\Interactive Features***

 

 

[]{#related-topics}

